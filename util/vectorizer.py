from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
def vectorize_text(text_data, method='bow'):
    if method == 'bow':
        vectorizer = CountVectorizer()
    elif method == 'tfidf':
        vectorizer = TfidfVectorizer()
    else:
        raise ValueError("Method should be 'bow' or 'tfidf'")

    X = vectorizer.fit_transform(text_data)

    return X ,vectorizer