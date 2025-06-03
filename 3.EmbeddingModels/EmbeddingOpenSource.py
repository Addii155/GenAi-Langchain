from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding= HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)
sentences = [
    "Rohit Sharma is known for his elegant batting and holds the record for the highest individual score in ODIs (264 runs).",
    "Jasprit Bumrah is India's premier fast bowler, recognized for his deadly yorkers and unique bowling action.",
    "Ravindra Jadeja is a world-class all-rounder, famous for his quick fielding, tight bowling, and handy lower-order batting."
]
query_text = "Who is the best all-rounder in India?"

embeddings = embedding.embed_documents(sentences)
query_embedding= embedding.embed_query(query_text)

similarities = cosine_similarity([query_embedding], embeddings)[0]
 
index,similarity_score= sorted(list(enumerate(similarities)),key=lambda x: x[1])[-1]

print(f"Most similar sentence: {sentences[index]}")
print(f"Similarity score: {similarity_score:.4f}")