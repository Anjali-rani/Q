from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from Ac.models import extendeduser, Quize


def index(request):
    return render(request,'index.html')



def login(request):
    if request.method=="POST":
        uid=request.POST['adhar']
        pwd=request.POST['password']
        user=auth.authenticate(username=uid,password=pwd,)
        if user is not None:
            auth.login(request,user)
            return render(request,'welcome.html')
        else:
            return render(request, 'index.html', {'error': 'Invalid Login Credentials'})
    else:
        return render(request, 'index.html')



def signup(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['repassword']:
            try:
                user=User.objects.get(username=request.POST['adhar'])
                return render(request, 'register.html', {'error': 'Already Registered !'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['adhar'],first_name=request.POST['sname'],last_name=request.POST['roll'],email=request.POST['email'],password=request.POST['password'])
                college = request.POST['college']
                contact = request.POST['contact']
                newextendeduser=extendeduser(college=college,contact=contact,user=user)
                newextendeduser.save()
                #auth.login(request,user) if we want to login immediatly after sign up
                #return redirect(index)
                return render(request, 'register.html')
        else:
            return render(request,'register.html',{'error':'Password does not match !'})
    else:
        return render(request,'register.html')


@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return render(request,'index.html')

@login_required(login_url='/login/')
def exam(request):
    return render(request,'exam.html')


@login_required(login_url='/login/')
def score(request):
    FN=request.POST.get('NM','')
    CN=request.POST.get('CN','')
    MN=request.POST.get('MN','')
    RN = request.POST.get('RN', '')
    mark=0
    mark1 = 0
    A1 = request.POST.get('question-1-answers', '')
    A2 = request.POST.get('question-2-answers', '')
    A3 = request.POST.get('question-3-answers', '')
    A4 = request.POST.get('question-4-answers', '')
    A5 = request.POST.get('question-5-answers', '')
    A6 = request.POST.get('question-6-answers', '')
    A7 = request.POST.get('question-7-answers', '')
    A8 = request.POST.get('question-8-answers', '')
    A9 = request.POST.get('question-9-answers', '')
    A10 = request.POST.get('question-10-answers', '')
    A11 = request.POST.get('question-11-answers', '')
    A12 = request.POST.get('question-12-answers', '')
    A13 = request.POST.get('question-13-answers', '')
    A14 = request.POST.get('question-14-answers', '')
    A15 = request.POST.get('question-15-answers', '')
    A16 = request.POST.get('question-16-answers', '')
    A17 = request.POST.get('question-17-answers', '')
    A18 = request.POST.get('question-18-answers', '')
    A19 = request.POST.get('question-19-answers', '')
    A20 = request.POST.get('question-20-answers', '')
    A21 = request.POST.get('question-21-answers', '')
    A22 = request.POST.get('question-22-answers', '')
    A23= request.POST.get('question-23-answers', '')
    A24 = request.POST.get('question-24-answers', '')
    A25 = request.POST.get('question-25-answers', '')
    A26= request.POST.get('question-26-answers', '')
    A27 = request.POST.get('question-27-answers', '')
    A28 = request.POST.get('question-28-answers', '')
    A29 = request.POST.get('question-29-answers', '')
    A30 = request.POST.get('question-30-answers', '')
    A31 = request.POST.get('question-31-answers', '')
    A32 = request.POST.get('question-32-answers', '')
    A33 = request.POST.get('question-33-answers', '')
    A34 = request.POST.get('question-34-answers', '')
    A35 = request.POST.get('question-35-answers', '')
    A36 = request.POST.get('question-36-answers', '')
    A37 = request.POST.get('question-37-answers', '')
    A38 = request.POST.get('question-38-answers', '')
    A39 = request.POST.get('question-39-answers', '')
    A40 = request.POST.get('question-40-answers', '')
    A41 = request.POST.get('question-41-answers', '')
    A42 = request.POST.get('question-42-answers', '')
    A43 = request.POST.get('question-43-answers', '')
    A44 = request.POST.get('question-44-answers', '')
    A45 = request.POST.get('question-45-answers', '')
    A46 = request.POST.get('question-46-answers', '')
    A47 = request.POST.get('question-47-answers', '')
    A48= request.POST.get('question-48-answers', '')
    A49 = request.POST.get('question-49-answers', '')
    A50 = request.POST.get('question-50-answers', '')



    if A1=='B':
        mark=mark+1
    if A2=='A':
        mark=mark+1
    if A3=='B':
        mark=mark+1
    if A4 == 'C':
        mark = mark + 1
    if A5 == 'B':
        mark = mark + 1
    if A6 == 'C':
        mark = mark + 1
    if A7 == 'C':
        mark = mark + 1
    if A8 == 'B':
        mark = mark + 1
    if A9 == 'A':
        mark = mark + 1
    if A10 == 'B':
        mark = mark + 1
    if A11 == 'B':
        mark = mark + 1
    if A12 == 'A':
        mark = mark + 1
    if A13 == 'A':
        mark = mark + 1
    if A14 == 'C':
        mark = mark + 1
    if A15 == 'D':
        mark = mark + 1
    if A16 == 'D':
        mark = mark + 1
    if A17 == 'A':
        mark = mark + 1
    if A18 == 'B':
        mark = mark + 1
    if A19 == 'B':
        mark = mark + 1
    if A20 == 'C':
        mark = mark + 1
    if A21 == 'C':
        mark = mark + 1
    if A22 == 'D':
        mark = mark + 1
    if A23 == 'B':
        mark = mark + 1
    if A24 == 'C':
        mark = mark + 1
    if A25 == 'B':
        mark = mark + 1
    if A26 == 'C':
        mark1 = mark1 + 1
    if A27 == 'C':
        mark1 = mark1 + 1
    if A28 == 'D':
        mark1 = mark1 + 1
    if A29 == 'B':
        mark1 = mark1 + 1
    if A30 == 'B':
        mark1 = mark1 + 1
    if A31 == 'B':
        mark1 = mark1 + 1
    if A32 == 'C':
        mark1 = mark1 + 1
    if A33 == 'A':
        mark1 = mark1 + 1
    if A34 == 'D':
        mark1 = mark1 + 1
    if A35 == 'C':
        mark1 = mark1 + 1
    if A36 == 'C':
        mark1 = mark1 + 1
    if A37 == 'C':
        mark1 = mark1 + 1
    if A38 == 'D':
        mark1 = mark1 + 1
    if A39 == 'D':
        mark1 = mark1 + 1
    if A40 == 'B':
        mark1 = mark1 + 1
    if A41 == 'B':
        mark1 = mark1 + 1
    if A42 == 'B':
        mark1 = mark1 + 1
    if A43 == 'A':
        mark1 = mark1 + 1
    if A44 == 'C':
        mark1 = mark1 + 1
    if A45 == 'D':
        mark1 = mark1 + 1
    if A46 == 'B':
        mark1 = mark1 + 1
    if A47 == 'D':
        mark1 = mark1 + 1
    if A48 == 'C':
        mark1 = mark1 + 1
    if A49 == 'D':
        mark1 = mark1 + 1
    if A50 == 'C':
        mark1 = mark1 + 1

    mark=(mark+mark1)*2

    Qu = Quize(Roll_No=RN,Fullname=FN,College=CN,Mobile=MN,TotalMarks=mark)
    Qu.save()
    return render(request,'score.html',{'mark':mark})


#@login_required(login_url='/login/')
#def showdata(request):
    #datas=extendeduser.objects.filter(user=request.user)
   # return render(request,'show.html',{'data':datas})"""