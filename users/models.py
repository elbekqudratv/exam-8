from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PasswordResets(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Password reset for {self.user.email}"
