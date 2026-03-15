from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from config import *

load_dotenv()

def build_rag(transcript):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = splitter.create_documents([transcript])

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_store = FAISS.from_documents(docs, embeddings)

    retriever = vector_store.as_retriever(search_kwargs={"k": TOP_K})

    llm = HuggingFaceEndpoint(
        repo_id=LLM_MODEL,
        task="conversational",
        temperature=0.5,
        max_new_tokens=512
    )

    model = ChatHuggingFace(llm=llm)

    prompt = PromptTemplate(
        template="""
You are a helpful assistant.

Use ONLY the provided context to answer.

Context:
{context}

Question:
{question}
""",
        input_variables=["context", "question"]
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | prompt
        | model
        | StrOutputParser()
    )

    return chain