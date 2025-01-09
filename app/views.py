from django.shortcuts import render
import requests

def index(request):
    a=requests.get('https://fakestoreapi.com/products/')
    data=a.json()
    return render(request,'index.html',{"data":data})


def search(request):
    b=requests.get('https://restcountries.com/v2/all')
    data1=b.json()
    details=None
    # print(data1)
    if request.method=="POST":
       name=request.POST['country']
       print(name)
       for i in data1:
           if i['name']==name:
               details=i
            #    print(i)
    return render(request,'search.html',{'data1':data1,'details':details})