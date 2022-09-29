from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from owner.models import Owner, OwnerExpertAt, OwnerTestimonial, OwnerClient, OwnerCertificate, OwnerKnowledge, \
    OwnerResumeSubject, OwnerExperienceDetail


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    fields = (
        'first_name',
        'last_name',
        'age',
        'residence',
        'email',
        'phone',
        'address',
        'profile_image',
        'about_me',
        'pdf_cv',
        'main_expertise',
        'facebook',
        'twitter',
        'linkedin',
        'youtube',
        'instagram',
        'owner_expert_at',
        'owner_testimonial',
        'owner_client',
        'owner_certificate',
        'owner_knowledge',
        'owner_resume_subject',
    )

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    # list_display =
    # ordering =
    # search_fields =
    # readonly_fields =
    # fields =
    # list_filter =


@admin.register(OwnerExpertAt)
class OwnerExpertAtAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    ordering = ('order',)
    fields = (
        'name',
        'detail',
        'html_icon_class',
        'order',
    )


@admin.register(OwnerTestimonial)
class OwnerTestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'detail',
    )
    fields = (
        'user_name',
        'detail',
        'subject',
        'user_image',
    )


@admin.register(OwnerClient)
class OwnerClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    fields = (
        'name',
        'website_link',
        'logo',
    )


@admin.register(OwnerCertificate)
class OwnerCertificateAdmin(admin.ModelAdmin):
    list_display = (
        'detail',
        'certify_by',
        'certified_date',
    )
    ordering = ('certified_date',)
    fields = (
        'certify_by',
        'detail',
        'logo',
        'certified_date',
    )


@admin.register(OwnerKnowledge)
class OwnerKnowledgeAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
    )
    fields = (
        'name',
    )


@admin.register(OwnerResumeSubject)
class OwnerResumeSubjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    fields = (
        'name',
        'owner_experience_detail',
    )


@admin.register(OwnerExperienceDetail)
class OwnerExperienceDetailAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'the_place',
        'starting_year',
        'ending_year',
    )
    ordering = ('starting_year',)
    fields = (
        'subject',
        'content',
        'the_place',
        'starting_year',
        'ending_year',
    )
