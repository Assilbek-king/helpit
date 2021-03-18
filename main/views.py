from django.shortcuts import render
from main.models import *
from math import ceil
from datetime import datetime
# Create your views here.


def indexHandler(request):
    # prices = PriceItem.objects.filter(status=0)
    # comments = Comment.objects.all()
    sponsors = Sponsor.objects.all()
    contacts = Contact.objects.all()
    clients = Client.objects.all()[:3]
    student = Student.objects.all()[:3]

    return render(request, 'index12.html', {'sponsors':sponsors,

                                            'contacts':contacts,
                                            'clients':clients,
                                            'student':student,
                                          })

def teamHandler(request):
    team_member =Team_member.objects.all()[:6]

    return render(request, 'team-grid.html', {'team_member':team_member,
                                          })

def studentItemHandler(request , student_id):
    student = Student.objects.get(id=int(student_id))
    event_student = Event.objects.all()

    return render(request, 'team-single.html', {'student':student,
                                              'event_student':event_student,
                                          })

def contactHandler(request):
    contact = Contact.objects.all()

    return render(request, 'contact-4.html', {'contact':contact,
                                          })


def courseHandler(request):
    sponsors = Sponsor.objects.all()

    return render(request, 'kurs.html', {'sponsors':sponsors,
                                          })

