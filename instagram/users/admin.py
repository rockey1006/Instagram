"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Profile admin."""

	fieldsets = (
		('Profile', {
			'fields': (
				('user', 'picture'),
			)
		}),
		('Extra Info', {
			'fields': (
				('website', 'phone_number'),
				('biography')
			)
		}),
		('Metadata', {
			'fields': (
				('created', 'modified'),
			)
		})
	)

	list_display = ('id', 'user', 'phone_number', 'website', 'biography')
	list_display_links = ('id', 'user')
	# list_editable = ('phone_number',)
	search_fields = (
		'user__email',
		'user__username',
		'user__first_name',
		'user__last_name',
		'phone_number',
		'website',
		'biography',
	)
	list_filter = (
		'user__is_active',
		'user__is_staff',
		'created',
		'modified',
	)
	readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
	"""Profile inline admin for users."""

	model = Profile
	can_delete = False
	verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
	"""Add profile admin to base user admin."""

	inlines = (ProfileInline, )
	list_display = (
		'username',
		'email',
		'first_name',
		'last_name',
		'is_active',
		'is_staff',
	)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
