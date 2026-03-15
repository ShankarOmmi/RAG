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

    # retriever = vector_store.as_retriever(search_kwargs={"k": TOP_K})
    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": TOP_K, "lambda_mult": 0.5})

    llm = HuggingFaceEndpoint(
        repo_id=LLM_MODEL,
        task="conversational",
        temperature=0.5,
        max_new_tokens=512
    )

    model = ChatHuggingFace(llm=llm)

    prompt = PromptTemplate(
        template="""
    You are an assistant answering questions about a YouTube video using the provided transcript.

    Follow these rules strictly:

    1. Base your answer ONLY on the provided context.
    2. You may summarize or combine information from the context.
    3. Do NOT use outside knowledge.
    4. Keep the answer concise (1–3 sentences).

    If the context does NOT contain enough information to answer the question, respond EXACTLY with:

    The video does not contain information to answer this question.

    If the question is unrelated to the video topic, respond EXACTLY with:

    This question is not related to the content of the video.

    Do NOT explain your reasoning.
    Do NOT add extra sentences after the response.

    Context:
    {context}

    Question:
    {question}

    Answer:
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