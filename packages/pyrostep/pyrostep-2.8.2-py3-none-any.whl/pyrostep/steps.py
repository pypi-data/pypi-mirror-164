import asyncio
import typing

from pyrogram.client import Client as _Client
from pyrogram import ContinuePropagation
from pyrogram.handlers import MessageHandler
from pyrogram.filters import Filter
from pyrogram.types import Update

class MetaStore:
    def set_item(self, key: int, value: typing.Union[asyncio.Future, typing.Callable]) -> None:
        """
        Stores key-value.
        """
        pass

    def pop_item(self, key: int) -> typing.Union[asyncio.Future, typing.Callable]:
        """
        Gives stored key-value.

        raise KeyError if not found.
        """
        pass

    def delete_item(self, key: int) -> None:
        """
        Deletes stored key-value.
        """
        pass

    def clear(self) -> None:
        """
        Clears all stored key-value.
        """
        pass

loop = asyncio.get_event_loop()

class _RootStore(MetaStore, dict):
    def set_item(self, key: int, value: typing.Union[asyncio.Future, typing.Callable]) -> None:
        self[key] = value
    
    def pop_item(self, key: int) -> typing.Union[asyncio.Future, typing.Callable]:
        return self.pop(key)
    
    def delete_item(self, key: int) -> None:
        del self[key]

root = _RootStore() # type: MetaStore

def change_root_store(store: MetaStore) -> None:
    """
    changes root store.
    """
    global root
    root = store

def listen(
    app: _Client, store: MetaStore = None,
    handler: typing.Any = MessageHandler, filters: Filter = None, group: int = 0
) -> None:
    """
    listen client for steps.

    supported handlers:
        - `MessageHandler`
        - `CallbackQueryHandler`
        - `ChatJoinRequestHandler`
        - `ChatMemberUpdatedHandler`
        - `ChosenInlineResultHandler`
        - `EditedMessageHandler`
        - `InlineQueryHandler`
    
    Example::

        app = Client(...)
        pyrostep.listen(app)
    """
    store = store or root

    async def _listen_wrapper(_c, _u):
        fn = None

        try:
            fn = store.pop_item(_u.from_user.id)
        except (KeyError, AttributeError):
            
            try:
                fn = store.pop_item(_u.chat.id)
            except (KeyError, AttributeError):
                pass

        if not (fn is None):
            if isinstance(fn, asyncio.Future):
                fn.set_result(_u)
                return
            
            await fn(_c, _u)
            return
        
        raise ContinuePropagation
    
    app.add_handler(handler(_listen_wrapper, filters), group=group)

def register_next_step(
    id: int, _next: typing.Any, store: MetaStore = None
) -> None:
    """
    register next step for user/chat.

    Example::

        async def step1(client, msg):
            # code ...
            register_next_step(msg.from_user.id, step2)
        
        async def step2(client, msg):
            # code ...
    """
    (store or root).set_item(id, _next)

def unregister_steps(id: int, store: MetaStore = None) -> None:
    """
    unregister steps for `id`.
    """
    try:
        (store or root).delete_item(id)
    except KeyError:
        pass

async def _wait_future(id: int, timeout: float, store: MetaStore) -> Update:
    fn = loop.create_future()

    fn.add_done_callback(
        lambda _: unregister_steps(id, store)
    )

    store.set_item(id, fn)

    return await asyncio.wait_for(fn, timeout, loop=loop)

async def wait_for(
    id: int, timeout: float = None, store: MetaStore = None
) -> Update:
    """
    wait for update which comming from id.

    raise TimeoutError if timed out.

    Example::

        async def hello(_, message: Message):
            await message.reply_text("What's your name?")
            try:
                answer: Message = await pyrostep.wait_for(message.from_user, timeout=20)
            except TimeoutError:
                return
            
            await answer.reply_text(f"Your Name Is: {answer.text}")
    """
    return await _wait_future(id, timeout, store or root)

def clear(store: MetaStore = None) -> None:
    """
    Clears all registered key-value's.
    """
    (store or root).clear()
