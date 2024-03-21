from django.urls import path
from .import views

urlpatterns = [
    path('add_person',views.add_person,name='add_person'),
    path('update_person/<int:p_id>',views.update_person,name='update_person'),
    path('delete_person/<int:p_id>',views.delete_person,name='delete_person'),
]