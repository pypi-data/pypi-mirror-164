from phidl.device_layout import Device

from gdsfactory.component import Component, ComponentReference, Port
from gdsfactory.config import call_if_func
from gdsfactory.types import Layer


def from_phidl(component: Device, port_layer: Layer = (1, 0), **kwargs) -> Component:
    """Returns gf.Component from a phidl Device or function.

    Args:
        component: phidl component.
        port_layer: to add to component ports.

    """
    device = call_if_func(component, **kwargs)
    component = Component(name=device.name)

    for ref in device.references:
        new_ref = ComponentReference(
            component=ref.parent,
            origin=ref.origin,
            rotation=ref.rotation,
            magnification=ref.magnification,
            x_reflection=ref.x_reflection,
        )
        new_ref.owner = component
        component.add(new_ref)
        for alias_name, alias_ref in device.aliases.items():
            if alias_ref == ref:
                component.aliases[alias_name] = new_ref

    for p in device.ports.values():
        component.add_port(
            port=Port(
                name=p.name,
                center=p.midpoint,
                width=p.width,
                orientation=p.orientation,
                parent=p.parent,
                layer=port_layer,
            )
        )
    for poly in device.polygons:
        component.add_polygon(poly)
    for label in device.labels:
        component.add_label(
            text=label.text,
            position=label.position,
            layer=(label.layer, label.texttype),
        )
    return component


if __name__ == "__main__":
    import phidl.geometry as pg

    c = pg.rectangle()
    c = pg.snspd()

    c2 = from_phidl(component=c)
    print(c2.ports)
    c2.show(show_ports=True)
