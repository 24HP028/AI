import os
import openai
import sys
import json
import tiktoken
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ["OPENAI_API_KEY"] = 'sk-키 추가'

os.environ["TOKENIZERS_PARALLELISM"] = "false"

tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")

def tiktoken_len(text):
    tokens = tokenizer.encode(text)
    return len(tokens)

loader = PyPDFLoader("data/(2024)포트미스+가이드북.pdf")
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, length_function=tiktoken_len)
texts = text_splitter.split_documents(pages)

model_name = "jhgan/ko-sbert-nli"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

docsearch = Chroma.from_documents(texts, hf)

openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    streaming=False, 
    temperature=0
)

qa = RetrievalQA.from_chain_type(
    llm=openai,
    chain_type="stuff",
    retriever=docsearch.as_retriever(
        search_type="mmr",
        search_kwargs={'k': 3, 'fetch_k': 10}
    ),
    return_source_documents=True
)

def get_response(input_text):
    return qa.invoke({"query": input_text})

if __name__ == "__main__":
    input_text = sys.argv[1]
    try:
        chat_response = get_response(input_text)
        output = {
            "status": 200,
            "message": "채팅 응답 성공",
            "body": {
                "chatMessage": chat_response["result"]
            }
        }
    except Exception as e:
        output = {
            "status": 404,
            "message": "채팅 응답 실패",
            "body": {
                "error": str(e)
            }
        }
    
    print(json.dumps(output, ensure_ascii=False, indent=4))
