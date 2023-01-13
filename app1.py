from pycaret.classification import *
import streamlit as st
import pandas as pd
import pickle
import numpy as np

model=load_model('E_commerce_churn_prediction')
def predict(model,input_df):
    predictions_df=predict_model(estimator=model, data=input_df)
    predictions=predictions_df['Label'][0]
    return predictions
def run():
    from PIL import Image
    image=Image.open('logo.png')
    image_E_Commerce=Image.open('E_commerce.jpg')
    st.image(image,use_column_width=False)
    add_selectbox=st.sidebar.selectbox('How would you like to predict?',('Online','Batch'))
    st.sidebar.info('This app is created to predict customer churn')
    
    st.sidebar.image(image_E_Commerce)
    st.title('Churn-Guru Prediction')
    
    if add_selectbox=='Online':
        Complain=st.selectbox('Complain', [0,1])
        NumberOfAdress=st.number_input('NumberOfAdress',min_value=1,max_value=30,value=1)
        DaySinceLastOrder=st.number_input('DaySinceLastOrder',min_value=1,max_value=31,value=1)
        
        NumberOfDeviceRegistered=st.number_input('NumberOfDeviceRegistered',min_value=1,max_value=10,value=1)
        SatisfactionScore=st.number_input('SatisfactionScore',min_value=1,max_value=5,value=1)
        MaritalStatus=st.selectbox('MaritalStatus',['Single','Divorced','Married'])
        WarehouseToHome=st.number_input('WarehouseToHome',min_value=1,max_value=300,value=1)
        CityTier=st.selectbox('CityTier',[1,2,3])
        PreferredLoginDevice=st.selectbox('PreferredLoginDevice',['Mobile_Phone', 'Computer'])
        ouput=""
        input_dict={'Complain':Complain,'NumberOfAdress':NumberOfAdress,'DaySinceLastOrder':DaySinceLastOrder,
                    'NumberOfDeviceRegistered':NumberOfDeviceRegistered,'SatisfactionScore':SatisfactionScore,
                    'MaritalStatus':MaritalStatus,'PreferredLoginDevice':PreferredLoginDevice,'WarehouseToHome':WarehouseToHome,
                    'CityTier':CityTier}
        input_df=pd.DataFrame([input_dict])
        if st.button('Predict'):
            if predict(model=model,input_df=input_df)==1:
                output='Churn'
            else:
                output='Stay'
        st.sucess('This customer will {}.format(output)')
    if add_selectbox=='Batch':
        file_upload=st.file_uploader('Upload CSV file for predictions',type=['csv'])
        if file_upload is not None:
            data=pd.read_csv(file_upload)
            predictions=predict_model(estimator=model, data=data)
            st.write(predictions)
        
        