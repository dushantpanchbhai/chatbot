from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
import sys
from django.conf import settings
from django.conf.urls.static import static

def get_at_index(list, index):
    return list[index]

n1=[]
n2=[]
lp=-1
def home(request):
    return render(request,"home.html")

def answer(request):
    global lp,n1,n2
    inp=request.POST.get("box")
    n2.append(inp)
    out=run([sys.executable,"//home//dushant//Desktop//django//chatbot//chatbot//chatbot.py",inp],shell=False,stdout=PIPE)
    r=out.stdout
    o=r.decode("utf-8")
    n2.append(o)
    lp+=1
    return render(request,"ans.html",{'ans':n2,'question':n1,'index':lp})

def first_page(request) :
    return render(request, 'first_page.html')


def feedback(request) :
    return render(request, 'feedback.html')

def contactus(request) :
    return render(request, 'contactus.html')

def info(request) :
    return render(request, 'info.html')

def chat(request) :
    name = request.GET['name']
    return render(request, 'chat.html', {'name' : name})
#<!--  {%if (index%2==0) %}
#    {{i}}
#  {%endif%}
#-->
