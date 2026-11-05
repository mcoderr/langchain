from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from typing import Iterator

class CSVLoader(BaseLoader):
    """Custom loader that reads a CSV and creates one Document per row."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def lazy_load(self) -> Iterator[Document]:
        import csv
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                yield Document(
                    page_content=str(row),
                    metadata={"source": self.file_path, "row": i}
                )

# Usage
loader = CSVLoader("customers.csv")
docs = loader.load()             # Loads all at once
# or
for doc in loader.lazy_load():   # Memory-efficient streaming
    print(doc)