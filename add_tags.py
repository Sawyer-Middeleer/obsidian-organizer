import operator, collections, os, sys, re, string, nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tabulate import tabulate

rootdir = "/Users/sawyer/Documents/sawyerm"
target = sys.argv[1]

similarity_threshold = 0.1

stop_words = set(stopwords.words('english'))
md_regex = re.compile(r'.*md$')
tag_regex = re.compile(r'#([-_\d\w]+)')
link_regex = re.compile(r'\[\[(.*?)[|#]')


def read(file):
    with open(file, 'r') as f:
        content = f.read()
        f.close()
    return content.lower()

def remove_numbers(input_str):
    result = re.sub(r'\d+', '', input_str)
    return result

def remove_whitespace(input_str):
    result = re.sub(r'[\t\n\r]', '', input_str)
    return result    

def remove_punctuation(input_str):
    result = input_str.translate(str.maketrans('', '', string.punctuation))
    return result

def remove_stopwords(input_str):
    tokens = word_tokenize(input_str)
    result = [i for i in tokens if not i in stop_words]
    return result

def preprocess(file):
    return remove_stopwords(remove_whitespace(remove_punctuation(remove_numbers(read(file)))))

raw_target = read(sys.argv[1])
preprocessed_target = preprocess(sys.argv[1])