from django.shortcuts import render,redirect
from.models import Reg_tbl,toy_tbl,cart_tbl
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import Regform

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
        if obj:
            return redirect('/log')
            
        else:
            return render(request,"register.html")

    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        obj=Reg_tbl.objects.filter(eml=eml,psw=psw)
        if obj:
            request.session['ema']=eml
            request.session['psa']=psw
            for i in obj:
                idno=i.id
            request.session['idl']=idno
            return render(request,"home.html")
        else:
             msg="Invalid credentials"
             return render(request,"login.html",{"error":msg})
    return render(request,"login.html")

def users(request):
    obj=Reg_tbl.objects.all()
    return render(request,"users.html",{"users":obj})

def edit(request,pk):
    obj=Reg_tbl.objects.filter(id=pk)
    if request.method=='POST':
        fnm=request.POST.get('nm')
        idl=request.POST.get('idl')
        mob=request.POST.get('mb')
        eml=request.POST.get('em')   
        psw=request.POST.get('ps')
        obb=Reg_tbl.objects.filter(id=idl)
        obb.update(fnm=fnm,mob=mob,eml=eml,psw=psw)       #1st fnm is models.py 2nd fnm is views.py
        return redirect('/users')
    return render(request,"user.html",{"user":obj})
def delete(request,pk):
    obj=Reg_tbl.objects.filter(id=pk)
    obj.delete()
    return redirect('/users')

def toys(request):
    if request.method=='POST':
        tnm=request.POST.get('tn')
        tpr=request.POST.get('tp')
        tim=request.FILES.get('ti')
        des=request.POST.get('ds')
        obj=toy_tbl.objects.create(tname=tnm,tprc=tpr,timg=tim,desc=des)
        obj.save()
        return render(request,"products.html",{"msg":"Details Added..."})
    return render(request,"products.html")
def pets(request):
    obj=toy_tbl.objects.all()
    return render(request,"pets.html",{"pets":obj})
def cart(req,idn):
    product=toy_tbl.objects.get(id=idn)
    cid=req.session['idl']
    customer=Reg_tbl.objects.get(id=cid)
    cartitem,created=cart_tbl.objects.get_or_create(product=product,customer=customer)
    if not created:
        cartitem.qty+=1
        cartitem.save()
    messages.success(req,"Item added to cart...")
    return redirect("/pets")

def viewcart(request):
    cid=request.session['idl']
    cobj=Reg_tbl.objects.get(id=cid)
    cartobj=cart_tbl.objects.filter(customer=cobj)
    if cartobj:
        total_price=0
        for m in cartobj:
            pro=m.product.tprc*m.qty
            total_price=total_price+pro
        return render(request,"cart.html",{"cart":cartobj,"total":total_price})
    else:
        return render(request,"cart.html",{"info":"Your Cart is Empty..."})
    
def cartdelete(request,pid):
    product=cart_tbl.objects.get(id=pid)
    product.delete()
    return redirect('/viewcart')

def email(request):
    if request.method=='POST':
        to=request.POST.get('em')
        sub=request.POST.get('sb')
        msg=request.POST.get('ms')
        send_mail(sub,msg,settings.EMAIL_HOST_USER,[to],fail_silently=False)
        return render(request,"email.html",{"success":"Mail send Successfully..."})
    return render(request,"email.html")

def formview(request):
    form=Regform()
    if request.method=='POST':
        form=Regform(request.POST)
        if form.is_valid():
          f=form.cleaned_data.get('fnm')
          m=form.cleaned_data.get('mob')
          e=form.cleaned_data.get('eml')
          p=form.cleaned_data.get('psw')
          obj=Reg_tbl.objects.create(fnm=f,mob=m,eml=e,psw=p)
          obj.save() 
          if obj:     
             msg="Registered Successfully..."
          return render(request,"forms.html",{"forms":form,"success":msg})
   
    return render(request,"forms.html",{"forms":form})













