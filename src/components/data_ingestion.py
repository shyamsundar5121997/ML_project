import os # data ingestion use the reading dataset & os use the create a path , join path.
import sys # sys use for exception.
from src.logger import logging # logging is module which help us to track & record the log informations.
from src.exception import CustomException #
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
#A data class is a class typically containing mainly data, although there aren't really any restrictions. 
# It is created using the new @dataclass decorator, as follows: from dataclasses import dataclass
#  @dataclass 
# class DataClassCard: 
# rank: str suit: str.
from src.components.data_transformation import DataTransformation


## Intitialize the Data Ingetion Configuration

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv') # artifacts is a folder name & train_data_path is a variable name.
    test_data_path:str=os.path.join('artifacts','test.csv') # os.path is a current directory path.
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create a class for Data Ingestion
class DataIngestion:
    def __init__(self): # __init__ is a special method , which used for initialyzing the property or attributes.
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe') # logging.info tell us information about dataset.
            # i.e,(Dataset read as pandas Dataframe)

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True) #?
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)



