from django.contrib import admin
from apply.models import ApplyStatus ,Apply
from django.core.mail import send_mail

# Register your models here.

@admin.action(description='Approve selected applications and send Email')
def approve_applications(modeladmin,request,queryset):
    for object in queryset:
        if not hasattr(object,'status_of'):
            ApplyStatus.objects.create(apply=object,status='A')
            print(object.email)
            send_mail(
                'Ariana Apply',
                'you apply is approche',
                'apply@ariana.com',
                [object.email],
                fail_silently=False,
            )
@admin.action(description='Reject selected applications and send Email')
def reject_applications(modeladmin,request,queryset):
    for object in queryset:
        if not hasattr(object,'status_of'):
            ApplyStatus.objects.create(apply=object,status='R')
            send_mail(
                'Ariana Apply',
                'you apply is Reject',
                'apply@ariana.com',
                [object.email],
                fail_silently=False,
            )


class ApplyStatusAdmin(admin.ModelAdmin):
    fields = ['apply','status']
    list_display =('apply','status',)

class ApplyAdmin(admin.ModelAdmin):
    fields = ['email']
    list_display = ('id','email','create_timestamp','status')
    actions =[approve_applications,reject_applications]


admin.site.register(ApplyStatus,ApplyStatusAdmin)
admin.site.register(Apply,ApplyAdmin)

