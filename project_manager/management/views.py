from django.shortcuts import render,redirect
from.models import Reg_tbl,Task,status

# Create your views here.
def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=='POST':
        fname=request.POST.get('name')
        mobl=request.POST.get('Mobile')
        ema=request.POST.get('email')
        pssw=request.POST.get('password')
        obj=Reg_tbl.objects.create(fnm=fname,eml=ema,mob=mobl,psw=pssw)
        obj.save()
        return render(request,"reg.html",{"msg":"Registered Successfully..."})
    return render(request,"reg.html")

def task(request):
    if request.method=='POST':
        tnm=request.POST.get('tn')
        des=request.POST.get('ds')
        tsd=request.POST.get('sd')
        ted=request.POST.get('ed')
        obj=Task.objects.create(name=tnm,description=des,start_date=tsd,end_date=ted)
        obj.save()
        return render(request,"task.html",{"msg":"Task Added Successfully..."})
    return render(request,"task.html")

def pstatus(request):
    if request.method=='POST':
       pnm=request.POST.get('pnm')
       redate=request.POST.get('rd')
       ssumry=request.POST.get('ss')
       isdate=request.POST.get('is')
       updates=request.POST.get('ud')
       obj=status.objects.create(pname=pnm,rdate=redate,ssmry=ssumry,issues=isdate,update=updates)
       obj.save()
       return render(request,"status.html",{"msg":"Status Added Successfully..."})
    return render(request,"status.html")

