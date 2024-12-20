# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # bio = models.TextField(max_length=500, blank=True)
#     # location = models.CharField(max_length=30, blank=True)
#     # birth_date = models.DateField(null=True, blank=True)
#     # image = models.ImageField(upload_to='profile_images/', blank=True)
#     timestamp = models.DateField(null=True, blank=True, auto_now_add=True)
#     updated = models.DateField(null=True, blank=True, auto_now=True)
#     address = models.CharField(verbose_name="Address", max_length=100, null=True)
#     city = models.CharField(verbose_name="City", max_length=50, null=True)
#     state = models.CharField(verbose_name="State", max_length=50, null=True)
#     zip_code = models.CharField(verbose_name="Zip Code", max_length=10, null=True)
#     country = models.CharField(verbose_name="Country", max_length=50, null=True)
#     phone_number = models.CharField(verbose_name="Phone Number", max_length=20, null=True)
#     website = models.URLField(verbose_name="Website", max_length=200, null=True)
#     longitude = models.TextField(verbose_name="Longitude", max_length=50, null=True)
#     latitude = models.TextField(verbose_name="Latitude", max_length=50, null=True)
    
#     captcha_score =models.FloatField(default = 0.0)
#     has_profile = models.BooleanField(default = False)
    
#     is_active = models.BooleanField(default = True)
    
#     def __str__(self):
#         return f'{self.user}'
#     # cover_photo = models.ImageField(verbose_name="Cover Photo", upload_to='cover_images/', blank=True)
#     # profile_picture = models.ImageField(verbose_name="Profile Picture", upload_to='profile_images/', blank=True)
#     # google_map_url = models.URLField(verbose_name="Google Map URL", max_length=200, null=True)
#     # google_plus = models.URLField(verbose_name="Google Plus", max_length=200, null=True)
#     # facebook = models.URLField(verbose_name="Facebook", max_length=200, null=True)
#     # twitter = models.URLField(verbose_name="Twitter", max_length=200, null=True)
#     # linkedin = models.URLField(verbose_name="LinkedIn", max_length=200, null=True)
#     # instagram = models.URLField(verbose_name="Instagram", max_length=200, null=True)
#     # pinterest = models.URLField(verbose_name="Pinterest", max_length=200, null=True)
#     # about_me = models.TextField(verbose_name="About Me", max_length=500, null=True)
#     # experience = models.TextField(verbose_name="Experience", max_length=500, null=True)
#     # education = models.TextField(verbose_name="Education", max_length=500, null=True)
#     # skills = models.TextField(verbose_name="Skills", max_length=500, null=True)
#     # languages = models.TextField(verbose_name="Languages", max_length=500, null=True)
#     # certifications = models.TextField(verbose_name="Certifications", max_length=500, null=True)
#     # interests = models.TextField(verbose_name="Interests", max_length=500, null=True)
#     # hobbies = models.TextField(verbose_name="Hobbies", max_length=500, null=True)
#     # social_media_accounts = models.TextField(verbose_name="Social Media Accounts", max_length=500, null=True)
#     # is_verified = models.BooleanField(default=False)
#     # is_subscribed = models.BooleanField(default=False)
#     # is_active = models.BooleanField(default=True)
#     # is_deleted = models.BooleanField(default=False)
#     # is_staff = models.BooleanField(default=False)
#     # is_superuser = models.BooleanField(default=False)
#     # last_login = models.DateTimeField(null=True)
#     # date_joined = models.DateTimeField(null=True)
#     # password_reset_token = models.CharField(max_length=100, null=True)
#     # password_reset_token_expiry = models.DateTimeField(null=True)
#     # password_reset_token_created_at = models.DateTimeField(null=True)
#     # password_reset_token_used_at = models.DateTimeField(null=True)
#     # password_reset_token_used_count = models.IntegerField(default=0)
#     # password_changed_at = models.DateTimeField(null=True)
#     # last_password_change_attempt = models.DateTimeField(null=True)
#     # last_password_change_attempt_count = models.IntegerField(default=0)
#     # last_password_change_attempt_ip = models.CharField(max_length=50, null=True)
#     # last_password_change_attempt_succeeded = models.BooleanField(default=False)
#     # last_password_change_attempt_succeeded_at = models.DateTimeField(null=True)
#     # last_password_change_attempt_succeeded_ip = models.CharField(max_length=50, null=True)
#     # last_password_change_attempt_succeeded_count = models.IntegerField(default=0)
    




from django.db import models

class RegisterUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class LoginUser(models.Model):
    user = models.OneToOneField(RegisterUser, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    
    