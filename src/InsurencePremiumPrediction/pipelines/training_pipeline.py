from src.InsurencePremiumPrediction.components.data_ingestion import DataIngestion

import os 
import sys 
from src.InsurencePremiumPrediction.logger import logging
from src.InsurencePremiumPrediction.exception import customexception

import pandas as pd
 

obj=DataIngestion()
obj.initiate_data_ingestion() 