import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
def get_collection_as_dataframe(databasename:str,collection_name:str)->pd.DataFrame :
    try:
        logging.info("Reading data from database")
        df=pd.DataFrame(list(mongo_client[databasename][collection_name].find()))
        logging.info("Found columns")
        if "_id" in df.columns:
            df.drop("_id",axis=1,inplace=True)
        logging.info("Rows anc columns")
        return df
    except Exception as exc :
        raise SensorException(exc, sys)