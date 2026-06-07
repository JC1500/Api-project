
from schema import user_input
from schema.user_input import Annotated,Abc,Field
from fastapi import FastAPI
from model.predict import model_output,model_version,model
from fastapi.responses import JSONResponse

app=FastAPI()
@app.get('/')
def starter():
    return "Hello there"
@app.post('/predict'
          )
def func(details: user_input.Abc):
    data=details.model_dump(include={'bmi','age_group','lifestyle_risk','city_tier','income_lpa','occupation'})
    try:
        output=model_output(data)[0]
        return JSONResponse(status_code=200,content={'predict': f"{output} {data['city_tier']}"})
    
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e)   )

@app.get('/health')
def health_check():
    return {
        'statuc': 'ok',
        'version': model_version,
        'model_loaded': model is not None,
        'edited': "pl",
        "return": "hello"
    }

