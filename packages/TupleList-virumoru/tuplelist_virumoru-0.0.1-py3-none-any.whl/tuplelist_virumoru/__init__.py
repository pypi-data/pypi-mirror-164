class TupleList(list):
    def __init__(self, iterable=(), /):
        for i in iterable:
            if not isinstance(i, tuple):
                raise ValueError(
                    f"item inside iterable is not type 'tuple' but type '{type(i).__name__}' at index "
                    f"{iterable.index(i)}: {repr(i)}")
        super().__init__(iterable)

    def append(self, __object: tuple, /):
        if isinstance(__object, tuple):
            super().append(__object)
        else:
            raise TypeError("expected 'tuple', '" + type(__object).__name__ + "' found")

    def extend(self, iterable, /):
        for i in iterable:
            if not isinstance(i, tuple):
                raise ValueError(
                    f"item inside iterable is not type 'tuple' but type '{type(i).__name__}' at index "
                    f"{iterable.index(i)}: {repr(i)}")
        super().extend(iterable)

    def insert(self, __index, __object, /):
        if isinstance(__object, tuple):
            super().insert(__index, __object)
        else:
            raise TypeError("expected 'tuple', '" + type(__object).__name__ + "' found")

    def pack(self, *args):
        if len(args) == 0:
            raise TypeError("TupleList.pack() takes at least 1 positional argument but 0 was given")
        self.append(args)

    def __setitem__(self, key, value, /):
        if isinstance(value, tuple):
            super().__setitem__(key, value)
        else:
            raise TypeError("expected 'tuple', '" + type(value).__name__ + "' found")

    def __iadd__(self, iterable, /):
        for i in iterable:
            if not isinstance(i, tuple):
                raise ValueError(
                    f"item inside iterable is not type 'tuple' but type '{type(i).__name__}' at index "
                    f"{iterable.index(i)}: {repr(i)}")
        return super().__iadd__(iterable)
