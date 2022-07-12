
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.add,name="add"),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('cvbhome/',views.TaskListView.as_view(),name='cbvhome1'),
    path('cvbdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cvbdetail1'),
    path('cvbupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cvbupdate1'),
    path('cvbdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cvbdelete1')

]
