from django.contrib import admin
from django.db.models import fields

from .models import Question,Answer

#Admin panel for Answers
class AnswerInLineModel(admin.TabularInline):
	model = Answer
	fields = [
		'answer',
		'is_correct',
	]

#Admin panel for Questions
class QuestionAdmin(admin.ModelAdmin):
	fields = [ 
		'title',
		'points',
		'difficulty',
	]
	list_display = [ 
		'title',
		'updated_at'
	]
#now answers section will be below questions
	inlines = [ 
	     AnswerInLineModel
	]

admin.site.register(Question,QuestionAdmin)
	


