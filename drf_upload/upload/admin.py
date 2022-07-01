from django.contrib import admin
from .models import UploadImageTest, Owner, Tier

admin.site.register(Tier)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    fields = ("username", "password", "status")

@admin.register(UploadImageTest)
class UploadImageTestAdmin(admin.ModelAdmin):
    fields = ("name", "image")




