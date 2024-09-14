
from django.contrib import admin
from django.urls import include, path
from contacts.views import ContactView
from taskitem.views import TaskitemView
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'contacts', ContactView)
# # router.register(r'accounts', AccountViewSet)
# urlpatterns = router.urls


# router = routers.SimpleRouter()
# router.register(f'contacts', ContactView)

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('contacts/', ContactView.as_view()),
    path('contacts/<int:id>/', ContactView.as_view()),
    path('taskitems/', TaskitemView.as_view()),
    path('taskitems/<int:id>/', TaskitemView.as_view()),
]
