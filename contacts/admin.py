from django.contrib import admin

# Register your models here.
from .models import Contact 

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id','listing', 'name', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'listing')
  list_per_page = 25


admin.site.register(Contact, ContactAdmin)