#Anzahl Satzzeichen, Wörter, Zeilen, Sätze

import sklearn as sk
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import sys
import codecs



doc_path = "C:/Users/Mark/Desktop/schreibtisch/MasterINGINF/ATiML/Gutenberg_English_Fiction_1k/Gutenberg_English_Fiction_1k/Gutenberg_19th_century_English_Fiction/"
working_path = ""
meta = pd.read_csv(working_path+"Gutenberg_English_Fiction_1k/master996.csv", sep=";", header=0, encoding='latin1')
  
#Extract target Variable and filenames
target = meta["guten_genre"]
book_id = meta["book_id"]
filenames = [doc_path+id.split(".")[0]+"-content.html" for id in book_id]
file = codecs.open(filenames[0], "r", "utf-8").read()

file_ = [id for id in book_id]


rm = []

for q in range(len(filenames)-3):
    
    file = codecs.open(filenames[q], "r", "utf-8").read()
    words_ = len(file.split())
    
    if words_ <= 0:
    
        # rm.append(q)
        del filenames[q:q+1]
        del file_[q:q+1]


def num_words(name_list):

     
        word_num = []
        
        for q in range(len(name_list)):
        
            file = codecs.open(name_list[q], "r", "utf-8").read()

            words = len(file.split())
            
            
            
            word_num.append(words)
            
        return word_num
        

def num_lines(name_list):

        line_num = []
        for q in range(len(name_list)):
            file = codecs.open(name_list[q], "r", "utf-8").read()
            
            lines = file.count('<p>')
            
            line_num.append(lines)
            
        return line_num
        
def num_punctuation(name_list):

        punct_num = []
        for q in range(len(name_list)):
            file = codecs.open(name_list[q], "r", "utf-8").read()
            words = len(file.split())
            
            punct_1 = file.count(':') 
            punct_2 = file.count(',')
            punct_3 = file.count('"')
            punct_4 = file.count('/')
            punct_5 = file.count('(')
            punct_7 = file.count('[')
            punct_9 = file.count('{')
            punct_11 = file.count(';')
            punct_12 = file.count('&')
            punct_13 = file.count('-')
            punct = punct_1+punct_2+punct_3+punct_4+punct_5+punct_7+punct_9+punct_11+punct_12+punct_13
            
            
            
            # if words > 0:
            
            rel_punct = punct/words
            punct_num.append(rel_punct)
                
        return punct_num    
        
def num_sent(name_list):

        sent_num = []
        for q in range(len(name_list)):
            file = codecs.open(name_list[q], "r", "utf-8").read()
            words = len(file.split())
            
            sent_1 = file.count('.') 
            sent_2 = file.count('!')
            sent_3 = file.count('?')
     
            sent = sent_1+sent_2+sent_3
            
            
            
            # if words > 0:
            rel_sent = words/sent
            sent_num.append(rel_sent)
            
        return sent_num 



words = np.array(num_words(filenames))
punct = np.array(num_punctuation(filenames))
lines = np.array(num_lines(filenames))
sent = np.array(num_sent(filenames))


        
filenames = np.array(file_)

data_ndarray = np.stack((file_, words, lines, punct, sent ), axis = 1)
# data_ndarray = np.concatenate((sentiment_features, data_ndarray), axis=1)

# print(filenames.shape, words.shape, lines.shape, punct.shape, sent.shape )

features = pd.DataFrame(data_ndarray, columns=["Filename","Number of Words", "Number of Paragraphs", "Relative Punctuation", "Average Words per Sentence"])

features.to_csv("features_mark.csv", index=False)


# index = a.index(min(a))



    