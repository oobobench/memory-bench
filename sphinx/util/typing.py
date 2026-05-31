 
 import sys
 import typing
from struct import Struct
 from typing import Any, Callable, Dict, Generator, List, Optional, Tuple, TypeVar, Union
 
 from docutils import nodes
         return ':obj:`None`'
     elif cls is Ellipsis:
         return '...'
    elif cls is Struct:
        # Before Python 3.9, struct.Struct class has incorrect __module__.
        return ':class:`struct.Struct`'
     elif inspect.isNewType(cls):
         return ':class:`%s`' % cls.__name__
     elif cls.__module__ in ('__builtin__', 'builtins'):
         return annotation.__qualname__
     elif annotation is Ellipsis:
         return '...'
    elif annotation is Struct:
        # Before Python 3.9, struct.Struct class has incorrect __module__.
        return 'struct.Struct'
 
     if sys.version_info >= (3, 7):  # py37+
         return _stringify_py37(annotation)
