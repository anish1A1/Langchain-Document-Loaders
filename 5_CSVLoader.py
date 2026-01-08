from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("Social_Network_ads.csv")
docs = loader.load()
print(len(docs))
print(docs[0])
print(docs[1].page_content)
