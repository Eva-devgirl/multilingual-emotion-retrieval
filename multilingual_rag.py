import pandas as pd
from pathlib import Path

#separate the languages for easier retrieval 
df_el = pd.read_csv("data/el-projections.tsv", sep="\t", header = None)
df_ru = pd.read_csv("data/ru-projections.tsv", sep="\t", header = None)
df_de = pd.read_csv("data/de-projections.tsv", sep="\t", header = None)
df_zh = pd.read_csv("data/zh-projections.tsv", sep="\t", header = None)

#assign column names
df_el.columns = ["text", "labels"]
df_ru.columns = ["text", "labels"]
df_de.columns = ["text", "labels"]
df_zh.columns = ["text", "labels"]

#each senence is treated as one chunk
chunks = df_el["text"].tolist()

print(df_el.head())
print(df_el.shape)

#print(df_ru.head())
#print(df_ru.shape)

#print(df_de.head())
#print(df_de.shape)

#print(df_zh.head())
#print(df_zh.shape)


