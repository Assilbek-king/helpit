from django.contrib import admin
from main.models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course,CourseAdmin)


class CatalogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Catalog,CatalogAdmin)



class SponsorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sponsor,SponsorAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact,ContactAdmin)

class SuccesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Succes,SuccesAdmin)

class Team_memberAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team_member,Team_memberAdmin)

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client,ClientAdmin)

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery,GalleryAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student,StudentAdmin)


class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event,EventAdmin)

class SocialAdmin(admin.ModelAdmin):
    pass

admin.site.register(Social,SocialAdmin)


class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service,ServiceAdmin)


class ServiceitemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Serviceitem,ServiceitemAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Experience,ExperienceAdmin)


class DeveloperAdmin(admin.ModelAdmin):
    pass

admin.site.register(Developer,DeveloperAdmin)


class ItemserviceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Itemservice,ItemserviceAdmin)


class Experience_studentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Experience_student,Experience_studentAdmin)
