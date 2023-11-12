from functools import wraps
import inspect
from typing import Any, Callable, Generic, Optional, TypeVar, cast, Protocol
from collections import OrderedDict


FuncType = TypeVar('FuncType', bound=Callable[..., Any])

T = TypeVar('T', bound=Callable[..., Any])


class ReplacedFuncType(Protocol, Generic[T]):
    originalFunc: T
    def __call__(self, *args: Any, **kwds: Any) -> T:
        ...


def replaceFunc(replaceFunc: FuncType, *, isEnabled=True,
                filter_: Optional[Callable[["OrderedDict[str, Any]"], bool]] = None):
    '''
    replace wrapped function by replaceFunc
    @param isEnable:
        is replace functionality is enabled
    @param filter_:
        function that determines if original or replace function should be called\n
        if returns True then the replacement one is called
    >>> def devFunc():
    >>>     ...
    >>> @replaceFunc(devFunc, isEnabled=os.getenv("IS_DEV", "")=="true")
    >>> def prodFunc():
    >>>     ...
    call the original finction
    originalResult = prodFunc.originalFunc()
    '''
    def decorator(func: T):
        if not isEnabled:
            return func
        signature = inspect.signature(func)

        @wraps(func)
        def decorated(*args, **kwargs):
            if not filter_:
                return replaceFunc(*args, **kwargs)
            if filter_:
                kw = signature.bind(*args, **kwargs)
                if filter_(kw.arguments):
                    return replaceFunc(*args, **kwargs)
            return func(*args, **kwargs)
        decorated.originalFunc = func  # type: ignore
        return cast(ReplacedFuncType[T], decorated)
    return decorator
