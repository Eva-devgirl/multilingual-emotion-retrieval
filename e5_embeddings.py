import pandas as pd
from sentence_transformers import SentenceTransformer

#model e5-base load
model = SentenceTransformer("intfloat/multilingual-e5-base")

#greek dataset load
df_el = pd.read_csv("data/el-projections.tsv", sep="\t")

df_el.columns = ["text", "labels"]

#chunking
#in XED 1 chunk = 1 sentence
#chunks = sentences
chunks = df_el["text"].tolist()

#create embeddings 
embedding = model.encode(chunks)

print(len(chunks))
print(similarities.shape)
