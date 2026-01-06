from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


txt_loader = TextLoader('cricket.txt', encoding='utf-8')

docs = txt_loader.load()

llm = HuggingFaceEndpoint(
    repo_id= "moonshotai/Kimi-K2-Thinking",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

chain = prompt | model | parser
output = chain.invoke({'poem': docs[0].page_content})

print(docs)
# print(docs[0])

print("\n")
print(type(docs))
print(len(docs))
print("\n")
print(output)