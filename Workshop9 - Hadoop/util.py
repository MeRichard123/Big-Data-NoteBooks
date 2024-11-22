import nltk
from nltk.corpus import stopwords
import re
nltk.download('stopwords')
ENGLISH_STOP_WORDS = set(stopwords.words('english'))


def word_not_in_stopwords(word):
    return word not in ENGLISH_STOP_WORDS and word and word.isalpha()


def clean_word(word):
    return re.sub(r'[^\w\s]','',word).lower()


def split_data_into_chunks(data, chunk_size):
    return list(chunkify(data, chunk_size))

def chunkify(data, n):
    for i in range(0, len(data), n):
        yield (data[i:i + n])
