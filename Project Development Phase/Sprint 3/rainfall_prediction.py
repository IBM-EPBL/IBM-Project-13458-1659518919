import pickle
import numpy as np
import random
import warnings
warnings.filterwarnings('ignore')  #Filtering all warnings

#Initialising all paths for the saved model
scaler_path = 'D:\\7th Semester\\PRIEE\\GITHUB-REPO\\Project Development Phase\\Sprint 2\\SAVED_MODELS\\scale.pkl'
model_path = 'D:\\7th Semester\\PRIEE\\GITHUB-REPO\\Project Development Phase\\Sprint 2\\SAVED_MODELS\\rainfall.pkl'
encoder_path = 'D:\\7th Semester\\PRIEE\\GITHUB-REPO\\Project Development Phase\\Sprint 2\\SAVED_MODELS\\encoder.pkl'
data_path = 'D:\\7th Semester\\PRIEE\\GITHUB-REPO\\Project Development Phase\\Sprint 2\\SAVED_MODELS\\data.pkl'

#Function to make prediction on the pre-processed dataset
def make_prediction(test_data):
  scaler_custom_loaded = pickle.load(open(scaler_path,'rb'))
  model_custom_loaded = pickle.load(open(model_path,'rb'))
  x_test_data = np.array(test_data).reshape(1,-1)
  x_test_data = scaler_custom_loaded.transform(x_test_data)
  prediction = model_custom_loaded.predict(x_test_data.reshape(1,-1))[0]
  return prediction

#Function which pre-processes the data based on the location selected
def data_preprocessing(test_data_location):
  lencoders = pickle.load(open(encoder_path,'rb'))
  features = pickle.load(open(data_path,'rb'))
  location = lencoders['Location'].transform([test_data_location])[0]
  Data = features[features['Location']==location]
  x_test_data_series = Data.iloc[random.randint(0,len(Data))]
  return x_test_data_series

#Entry-point for making prediction
def prediction(location):
  preprocessed_data = data_preprocessing(location)
  p = make_prediction(preprocessed_data)
  return p

#Check
# print(prediction('BadgerysCreek'))