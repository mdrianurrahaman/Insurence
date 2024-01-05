import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.InsurencePremiumPrediction.logger import logging
from src.InsurencePremiumPrediction.exception import customexception
from sklearn.model_selection import train_test_split
from src.InsurencePremiumPrediction.components.data_transformation import DataTransformation
from src.InsurencePremiumPrediction.components.data_ingestion import DataIngestion
from src.InsurencePremiumPrediction.components.model_trainer import ModelTrainer
from src.InsurencePremiumPrediction.components.model_evaluation import ModelEvaluation






#if __name__ == "__main__":
obj = DataIngestion()
train_data, test_data = obj.initiate_data_ingestion()
data_transformation = DataTransformation()
train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
modeel_trainer=ModelTrainer()
modeel_trainer.initate_model_training(train_arr, test_arr)
model_eval_obj=ModelEvaluation()
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)
    