from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello, this is my first django page</h1>")
def about(request):
    return HttpResponse("hello, this is my about page")