"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._count = 0
        return cls._instance

    @property
    def count(self):
        return self._count

    def increment(self):
        self._count += 1
        return self._count

    def __str__(self):
        return f"Count: {self._count}"

    # TODO write count property
    # TODO write increment method
