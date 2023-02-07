# Herat Disease Machine Learning API
This project is developed with [Django Rest Framework](https://www.django-rest-framework.org/) \
Machine learning models come from [this project](https://github.com/HaomingJue/Heart-Disease-Detection)  

### To install the dpendencies
<code>pip install -r requirements.txt</code>
### To start the server locally (localhost:8000)
<code>python manage.py runserver</code>

## API
API URL Pattern \
<code>[get] <deploy_url>/ml/<model_name></code> \
If you run the project locally, the default url should be http://localhost:8080

### Valid <model_name>
DecisionTree \
GBT \
KNN \
NaiveBayes \
NN \
SVMLinear \
SVMRBF 

**Note:** The <model_name> parameter should be consistent with one of the models in saved_models directory

### Body of requests
parameter **input:** a 10*1 array representing lists of data input by user \
example request body: \

    {
        "input": [8.0, 1.0, 4.0, 355.0, 99.0, 1.0, 2.0, 2.0, 1, 2]
    }


### Response
a binary value indicating having heart disease risk or not.

### How to update the trained models
Replace joblib model files in <code>saved_models</code> directory

