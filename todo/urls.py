from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, signup

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = router.urls
urlpatterns += [
    path('signup/', signup, name='signup'),  # ثبت‌نام
]
