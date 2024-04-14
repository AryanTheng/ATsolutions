from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
     return render(request, "index.html")
    #return HttpResponse("This is homepages")

def about(request):
    return render(request, "about.html")
    #return HttpResponse("This is about page")
