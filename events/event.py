import asyncio as _asyncio
import typing as _T

class EventHandler():
    def __init__(self):
        self._functions: list[_T.Callable[..., _T.Any]] = []
    
    def addEventFunction(self, func: _T.Callable[..., _T.Any]) -> None:
        self._functions.append(func)
    
    def removeEventFunction(self, func: _T.Callable[..., _T.Any]) -> None:
        self._functions.remove(func)
    
    def emit(self, *values) -> None:
        for func in self._functions:
            _asyncio.create_task(self._run(func, values))
    
    async def _run(self, func, values):
        if _asyncio.iscoroutinefunction(func):
            await func( *values )
        else:
            func( *values )
