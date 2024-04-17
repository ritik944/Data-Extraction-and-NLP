#%%
import nltk
import pandas as pd
from text_analysis import analysis
#%%
class output_variables:
    
    def primary(self,data):
        output=[]
        list=[]
        for i,j,k in zip(data['URL'],data['URL'],data['artical']):
            pre_process_words=analysis().corpus(k)
            
            neg_data,pos_data= analysis().master_dictonary()
            
            #1 positive score
            pos_count=[]
            for word in pre_process_words:
                if word in pos_data:
                    pos_count.append(word)
            pos_score=len(pos_count)
            
            #2 negative score 
            neg_count=[]
            for word in pre_process_words:
                if word in neg_data:
                    neg_count.append(word)
            neg_score=len(neg_count)
            
            #3 	POLARITY SCORE
            polarity_score=(pos_score - neg_score)/((pos_score+neg_score)+0.000001)
            
            #4.	SUBJECTIVITY SCORE
            subjective_score=(pos_score+neg_score)/(len(pre_process_words)+0.000001)
            
            #5.	AVG SENTENCE LENGTH
            total_sen=len(nltk.sent_tokenize(k))
            avg_sentence_len=round(len(pre_process_words)/total_sen,0)
            
            #6.	PERCENTAGE OF COMPLEX WORDS 
            precent_of_complex_words,total_num_of_complex_word=analysis().complex_word_count(pre_process_words)
            
            #7 fog index
            fog_index=0.4*(avg_sentence_len+precent_of_complex_words)
            
            #8 	AVG NUMBER OF WORDS PER SENTENCE
            avg_no_word_pre_sentence=round(len(k.split())/total_sen,0)
            
            #9 	COMPLEX WORD COUNT
            total_num_of_complex_word
            
            #10 word count
            word_count=len(pre_process_words)
            
            #11 SYLLABLE PER WORD
            syllable_per_word=analysis().count_syllable_per_word(pre_process_words)
            
            #12	PERSONAL PRONOUNS
            presonal_pro=analysis().Personal_Pronouns(nltk.word_tokenize(k))
            
            #13 avg word length
            word_len=analysis().avg_word_len(pre_process_words)
            avg_word_len=round(word_len/len(pre_process_words),0)
            
            final={
                'URL_ID':i,
                'URL':  j,
                'POSITIVE SCORE':pos_score,
                'NEGATIVE SCORE':neg_score,
                'POLARITY SCORE':polarity_score, 
                'SUBJECTIVITY SCORE':subjective_score,
                'AVG SENTENCE LENGTH':avg_sentence_len,
                'PERCENTAGE OF COMPLEX WORDS':precent_of_complex_words,
                'FOG INDEX':fog_index,
                'AVG NUMBER OF WORDS PER SENTENCE':avg_no_word_pre_sentence,
                'COMPLEX WORD COUNT': total_num_of_complex_word,
                'WORD COUNT':word_count,
                'SYLLABLE PER WORD':syllable_per_word,
                'PERSONAL PRONOUNS':presonal_pro,
                'AVG WORD LENGTH':avg_word_len
            }
            
            list.append(final)
            
        df=pd.DataFrame(list)
        df.to_csv(r'C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\output\Output Data Structure.csv')
        return df
# %%
