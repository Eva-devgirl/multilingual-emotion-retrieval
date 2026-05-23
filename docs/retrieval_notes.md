
# Retrieval Notes

## Dataset

We use the XED annotated dataset

Languages: Greek, Russian, German, Chinese

## Chunking 

In XED 1 chunk = 1 sentence

## Embeddings

We use multilingual-e5
- multilingual embeddings
- support all four languages
- semantic retrieval

## Retrieval

- FAISS : similarity search between embeddings

## planned pipeline
Text -> chunk -> Embedding -> FAISS Index -> similarity retrieval

## Current progress

So far, we have implented the first retrieval prototype steps:

1. Loaded the Greek, Russian, German and Chinese XED dataset
2. Applied basic preprocessing only for the Greek one (to explore how it works)
3. Used Sentence level chunking
4. Loaded the e5-multilingual-base 
5. Generated embeddings for the first 100 Greek chunks (sentences).  
6. TO DO : FAISS-based retrieval

## Current limitations

At this point the system retrieves semantically similar sentences.

The emotion labels are available in XED dataset, but they are still not included.

