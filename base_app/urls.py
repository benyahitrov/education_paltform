from django.urls import path
import base_app.views as base_app


app_name = 'base_app'

urlpatterns = [
    path('', base_app.CourseListView.as_view(), name='index'),
    path('course/<int:pk>/',
         base_app.CourseDetailView.as_view(),
         name='course_detail'),
    path('course/create/', base_app.CourseCreateView.as_view(), name='create'),
    path('course/update/<int:pk>/',
         base_app.CourseUpdateView.as_view(),
         name='course_update'),
    path('course/delete/<int:pk>/',
         base_app.CourseDeleteView.as_view(),
         name='course_delete'),


]
