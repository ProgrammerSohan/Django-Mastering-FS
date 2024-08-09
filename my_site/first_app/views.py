from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
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
    try: 
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = 'No page for that topic!'
        return HttpResponseNotFound(result)


def add_view(request,num1,num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    # domain.com/first_app/3/4 --> 72
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))


""" 
def sports_view(request):
   # return HttpResponse("Sports Page")
   return HttpResponse(articles['sports'])
    
def finance_view(request):
   # return HttpResponse("Finance Page")
   return HttpResponse(articles['finance'])
""" 


