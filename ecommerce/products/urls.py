from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static


def index(request):
    return HttpResponse("this is products page")

urlpatterns = [
    path('/index',index),
    path('/products',views.index),
    path('/addProducts', views.post_product_data),
    path('/getForm', views.getForm),
    path('/getStudentForm', views.post_student),
    path('/getStudents', views.get_student),
    path('/deleteStudent/<int:student_id>', views.deleteStudent),
    path('/updateStudent/<int:student_id>', views.updateStudent),
    path('/getPersonMF', views.show_person_mf),
    path('/postPersonMF', views.post_person_mf),
    path('/deletePersonMF/<int:person_id>',views.deletePersonMF),
    path('/updatePersonMF/<int:person_id>', views.updatePersonMF),
    path('/postFile', views.post_file),
    path('/getFile', views.get_file),
    path('/deleteFile/<int:file_id>', views.delete_file),
    path('/postFileMF', views.post_file_mf),
    path('/getFileMF', views.get_file_mf),
    path('/deleteFileMF/<int:file_id>', views.delete_file_mf),
    path('/updateFileMF/<int:file_id>', views.update_file_mf),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_URL)
