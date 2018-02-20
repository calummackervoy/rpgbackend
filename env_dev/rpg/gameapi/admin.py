from django.contrib import admin
from .models import ImageContent, TextContent, Option, Page

#Admin configurations
class TextContentAdmin(admin.ModelAdmin):
    list_display = ('text', 'priority')

class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')
    #offer filters for this model
    #list_filter = ('publication_date',)
    #order fields are shown in edit/create form (fields left out are excluded)
    #fields = ('title', 'authors', 'publisher', 'publication_date')
    filter_horizontal = ('content','images','options')

admin.site.register(ImageContent)
admin.site.register(TextContent, TextContentAdmin)
admin.site.register(Option)
admin.site.register(Page, PageAdmin)
