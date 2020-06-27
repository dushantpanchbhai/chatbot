from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
import sys
from django.contrib import messages
def home(request):
    messages.success(request,'this is message',extra_tags="sucess",fail_silently=False)
    return render(request,"home.html")

def answer(request):
    inp=request.POST.get("box")
    out=run([sys.executable,"//home//dushant//Desktop//django//chatbot//chatbot//chatbot.py",inp],shell=False,stdout=PIPE)
    r=out.stdout
    o=r.decode("utf-8")
    return render(request,"ans.html",{'ans':o})
