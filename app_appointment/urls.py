"""app_appointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from laboratory.viewsAPI import viewsTest, viewsAffiliate, viewsAppointment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', viewsTest.LaboratoryTestApiView.as_view(), name="simple"),
    path('api/test/<int:id>/', viewsTest.LaboratoryTestDetailApiView.as_view(), name="details"),
    path('api/affiliate/', viewsAffiliate.LaboratoryAffiliateApiView.as_view(), name="simple_Affi"),
    path('api/affiliate/<int:id>/', viewsAffiliate.LaboratoryAffiliateDetailApiView.as_view(), name="details_Affi"),
    path('api/appointment/', viewsAppointment.LaboratoryAppointmentApiView.as_view(), name="simple_Appo"),
    path('api/appointment/<int:id>/', viewsAppointment.LaboratoryAppointmentDetailApiView.as_view(), name="details_Appo"),
]
