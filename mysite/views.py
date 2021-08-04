from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About Mayur")

def remover(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newLine=request.POST.get('newLine','off')
    extraSpace=request.POST.get('extraSpace','off')
    
    punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc=="on":
        clear_text=""
        for char in djtext:
            if char not in punctuations:
                clear_text= clear_text + char
        djtext=clear_text
        
    if uppercase=="on":
        clear_text=""
        for char in djtext:
            clear_text= clear_text + char.upper()
        djtext=clear_text

    if newLine=="on":
        clear_text=""
        for char in djtext:
            if char !="\n" and char!="\r":
                clear_text=clear_text+char
        djtext=clear_text

    if extraSpace=="on":
        clear_text=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                clear_text=clear_text+char
        djtext=clear_text
    
    if(removepunc!="on" and uppercase!="on" and newLine!="on" and extraSpace!="on"):
        return HttpResponse("Please select an option !!!")

    
    params={'txt': djtext}
    return render(request, 'analyse.html',params)