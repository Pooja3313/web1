# Create your views here.
from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import Signup,Entry,Register,Pro
from django.db.models import Q


# Create your views here.
def helloview(request):
    a=Signup.objects.all()
    b=Entry.objects.all()
    return render(request,'pages/index.html',{'s':a ,'r':b})

def contact(request):
    return render(request,'pages/contact.html')
def profile(request):
    return render(request,'pages/profile.html')
def nav(request):
    return render(request,'pages/nav.html')

def signup(request):
    return render(request,'pages/signup.html')

def login(request):
    return render(request,'pages/login.html',)

def home(request):
    return render(request,'pages/home.html')
    
def home(request):
    return render(request,'pages/home.html')




def signupview(request):
    if request.method=='POST':
        model=Signup()
        model.username=request.POST['username']
        model.email=request.POST['email']
        model.ph_no=request.POST['contact']
        model.password=request.POST['password']
        model.save()
        return redirect('login')
    return render(request,'pages/register.html')

        
def datapost(request):
    if request.method=='POST':
       model=Product()
       model.name=request.POST['username']
       model.email=request.POST['email']
       model.save()
    return render(request,'datapost.html')
    


def productview(request,abc):
    v=Pro.objects.get(id=abc)
    return render(request,'productview.html',{'v':v})    
def productdelete(request,abc):
    v=Pro.objects.get(id=abc)
    v.delete()
    return redirect('proall')
def proall(request):
    if 'xyz' in request.session.keys():
        l=Pro.objects.all()
        return render(request,'proall.html',{'l':l})
    else:
        return redirect('login')   
def loginview(request):
    if request.method=='POST':
        try:
            m=Signup.objects.get(email=request.POST['email'])
            if m.password==request.POST['password']:
                request.session['xyz']=m.id
                return redirect('proall')
            else:
                return HttpResponse("wrong password")
        except:
            return HttpResponse("wrong email")    
    return render(request,'pages/login.html')                

                        
def searchview(request):
    q=request.GET.get('search')
    if q:
        pr= Pro.objects.filter(Q(name__icontains=q)| Q(des__icontains=q) |Q( price__icontains=q))
        data={'p':pr}
    else:
        data={}
    return render(request,'pages/search.html',data)   

def aboutview(request):
    return render(request,'pages/about.html') 
            
def logout(request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
        return redirect('login')
    else:
        return redirect('login')

def Productadd(request):
    if request.method=='POST':
        model=Pro(request.POST)
        model.name=request.POST['name']
        model.des=request.POST['des']
        model.img=request.FILES.get('image')
        model.save()
        return redirect('')