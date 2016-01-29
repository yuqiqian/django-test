from django.contrib import admin
from .models import Article, Person

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'update_time',)
	def save_model(self, request, obj, form, change):
		if change:
			obj_original = self.model.objects.get(pk=obj.pk)
		else:
			obj_original = None
 
		obj.user = request.user
		obj.save()
		
	def delete_model(self, request, obj):
		"""
		Given a model instance delete it from the database.
		"""
		# handle something here
		obj.delete()

class PersonAdmin(admin.ModelAdmin):
	list_display = ('full_name',)


class MyModelAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super(MyModelAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		else:
			return qs.filter(author=request.user)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)

