from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class Moderator(AbstractUser):
    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='moderator_groups',  
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='moderator_user_permissions',  
        help_text=_('Specific permissions for this user.'),
    )

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'news'