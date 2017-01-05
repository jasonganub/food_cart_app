from django.contrib import admin
from .models import Owner, OpeningHours, ClosingRules




class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 0


class ClosingRulesInline(admin.TabularInline):
    model = ClosingRules
    extra = 0


class OwnerAdmin(admin.ModelAdmin):
    inlines = [OpeningHoursInline, ClosingRulesInline]
    search_fields = ['name']


admin.site.register(Owner, OwnerAdmin)
