import pandas as pd
import re
import nltk


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #import Indonesian Stemmer




nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


lemma = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words('indonesian','english'))        


def Cleantweet(txt):
    txt = re.sub(r'http\s+', ' ', txt)
    txt = re.sub('[^a-zA-Z]', ' ', txt)
    txt = str(txt).lower()
    txt = word_tokenize(txt)
    txt = [item for item in txt if item not in stop_words]
    txt = [stemmer.stem(i) for i in txt]
    # txt = [lemma.lemmatize(word=w,pos='v') for w in txt]
    txt = [i for i in txt if len(i) > 2]
    txt = ' '.join(txt)
    return txt
