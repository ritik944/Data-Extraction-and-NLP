#%%
from data_ingestion import data_ingestion
from variables import output_variables

#%%
if __name__=="__main__":
    obj=data_ingestion()
    obj2=output_variables()
    df1,df2=obj.data_extraction()
    df=obj.merge(df1,df2)
    final=obj2.primary(df)


# %%
