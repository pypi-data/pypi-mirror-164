# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import abc
from typing import Union, Optional, overload

from .. import _util
from ..technology import (
    property_ as prp, net as net_, mask as msk, primitive as prm, technology_ as tch,
)
from . import library as lbry


__all__ = ["CircuitFactory"]


class _Instance(abc.ABC):
    @abc.abstractmethod
    def __init__(self, name, ports):
        assert all((
            isinstance(name, str),
            isinstance(ports, net_.Nets),
        )), "Internal error"

        self.name = name
        ports._freeze_()
        self.ports = ports


class _InstanceNet(net_.Net):
    def __init__(self, inst, net):
        assert all((
            isinstance(inst, _Instance),
            isinstance(net, net_.Net),
        )), "Internal error"
        super().__init__(net.name)
        self.inst = inst
        self.net = net
        self.full_name = f"{inst.name}.{net.name}"

    def __hash__(self):
        return hash(self.full_name)

    def __eq__(self, other):
        return isinstance(other, _InstanceNet) and ((self.full_name) == other.full_name)


class _InstanceNets(_util.ListStrMappingOverride[_InstanceNet], net_.Nets):
    @property
    def _elem_type_(self):
        return _InstanceNet
    @property
    def _index_attribute_(self):
        return "full_name"


class _Instances(_util.TypedListStrMapping[_Instance]):
    @property
    def _elem_type_(self):
        return _Instance


class _PrimitiveInstance(_Instance):
    def __init__(self, name, prim, **params):
        assert all((
            isinstance(name, str),
            isinstance(prim, prm._Primitive),
        )), "Internal error"

        self.name = name
        super().__init__(
            name, net_.Nets(_InstanceNet(self, port) for port in prim.ports),
        )

        self.prim = prim
        self.params = params


class _CellInstance(_Instance):
    def __init__(self, name: str, cell: lbry._Cell, *, circuitname: Optional[str]=None):
        self.name = name
        self.cell = cell

        if circuitname is None:
            try:
                circuit = self.cell.circuit
            except AttributeError:
                raise TypeError(
                    "no circuitname provided for cell without default circuit"
                )
        else:
            circuit = cell.circuits[circuitname]
        self.circuitname = circuitname
        self.circuit = circuit

        super().__init__(
            name, net_.Nets(_InstanceNet(self, port) for port in circuit.ports),
        )

    # TODO: temporary implementation in wait of better engineered polygon iteration
    # implementation in _Layout
    def net_polygons(self, *, net, layoutname=None):
        if isinstance(net, str):
            try:
                net = self.circuit.nets[net]
            except KeyError:
                raise ValueError(
                    f"net '{net}' does not exist for instance '{self.name}'"
                    f" of cell '{self.cell.name}'"
                )
        if not isinstance(net, net_.Net):
            raise TypeError(
                f"net has to be 'None' or of type 'Net', not {type(net)}"
            )
        if net not in self.circuit.nets:
            raise ValueError(
                f"net '{net.name}' is not a net of instance '{self.name}'"
                f" of cell '{self.cell.name}'"
            )
        layout = None
        if layoutname is None:
            if self.circuitname is not None:
                try:
                    layout = self.cell.layouts[self.circuitname]
                except KeyError:
                    pass
        else:
            if not isinstance(layoutname, str):
                raise TypeError(
                    "layoutname has to be 'None' or a string, not of type"
                    f" '{type(layoutname)}'"
                )
            try:
                layout = self.cell.layouts[layoutname]
            except KeyError:
                raise ValueError(
                    f"layout '{layoutname}' does not exist of instance '{self.name}'"
                    f" of cell '{self.cell.name}'"
                )
        if layout is None:
            try:
                layout = self.cell.layout
            except AttributeError:
                raise ValueError(
                    f"cell '{self.cell.name}' of instance '{self.name}'"
                    " does not have a default layout"
                )
        yield from layout.net_polygons(net=net)


class _CircuitNet(net_.Net):
    def __init__(self,
        circuit: "_Circuit", name: str, external: bool,
    ):
        super().__init__(name)
        self.circuit = circuit
        self.childports = _InstanceNets()
        self.external = external

    def freeze(self):
        self.childports._freeze_()


class _CircuitNets(_util.ListStrMappingOverride[_CircuitNet], net_.Nets):
    _elem_type = _CircuitNet


class _Circuit:
    def __init__(self, name: str, fab: "CircuitFactory"):
        self.name = name
        self.fab = fab

        self.instances = _Instances()
        self.nets = _CircuitNets()
        self.ports = _CircuitNets()

    @overload
    def instantiate(self,
        object_: prm._Primitive, *, name: str, **params,
    ) -> _PrimitiveInstance:
        ... # pragma: no cover
    @overload
    def instantiate(self,
        object_: lbry._Cell, *, name: str, **params,
    ) -> _CellInstance:
        ... # pragma: no cover
    def instantiate(self, object_, *, name, **params) -> Union[
        _PrimitiveInstance, _CellInstance,
    ]:
        if not isinstance(name, str):
            raise TypeError("name has to be a string")

        if isinstance(object_, prm._Primitive):
            params = object_.cast_params(params)
            inst = _PrimitiveInstance(name, object_, **params)
        elif isinstance(object_, lbry._Cell):
            circuitname = params.pop("circuitname", None)
            if params:
                raise NotImplementedError("Parametric Circuit instance")
            inst = _CellInstance(name, object_, circuitname=circuitname)
        else:
            raise TypeError(
                f"object_ has to be of type '_Primitive' or '_Cell', not {type(object_)}",
            )

        self.instances += inst
        return inst

    def new_net(self, name, *, external, childports=None):
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        if not isinstance(external, bool):
            raise TypeError("external has to be a bool")
        
        net = _CircuitNet(self, name, external)
        self.nets += net
        if external:
            self.ports += net
        if childports:
            net.childports += childports
        return net

    @property
    def subcells_sorted(self):
        cells = set()
        for inst in self.instances.__iter_type__(_CellInstance):
            if inst.cell not in cells:
                for subcell in inst.cell.subcells_sorted:
                    if subcell not in cells:
                        yield subcell
                        cells.add(subcell)
                yield inst.cell
                cells.add(inst.cell)

    def net_lookup(self, *, port: "_InstanceNet") -> "_CircuitNet":
        for net in self.nets:
            for childport in net.childports:
                if (childport.inst == port.inst) and (childport.name == port.name):
                    return net
        else:
            raise ValueError(
                f"Net for port {port.name} of instance {port.inst.name} not found",
            )


class _Circuits(_util.TypedListStrMapping[_Circuit]):
    @property
    def _elem_type_(self):
        return _Circuit


class CircuitFactory:
    def __init__(self, tech):
        if not isinstance(tech, tch.Technology):
            raise TypeError("tech has to be of type 'Technology'")
        self.tech = tech

    def new_circuit(self, name):
        if not isinstance(name, str):
            raise TypeError("name has to be a string")
        return _Circuit(name, self)
