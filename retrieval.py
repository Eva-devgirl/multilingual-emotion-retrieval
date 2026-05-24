import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from preprocessing import load_greek_chunks

chunks = load_greek_chunks()

model = SentenceTransformer("intfloat/multilingual-e5-base")

passages = ["passage: " + chunk for chunk in chunks[:100]]

embeddings = model.encode(passages, normalize_embeddings=True)

#create faiss index
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

query = "query: Είμαι πολύ χαρούμενη σήμερα"

query_embedding = model.encode([query], normalize_embeddings=True)

# convert for faiss
query_embedding = np.array(query_embedding).astype("float32")

#retrieval 
scores, indices = index.search(query_embedding, k=5)

print("Query:", query)
print("\nTop 5 similar chunks:")

for score, idx in zip(scores[0], indices[0]):
	print("\nScore:", score)
	print("Text:", chunks[idx])
