# Connect to psycopg

```python
import psycopg
from psycopg.rows import namedtuple_row
from psycopg_pool import AsyncConnectionPool
import os
from collections import namedtuple
from contextlib import asynccontextmanager

Session = namedtuple("Session", ["connection", "cursor"])


@asynccontextmanager
async def connect(url=os.environ["DATABASE_URL"]):
    """Create a connection pool."""

    # Create a connection pool once.
    async with AsyncConnectionPool(os.getenv("DATABASE_URL")) as pool:

        @asynccontextmanager
        async def session():
            """Returns the connection and cursor."""
            async with pool.connection() as conn:
                # The connection is in autocommit mode by default
                # You can use a row factory to get dict rows
                async with conn.cursor(row_factory=namedtuple_row) as cur:
                    yield Session(connection=conn, cursor=cur)

        yield session


async def add(session: Session, a: int, b: int) -> int:
    """Add two numbers."""
    result = await session.cursor.execute("SELECT %(a)s + %(b)s as sum", dict(a=a, b=b))
    total = await result.fetchone()
    return total.sum


async def main():
    async with connect() as session:
        async with session() as (conn, cur):
            result = await cur.execute("SELECT 1 + 1 as sum")
            total = await result.fetchone()
            print(total.sum)
            # The connection is autocommit, so no BEGIN executed.

            try:
                async with conn.transaction():
                    # BEGIN is executed, a transaction started
                    await cur.execute(
                        "INSERT INTO users(name) VALUES (%s)", ("Thunder",)
                    )
                    await cur.execute("INSERT INTO users(name) VALUES (%s)", ("Bob",))
            except psycopg.errors.UniqueViolation:
                # This is a unique violation error
                # ROLLBACK is executed, the transaction is aborted
                pass
            # These two operation run atomically in the same transaction
            result = await cur.execute("SELECT * FROM users")
            users = await result.fetchall()
            print(users)
            # COMMIT is executed at the end of the block.
            # The connection is in idle state again.

        print("adding with session")
        async with session() as sess:
            print(await add(sess, 1, 2))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```
