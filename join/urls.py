
from django.contrib import admin
from django.urls import include, path
from contacts.views import contact_detail, create_contact, get_contacts
from taskitem.views import TaskitemDetailView, create_subtask, create_task, get_tasks, task_detail, task_status
from login.views import LoginView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from users.views import SignupAPIView

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/signup/', SignupAPIView.as_view(), name='signup_api_view'),
    # path('api/login/', obtain_auth_token, name='login_api_view'),
    path('api/login/', LoginView.as_view()),
    path('api/contacts/', get_contacts, name='get_contacts'),
    path('api/contacts/create/', create_contact, name='create_contact'),
    path('api/contacts/<int:pk>/', contact_detail, name='contact_detail'),
    # path('api/contacts/<int:id>/', ContactView),
    path('api/taskitems/', get_tasks, name='get_tasks'),
    path('api/taskitems/create/', create_task, name='create_task'),
    # path('api/taskitems/<int:id>/', TaskitemDetailView.as_view()),
    path('api/taskitems/<int:pk>/', task_detail, name='task_detail'),
    path('api/taskitems/<int:pk>/status/', task_status, name='task_status'),

     path('api/subtasks/create/', create_subtask, name='create_subtask'),
]
