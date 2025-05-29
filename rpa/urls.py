from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

path("", views.index, name="index"),
path("business-units/", views.business_units, name="business_units"),
path("add-business-unit/", views.add_business_unit, name="add_business_unit"),
path("view-business-unit/<int:id>", views.view_business_unit, name="view_business_unit"),
path("edit-business-unit/<int:id>", views.edit_business_unit, name="edit_business_unit"),
path("delete-business-unit/<int:id>", views.delete_business_unit, name="delete_business_unit"),
path("add-busniess-unit-managers/<int:id>", views.add_business_unit_managers, name="add_business_unit_managers"),


path("Add-Process/<int:id>", views.add_process, name="add_process"),
path("view-Process/<int:id>", views.view_process, name="view_process"),
path("Process-Compatability/<int:id>", views.comp, name="comp"),
path("edit-Process/<int:id>", views.edit_process, name="edit_process"),
path("delete-Process/<int:id>", views.delete_process, name="delete_process"),

path("Config/<int:id>", views.config_process, name="process_config"),
path("edit-Comp/<int:id>", views.edit_comp, name="edit_comp"),



]