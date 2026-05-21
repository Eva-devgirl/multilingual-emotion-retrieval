import pandas as pd

df_el = pd.read_csv("data/el-projections.tsv", sep="\t")

df_el.columns = ["text", "labels"]

chunks = df_el["text"].dropna().astype(str).str.strip()

chunks = chunks[chunks != ""].tolist()

print(len(chunks))
print(chunks[:5])
