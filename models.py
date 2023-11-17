class churn_model(models.model):
    Contract=[(0,'Month-to-Month'),(1,'One Year'),(2,'Two Year')]
    
    online_Security=[(0,'No'),(1,'yes'),(2,'no internet')]

    internet_service=[(0,'DSL'),(1,'fiber optics'),(2,'No')]

    online_backup=[(0,'yes'),(1,'no'),(2,'No internet service')]
    
    tech_support=[(0,'no'),(1,'yes'),(2,'No internet service')]
    
    paperless_biling=[(0,'yes'),(1,'no')]
    
    phone_service=[(0,'no'),(1,'yes')]

    Contract = models.IntegerField(verbose_name= "Contract",choices =Contract)
    Tenure = models.IntegerField(verbose_name="Tenure")
    OnlineSecurity = models.IntegerField(verbose_name="Online Security", choices=online_Security)
    monthlyCharges = models.FloatField(verbose_name="Monthly Charges", default=None)
    internetService = models.IntegerField(verbose_name="Internet Service",choices = internet_service)
    
    Online_backup = models.IntegerField(verbose_name="Online Backup", choices=online_backup)
    techSupport = models.IntegerField(verbose_name = "Tech Support", choices = tech_support)
    seniorcitizen = models.IntegerField(verbose_name = "Senior Citizen", default=None)
    paperlessBilling = models.IntegerField(verbose_name= "Paperless Billing", choices=paperless_biling)
    phoneservice = models.IntegerField(verbose_name="Phone Service",choices = phone_service)
    Confidence = models.CharField(verbose_name="Confidence Factor", max_length=10, blank=True )
    Churn = models.CharField(verbose_name="Customer Churn",default=None, max_length=4, blank=True)
    
    def __str__self():
        return "churn_model"