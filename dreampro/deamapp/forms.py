from django import forms 
from .models import CSVMap 
  
  
# creating a form 
class CSVMapForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = CSVMap 
  
        # specify fields to be used 
        fields = [ 
            "id_in_doc", 
            "first_name", 
            "last_name",
            "email",
            "ip_address",
            "gender",
            "app_name",
            
        ] 
