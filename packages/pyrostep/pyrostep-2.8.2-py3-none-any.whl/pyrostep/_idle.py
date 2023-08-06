import asyncio as _a
import logging as _log

async def safe_idle() -> None:
    """
    safe_idle works like pyrogram.idle, but pyrogram.idle works with asyncio.Task,
    and this may cause a crash in a program where asyncio.Future is used.

    *safe_idle not handle signals
    """
    while True:
        try:
            await _a.sleep(600)
        except KeyboardInterrupt:
            break
        except Exception as e:
            _log.error(e, exc_info=True)
