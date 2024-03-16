from django.contrib import admin
from . models import UserProfile ,Skill,ContactProfile,Certificate\
                    ,Portfolio,Blog,Testimonial,Media
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(ContactProfile)
admin.site.register(Certificate)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Media)
