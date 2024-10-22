# Sqlite3

https://remusao.github.io/posts/few-tips-sqlite-perf.html

## Commit



If you do any mutations, make sure to run commit on `Connection`, not `Cursor`.


## Connecting

```python
con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute("insert into ...")
con.commit()
```

## Getting last id

```python
con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute(
		"""
		INSERT INTO documents (full_path, content, content_hash)
		VALUES (?, ?, ?)
		RETURNING id
		""",
		(full_path, content, content_hash),
)
row = cur.fetchone()
(inserted_id,) = row if row else None
con.commit()
```

If you are using `sqlite3.Row` as the `row_factory`:

```python
row = cur.fetchone()
inserted_id = row["id"] if row else None
self.con.commit()
```


## Returning Dict instead of tuple


By default, sqlite3 returns the result as tuple instead of dict. To override it:

```
con.row_factory = sqlite3.Row
```

You can set it at `Connection` or `Cursor` level.
The latter will not affect the former.

Example:

```python
con = sqlite3.connect('test.db')
con.row_factory = sqlite3.Row

cur = con.cursor()
res = cur.execute("select 1 + 1 as count")
print(dict(res.fetchone()))
con.commit()
```

## Pydantic

To convert to pydantic:

```python
from pydantic import BaseModel


class Doc(BaseModel):
    id: int
    full_path: str
    content: str
    content_hash: str
    created_at: datetime
    updated_at: datetime


def doc_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return Doc(**{k: v for k, v in zip(fields, row)})


cur.row_factor = doc_factory
```

Or after obtaining the result, just do a conversion:
```python
res = cur.fetchone()
Doc(**res)
```
