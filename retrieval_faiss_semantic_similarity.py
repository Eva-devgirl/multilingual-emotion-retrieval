import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from preprocessing import load_greek_chunks

def retrieval():
	chunks = load_greek_chunks()

	model = SentenceTransformer("intfloat/multilingual-e5-base")

	passages = ["passage: " + chunk for chunk in chunks[:1000]]

	embeddings = model.encode(passages, normalize_embeddings=True)

	#create faiss index
	dimension = embeddings.shape[1]
	index = faiss.IndexFlatIP(dimension)
	index.add(embeddings)

	#I am very happy today
	#I am very sad today
	queries = ["Είμαι πολύ χαρούμενη σήμερα",
	  "Eίμαι πολύ λυπημένη σήμερα"
	]

	query_embeddings = model.encode(queries, normalize_embeddings=True)

	# convert for faiss
	query_embedding = np.array(query_embeddings).astype("float32")

	#retrieval
	scores, indices = index.search(query_embedding, k=5)

	print("Query:", queries)
	print("\nTop 5 similar chunks:")

	for query, query_scores, query_indices in zip(queries, scores, indices):
		print("\nQuery:", query)
		for score, idx in zip(query_scores, query_indices):
			print("\nScore:", score)
			print("Text:", chunks[idx])

	return scores, indices

def main():
	retrieval()

if __name__ == "__main__":
	main()

