from django.urls import path
from .import views
urlpatterns = [
    path('',views.messageview),
    path('One/<int:pk>',views.readone),
    path('postdata',views.PostData),
    path('update/<int:pk>',views.UpdateData),
    path('updateone/<int:pk>',views.UpdateOne),
    path('delete/<int:pk>',views.DeleteData),

]
