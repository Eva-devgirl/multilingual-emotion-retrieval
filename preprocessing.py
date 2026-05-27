import pandas as pd

def load_greek_chunks(): 
	df_el = pd.read_csv("data/el-projections.tsv", sep="\t", header=None)

	df_el.columns = ["text", "labels"]

	chunks = df_el["text"].dropna().astype(str).str.strip()

	chunks = chunks[chunks != ""].tolist()

	return chunks

def main():	
	chunks = load_greek_chunks()
	
	print(len(chunks))
	print(chunks[:5])
	
if __name__ == "__main__":
	main():
