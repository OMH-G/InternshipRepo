from django.shortcuts import HttpResponse,render
def homepage(request):
    #use render function to render template which will be for design purpose in making pizza app.
    return HttpResponse('Hello this is pizza app')