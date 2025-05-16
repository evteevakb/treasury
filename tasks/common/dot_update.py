def dot_update(
        d,
        update_dict,
        ) -> None:
    """dict.update with dot-notation support (mutates d). E.g.:

    >>> a = {'bar': {'bar': 1}}
    >>> dot_update(a, {'foo': 1, 'bar.baz': 2, 'bar.quux': 3, 'other.else': 9000})
    >>> a
    {'foo': 1, 'bar': {'quux': 3, 'baz': 2, 'bar': 1}, 'other': {'else': 9000}}
    """
    for key, value in update_dict.items():
        keys = key.split(".")
        if len(keys) > 1:
            current = d
            for i in range(len(keys) - 1):
                if keys[i] not in current:
                    current[keys[i]] = dict()
                current = current[keys[i]]
            current[keys[-1]] = value  
        else:
            d[key] = value

dot_update(
    d={"bar": {"bar": 1}},
    update_dict={"foo": 1, "bar.baz.bic": 2, "bar.quux": 3, "other.else": 9000},
)
