# SQL via SQLAlchemy - Introduction

## Table of Contents

- [Virtual Environment](#virtual-environment)
- [SQLite](#sqlite)
- [Hello, SQLAlchemy](#hello-sqlalchemy)
- [Helpful links](#helpful-links)

### Virtual Environment

```shell
╰─➤  python3 -m venv sqla
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: %Path-to-the-venv%
```

Ok, no problem with that, thanks for the tip.

```shell
╰─➤  sudo apt install python3-venv
[sudo] password for stankudrow: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.10-venv
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3-venv
  python3.10-venv
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 2,474 kB of archives.
After this operation, 2,888 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
...
Setting up python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.1) ...
Setting up python3-pip-whl (22.0.2+dfsg-1ubuntu0.3) ...
Setting up python3.10-venv (3.10.12-1~22.04.2) ...
Setting up python3-venv (3.10.6-1~22.04) ...
```

Trying again and the venv is successfully created. A high time to activate it.

```shell
╰─➤  source ./sqla/bin/activate
(sqla) ╭─<...@...> ~/Projects/SQL-via-Alchemy  ‹main*› 
╰─➤  
```

As you can see, the `(sqla)` prompt prefix points that the venv is activated. If you need to quit it, Type `deactivate` command.

Now two things:

1. checking the environment is clear (just for educational purpose)

2. upgrading `pip` installer

3. installing SQLAlchemy package with `>=2` version.

```shell
╰─➤  which python3
/home/<...>/Projects/SQL-via-Alchemy/sqla/bin/python3

╰─➤  which pip3
/home/<...>/Projects/SQL-via-Alchemy/sqla/bin/pip3

╰─➤  pip3 install --upgrade pip
Requirement already satisfied: pip in ./sqla/lib/python3.10/site-packages (22.0.2)
Collecting pip
  Downloading pip-23.3.1-py3-none-any.whl (2.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 5.5 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.0.2
    Uninstalling pip-22.0.2:
      Successfully uninstalled pip-22.0.2
Successfully installed pip-23.3.1

╰─➤  pip3 install "sqlalchemy>=2"
Collecting sqlalchemy>=2
  Downloading SQLAlchemy-2.0.22-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.4 kB)
Collecting typing-extensions>=4.2.0 (from sqlalchemy>=2)
  Downloading typing_extensions-4.8.0-py3-none-any.whl.metadata (3.0 kB)
Collecting greenlet!=0.4.17 (from sqlalchemy>=2)
  Downloading greenlet-3.0.0-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Downloading SQLAlchemy-2.0.22-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 7.1 MB/s eta 0:00:00
Downloading greenlet-3.0.0-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (612 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━ 612.9/612.9 kB 31.8 MB/s eta 0:00:00
Downloading typing_extensions-4.8.0-py3-none-any.whl (31 kB)
Installing collected packages: typing-extensions, greenlet, sqlalchemy
Successfully installed greenlet-3.0.0 sqlalchemy-2.0.22 typing-extensions-4.8.0
```

The [greenlet](https://pypi.org/project/greenlet/) package provides lightweight pseudo-thread structures, mostly like coroutines. A coroutine can have multiple entry points, i.e., locations where the coroutine may be suspended (leaving the coroutine) and resumed (the control is back to the coroutine).

Consider reading more about greenlets:

- [gevent-socketio docs: General concepts](https://learn-gevent-socketio.readthedocs.io/en/latest/general_concepts.html)

- [greenlet: official docs](https://greenlet.readthedocs.io/en/latest/index.html)

**A piece of advice**: if you know little or nothing about concurrency, you definitly need to master it. A good starter for concurrency in Python is [SuperFastPython](https://superfastpython.com/) in my humble opinion. Also it is good for you to have a well-grounded understanding of Python `asyncio` module, so these sources are helpful:

- [SuperFastPython: asyncio learning path](https://superfastpython.com/learning-paths/#Asyncio_Learning_Path)

- [Python Concurrency with asyncio by Matthew Fowler](https://www.manning.com/books/python-concurrency-with-asyncio)

More about installing SQLAlchemy in the [installation](https://docs.sqlalchemy.org/en/20/intro.html#installation) section.

Another handy (pip-installable) packages:

- [IPython](https://ipython.org/) - an enhanced interactive Python shell;

- [Jupyter notebook](https://docs.jupyter.org/en/latest/index.html) - just try it out and behold the opportunities.

### SQLite

[SQLite](https://www.sqlite.org/index.html) is a C-language library implementing SQL database engine.

The Python programming language has [sqlite3](https://docs.python.org/3/library/sqlite3.html) standard library module, but it is not designed for asynchronous code. That is the reason for referring to the [aiosqlite](https://pypi.org/project/aiosqlite/) DB API package.

See more about SQLite in SQLAlchemy in the [official docs](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html) details when you are ready.

### Hello, SQLAlchemy

Consider running the [sqla_introduction.py](./sqla_introduction.py) script several times. It is full with comments, docstrings and the superfluous-like output. Consider referring to the [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html) which is really helpful.

The following tutorials will be in the form of Jupyter notebooks: all the notes, drawings, and most importantly the code et cetera will be within one document.

**Homework**: the script deals with in-memory database mode. What about saving a database in a file and loading data from it? Enjoy:)

### Helpful links

- [VSCode: Python indentation settings](https://stackoverflow.com/questions/42118651/how-to-set-python-language-specific-tab-spacing-in-visual-studio-code)

- [SQLAlchemy ORM Tutorial: YouTube](https://www.youtube.com/playlist?list=PL4iRawDSyRvVd1V7A45YtAGzDk6ljVPm1)

- [SQLite in SQLAlchemy](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html)

- [aiosqlite docs](https://pypi.org/project/aiosqlite/)

- [asyncpg docs](https://magicstack.github.io/asyncpg/current/)
