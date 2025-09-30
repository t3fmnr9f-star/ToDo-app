from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoSerializer

# --------------------------
# Todo ViewSet
# --------------------------
class TodoViewSet(viewsets.ModelViewSet):
    """
    مدیریت TodoItemها: 
    - فقط کاربر لاگین‌شده می‌تواند آیتم‌های خودش را ببیند
    - قابلیت Search و Sort
    - CRUD کامل
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # فیلدهای قابل سرچ و sort
    search_fields = ['title', 'content']
    ordering_fields = ['updated_at', 'title']
    ordering = ['-updated_at']  # پیش‌فرض: آیتم‌های جدیدتر یا آپدیت شده‌تر اول

    def get_queryset(self):
        # فقط آیتم‌های کاربر لاگین‌شده نمایش داده شوند
        return TodoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # موقع ایجاد، کاربر خودکار ست شود
        serializer.save(user=self.request.user)


# --------------------------
# Signup
# --------------------------
@api_view(['POST'])
def signup(request):
    """
    ثبت‌نام کاربر جدید
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"error": "Username and password required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.create_user(username=username, password=password)
    return Response(
        {"message": "User created successfully"},
        status=status.HTTP_201_CREATED
    )
