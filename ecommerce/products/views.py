from django.shortcuts import render, redirect
from .models import Product, Person, FileUpload
from .forms import ProductForm, FileForm
from .forms import PersonForm
from .models import Student
from django.http import HttpResponse
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import PersonFilter
from accounts.auth import user_only

@login_required
@user_only
def index(request):
    items = Product.objects.all()
    context = {
        'products': items
    }
    return render(request, 'products/products.html',context)

@user_only
@login_required
def post_product_data(request):
    form = ProductForm()
    context = {
        'form':form
    }
    return render(request, 'products/postProduct.html',context)

@login_required
@user_only
def getForm(request):
    form = PersonForm()
    context = {
        'form':form
    }
    return render(request, 'products/getForm.html', context)

@login_required
def post_student(request):
    if request.method == 'POST':
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        batch = data['batch']
        image_url = data['image_url']
        category = data['category']
        student = Student.objects.create(firstname=firstname,
                                          lastname=lastname,
                                          batch=batch,
                                          image_url=image_url,
                                          category=category)
        if student:
            return redirect('/products/getStudents')

    return render(request, 'products/addStudent.html')

@login_required
def get_student(request):
    students = Student.objects.all()
    context = {
        'students':students,
        'activate_student':'active'
    }
    return render(request, 'products/getStudents.html', context)

@login_required
def deleteStudent(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/getStudents')

@login_required
def updateStudent(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        data = request.POST
        student.firstname = data['firstname']
        student.lastname = data['lastname']
        student.batch = data['batch']
        student.category = data['category']
        student.image_url = data['image_url']
        student.save()
        return redirect('/products/getStudents')
    context = {
        'student': student
    }
    return render(request, 'products/updateStudent.html', context)

@login_required
def show_person_mf(request):
    person = Person.objects.all()
    person_filter = PersonFilter(request.GET,queryset=person)
    person_final = person_filter.qs
    context = {
        'person':person_final,
        'activate_personMF':'active',
        'person_filter':person_filter
    }
    return render(request, 'products/showPersonMF.html', context)

@login_required
def post_person_mf(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,'Person Added Successfully')
            return redirect('/products/getPersonMF')
        else:
            messages.add_message(request, messages.ERROR,'Error in adding Person')
            return render(request, 'products/postPersonMF.html',{'form':form})
    context = {
        'form':PersonForm
    }
    return render(request, 'products/postPersonMF.html', context)

@login_required
def deletePersonMF(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect('/products/getPersonMF')

@login_required
def updatePersonMF(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/products/getPersonMF')
    context = {
        'form':PersonForm(instance=person)
    }
    return render(request, 'products/updatePersonMF.html', context)

@login_required
def post_file(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        file_obj = FileUpload(title=title, file=file)
        file_obj.save()
        if file_obj:
            return redirect('/products/getFile')
        else:
            return HttpResponse("File cannot be added")
    context = {
        'activate_file': 'active'
    }
    return render(request, 'products/addFile.html', context)

@login_required
def get_file(request):
    files = FileUpload.objects.all()
    context = {
        'files': files,
        'activate_file': 'active'
    }
    return render(request, 'products/showFile.html', context)
@login_required
def delete_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    file.delete()
    return redirect('/products/getFile')

@login_required
def get_file_mf(request):
    files = FileUpload.objects.all()
    context= {
        'files':files,
        'activate_fileMF':'active'
    }
    return render(request, 'products/showFileMF.html', context)
@login_required
def post_file_mf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/getFileMF')
    context = {
        'form':FileForm,
        'activate_fileMF':'active'
    }
    return render(request, 'products/addFileMF.html', context)
@login_required
def delete_file_mf(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    os.remove(file.file.path)
    file.delete()
    return redirect('/products/getFileMF')

@login_required
def update_file_mf(request, file_id):
    instance = FileUpload.objects.get(id=file_id)
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/products/getFileMF')
    context = {
        'form': FileForm(instance=instance),
        'activate_fileMF': 'active'
    }
    return render(request, 'products/updateFileMF.html', context)






