from django.contrib import admin

from website.models import KeyWord, WebsiteSpecification


@admin.register(KeyWord)
class KeyWordAdmin(admin.ModelAdmin):
    list_display = (
        'keyword',
    )
    fields = (
        'keyword',
    )


@admin.register(WebsiteSpecification)
class WebsiteSpecificationAdmin(admin.ModelAdmin):
    list_display = (
        'meta_title',
        'meta_author',
    )
    fields = (
        'meta_author',
        'meta_title',
        'meta_description',
        'meta_keywords',
    )

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
