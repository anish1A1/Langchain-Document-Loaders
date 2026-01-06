from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

txt_loader = TextLoader('cricket.txt', encoding='utf-8')
docs = txt_loader.load()
llm = HuggingFaceEndpoint(
    repo_id= "moonshotai/Kimi-K2-Thinking",
    task="text-generation"
)

print(docs)
# print(docs[0])



print("\n")
print(type(docs))
print(len(docs))
