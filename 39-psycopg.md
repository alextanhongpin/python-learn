# Connect to psycopg

`db.py`:

```python
import psycopg
from psycopg.rows import namedtuple_row
from psycopg_pool import AsyncConnectionPool
from collections import namedtuple
from contextlib import asynccontextmanager
from typing import Callable

type Connection = psycopg.AsyncConnection
Session = Callable[[], Connection]


@asynccontextmanager
async def connect(url):
    """Create a connection pool."""
    if not url:
        raise ValueError("DATABASE_URL is not set")

    # Create a connection pool once.
    async with AsyncConnectionPool(url) as pool:

        @asynccontextmanager
        async def create_session() -> Connection:
            """Returns the connection and cursor."""
            async with pool.connection() as conn:
                # Set the row factory to namedtuple_row
                conn.row_factory = namedtuple_row

                yield conn

        yield create_session
```

`main.py`:

```python
import psycopg
import os
from db import Session, Connection, connect


async def add(conn: Connection, a: int, b: int) -> int:
    """Add two numbers."""
    result = await conn.execute("SELECT %(a)s + %(b)s as sum", dict(a=a, b=b))
    total = await result.fetchone()
    return total.sum


async def main():
    connstring = os.environ["DATABASE_URL"]
    async with connect(connstring) as Session:
        async with Session() as conn:
            result = await conn.execute("SELECT 1 + 1 as sum")
            total = await result.fetchone()
            print(total.sum)
            # The connection is autocommit, so no BEGIN executed.

            try:
                async with conn.transaction():
                    # BEGIN is executed, a transaction started
                    await conn.execute(
                        "INSERT INTO users(name) VALUES (%s)", ("Alice",)
                    )
                    await conn.execute(
                        "INSERT INTO users(name) VALUES (%s)", ("Charles",)
                    )
            except psycopg.errors.UniqueViolation:
                # This is a unique violation error
                # ROLLBACK is executed, the transaction is aborted
                pass
            # These two operation run atomically in the same transaction
            result = await conn.execute("SELECT * FROM users")
            users = await result.fetchall()
            print(users)
            # COMMIT is executed at the end of the block.
            # The connection is in idle state again.

        async with Session() as conn:
            print(await add(conn, 1, 2))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```
