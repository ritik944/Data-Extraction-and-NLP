#%%
import os
import re 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
wl=WordNetLemmatizer()
#%%
stopwords_doc=[]

path=r"C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\StopWords"
os.chdir(path=path)
def read_text_file(file_path):
    with open(file_path,encoding='ISO-8859-1') as f:
        stopwords_doc.append(f.read().split('\n'))
    
    
for file in os.listdir():
    if file.endswith(".txt"):
        file_path= f"{path}\{file}"
        read_text_file(file_path)

from pandas.core.common import flatten
stopwords_doc=list(flatten(stopwords_doc))
#%%
class analysis:
    def master_dictonary(self):
        file_neg=open(r'C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\MasterDictionary\negative-words.txt','r',encoding='ISO-8859-1')
        file_neg=file_neg.read().split()
        
        file_pos=open(r'C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\MasterDictionary\positive-words.txt')
        file_pos=file_pos.read().split()

        return file_neg,file_pos
    
    def corpus(self,x):
        review=str(x).lower()
        review=re.sub('^[a-zA-Z]',' ',review).strip()
        review=word_tokenize(review)
        review=[wl.lemmatize(word) for word in review if word not in (stopwords_doc)]
        return review
    
    def count_Syllable(self,word):
        syllable=("a","e","i","o","u","y")
        exceptions=["es","ed"]
        count=0
        pre=False
        for exception in exceptions:
            if word.endswith(exception):
                return 0
            
        for char in word:
            if char in syllable:
                if not pre:
                    count+=1
                pre=True
            else:
                pre=False
        
        return count
    
    def count_syllable_per_word(self,words):
        num_syllable_per_word={word: self.count_Syllable(word) for word in words}
        return num_syllable_per_word
    
    def complex_word_count(self,words):
        num_complex=sum(1 for word in words if self.count_Syllable(word)>=2)
        total_words= len(words)
        precentage_complex_words=(num_complex/total_words)*100
        return precentage_complex_words,num_complex
    
    def Personal_Pronouns(self,words):
        presonal_words=("I", "we", "my","ours","us")
        count=0
        for char in words:
            if char in presonal_words:
                count+=1
        return count
    
    def avg_word_len(self,words):
        count=0
        for i in words:
            for j in i:
                 count+=1
        return count
    