# Pyrostep

[![Downloads](https://static.pepy.tech/personalized-badge/pyrostep?period=total&units=abbreviation&left_color=red&right_color=grey&left_text=Downloads)](https://pepy.tech/project/pyrostep) ![Python](https://img.shields.io/static/v1?label=Language&message=Python&color=blue&style=flat&logo=python) ![Pyrogram](https://img.shields.io/static/v1?label=Framework&message=Pyrogram&color=red&style=flat)

A Python library to handle steps in pyrogram framework.

Pyrostep helps you to use pyrogram:
- very easy step handling, waiting for answer, ...
- change connection timeout, retries, etc.

#### **Updated to 2.8.2**
In this update, pyrostep completely changed ...

- New Methods:
    - **safe_idle**
    - **install**
    - **MetaStore** method's name changed.
    - **wait_for**

- Renamed Methods:
    - **change_store** to **change_root_store**

- Removed Methods:
    - **listen_on_the_side**
    - **ask**
    - **ask_wait**

- Removed Package:
    - **filters**

- [Install](#install)
- [Learn](#learn):
    - [step handling](#step-handling)
    - [wait_for method](#waitfor-method)
    - [safe idle](#about-safeidle)
- [Other](#other-packages-and-shortcuts)

# install
```bash
python3 -m pip install -U pyrostep
```

# Learn
to start with pyrostep, you have to do two steps:
1. import pyrostep
2. listen on which client you want

```python
import pyrostep
# ...
cli = Client(...)
pyrostep.listen(cli)
```

- [**Learn step handling**](#step-handling)
- [**Learn wait_for method**]()
- [**Learn about safe_idle**]()

### step handling

step handling have two methods:
- `pyrostep.register_next_step(...)`
- `pyrostep.unregister_steps(...)`

`register_next_step` register next step, and `unregister_steps` removes step for user.

see example: ( [see examples]() )
```python
# ...

async def step1(client, msg):
    await msg.reply(
        "Send your name?"
    )
    pyrostep.register_next_step(
        msg.from_user.id,
        step2
    )

async def step2(client, msg):
    await msg.reply(
        f"Your name is {msg.text}"
    )

# ...
```

### wait_for method

if you dont like step handling, can use this method.

see example: ( [see examples]() )
```python
# ...

async def get_name(client, msg):
    await msg.reply(
        "Send your name?"
    )
    answer = await pyrostep.wait_for(
        msg.from_user.id
    )
    await msg.reply(
        f"Your name is {answer.text}"
    )

# ...
```

### about safe_idle
I recommended use `pyrostep.safe_idle` instead of `pyrogram.idle` when using pyrostep.

**why?** safe_idle works like pyrogram.idle, but pyrogram.idle works with asyncio.Task,
and this may cause a crash in a program where asyncio.Future is used.

> safe_idle not handle signals.

example: ( [see examples]() )
```python
# ...
async def main():
    await app.start()
    await pyrostep.safe_idle()
    await app.stop()

app.run(main())
```

# Other packages and shortcuts

## Connection

### `connection_max_retries` method:

*Change connection max retries. (default 3)*

#### `invoke_max_retries` method:

*Change invoke max retries. (default 5)*

#### `session_start_timeout` method:

*Change start timeout. (default 1)*

#### `session_max_retries` method:

*Change session max retries ( and tcp connection mode ).*

- TCP Connection Modes:
    - TCPFull
    - TCPAbridged
    - TCPIntermediate
    - TCPAbridgedO
    - TCPIntermediateO

## Shortcuts
import shortcuts:
```python
from pyrostep import shortcuts
```

Now see methods:

`split_list` splites lst list:
```python
>>> shortcuts.split_list([1, 2, 3, 4, 5, 6], 2)
# [[1, 2], [3, 4], [5, 6]]
>>> shortcuts.split_list([1, 2, 3], 2)
# [[1, 2], [3]]
```

`keyboard` creates ReplyKeyboardMarkup from your list:
```python
buttons = [
    [
        ["Top Left"], ["Top Right"]
    ],
    [
        ["Bottom | Request Contact", True, "request_contact"]
    ]
]
kb = shortcuts.keyboard(buttons)
```

`inlinekeyboard` creates InlineKeyboardMarkup from your list:
```python
buttons = [
    [
        ["Top Left", "data_1"], ["Top Right", "data_2"]
    ],
    [
        ["Bottom", "Your URL", "url"]
    ]
]
ikb = inlinekeyboard(buttons)
```

`validation_channels` checks user already in channels or not:
```python
user_id = 56392019
channels = [-102792837, -10823823, 'channel_username']

is_joined = await validation_channels(
    app, user_id, channels
)
# ...
async def invite(app, id, channels) -> None:
    print(
        f"User {id} is not member of channels ({channels})"
    )

is_joined = await validation_channels(
    app, user_id, channels,
    invite_func=invite
)
```
