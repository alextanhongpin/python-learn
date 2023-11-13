# Unstructure library loading Markdown

```python
from langchain.document_loaders import UnstructuredMarkdownLoader

markdown_path = "DESIGN.md"


loader = UnstructuredMarkdownLoader(markdown_path)
docs = loader.load()

print(docs)

for doc in docs:
    print()
    print("Page Content:")
    print(doc.page_content)

    print("Metadata:")
    print(doc.metadata)
```
