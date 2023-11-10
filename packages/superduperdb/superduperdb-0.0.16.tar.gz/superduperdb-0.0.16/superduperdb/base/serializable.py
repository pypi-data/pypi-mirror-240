import dataclasses as dc
import importlib
import inspect
import typing as t

from superduperdb.misc.serialization import asdict


def is_component_metadata(r: dict) -> bool:
    COMPONENT_KEYS = {'type_id', 'identifier', 'version'}
    if COMPONENT_KEYS == set(r):
        return True
    return False


def is_component(r: dict) -> bool:
    COMPONENT_KEYS = {'cls', 'dict', 'module'}
    if COMPONENT_KEYS <= set(r):
        return True
    return False


def _deserialize(r: t.Any, db: None = None) -> t.Any:
    if isinstance(r, list):
        return [_deserialize(i, db=db) for i in r]

    if not isinstance(r, dict):
        return r
    if not is_component(r):
        return {k: _deserialize(v, db=db) for k, v in r.items()}

    module = importlib.import_module(r['module'])
    component_cls = getattr(module, r['cls'])

    kwargs = _deserialize(r['dict'])
    if 'db' in inspect.signature(component_cls.__init__).parameters:
        kwargs.update(db=db)

    return component_cls(**kwargs)


def _serialize(item: t.Any) -> t.Dict[str, t.Any]:
    def unpack(k, v):
        attr = getattr(item, k)
        if isinstance(attr, Serializable):
            return _serialize(attr)

        if isinstance(attr, list):
            for i, sc in enumerate(attr):
                if isinstance(sc, Serializable):
                    v[i] = _serialize(sc)

        if isinstance(attr, dict):
            for key, value in attr.items():
                if isinstance(value, Serializable):
                    v[key] = _serialize(value)
        return v

    d = {k: unpack(k, v) for k, v in item.dict().items()}

    from superduperdb.components.component import Component

    to_add = {}
    if isinstance(item, Component):
        to_add = {
            'type_id': item.type_id,
            'identifier': item.identifier,
            'version': getattr(item, 'version', None),
        }

    return {
        'cls': item.__class__.__name__,
        'dict': d,
        'module': item.__class__.__module__,
        **to_add,
    }


@dc.dataclass
class Serializable:
    """
    Base class for serializable objects. This class is used to serialize and
    deserialize objects to and from JSON + Artifact instances.
    """

    deserialize = staticmethod(_deserialize)
    serialize = _serialize

    def dict(self) -> t.Dict[str, t.Any]:
        return asdict(self)
