# Retrieval Notes

Goal of the project : It investigates retrieval-based example selection for multilingual emotion classification

## Dataset

We use the XED annotated dataset because all languages for our project are inluded.

Languages: Greek, Russian, German, Chinese

## Chunking 

In XED 1 chunk = 1 sentence

## Embeddings

We use multilingual-e5-base at the prototype retrieving part because its easy to handle with and we will change to multilingual-e5-large

- multilingual embeddings
- support all four languages

## Retrieval

- FAISS : dense semantic similarity search between embeddings
- bm25: lexical similarity search in tokens

## planned pipelines

Text -> sentence chunks -> Embeddings -> FAISS Index -> similarity retrieval
Text -> sentence chunks -> tokens -> bm25 -> lexical retrieval

## Current progress

So far, we have implemented the first retrieval prototype:

1. Loaded the Greek, Russian, German and Chinese XED dataset
2. Applied basic preprocessing only for the Greek one (to explore how it works)
3. Used sentence-level chunking for both FAISS and bm25
4. Loaded the e5-multilingual-base (https://huggingface.co/intfloat/multilingual-e5-base)
5. Generated dense embeddings for the first 1000 Greek chunks (sentences).  
6. Implemented semantic retrieval using FAISS (https://ai.meta.com/tools/faiss/). FAISS uses mathematical shortcuts, clustering, 
   and advanced indexing to filter the search space and retrieve nearest neighbors in milliseconds. 
7. Implemented lexical retrieval using BM25 (it takes tokens/words, not embeddings)  
8. Queries in Greek: query_1 for joy, query_2 for sadness
8. Scores for the top 5


## Current limitations

1. The emotion labels are available in XED dataset, but they are still not integrated into the retrieval pipelines.
2. The prototype currently uses only 1000 examples from the Greek dataset for testing.
3. No retrieval evaluation has been done.


## To do

1. Same procedure for all languages
2. Use the labels for emotions joy, sadness, surprise, fear, anger
3. Future evaluation of retrieval quality using ndcg metric. It measures how good a ranking is by considering both the relevance and position.







