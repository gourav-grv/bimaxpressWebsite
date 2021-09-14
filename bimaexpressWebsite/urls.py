"""bimaexpressWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name="home"),
    path('pricing', views.pricing ,name="pricing"),
    path('planDetails', views.planDetails ,name="planDetails"),
    path('covid', views.covid ,name="covid"),
    path('claimReimbursement', views.claimReimbursement , name="claimReimbursement"),
    path('cashlessClaim', views.cashlessClaim ,name="cashlessClaim"),

    # after price

    path('afterPricehospitalDetail', views.afterPricehospitalDetail ,name="afterPricehospitalDetail"),
    path('userDetails', views.userDetails ,name="userDetails"),
    path('empanelled_companies', views.empanelled_companies ,name="empanelled_companies"),
    path('savehospitaldetails', views.savehospitaldetails ,name="savehospitaldetails"),
    path('saveusercreation', views.saveusercreation ,name="saveusercreation"),
    path('savedoctorcreation', views.savedoctorcreation ,name="savedoctorcreation"),
    path('logout', views.logout ,name="logout"),
    path('valuegot', views.valuegot ,name="valuegot"),
    path('email', views.email ,name="email"),
    path('emailLogin', views.emailLogin ,name="emailLogin"),
    path('blogredirect', views.blogredirect ,name="blogredirect"),
    path('contact', views.contact ,name="contact"),
    path('emailGoogle', views.emailGoogle ,name="emailGoogle"),
    path('emailYahoo', views.emailYahoo ,name="emailYahoo"),
    path('emailAws', views.emailAws ,name="emailAws"),
    path('enc', views.enc ,name="enc"),
    path('privacy-policy', views.privacy_policy ,name="privacy-policy"),
    path('terms-and-conditions', views.privacy_policy ,name="terms-and-conditions"),
]


# from django.conf.urls import url
# from django.views.generic import RedirectView    

# from . import views

# urlpatterns = [
#    url(r'', views.home, name='home'),
#    url('pricing', views.pricing ,name="pricing"),
# ]
