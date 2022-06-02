from django.urls import path
from myapp import views

urlpatterns = [
    path('create/<str:n1>/<int:n2>/', views.insert),
    path('update/<int:stud_id>/<str:n1>/<int:n2>/', views.update),
    path('delete/<int:stud_id>/', views.delete),
    path('show/<int:id>/', views.showAll),
    path("getStudentById/<int:STUDid>/", views.studentApiMethods.getStudentById, ),
    path("FetchAllStudents/", views.studentApiMethods.getAllStudents, ),
    path("addNewStudent/", views.studentApiMethods.post, ),
    path("orderStudents/", views.studentApiMethods.orderStudents, ),
    path("getStudentsGreaterThanSpecificAge/<int:age>/", views.studentApiMethods.getStudentsGreaterThanSpecificAge, ),
    path("register/", views.studentApiMethods.register, ),
    path("getAllUsers/", views.studentApiMethods.getAllUsers, ),
    path("login/", views.studentApiMethods.login,),
]
