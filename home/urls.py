from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('home/new-issue', views.new_issue, name='new_issue'),
    path('home/issue/<int:issue_id>', views.issue, name='issue'),
    path('home/issue/edit/<int:issue_id>', views.issue_edit, name='issue_edit'),
    path('home/issue/get/<int:issue_id>', views.get_issue_by_id, name='get_issue_by_id'),
    path('home/post_new_issue', views.post_new_issue, name='post_new_issue'),
    path('/post_new_issue', views.post_new_issue, name='post_new_issue')
]
