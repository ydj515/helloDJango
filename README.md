# helloDJango

### DJango 설치
* **pip install Django**
* **git clone https://github.com/django/django.git**
* **pip install -e django/**


### 실행방법
**python manage.py runserver**


### 명령어
* (models.py 에서) 모델을 변경해 줄 수 있음.
* **python manage.py makemigrations**을 통해 이 변경사항에 대한 마이그레이션을 만들기
* **python manage.py migrate** 명령을 통해 변경사항을 데이터베이스에 적용
* **python manage.py createsuperuser**
```
id : admin
email : ydj515@naver.com
pw : admin
```
* 접속 URL
**http://127.0.0.1:8000/admin/**

### 실습해보기
- [mysite] - [polls] - urls.py를 연다

```python
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

- 위와 같은 곳에서 django 1.x 버전과 2.0 버전의 차이점 중의 하나가 나타남
- 1.x 버전에서는 url 지정에서 url 함수를 사용하며 정규식을 사용하는데 2.0 이후부터는 path함수를 통해 정규식이 필요 없음


