import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

def clean_html(text):
    #html = re.compile('<.*?>')#regex
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+', '', text) # remove http links
    text = re.sub(r'bit.ly/\S+', '', text) # remove bitly links
    text = text.strip('[link]') # remove [links]
    return text

# remove non ascii character
def non_ascii(s): 
    # non ascii example: Ñ 
    return "".join(i for i in s if ord(i)<128)

def lower(text):
    return text.lower()

# remove email address
def email_address(text):
    email = re.compile(r'[\w\.-]+@[\w\.-]+')
    return email.sub(r'',text)

def punct(text):
  text = re.sub(r'[^\w\s]', '', text)
  return text

# remove stopwords
def removeStopWords(str):
    #select english stopwords
    cachedStopWords = set(stopwords.words("english"))
    #add custom words
    cachedStopWords.update(('and','I','A','http','And','So','arnt','This','When','It','many','Many','so','cant','Yes','yes','No','no','These','these','mailto','regards','ayanna','like','email'))
    #remove stop words
    new_str = ' '.join([word for word in str.split() if word not in cachedStopWords]) 
    return new_str

def remove_underscore(text):
    text = re.sub('([_]+)', "", text)
    return text

def stemming(text):
    stem_text = ''.join([porter_stemmer.stem(word) for word in text])
    return stem_text

def lemmatizer(text):
    lemm_text = ''.join([wordnet_lemmatizer.lemmatize(word) for word in text])
    return lemm_text

if __name__ == "__main__":
    text = "This is a link <https://no?> it is. This movie deserves the 10 I'm giving it.<br /><br />But it's not the 10 that you'd give to movies like 'The Godfather"
    print(clean_html(text))
    print(non_ascii('this is %1 Ñ'))
    print(email_address('hj96998@gmail sd'))
    print(punct(text))
    print(removeStopWords("this is not a good_ _thing"))
    print(remove_underscore("this is not a good_ _thing"))