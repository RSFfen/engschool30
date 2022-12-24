from django.contrib import admin

from .models import Option, Riddle


class OptionInline(admin.TabularInline):
    model = Option
    raw_id_fields = ['riddle']


class RiddleAdmin(admin.ModelAdmin):
    model = Riddle
    list_display = ('riddle_text', 'pub_date')
    search_fields = ('riddle_text', )
    inlines = [OptionInline]


admin.site.register(Option)
admin.site.register(Riddle, RiddleAdmin)