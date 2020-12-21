from django.shortcuts import render
from django.shortcuts import redirect
from . import form

def recordproblemform(request):
    if request.method=='POST':
        f2=form.CreateFormR(request.POST,request.FILES)
        f=form.CreateForm(request.POST,request.FILES)
        if f2.is_valid():
            f2.save()
            return render(request, 'contactus/index.html', {'formR': f2,'formP': f})
        if f.is_valid():
            f.save()
            return render(request, 'contactus/index.html', {'formP': f,'formR': f2})
    else:
        f2=form.CreateFormR()
        f=form.CreateForm()
    return render(request,'contactus/index.html',{'formR':f2,'formP': f})



