
from django.contrib import admin
from django.urls import include, path
from contacts.views import contact_detail, create_contact, get_contacts
from taskitem.views import TaskitemDetailView, TaskitemView
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
    path('api/taskitems/', TaskitemView),
    path('api/taskitems/<int:id>/', TaskitemDetailView.as_view()),
]
