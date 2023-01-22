from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth.models import User, auth 
from django.contrib import messages 
from django.urls import reverse 
from django.template import loader
from .models import Contact,Recharge,Subscribe,CardDetails,Recommended,HeroUnlimited,OtherPacks
from .serializers import RecommendedSerializer,HeroUnlimitedSerializer,OtherPacksSerializer
import requests
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


def true5g(request):
    return render(request,'true5g.html')

def contact(request):
    return render(request,'contactus.html')

def login(request):
    return render(request,'login.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,'afterloginrecharge.html')

        else:
            messages.info(request,'credential invalid')
            return HttpResponseRedirect(reverse('login'))

    else:
        return render(request,'login.html')

    

def register(request): 
        template = loader.get_template('register.html')
        return HttpResponse(template.render({},request))

def createData(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email cant be same')
                return HttpResponseRedirect(reverse('register'))

            else:
                user = User.objects.create_user(username = username, email=email,password=password)
                user.save()
                return HttpResponseRedirect(reverse('login'))

        else:
            messages.info(request,'Password not the same')
            return HttpResponseRedirect(reverse('register'))

    else:
        return HttpResponseRedirect(reverse('register'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def contactdetail(request):
    data1= request.POST['customername']
    data2= request.POST['email']
    data3= request.POST['sub']
    data4= request.POST['textarea']
    newdata = Contact(name=data1,email=data2,subject=data3,message=data4)
    newdata.save()
    return HttpResponseRedirect(reverse('index')) 

def afterlogin(request):
    data1 = request.POST['mobnum']
    data2 = request.POST['amount']
    data3 = request.POST['operator']
    data4 = request.POST['description']
    #data5= request.POST['check']
    newdata1 = Recharge(number=data1,rechargeamount=data2,operator=data3,description=data4)
    newdata1.save()
    return render(request,'payment.html')

def subscribe(request):
    data1= request.POST['email']
    newdata = Subscribe(email=data1)
    newdata.save()
    return render(request,'subscribe.html')

def carddetails(request):
    data1= request.POST['name']
    data2= request.POST['email']
    data3= request.POST['address']
    data4= request.POST['city']
    data5= request.POST['state']
    data6= request.POST['zipcode']
    data7= request.POST['nameoncard']
    data8= request.POST['creditno']
    data9= request.POST['expirymonth']
    data10= request.POST['expiryyear']
    data11= request.POST['cvv']
    newdata = CardDetails(username=data1,email=data2,address=data3,city=data4,state=data5,zipcode=data6,card_on_name=data7,creditno=data8,expmonth=data9,expyear=data10,cvv=data11)
    newdata.save()
    return HttpResponse(request,'<h1>Hurray Recharge Successful</h1>')


def RecommendedPlans(request):
    if request.method == 'GET':
        plans = Recommended.objects.all()  #queryset 
        serializer = RecommendedSerializer(plans,many=True)
        return JsonResponse(serializer.data,safe=False)


def HeroPlans(request):
    if request.method == 'GET':
        plans = HeroUnlimited.objects.all()  #queryset 
        serializer = HeroUnlimitedSerializer(plans,many=True)
        return JsonResponse(serializer.data,safe=False)


def OtherPlans(request):
    if request.method == 'GET':
        plans = OtherPacks.objects.all()  #queryset 
        serializer = OtherPacksSerializer(plans,many=True)
        return JsonResponse(serializer.data,safe=False)

def Allplans(request):
    response1 = requests.get('http://127.0.0.1:8000/recommendedplans/').json()  #fetching data from database by api endpoint
    response2 = requests.get('http://127.0.0.1:8000/otherplans/').json()
    response3 = requests.get('http://127.0.0.1:8000/hero-plans/').json()
    context = {
        'response1' : response1,
        'response2' : response2,
        'response3' : response3 

    }
    return render(request,'view.html',context) 
        

            


            

        

    


    
        
    






    