from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
import sys
def home(request):
    return render(request,"home.html")

def answer(request):
    inp=request.POST.get("box")
    out=run([sys.executable,"//home//dushant//Desktop//django//chatbot//chatbot//chatbot.py",inp],shell=False,stdout=PIPE)
    r=out.stdout
    o=r.decode("utf-8")
    return render(request,'ans.html',{"msg":o})
