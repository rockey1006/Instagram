"""Posts admin."""

# Django
from django.contrib import admin

# Models
from posts.models import Post
# from posts.models import Post, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	"""Post admin."""

	fieldsets = (
        ('Usuario', {
            'fields': (
                ('user', 'profile'),
            )
        }),
        ('Contenido', {
            'fields': (
                ('title'),
                ('slug'),
                ('photo'),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        }),
    )

	prepopulated_fields = {"slug": ("title",)}
	list_display = ('id', 'profile', 'title', 'photo')
	search_fields = ('title', 'slug', 'user__username', 'user__email')
	list_filter = ('created', 'modified')
	readonly_fields = ('created', 'modified')
