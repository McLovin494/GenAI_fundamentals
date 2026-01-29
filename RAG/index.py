# responsible for indexing the data
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from sentence_transformers import SentenceTransformer

pdf_path = Path(__file__).parent / "dsa.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs = (
    loader.load()
)  # every single page, we are getting page by page, gives pages, we can iterate over this

# split the docs into smaller chunks
# take some from previous chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
chunks = text_splitter.split_documents(documents=docs)

## create vector embeddings for the chunks
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
)
print("Indexing of documents done.....")
