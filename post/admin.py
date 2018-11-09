from django.contrib import admin

# Register your models here.
from .models import Post  # veya from post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug'] # baslik ve tariihini admin sayfasinda gosterecektir
    list_display_links = ['publishing_date']    # tarihe link ozelligini ekler
    list_filter = ['publishing_date']           # tarihe gore filtreleme ozelligi
    search_fields = ['title', 'content']        # arama yaparken baslik ve icerige gore arama yapar
    list_editable = ['title']                   # basligi goruldugu yerde editable yapar

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)