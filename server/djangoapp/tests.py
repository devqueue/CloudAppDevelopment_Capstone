from django.test import TestCase

# Create your tests here.
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='#', view=views.get_dealerships, name='index'),
    # path for about view
    path(route='about/', view=views.about, name='about'),
    # path for contact us view
    path(route='contact/', view=views.contact, name='contact'),
    # path for registration
    path(route='register/', view=views.registration_request, name='registeration'),
    # path for login

    # path for logouts
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


{
  "apikey": "PIdnXpXAohmr8Pi-IaQ7XHpVR8y-4cK4qYmY5JkCu5zw",
  "host": "eb6737b9-e8ef-47f4-b17a-aa24c7184513-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key e4e5d826-8163-488b-81a5-6f1e3233284a",
  "iam_apikey_name": "for-guestbook",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/1a73ce75a6f84ac7ac8bd65707c5f873::serviceid:ServiceId-fd51fa60-d855-4f68-b3e8-821e44ffe901",
  "password": "2cf2ca31617b8f2d70ce5faea60fc722",
  "port": 443,
  "url": "https://apikey-v2-1yftfuamgm91wh4i7lbafnug4oesjk4eu4f7vuc9drgn:2cf2ca31617b8f2d70ce5faea60fc722@eb6737b9-e8ef-47f4-b17a-aa24c7184513-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "apikey-v2-1yftfuamgm91wh4i7lbafnug4oesjk4eu4f7vuc9drgn"
}