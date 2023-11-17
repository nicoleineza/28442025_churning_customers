from django import forms
from .models import churn_model
from django.db import models
class churning(forms.ModelForm):
        class Meta:
            model=churn_model
            fields=["Contract","Tenure", "OnlineSecurity", "monthlyCharges", "internetService", 
                    'Online_backup', "techSupport", "seniorcitizen", 
                    "paperlessBilling", "phoneservice","Confidence","Churn"]
