"""SQL via SQLAlchemy.

The module with basic examples of using SQLAlchemy in asyncio code.
The docstring format is written according to the NumPy docstyle.

Read the program and its output carefully.
"""


import asyncio
import pathlib

import sqlalchemy as sqla
import sqlalchemy.ext.asyncio as async_sqla


SQLALCHEMY_VERSION = tuple(int(item) for item in sqla.__version__.split("."))


if SQLALCHEMY_VERSION < (2, 0, 0):
    raise ImportError("SQLAlchemy < 2.0")


def get_sqlite_engine(
    dbfile: pathlib.Path | str | None = None,
) -> async_sqla.AsyncEngine:
    """Returns the SQLite via aiosqlite DBAPI `sqlalchemy.Engine` object.

    The engine is typically a global object created
    just once for a particular database server,
    and is configured using a URL string
    which will describe how it should connect to the database host or backend.

    URL connection string:
    * SQLAlchemy dialect -> `sqlite` -> the kind of a database (DB)
    * DB API -> `aiosqlite` -> a third-party driver to interact with a DB
    * DB location - either a file or in-memory mode -> SQLite specific

    Returns
    -------
    sqlalchemy.Engine

    References
    ----------
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
    https://docs.sqlalchemy.org/en/20/tutorial/engine.html
    https://docs.sqlalchemy.org/en/20/glossary.html#term-dialect
    https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
    https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#module-sqlalchemy.dialects.sqlite.aiosqlite
    """

    db_loc = str(dbfile) if dbfile else ":memory:"
    constr: str = f"sqlite+aiosqlite:///{db_loc}"
    return async_sqla.create_async_engine(
        url=constr,
        connect_args={
            "check_same_thread": False,
        },
        echo=True,
    )


async def hello_sql(engine: async_sqla.AsyncEngine) -> None:
    """Performs `SELECT 'Hello, SQLAlchemy'` query.

    The sole purpose of the Engine object from a user-facing perspective
    is to provide a unit of connectivity to the database called the Connection.
    When working with the Core directly,
    the Connection object is how all interaction with the database is done.

    The ROLLBACK message at the end of the operation
    means that the latter does no affect/change the DB.
    Any changes within the context manager are rolled back
    unless they are commited explicitly.

    References
    ----------
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
    """

    async with engine.connect() as conn:
        request: sqla.TextClause = sqla.text("SELECT 'Hello, SQLAlchemy!'")
        result: sqla.CursorResult = await conn.execute(statement=request)
        print(f"Hello SQL Request: {request}")
        print(f"Hello SQL Result: {result.fetchone()}")


async def create_coords_table(engine: async_sqla.AsyncEngine) -> None:
    """Creates the table Coords with (x, y) attributes/columns.

    The Coords table is populated with values meaning 2D coordinates.
    When this script is over, if in memory mode, all changes will disappear.


    References
    ----------
    Basics of Statement Execution:
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#basics-of-statement-execution
    """

    tabname: str = "Coords"
    # `:x` is a placeholder for the `x` attribute/column in the Coords table
    ins_stmt: str = f"INSERT INTO {tabname} (x, y) VALUES (:x, :y)"
    async with engine.connect() as conn:
        await conn.execute(sqla.text(f"CREATE TABLE {tabname} (x float, y float)"))
        await conn.execute(
            statement=sqla.text(ins_stmt),
            parameters=[
                {"x": 0, "y": 0},
                {"x": 1.2, "y": 2.1},
                {"x": -2.1, "y": 4.2},
                {"x": -5, "y": -9},
                {"x": 9.9, "y": -13.2},
            ],
        )
        # Saving the results
        await conn.commit()
    # the "begin" style -> no need for explicit commits
    # the connection is returned, but with transaction mode enabled
    async with engine.begin() as transaction:
        await transaction.execute(
            statement=sqla.text(ins_stmt),
            parameters=[
                {"x": 100, "y": 200},
            ],
        )
    # ensuring all the previous data persist in the DB
    async with engine.connect() as conn:
        rows: sqla.CursorResult = await conn.execute(
            sqla.text(f"SELECT x, y FROM {tabname}")
        )
        for nth, row in enumerate(rows, 1):
            print(f"Row{nth}: (x: {row.x}, y: {row.y})")


async def main():
    """Main entry point.

    References
    -----------
    https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
    """

    print(f"SQLAlchemy version: {SQLALCHEMY_VERSION}")

    engine = get_sqlite_engine()

    print("\nQuery 1")
    await hello_sql(engine)
    print("\nQuery 2")
    await create_coords_table(engine)

    # it is mandatorily good to clean up resources
    print("\nSo long")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
