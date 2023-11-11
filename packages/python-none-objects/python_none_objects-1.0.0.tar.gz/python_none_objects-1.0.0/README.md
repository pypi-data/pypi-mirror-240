# A collection of "None" objects compatible with various Python types

The following code yields warning for "Default argument value is mutable".

```python3
from typing import List, Dict

def foo(some: int, other: List = [], thing: Dict = {}):
    for o in other:
        bar(some, o, thing)
```

It is usually recommended to use None instead
(<https://stackoverflow.com/questions/41686829/why-does-pycharm-warn-about-mutable-default-arguments-how-can-i-work-around-the>):

```python3
from typing import List, Dict, Optional

def foo(some: int, other: Optional[List] = None, thing: Optional[Dict] = None):
    if other is None:
        other = []
    if thing is None:
        thing = {}
    for o in other:
        bar(some, o, thing)
```

But I prefer less boilerplate code like this:

```python3
from typing import Iterable, Mapping
from types import MappingProxyType

def foo(some: int, other: Iterable = (), thing: Mapping = MappingProxyType({})):
    for o in other:
        bar(some, o, thing)
```

This package introduces constants to make the code more readable:

```python3
from typing import Iterable, Mapping
from python_none_objects import NoneIterable, NoneMapping

def foo(some: int, other: Iterable = NoneIterable, thing: Mapping = NoneMapping):
    for o in other:
        bar(some, o, thing)
```

I think it would be better to have this kind of constants in the standard library.
But I'm not good at defending this kind of ideas on the mailing lists and discussions
that mostly throw 99 % ideas to the trash.
If you want to defend this on python-dev or python-ideas, please do :).
