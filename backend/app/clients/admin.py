from django.contrib import admin

from .models import Client, ClientDocument, ClientProfile


class DocumentInline(admin.TabularInline):
  model = ClientDocument
  extra = 1


class ClientProfileInline(admin.TabularInline):
  model = ClientProfile
  extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
  list_display = ['id', 'last_name', 'phone', 'email']
  save_on_top = True
  inlines = [ClientProfileInline, DocumentInline,]