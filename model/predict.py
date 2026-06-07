import pickle
import pandas as pd
model_version='1.0.0'

with open('model/model.pkl','rb') as f:
    model=pickle.load(f)

def model_output(data :dict):
    data_df=pd.DataFrame([data])
    return model.predict(data_df)
