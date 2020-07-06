from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'post/index.html')

def analyze(request):
    djtext= request.POST.get('text', 'default')
    #checkbox values 
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
#check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[]\^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed =analyzed + char
        params = {'purpose':'removed punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
      

    if(fullcaps =="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()   
        params = {'purpose':'upper case', 'analyzed_text':analyzed}
        djtext = analyzed
        
    if(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!= "\r":
                analyzed = analyzed+char  
        params = {'purpose':'Remove newline', 'analyzed_text':analyzed}
        djtext = analyzed
   
    if(spaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed+char  
        params = {'purpose':'Remove space', 'analyzed_text':analyzed}
        djtext = analyzed
        
    if(charcount=="on"):
        analyzed=0
        
        analyzed=len(djtext)
        params = {'purpose':'charcount', 'analyzed_text':analyzed}



    if(removepunc!="on" and newlineremover!= "on" and spaceremover!= "on" and fullcaps!="on" and charcount!= "on"):
        return render(request, 'post/error.html')    

    return render(request, 'post/analyze.html', params)    


def about(request):
    return render(request, 'post/about.html')

def contact(request):
    return render(request, 'post/contact.html')
def error(request):
    return render(request, 'post/error.html')