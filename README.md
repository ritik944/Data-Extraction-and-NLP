# Data-Extraction-and-NLP
# Objective
The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below. 

    >  src  >  requirment.txt
    >  input  >  input.xlsx
    >  src  >  pipeline.py
    >  output  >  Output Data Structure.csv
    >  text file  >  all the extracted artical in txt file
  
    
# Data Extraction
To extract data from each artile given in the input.xlsx file ,save each aritle in a text file and save those data into csv file to do this i created a class data data ingestion in it used pandas ,requests , BeautifulSoup for data crawaling 
then by using soup extracted only title and the body text . extracting title just used find title tag and extract text but for text have to inspect the class for the text .all the url wasn't have same body tag so then i created a differnt list and save all urls who text aren't extracted and then by inspecting the webpage of the article i found a differnt body tag then extract and merge all article in a csv and save all article in txt foramt in data folder 


#output

    output.cv

    1.URL_ID	
    2.URL	
    3.POSITIVE SCORE	
    4.NEGATIVE SCORE	
    5.POLARITY SCORE	
    6.SUBJECTIVITY SCORE	
    7.AVG SENTENCE LENGTH	
    8.PERCENTAGE OF COMPLEX WORDS	
    9.FOG INDEX	
    10.AVG NUMBER OF WORDS PER SENTENCE	
    11.COMPLEX WORD COUNT	
    12.WORD COUNT	
    13.SYLLABLE PER WORD	
    14.PERSONAL PRONOUNS	
    15.AVG WORD LENGTH

#code flow

      1.install all the requirements file ,
          pip install -r requirements.txt

      2. In src there are  4 file
          1.data_ingestion.py used for ingestioning data in text ,scraping and return a data frame
          2.text_analysis.py  used for preforming all text analysis part 
          3.variables.py  used to perform all text_analysis method and creating a output file while filling all the variabbles
          4.pipeline.py   used inbuilt __name__ method and creating objects of classes

        
#Technology used

      1.Python
      2.Beautifulsoup
      3.NLTK Lib
