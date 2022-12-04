import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

@dataclass
class Environmentvariable:  
    mongodb_url:str=os.getenv('MONGODB_URL')

env_var=Environmentvariable()
mongo_client=pymongo.MongoClient(env_var.mongodb_url)

