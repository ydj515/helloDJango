from django.contrib import admin

# from .models import Question # 관리 사이트에 Question 객체가 관리 인터페이스를 가지고 있다는것을 알려주는 것
from .models import Choice, Question
# admin.site.register(Question) # 관리 사이트에 Question 객체가 관리 인터페이스를 가지고 있다는것을 알려주는 것

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)