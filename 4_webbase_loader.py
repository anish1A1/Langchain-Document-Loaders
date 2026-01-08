from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

URL = "https://www.flipkart.com/apple-iphone-16-black-128-gb/p/itmb07d67f995271?pid=MOBH4DQFG8NKFRDY&lid=LSTMOBH4DQFG8NKFRDYNBDOZI&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=default_BestsellerId_tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=b5fe0a1e-3f75-4e4f-acf9-7c59eab1afd8.MOBH4DQFG8NKFRDY.SEARCH&ppt=browse&ppn=browse&ssid=jyhkuqa1uo0000001767840733274"


loader = WebBaseLoader(URL)
docs = loader.load()



llm = HuggingFaceEndpoint(
    repo_id= "moonshotai/Kimi-K2-Thinking",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text  - \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

chain = prompt | model | parser
output = chain.invoke({'question': 'What is the Rating of this product?' ,'text': docs[0].page_content})

# print(docs)
# print(len(docs))
# print(docs[0].page_content)

print("\n Output -> ", output)