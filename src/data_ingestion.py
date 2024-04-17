#%%
import warnings
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
warnings.filterwarnings('ignore')


#%%
class data_ingestion:
    
    def data_extraction(self):
        url_data= pd.read_excel(r'C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\Input.xlsx')
        df=url_data.copy()
        list1=[]
        no_data=[]
        blank_link={}
        for i,url in enumerate(df['URL']):
            resp=requests.get(url)
            soup=bs(resp.text,'html.parser')
            title=soup.find('title').text
            text=soup.find("div","td-post-content tagdiv-type")
            print(i)
            if text is not None:
                text=text.get_text(strip=True,separator='\n')
                text=text.splitlines()
            else:
                blank_link[i+1]=url
                blank={
                    'URL_ID':df["URL_ID"][i],
                    'URL':url
                }
                no_data.append(blank)
            
            data={
                'URL_ID':df["URL_ID"][i],
                'URL':url,
                'artical':str(title)+str(text)
            }
            list1.append(data)
        
            fname=df['URL_ID'][i]
            path=r'C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\text file'
            with open(f"{path}\{fname}.txt",'w+',encoding='utf-8') as file:
                file.writelines(df['URL_ID'][i])
                file.writelines(" ")
                file.writelines(title)
                file.writelines(" ")
                file.writelines(url)
                file.writelines(" ")
                if text is None:
                    file.writelines("text not available")
                else:
                    file.writelines(text)
    
        list2=[]
        for item in no_data:
            x=item['URL_ID']
            url=item['URL']
            print(x)
            resp=requests.get(url)
            soup=bs(resp.text,"html.parser")
            title=soup.find('title').text
            text=soup.find("div","tdi_130")
            
            if text is not None:
                text=text.get_text(strip=True,separator='\n')
                text=text.splitlines()
                
            data={
                'URL_ID':x,
                'URL':url,
                'artical':str(title)+str(text)
            }
            list2.append(data)
            
            fname=x
            path=r'C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\text file'
            with open(f"{path}\{fname}.txt",'w+') as file:
                file.writelines(title)
                file.writelines(" ")
                file.writelines(f"{x}")
                file.writelines(" ")
                file.writelines(url)
                file.writelines(" ")
                if text is None:
                    file.writelines("text not available")
                else:
                    file.writelines(text)
            
        return pd.DataFrame(list1),pd.DataFrame(list2)
    
    def merge(self,list1,list2):
        list1.update(list2)
        list1=list1.dropna()
        list1.reset_index(drop=True,inplace=True)
        
        list1.to_csv(r"C:\Users\ritik\data science\nlp\assignment\20211030 Test Assignment\data\final.csv",index=False)
        
        return list1

# %%
