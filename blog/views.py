from django.shortcuts import render
from .models import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


# Create your views here.
def about_page_view(request):
    about_data = About.objects.all()
    call_data = CustomerCall.objects.all()
    email_data = CustomerEmail.objects.all()

    context = {
        'about_data':about_data,
        'call_data':call_data,
        'email_data':email_data,
    }
    return render(request, 'blog/about.html', context)


def privacy_policy_view(request):
    return render(request, 'blog/privacy_policy.html')


def terms_conditions_view(request):
    return render(request, 'blog/term_condition.html')








