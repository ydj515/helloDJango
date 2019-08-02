from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), # polls폴더 밑의 경로이고, urls.py(URL config)를 연결
    path('admin/', admin.site.urls),
]