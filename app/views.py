from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session['name']='zaid'
    return render(request,'app/setsession.html')

#function for get session
def getsession(request):
    if 'name' in request.session:
        name=request.session['name']
        request.session.modified=True
        return render(request,'app/getsession.html',{'name':name})
    else:
        return HttpResponse('hey your session is expired')

    # name=request.session['name']
    # name=request.session.get('name',default='guest')
    # return render(request,'app/getsession.html',{'name':name})

#function for deleting session
def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expire()
    return render(request,'app/delsession.html')
