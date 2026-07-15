from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

urls = [
    "https://www.who.int/news-room/fact-sheets/detail/diabetes",
    "https://www.cdc.gov/diabetes/",
    "https://www.cdc.gov/diabetes/prevention/index.html",
    "https://www.cdc.gov/diabetes/living-with/index.html",
    "https://www.niddk.nih.gov/health-information/diabetes",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/symptoms-causes",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/tests-diagnosis",
    "https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-type-2-diabetes"
]

documents = []

for url in urls:
    try:
        print("Loading:", url)
        loader = WebBaseLoader(url)
        documents.extend(loader.load())
    except Exception as e:
        print(e)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.from_documents(docs, embeddings)

vector_db.save_local("vector_db")

print("Vector database created successfully.")