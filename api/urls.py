from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("student/((?P<pk>\d+)/)?", csrf_exempt(StudentView.as_view())),
    re_path("school/((?P<pk>\d+)/)?", csrf_exempt(SchoolView.as_view())),
    re_path("subcounty/((?P<pk>\d+)/)?", csrf_exempt(SubcountyView.as_view())),
    re_path("county/((?P<pk>\d+)/)?", csrf_exempt(CountyView.as_view())),

]