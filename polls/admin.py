from django.contrib import admin
from polls.models import Poll
from polls.models import Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, 				 {'fields' : ['question']}),
			('Date information', {'fields': ['pub_date']}),
				]
	inlines       = [ChoiceInline]
	list_display  = ('question', 'pub_date', 'wasPublishedRecently')
	list_filter   = ['pub_date']	
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)
# Register your models here.
