from django.shortcuts import render, redirect
from .models import Student
def mainPage(request):
    if request.method == 'GET':
        data = Student.objects.all()
        return render(request, 'mainpage.html', {'data':data})

def addStudent(request):
    if request.method == 'GET':
        data = Student.objects.all()
        return render(request, 'add_student.html', {'data':data})
    else:
        fname1 = request.POST['fname']
        lname1 = request.POST['lname']
        email1 = request.POST['email']
        exp1 = request.POST['exp']
        skill1 = request.POST['skill']
        mobile1 = request.POST['mobile']
        company1 = request.POST['company']
        location1 = request.POST['location']
        roll_number1 = request.POST['roll_number']
        Student(
            first_name = fname1,
            last_name = lname1,
            email = email1,
            experience = exp1,
            skill = skill1,
            mobile = mobile1,
            company = company1,
            location = location1,
            roll_number = roll_number1
        ).save()
    return render(request, 'add_student.html')

def display_details(request):
    if request.method == 'GET':
        data = Student.objects.all()
        return render(request,'displaydetails.html', {'data':data})

def updated_page(request):
    if request.method == 'GET':
        return render(request,'updatepage.html')
    else:
        roll_no = request.POST.get('roll')
        data =  Student.objects.filter(roll_number=roll_no).first()
        if data:
            return render(request, 'updatedetails.html', {'data':data})

def updated_data(request,id):
    data = Student.objects.get(id=id)
    data.first_name = request.POST.get('fname')
    data.last_name = request.POST.get('lname')
    data.email = request.POST.get('email')
    data.experience = request.POST.get('exp')
    data.skill = request.POST.get('skill')
    data.mobile = request.POST.get('mobile')
    data.company = request.POST.get('company')
    data.location = request.POST.get('location')
    data.save()
    return redirect(mainPage)

def deletepage(request):
    data = Student.objects.all()
    data.delete()
    return render(request, 'deletepage.html',)
    return render(mainPage)
