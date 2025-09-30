from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    """
    مدل یک آیتم ToDo
    """
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='todos',
        help_text="کاربری که این آیتم متعلق به اوست"
    )
    title = models.CharField(
        max_length=200,
        blank=True,
        default="",
        help_text="عنوان آیتم ToDo"
    )
    content = models.TextField(
        blank=True,
        default="",
        help_text="توضیحات بیشتر برای آیتم"
    )
    completed = models.BooleanField(
        default=False,
        help_text="آیا آیتم انجام شده است؟"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="تاریخ و زمان آخرین بروزرسانی"
    )

    class Meta:
        ordering = ['-updated_at']  # آیتم‌های جدیدتر یا آپدیت شده‌تر اول نمایش داده شوند
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"

    def __str__(self):
        return self.title if self.title else "Untitled"
