from __future__ import annotations

from typing import AsyncIterator, Iterable


async def to_aiter(it: Iterable) -> AsyncIterator:
    for x in it:
        yield x


async def azip(*iters: Iterable | AsyncIterator) -> AsyncIterator[tuple]:
    aiters = [x if isinstance(x, AsyncIterator) else to_aiter(x) for x in iters]
    if aiters:
        while True:
            try:
                yield tuple([await x.__anext__() for x in aiters])
            except StopAsyncIteration:
                return
