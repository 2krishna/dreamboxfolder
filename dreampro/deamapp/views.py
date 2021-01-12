from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from .forms import * 
# Create your views here.
def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return ip  


def create_csvmap(request):
    context ={} 
    ip_address = get_ip_address(request)
    # add the dictionary during initialization 
    form = CSVMapForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 

        return HttpResponse('data insedetd')
          
    context['form']= form 
    return render(request, "create_csvview.html", context)




def list_csvview(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["csvdata"] = CSVMap.objects.all() 
    
    return render(request, "list_csvview.html", context) 