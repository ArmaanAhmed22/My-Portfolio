from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from .models import *
from django.conf import settings

from django.contrib import messages

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

import datetime

#from pprint import pprint


def get_default_context():
    return {'socialmedia': SocialMedia.objects.all()}

# Create your views here.
def home(request):
    return render(request, 'main/home.html', get_default_context())

def projects(request):
    myprojects = Project.objects.all()
    return render(request, 'main/projects.html', get_default_context() | {'projects': myprojects})

def current_project(request, current_project_id):
    queryset = Project.objects.filter(where_is_projects_on_website=current_project_id)
    
    if len(queryset) != 1:
        raise Http404()
    return render(request, 'main/current_project.html', get_default_context() | {'current_project': queryset[0], 'tags': queryset[0].list_tags.all()})

def error_404_view(request, exception):
    response = render(request, 'main/404.html', get_default_context())
    response.status_code = 404
    return response

def resume_view(request):
    categories_queryset = CVCategory.objects.all().order_by('priority')
    cvitems_split_by_category = {category.name: [] for category in categories_queryset}
    for item in CVItem.objects.all():
        cvitems_split_by_category[item.category.name].append(item)
    for category in CVCategory.objects.all():
        cvitems_split_by_category[category.name].sort(key = lambda item: item.end_year+item.end_month/13, reverse=True)
        cvitems_split_by_category[category.name].sort(key = lambda item: 1 if item.end_year == -1 or item.end_month == -1 else 0, reverse=True)
    
    skills_queryset = CVItemListExpandible.objects.all()
    return render(request, 'main/resume.html', get_default_context() | {'categories': categories_queryset, 'cvitems': cvitems_split_by_category, 'skills': skills_queryset})


def send_inquiry(email_subject, email_message, email_from="unknown", name = "unknown"):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.SENDINBLUE_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
    send_params = {
        "subject": email_subject,
        "text_content": f"Sender Name: {name}\nSender Email: {email_from}\n\n{email_message}",
        "sender": {"name": "No-reply", "email": "email@ahmed.science"},
        "to": [{"name": "Armaan Ahmed", "email": "armaan@ahmed.science"}],
        
    }
    if email_from != "unknown":
        send_params["reply_to"] = {"name": name, "email": email_from}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(**send_params)
    api_instance.send_transac_email(send_smtp_email)
    
def generate_contact_model(subject, message, first_name=None, last_name=None, sender_email=None):
    contact_time = datetime.datetime.now()
    
    return ContactItem(subject=subject, message=message, first_name=first_name, last_name=last_name, sender_email=sender_email, contact_time=contact_time)


def contact_view(request):
    if request.method == 'POST':
        model = generate_contact_model(subject = request.POST.get("form-subject"), message = request.POST.get("form-inquiry"), first_name = request.POST.get("form-first-name"), last_name = request.POST.get("form-last-name"), sender_email = request.POST.get("form-email"))
        try:
            send_inquiry_params = {
                "email_subject": request.POST.get("form-subject"),
                "email_message": request.POST.get("form-inquiry")
            }
            if not (request.POST.get("form-first-name") == "" and request.POST.get("form-first-name") == ""):
                send_inquiry_params["name"] = request.POST.get("form-first-name") + " " + request.POST.get("form-last-name")
            if not request.POST.get("form-email") == "":
                send_inquiry_params["email_from"] = request.POST.get("form-email")
            send_inquiry(**send_inquiry_params)
            model.send_status = 1
            model.save()
        except:
            messages.error(request, "Unable to send inquiry")
            model.save()
            return redirect("main:contact")
        messages.success(request, "Inquiry sent!")
        redirect("main:home")
    return render(request, 'main/contact.html', get_default_context())