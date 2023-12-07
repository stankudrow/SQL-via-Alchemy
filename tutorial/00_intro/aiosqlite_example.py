import asyncio

import aiosqlite


URL: str = ":memory:"


INTRO_SQL_SCRIPT: str = """
CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY,  -- no AUTOINCREMENT is needed
    name NVARCHAR(120)
);

INSERT INTO playlists (name)
VALUES ('SQL Rocks!'), ('SQLite as well');
"""


async def main():
    """Entry point."""

    db: aiosqlite.Connection = await aiosqlite.connect(URL)

    await db.executescript(INTRO_SQL_SCRIPT)

    async with db.execute("SELECT * FROM playlists;") as cursor:
        async for row in cursor:
            print(f"Row = {row}")
        print()

    await db.close()

    print("Good bye!")


if __name__ == "__main__":
    asyncio.run(main())
