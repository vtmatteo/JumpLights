from django.conf.urls import url
from hilltractsy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view())
]
