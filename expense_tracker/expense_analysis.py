from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_relevant_chunks(df, query, vectorizer, top_n=3):
    text_data = df.to_string(index=False)
    chunks = text_data.split('\n')

    # Vectorizing text data
    vectors = vectorizer.fit_transform(chunks).toarray()
    query_vec = vectorizer.transform([query]).toarray()
    similarities = cosine_similarity(query_vec, vectors).flatten()

    top_indices = similarities.argsort()[-top_n:][::-1]
    return [chunks[i] for i in top_indices]
