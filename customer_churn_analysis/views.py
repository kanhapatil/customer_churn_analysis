from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, "home.html")


def result(request):

    cls = joblib.load("Customer_Churn_Prediction.pkl")

    lis = []

    lis.append(request.GET['CreditScore'])
    lis.append(request.GET['Geography'])
    lis.append(request.GET['Gender'])
    lis.append(request.GET['Age'])
    lis.append(request.GET['Tenure'])
    lis.append(request.GET['Balance'])
    lis.append(request.GET['NumOfProducts'])
    lis.append(request.GET['HasCrCard'])
    lis.append(request.GET['IsActiveMember'])
    lis.append(request.GET['EstimatedSalary'])

    ans = cls.predict([lis])
    return render(request, "result.html", {"ans":ans})