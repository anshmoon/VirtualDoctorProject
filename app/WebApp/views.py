from django.shortcuts import render,HttpResponse
import joblib
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
# Create your views here.
def appindex(request):
   
    return render(request, 'try.html')
def dia(request):
    return render(request, 'dia.html') 
def heart(request):
    return render(request, 'heart.html') 

def getFinalPrediction(nb_predict,lr_predict,rf_predict):
    positive=0
    negative=0
    if nb_predict==0:
       negative+=1
    else:
        positive+=1
    if lr_predict==0:
       negative+=1
    else:
        positive+=1
    if rf_predict==0:
       negative+=1
    else:
        positive+=1
    
    return negative>positive

def heartDiseasesPredictionResult(request):
    val1=float(request.GET['hid1'])
    val2=float(request.GET['hid2'])
    val3=float(request.GET['hid3'])
    val4=float(request.GET['hid4'])
    val5=float(request.GET['hid5'])
    val6=float(request.GET['hid6'])
    val7=float(request.GET['hid7'])
    val8=float(request.GET['hid8'])
    val9=float(request.GET['hid9'])
    val10=float(request.GET['hid10'])
    val11=float(request.GET['hid11'])
    val12=float(request.GET['hid12'])
    val13=float(request.GET['hid13'])
    
    
    #Loading model
    nb = joblib.load('naiveBayes_model.joblib')
    lr=joblib.load('LogisticRegression_model.joblib')
    rf=joblib.load('RandomForest_model.joblib')
    
    new_data=[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13]

    #Predict value
    nb_predict=nb.predict([new_data])
    lr_predict=lr.predict([new_data])
    rf_predict=rf.predict([new_data])

    #Final Result
    if (getFinalPrediction(nb_predict[0],lr_predict[0],rf_predict)):
        hresult='The Person does not have a Heart Disease'
    else:
        hresult='The Person has Heart Disease'
    return render(request, 'heart.html',{"hresult":hresult})       

def trial(request):
    return render(request, 'try.html')
def paper(request):
    return render(request,'paper.html')
   