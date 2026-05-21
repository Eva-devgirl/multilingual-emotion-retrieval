
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

