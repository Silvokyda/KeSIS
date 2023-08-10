from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *

from .models import Student

@login_required(login_url='login')
def index(request):
    total_students = Student.objects.count()
    male_students = Student.objects.filter(gender='male').count()
    female_students = Student.objects.filter(gender='female').count()
    other_students = Student.objects.filter(gender='other').count()

    if total_students > 0:
        male_percentage = (male_students / total_students) * 100
        female_percentage = (female_students / total_students) * 100
        other_percentage = (other_students / total_students) * 100
    else:
        male_percentage = 0
        female_percentage = 0
        other_percentage = 0

    context = {
        'segment': 'index',
        'total_students': total_students,
        'male_percentage': male_percentage,
        'female_percentage': female_percentage,
        'other_percentage': other_percentage,
        'user_groups': [group.name for group in request.user.groups.all()],  
    }

    return render(request, "pages/index.html", context)


def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)
