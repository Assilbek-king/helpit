from django.shortcuts import render
from main.models import *
from math import ceil
from datetime import datetime


def indexHandler(request):
    sponsors = Sponsor.objects.all()
    contacts = Contact.objects.all()
    clients = Client.objects.all()[:3]
    student = Student.objects.all()
    courses = Course.objects.all()[:3]
    catalogs = Catalog.objects.all()

    return render(request, 'index12.html', {'sponsors':sponsors,
                                            'courses':courses,
                                            'catalogs': catalogs,
                                            'contacts':contacts,
                                            'clients':clients,
                                            'student':student,
                                          })

def teamHandler(request):
    team_members = Team_member.objects.all()
    return render(request, 'team-grid.html', {'team_members':team_members
                                          })

def teamitemHandler(request, team_id):
    team_members = Team_member.objects.get(id=int(team_id))
    experiences = Experience.objects.all()
    return render(request, 'team-single.html', {'team_members':team_members,
                                                'experiences':experiences
                                          })


def studentItemHandler(request , student_id):
    student = Student.objects.get(id=int(student_id))
    event_student = Event.objects.all()
    experience_student = Experience_student.objects.all()

    return render(request, 'team-student.html', {'student':student,
                                                 'event_student':event_student,
                                                 'experience_student':experience_student,
                                          })

def contactHandler(request):
    contact = Contact.objects.all()

    return render(request, 'contact-4.html', {'contact':contact,
                                          })


def courseHandler(request):
    sponsors = Sponsor.objects.all()
    courses = Course.objects.all()
    catalogs = Catalog.objects.all()

    return render(request, 'kurs.html', {'sponsors': sponsors,
                                         'courses': courses,
                                         'catalogs': catalogs
                                          })

def serviceHandler(request):
    services = Service.objects.all()
    service_items = Serviceitem.objects.all()

    return render(request, 'service.html', {'services': services,
                                         'service_items': service_items,
                                          })

def serviceitemHandler(request, serviceitem_id):
    service_items = Serviceitem.objects.get(id=int(serviceitem_id))
    serviceitems = Serviceitem.objects.all()
    item_services = Itemservice.objects.all()


    return render(request, 'serviceitem.html', {
                                         'service_items': service_items,
                                         'serviceitems': serviceitems,
                                         'item_services': item_services,
                                          })
