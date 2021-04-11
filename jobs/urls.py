from jobs import views
from django.conf.urls import url
urlpatterns = [
    url(r'detail/', views.detail, name="detail"),
    # url(r'detail/(?P<job_id>\d+)/$', views.detail, name="detail"),
    url('joblist/', views.joblist, name="job_list")
]