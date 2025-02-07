from util.label_encoder import encode_labels
from util.preprocess import process_text
from util.read_csv import read_csv
from util.vectorizer import vectorize_text
from sklearn.naive_bayes import MultinomialNB
import pickle

def main():
    # Load and preprocess data
    data = read_csv('data/flipitnews-data.csv')
    data['Article'] = data['Article'].apply(process_text)
    data, label_encoder = encode_labels(data, 'Category')

    # Vectorize the text using bag of words
    X,vectorizer = vectorize_text(data['Article'], method='bow')
    y = data['Category']

    # Train the model
    model = MultinomialNB()
    model.fit(X, y)

    # Save the label encoder and model
    with open('models/label_encoder.pkl', 'wb') as file:
        pickle.dump(label_encoder, file)

    
    with open('models/classifier.pkl', 'wb') as file:
        pickle.dump(model, file)

    with open('models/vectorizer.pkl', 'wb') as file:
        pickle.dump(vectorizer, file)
        
if __name__ == "__main__":
    main()