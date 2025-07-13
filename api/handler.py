import pickle
import os
import sys

import pandas as pd

from flask                   import Flask, request,Response
from api.model_churn.model_churn import Model_Churn

# Adiciona o diretório atual (`api/`) ao path
sys.path.append(os.path.dirname(__file__))

# Carregando modelo
model = pickle.load(open('/model/model_xgboost.pkl','rb'))

app = Flask(__name__)

@app.route('/model_churn/predict',methods=['POST']) # endpoint  

def fun_model_churn_predict():
    test_json = request.get_json()
    
    # Ha dado?  
    if test_json:
        if isinstance(test_json,dict):
            test_raw = pd.DataFrame(test_json,index=[0]) # para uma linha
        else:
            test_raw = pd.DataFrame(test_json,columns = test_json[0].keys()) # mais linhas
        
        pipeline = Model_Churn() # instanciar a classse Churn
        
        df = pipeline.feature_engineering(test_raw)
        
        df_response = pipeline.get_prediction(model,test_raw,df)
        
        return df_response
    else:
        return Response('{}',status=200,minetype = 'application/json') # pq ta indicando que vem de uma aplicacao json

if __name__ == '__main__':
    port = os.environ.get('PORT',5000)
    app.run(host='0.0.0.0',port=port)