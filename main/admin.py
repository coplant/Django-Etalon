from django.contrib import admin
from .models import Review, User, Schedule, Subscription, Direction


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'date')
    list_display_links = ('id',)
    search_fields = ('author',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_coach', 'is_active', 'date_joined')
    list_display_links = ('id', 'username')
    search_fields = ('username',)
    list_editable = ('is_active', 'is_coach')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'direction', 'date')
    list_display_links = ('id',)
    search_fields = ('direction', 'date')
    list_editable = ('date',)
    list_filter = ('direction', 'date')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')
    list_editable = ('price',)


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Direction, DirectionAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
