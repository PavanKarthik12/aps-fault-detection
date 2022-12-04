from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity import config_entity
import os,sys
from sensor.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from sensor.components.data_ingestion import DataIngestion

if __name__=="__main__":
     try:
          training_pipeline_config=config_entity.TrainingPipelineConfig()
          data_ingestion_config=DataIngestionConfig(training_pipeline_config)
          logging.info(data_ingestion_config.to_dict())
          data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
          print(data_ingestion_artifact)
     except Exception as e:
          logging.info(e)
          