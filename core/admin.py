from django.contrib import admin
from .models import Post, Category, Contact, Tag,Post_comment

# Register your models here.

# My admin customization is starting here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'Name',)
    search_fields = ['Name']

class TagTabulerInline(admin.TabularInline):
    model=Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('profile_image', 'Title','category', 'Publish','Draft','section','Main_Post','Date')
    list_editable= ('Title','category',  'Publish','Draft', 'section',)
    list_filter = ('Title',)
    inlines=[TagTabulerInline]



# MODEL REGISTER ONE
admin.site.register(Post, PostAdmin)

# MODEL REGISTER TWO
admin.site.register(Category, CategoryAdmin)

admin.site.register(Contact)

admin.site.register(Tag)

admin.site.register(Post_comment)