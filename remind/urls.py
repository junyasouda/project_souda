from django.urls import path
from . import views

app_name = 'remind'

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'), #/remind
    path('add/',views.AddView.as_view(),name='add'), #/diary/add
    path('update/<int:pk>',views.UpdateView.as_view(),name='update'),# diary/update/1
    path('delete/<int:pk>/',views.DeleteView.as_view(),name='delete'), #diary/delete/1
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail') #diary/detail/1
]