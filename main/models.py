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

class Team_member(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    is_main = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Client(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=300, blank=True)
    mini_description = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
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
    description = models.CharField(max_length=1000)
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