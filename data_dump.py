import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"
DATA_DUMP='/config/workspace/aps_failure_training_set1.csv'


if __name__=="__main__":
    sensor_data=pd.read_csv(DATA_DUMP)

    #Connvert dataframe to json so that we can dump record in mongo db

    sensor_data.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(sensor_data.T.to_json()).values())

    print(json_record[0])

    ##insert converted json record to MongoDB

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record
