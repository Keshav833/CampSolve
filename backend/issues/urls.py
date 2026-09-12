from django.urls import path 
from . import views

urlpatterns = [
    path("", views.issue_list,name= "issue-list"), 
    path("create/",views.create_issue, name = "create-issue"),
    path("<int:issue_id>/",views.issue_detail, name = "issue-detail"),
    path("<int:issue_id>/edit/", views.edit_issue, name = "edit-issue"),
    path("<int:issue_id>/delete/", views.delete_issue, name = "delete-issue"),
]
