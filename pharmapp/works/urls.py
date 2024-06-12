from django.urls import path
from works import views

app_name = 'works'

urlpatterns = [
    path('create-work/', views.create_work, name='create_work'),
    path('upload-results/', views.upload_results, name='upload_results')
]