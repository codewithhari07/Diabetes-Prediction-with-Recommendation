from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k":3}
)

def retrieve_context(question):

    docs = retriever.invoke(question)

    context = ""

    sources = []

    for doc in docs:

        context += doc.page_content + "\n\n"

        if "source" in doc.metadata:
            sources.append(doc.metadata["source"])

    return context, list(set(sources))