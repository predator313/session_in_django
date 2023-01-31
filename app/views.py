from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='zaid'
    return render(request,'app/setsession.html')

#function for get session
def getsession(request):
    name=request.session['name']
    return render(request,'app/getsession.html',{'name':name})
