from django.shortcuts import render
from owner.models import Owner, OwnerExpertAt, OwnerTestimonial, OwnerClient, OwnerResumeSubject, OwnerKnowledge, \
    OwnerCertificate


def home(request, theme=None):
    context = {}
    owner = Owner.objects.all()[0]
    context['owner'] = owner

    expert_at = OwnerExpertAt.objects.filter(owner=owner)
    number_of_item = expert_at.count()

    expert_at_left = expert_at[:int(number_of_item / 2)]
    context['expert_at_left'] = expert_at_left

    expert_at_right = expert_at[int(number_of_item / 2):]
    context['expert_at_right'] = expert_at_right

    testimonials = OwnerTestimonial.objects.filter(owner=owner)
    context['testimonials'] = testimonials

    clients = OwnerClient.objects.filter(owner=owner)
    context['clients'] = clients

    resume_subjects = OwnerResumeSubject.objects.filter(owner=owner)
    context['resume_subjects'] = resume_subjects

    knowledge = OwnerKnowledge.objects.filter(owner=owner)
    context['knowledge'] = knowledge

    certificates = OwnerCertificate.objects.filter(owner=owner)
    context['certificates'] = certificates

    if request.method == 'GET':
        return render(request, 'light/home.html', context)
    else:
        return render(request, 'light/home.html', context)

