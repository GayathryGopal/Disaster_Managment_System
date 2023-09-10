from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from flood.models import floods,form,regist

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def camp(request):
    data=floods.objects.all()
  
    return render(request,'camp.html',{'a':data})
def mores(request):
     b=request.GET['id']
     
     data=floods.objects.get(Camp_id=b)
     ab=form.objects.filter(Camp_Id=b)
    #  abc=form.objects.filter(Address="TVM")
     return render(request,'details.html',{'b':data,'h':ab})

def addperson(request):
   
    if request.method=="POST":
  
         obj=form()
         obj.Name=request.POST['n']
         obj.Camp_Id=request.POST['no']
         obj.Age=request.POST['a']
         obj.Gender=request.POST['g']
         obj.Address=request.POST['ad']
         obj.Contact=request.POST['c']
         
         obj.save()
         Cid=request.POST['no']
         data=floods.objects.get(Camp_id=Cid)
         tot=data.Total_noof_capacity
         data.Total_noof_capacity=int(tot)-1
         data.save(update_fields=['Total_noof_capacity'])
         return HttpResponseRedirect("ad")
    return render(request,'add.html',{})
def requirement(request):
    
    if request.method=="POST":
         obj=regist()
         obj.Camp_Id=request.POST['cp']
         obj.Product=request.POST['p']
         obj.Quantity=request.POST['q']
         obj.save()
         return HttpResponseRedirect("req")
    return render(request,'requirment.html',{})
def requ1(request):
    
    if request.method=="POST":
        CID=request.POST['cp']
        # data=floods.objects.get(Camp_id=CID)
        # if data:
        #     return HttpResponseRedirect('/reqmore?CID='+CID)

        # else:
        #     msg="No camp found"
        #     return render(request,'requirement1.html',{'msg':msg})
        try:
           data=floods.objects.get(Camp_id=CID)
           return HttpResponseRedirect('/reqmore?CID='+CID)
        except:
            msg="No camp found"
            return render(request,'requirement1.html',{'msg':msg})

    return render(request,'requirement1.html',{})
def reqmore(request):
    cid=request.GET['CID']
    if request.method=="POST":
        obj=regist()
        obj.Camp_Id=cid
        obj.Product=request.POST['pro']
        obj.Quantity=request.POST['Qua']
        obj.save()
        return HttpResponseRedirect('reqmore?CID='+cid)
    return render(request,'reqmore.html',{})