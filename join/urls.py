
from django.contrib import admin
from django.urls import include, path
from contacts.views import ContactView
from taskitem.views import TaskitemView
from login.views import LoginView
from rest_framework import routers

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('contacts/<int:id>/', ContactView.as_view()),
    path('taskitems/', TaskitemView.as_view()),
    path('taskitems/<int:id>/', TaskitemView.as_view()),
]
