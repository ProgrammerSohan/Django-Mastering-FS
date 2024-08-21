from django.shortcuts import render
from django.http.response import HttpResponse,Http404,HttpResponseRedirect
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
       # return HttpResponse(articles[topic])
        return HttpResponse(result)
    #except:
    except KeyError:
       # result = 'No page for that topic!'
       # return HttpResponseNotFound(result)
       raise Http404("404 GENERIC ERROR") #404.html

""" 
def add_view(request,num1,num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    # domain.com/first_app/3/4 --> 72
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))
"""

""" 
def sports_view(request):
   # return HttpResponse("Sports Page")
   return HttpResponse(articles['sports'])
    
def finance_view(request):
   # return HttpResponse("Finance Page")
   return HttpResponse(articles['finance'])
""" 
#domain.com/first_app/0 ---> domain.com/first_app/sports

def num_page_view(request,num_page):

    topics_list = list(articles.keys()) #['sports','finance','politics']

    if num_page >= len(topics_list):
        raise Http404("Invalid page number.")

    topic = topics_list[num_page]

    #return HttpResponseRedirect(topic)
    return HttpResponseRedirect(f"/first_app/{topic}/")

