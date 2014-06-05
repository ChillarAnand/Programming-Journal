from django.views.generic.base import View
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import date


class HelloWorldView(View):
    def get(self, request):
        #return HttpResponse("Hello World!")
        return render_to_response('hello.html', 
                                    { 'date' : date.today() })
