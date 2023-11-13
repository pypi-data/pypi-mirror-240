__all__ = [
    'singular',
    'plural',
]

Plural = list | tuple | set

def singular(o):
    if isinstance(o, Plural) and len(o) == 1:
        [p] = o
        return p
    else:
        return o

def plural(o):
    if isinstance(o, Plural):
        return o
    else:
        return [o]
