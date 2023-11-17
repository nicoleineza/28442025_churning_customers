from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import churning
from .models import churn_model
from . import signals
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse
from sklearn.preprocessing import StandardScaler
import joblib 
import os
from keras.models import load_model
def predict_churn(request): #path to the model path
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "churn_model")
    SCALER_PATH = os.path.join(os.path.dirname(__file__), "churnscaler")
    template_name = "C:\Users\Nicole\Desktop\AIPROJECT\user/INDEX.html"
    


    if request.method =='POST':
        form = churning(request.POST) 
        if form.is_valid():
            '''
            ["Contract","Tenure", "OnlineSecurity", "monthlyCharges", "internetService", 
                    'Online_backup', "techSupport", "seniorcitizen", 
                    "paperlessBilling", "phoneservice","Confidence","Churn"]

           
            
            '''
            Contract = form.cleaned_data["Contract"]
            Tenure = form.cleaned_data["Tenure"]
            OnlineSecurity = form.cleaned_data["OnlineSecurity"]
            MonthlyCharges = form.cleaned_data["MonthlyCharges"]
            InternetService = form.cleaned_data["InternetService"]
            online_backup = form.cleaned_data["online_backup"]
            techSupport = form.cleaned_data["techSupport"]
            seniorcitizen = form.cleaned_data["seniorcitizen"]
            paperlessBilling = form.cleaned_data["paperlessBilling"]
            phoneservice = form.cleaned_data["phoneservice"]
           
            

            data = [[Contract,Tenure, OnlineSecurity, monthlyCharges, internetService, 
                    Online_backup, techSupport, seniorcitizen, 
                    paperlessBilling, phoneservice,Confidence,Churn]]

            scaler = joblib.load(SCALER_PATH)
            transformed_data = scaler.transform(data)

            model  = load_model(MODEL_PATH)

            value = model.predict(transformed_data)
            if value[0][0]>0.5:
                prediction_form = Churning(initial={'Confidence': f"{round(value[0][0]*100,2)}%",'Churn': "Yes"})
                prediction_form.fields["Contract"].initial = None
                prediction_form.fields["Tenure"].initial = None
                prediction_form.fields["OnlineSecurity"].initial = None
                prediction_form.fields["MonthlyCharges"].initial = None
                prediction_form.fields["InternetService"].initial = None
                prediction_form.fields["Online_backuo"].initial = None
                prediction_form.fields["techSupport"].initial = None
                prediction_form.fields["seniorcitizen"].initial = None
                prediction_form.fields["paperlessBilling"].initial = None
                prediction_form.fields["phoneService"].initial = None

                return render(request,template_name,{"form":prediction_form})
            else:

                prediction_form = churning(initial={'Confidence':f"{round(value[0][0]*100,2)}%",'Churn': "No"})
                prediction_form.fields["Contract"].initial = None
                prediction_form.fields["Tenure"].initial = None
                prediction_form.fields["OnlineSecurity"].initial = None
                prediction_form.fields["MonthlyCharges"].initial = None
                prediction_form.fields["InternetService"].initial = None
                prediction_form.fields["Online_backuo"].initial = None
                prediction_form.fields["techSupport"].initial = None
                prediction_form.fields["seniorcitizen"].initial = None
                prediction_form.fields["paperlessBilling"].initial = None
                prediction_form.fields["phoneService"].initial = None
                return render(request,template_name,{"form":prediction_form})

    else:
        form = churning()


    return render(request,template_name,{"form":churning()})

    
