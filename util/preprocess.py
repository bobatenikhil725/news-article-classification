import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required nltk data if not already done
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def process_text(text):
    # Preserve numbers, basic punctuation, and domain-specific symbols
    text = re.sub(r'[^a-zA-Z0-9\s\@\#\-\.\$%]', ' ', text)

    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join the words back into a single string
    return ' '.join(words)