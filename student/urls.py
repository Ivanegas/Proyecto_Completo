from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('estudianteclick', views.studentclick_view),
path('estudiantelogin', LoginView.as_view(template_name='student/estudiantelogin.html'),name='estudiantelogin'),
path('estudianteregistro', views.student_signup_view,name='estudianteregistro'),
path('estudianteinicio', views.student_dashboard_view,name='estudianteinicio'),
path('estudiante_examen', views.student_exam_view,name='estudiante_examen'),
path('tomar_examen/<int:pk>', views.take_exam_view,name='tomar_examen'),
path('iniciarexamen/<int:pk>', views.start_exam_view,name='iniciarexamen'),
path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
path('view-result', views.view_result_view,name='view-result'),
path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('estudiante_puntos', views.student_marks_view,name='estudiante_puntos'),
]