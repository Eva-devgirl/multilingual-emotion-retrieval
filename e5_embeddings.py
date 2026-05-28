import pandas as pd
from sentence_transformers import SentenceTransformer
from preprocessing  import load_greek_chunks

def create_embeddings():
	# model e5-base load
	model = SentenceTransformer("intfloat/multilingual-e5-base")

	chunks = load_greek_chunks()

	# passage is a special format of e5-models
	# sentence = passage = chunk
	passages = ["passage: " + chunk
	    for chunk in chunks[:100]
	]

	# create embeddings
	embeddings = model.encode(passages, normalize_embeddings=True)

	return passages, embeddings


if __name__ == "__main__"git :
	passages, embeddings = create_embeddings()
	print("Number of chunks: ", len(passages))
	print("Embedding shape for the first 100 chunks:", embeddings.shape)
	print("First 10 Values for the first Embedding:", embeddings[0][:10])


