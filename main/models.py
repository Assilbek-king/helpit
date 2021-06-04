from django.db import models

# Create your models here.


class Catalog(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=300)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=True, default=0)
    logo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Sponsor(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    city = models.CharField(max_length=300)
    street = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.city

class Succes(models.Model):
    title = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)
    mini_description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

class Developer(models.Model):
    title = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
            return self.title


class Team_member(models.Model):
    last_name = models.CharField(max_length=300, default='')
    first_name = models.CharField(max_length=300, default='')
    title = models.CharField(max_length=300, blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, default=0)
    image = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=300)
    description = models.TextField(default='')
    rating = models.IntegerField(default=0)
    is_main = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    instagram = models.CharField(max_length=300, blank=True, default='')
    telegram = models.CharField(max_length=300, blank=True, default='')
    whatsapp = models.CharField(max_length=300, blank=True, default='')
    facebook = models.CharField(max_length=300, blank=True, default='')
    email = models.EmailField(max_length=64, blank=True, default='')

    def __str__(self):
        return self.last_name + "  " + self.first_name


class Client(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    mini_description = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(blank=True)
    member = models.ForeignKey(Team_member, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    mini_description = models.CharField(max_length=500)
    link = models.TextField(blank=True)
    description = models.TextField()
    date = models.DateTimeField(blank=True)
    member = models.ForeignKey(Team_member, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title



class Gallery(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Student(models.Model):
    last_name = models.CharField(max_length=300, blank=True)
    first_name = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=300)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    instagram = models.CharField(max_length=300, blank=True)
    telegram = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    email = models.EmailField(max_length=64, blank=True)

    def __str__(self):
        return self.last_name

class Event(models.Model):
    title = models.CharField(max_length=300,)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True)
    mini_description = models.CharField(max_length=300)
    start_date = models.DateTimeField(default='')
    finish_date = models.DateTimeField(default='')
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class Social(models.Model):
    title = models.CharField(max_length=300,)
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=300,)
    logo = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Serviceitem(models.Model):
    title = models.CharField(max_length=300,)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='upload', blank=True, default='')
    icon = models.CharField(max_length=600, default='la la-bar-chart')
    mini_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=300)
    quality = models.IntegerField(default=0)
    member = models.ForeignKey(Team_member, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Experience_student(models.Model):
    title = models.CharField(max_length=300)
    quality = models.IntegerField(default=0)
    member = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Itemservice(models.Model):
    serviceitem = models.ForeignKey(Serviceitem,  on_delete=models.CASCADE)
    mini_description = models.CharField(max_length=1000)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.serviceitem.title

class Request(models.Model):
    fio = models.CharField(max_length=1000)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=20,default=0)

    def __str__(self):
        return self.fio

