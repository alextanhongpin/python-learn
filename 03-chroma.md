# Chroma basic usage

```python
import chromadb
from embedding import generate_embeddings

CHROMA_PATH = "./.chroma"
CHROMA_COLLECTION = "documents"

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = chroma_client.get_or_create_collection(name=CHROMA_COLLECTION)

print(collection.peek())
print(collection.count())

texts = ["a cute cat", "a big dog", "nice weather"]

embeddings = []
documents = []
metadatas = []
ids = []

for i, text in enumerate(texts):
    embeddings.append(generate_embeddings(text))
    documents.append(text)
    metadatas.append({"size": len(text)})
    ids.append(str(i + 1))

collection.upsert(
    embeddings=embeddings, documents=documents, metadatas=metadatas, ids=ids
)


results = collection.query(
    query_embeddings=[generate_embeddings("cat me")],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"},
    # where_document={"$contains": "search string"},
)

print(results)
# By default, embeddings is None.
# To return it, do `collection.get(ids=['2'], include=['embeddings'])`
# collection.get(ids=["id1", "id2"], where={"style": "style1"})
```
