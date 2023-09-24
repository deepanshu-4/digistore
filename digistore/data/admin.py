from django.contrib import admin
from .models import Post, PostImage
from .models import pPost, Postpdf
from .models import fpPost,fPostpdf,listing
# Register your models here.
from data.models import Contact,video
admin.site.register(Contact)
admin.site.register(video)
admin.site.register(listing)
class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


#for music
class PostpdfAdmin(admin.StackedInline):
    model = Postpdf

@admin.register(pPost)
class pPostAdmin(admin.ModelAdmin):
    inlines = [PostpdfAdmin]

    class Meta:
       model = pPost

@admin.register(Postpdf)
class PostpdfAdmin(admin.ModelAdmin):
    pass

#for files

class fPostpdfAdmin(admin.StackedInline):
    model = fPostpdf

@admin.register(fpPost)
class fpPostAdmin(admin.ModelAdmin):
    inlines = [fPostpdfAdmin]

    class Meta:
       model = fpPost

@admin.register(fPostpdf)
class fPostpdfAdmin(admin.ModelAdmin):
    pass