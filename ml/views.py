from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import joblib
import os

base_dir = os.path.dirname(__file__)


# Create your views here.
@api_view(['GET'])
def predict(request, model_name):
    test_data = [[8.0, 1.0, 4.0, 355.0, 99.0, 1.0, 2.0, 2.0, 1, 2]]
    print(len(test_data[0]))
    data = request.data["input"]
    print(data)

    load_model = joblib.load(open(base_dir + "/saved_models/" + model_name + ".joblib", 'rb'))
    y_pred = load_model.predict(test_data)
    return JsonResponse(y_pred[0], safe=False)