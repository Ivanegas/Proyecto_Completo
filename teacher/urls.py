from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('profesorlogin', LoginView.as_view(template_name='teacher/profesorlogin.html'),name='profesorlogin'),
path('profesor_registro', views.teacher_signup_view,name='profesor_registro'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('profesorexamen', views.teacher_exam_view,name='profesorexamen'),
path('profesor-add-examen', views.teacher_add_exam_view,name='profesor-add-examen'),
path('profesor-view-examen', views.teacher_view_exam_view,name='profesor-view-examen'),
path('eliminar-examen/<int:pk>', views.delete_exam_view,name='eliminar-examen'),


path('profesorpregunta', views.teacher_question_view,name='profesorpregunta'),
path('profesor-add-pregunta', views.teacher_add_question_view,name='profesor-add-pregunta'),
path('profesor-view-pregunta', views.teacher_view_question_view,name='teacher-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),
]