from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='zaid'
    return render(request,'app/setsession.html')

#function for get session
def getsession(request):
    # name=request.session['name']
    name=request.session.get('name',default='guest')
    return render(request,'app/getsession.html',{'name':name})

#function for deleting session
def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'app/delsession.html')
