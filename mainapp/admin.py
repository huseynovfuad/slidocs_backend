from django.contrib import admin
from .models import About, PrivacyPolicy, RefundPolicy, TermCondition, Contact, Slider

# Register your models here.


admin.site.register(About)
admin.site.register(PrivacyPolicy)
admin.site.register(RefundPolicy)
admin.site.register(TermCondition)
admin.site.register(Contact)
admin.site.register(Slider)