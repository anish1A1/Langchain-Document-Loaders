from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
# print(docs)
print(docs[0])
print("\n",docs[3].page_content)
print("\n", docs[348].metadata)



print("\n Total length/pages of all pdfs", len(docs))
