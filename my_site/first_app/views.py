from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
""" 
def simple_view(request):
    return HttpResponse("Simple view by Sohan") #template html file (jinja)
"""

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'

}

def news_view(request,topic):
    return HttpResponse(articles[topic])


""" 
def sports_view(request):
   # return HttpResponse("Sports Page")
   return HttpResponse(articles['sports'])
    
def finance_view(request):
   # return HttpResponse("Finance Page")
   return HttpResponse(articles['finance'])
""" 


