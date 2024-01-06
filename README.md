# this is my end to end project 


first initialize the git
'''
git init
'''
git add abc.txt
'''
git add .
'''
git commit -m "this is my first commit"
'''
git pull
'''
bash your_file_name.sh
'''
python setup.py install


# another way you can mention -e . in your requirement file and you can run


pip install -r requirements.txt

# Approach :
  Applying machine learing tasks like Data Exploration, Data Cleaning, Feature Engineering, Model Building and model testing to build a solution that should able to predict the premium of the personal for health insurance.

  Data Exploration : Exploring the dataset using pandas, numpy, matplotlib, plotly and seaborn.

  Exploratory Data Analysis : Plotted different graphs to get more insights about dependent and independent variables/features.

  Feature Engineering : Numerical features scaled down and Categorical features encoded.

  Model Building : In this step, first dataset Splitting is done. After that model is trained on different Machine Learning Algorithms such as:

     Linear Regression
     Decision Tree Regressor
     Random Forest Regressor
     Gradient Boosting Regressor
     XGBoost Regressor
  Model Selection : Tested all the models to check the RMSE & R-squared.

  Pickle File : Selected model as per best RMSE score & R-squared and created pickle file using pickle library.

# Webpage &Deployment : 
      Created a web application that takes all the necessary inputs from the user & shows the output. Then deployed project on the AWS Platform. As the aws app runner charge me much money so i have to delete the ecr reposotory of the project on AWS . 


# MLflow

# local command

  mlflow ui

# DVC cmd
dvc init
dvc repro
dvc dag
  


# Dagshub:
# MLFLOW_TRACKING_URI=https://dagshub.com/mdrianurrahaman/Insurence.mlflow 
  MLFLOW_TRACKING_USERNAME=mdrianurrahaman 
  MLFLOW_TRACKING_PASSWORD=your_token  
  python script.py