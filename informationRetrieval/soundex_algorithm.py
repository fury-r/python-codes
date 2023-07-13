import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os

from nltk.corpus import stopwords

def get_files(path):
    p=os.listdir(path)
    book=[]
    print(f"{p}  list of file")
    for i in p:
        if i.endswith('.txt'):
            with open(path+"/"+str(i),'r') as f:
                book.append(f.read().lower())

    return book,p

def apply_soundex_algorithm(word):
    word = word[:1].upper()+word[1:].lower()
    codes = {
        'b': 1, 'f': 1, 'p': 1, 'v': 1, 'c': 2, 'g': 2, 'j': 2, 'k': 2, 'q': 2, 's': 2, 'x': 2, 'z': 2, 'd': 3, 't': 3, 'l': 4, 'm': 5, 'n': 5, 'r': 6
    }
    coded_output = ''
    vowel = 'aeiou'
    for i in word:
        if i in codes:
            coded_output += str(codes[i])
        elif i not in vowel:
            coded_output += i
    if len((coded_output[:4])) < 4:
        coded_output = coded_output[:4]+"0"*(4-len(coded_output[:4]))
    return coded_output[:4]


def process_data(file):
    matrix = {}
    stop = stopwords.words('english')

    file = word_tokenize(" ".join(file))
    print(file)
    for word in file:
        if word not in string.punctuation and word not in stop:
            word = word[:1].upper()+word[1:].lower()
            hash = apply_soundex_algorithm(word)

            if hash not in matrix:
                matrix[hash] = word
            else:
                if word not in matrix[hash]:
                    matrix[hash] += " "+word
    return matrix


def check_correction(matrix, s):
    z = apply_soundex_algorithm(s)
    print(z)
    if z in matrix.keys():

        return "Did you mean any of these [ "+matrix[z]+" ]"


file_data, _ = get_files('exp')

print(file_data)
matrix = process_data(file_data)
# matrix=create_matrix(['Bangalore']+file_data.keys())

print(check_correction(matrix, input("Query ")))
