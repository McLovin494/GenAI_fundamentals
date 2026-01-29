# i need my embedding model
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

openai_client = OpenAI(
    api_key="your api key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
# user query must be embedded using the same model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    embedding=embedding_model,
    collection_name="learning_rag",
)

# let us take user input
user_query = input("Ask something")
# now we would want to do a similarity search
# gives us relevant chunks
search_result = vector_db.similarity_search(query=user_query)


# from the vector db
context = "\n\n\n".join(
    [
        f"Page Content:{result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location:{result.metadata['source']}"
        for result in search_result
    ]
)

"\n\n\n"


SYSTEM_PROMPT = """
You are a helpful AI Assistant who answers user query based on the available context retrieved from a PDF file along with the page_contents and page number.

You should only ans the user based on the following context and navigate the user to open right page number to know more

Context:{context}
"""
response = openai_client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
)
print(f"🤖: {response.choices[0].message.content}")
