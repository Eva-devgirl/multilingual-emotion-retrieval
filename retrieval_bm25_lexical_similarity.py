from rank_bm25 import BM25Okapi
from preprocessing import load_greek_chunks

def tokenize(text):
    return text.lower().split()

def bm25_retrieval():
    chunks = load_greek_chunks()
    chunks = chunks[:1000]

    tokenized_chunks = [tokenize(chunk) for chunk in chunks]

    bm25 = BM25Okapi(tokenized_chunks)


    queries = [
        "Είμαι πολύ χαρούμενη σήμερα",
        "Είμαι πολύ λυπημένη σήμερα"
    ]

    for query in queries:
        tokenized_query = tokenize(query)

        scores = bm25.get_scores(tokenized_query)

        top_indices = scores.argsort()[-10:][::-1]

        print("\nQuery:", query)
        print("Top 5 BM25 results:")

        for idx in top_indices[:5]:
            print("\Score:", scores[idx])
            print("Text:", tokenized_chunks[idx])

def main():
    bm25_retrieval()

if __name__ == "__main__":
    main()

