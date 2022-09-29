from django.db import models


class OwnerExpertAt(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, verbose_name='owner expert at: ')
    detail = models.TextField(null=False, blank=False, verbose_name='detail')
    html_icon_class = models.CharField(null=False, blank=False, max_length=255, verbose_name='html icon class - example: lnr lnr-pencil')
    order = models.PositiveSmallIntegerField(verbose_name="ordering")

    def __str__(self):
        return self.name


class OwnerTestimonial(models.Model):
    user_name = models.CharField(null=False, blank=False, max_length=255, verbose_name='who suggest owner?')
    detail = models.TextField(null=False, blank=False, verbose_name='detail')
    subject = models.CharField(null=True, blank=True, max_length=255, verbose_name='subject')
    user_image = models.ImageField(upload_to='testimonials', blank=True, default='testimonial-default.jpg', verbose_name='testimonial user image')

    def __str__(self):
        return self.user_name + " : " + self.detail


class OwnerClient(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, verbose_name="client name")
    website_link = models.URLField(null=True, blank=True, verbose_name="client website link")
    logo = models.ImageField(upload_to='client_logo', default='default_logo.png', blank=True, verbose_name='client logo')

    def __str__(self):
        return self.name


class OwnerCertificate(models.Model):
    certify_by = models.CharField(null=False, blank=False, max_length=255, verbose_name='certified by')
    detail = models.CharField(null=False, blank=False, max_length=255, verbose_name='detail')
    logo = models.ImageField(upload_to='certificate', blank=True, default='default_logo.png', verbose_name='certificate logo')
    certified_date = models.DateField(null=False, blank=False, verbose_name='certified date')

    def __str__(self):
        return "this certificate confirm by: " + self.certify_by + " - detail: " + self.detail


class OwnerKnowledge(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, verbose_name='owner knowledge')

    def __str__(self):
        return self.name


class OwnerExperienceDetail(models.Model):
    starting_year = models.CharField(null=False, blank=False, max_length=255, verbose_name='starting year')
    ending_year = models.CharField(null=False, blank=False, max_length=255, verbose_name='ending year')
    the_place = models.CharField(null=False, blank=False, max_length=255, verbose_name='the place')
    subject = models.CharField(null=False, blank=False, max_length=255, verbose_name='subject')
    content = models.TextField(null=False, blank=False, verbose_name='content')

    def __str__(self):
        return self.subject


class OwnerResumeSubject(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, verbose_name='name')
    owner_experience_detail = models.ManyToManyField(OwnerExperienceDetail, blank=True, verbose_name='owner experience detail')

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=255, verbose_name='first name')
    last_name = models.CharField(null=False, blank=False, max_length=255, verbose_name='last name')
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='age')
    residence = models.CharField(null=True, blank=True, max_length=255, verbose_name='residence')
    email = models.EmailField(null=True, blank=True, verbose_name='email')
    phone = models.CharField(null=True, blank=True, max_length=255, verbose_name='phone')
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name='address')
    profile_image = models.ImageField(null=True, blank=True, upload_to='owner_pic', default='main_photo.png', verbose_name='profile pic')
    about_me = models.TextField(null=True, blank=True, verbose_name='about me')
    pdf_cv = models.FileField(null=True, blank=True, upload_to='', verbose_name='CV.pdf')
    main_expertise = models.CharField(null=False, blank=False, max_length=255, verbose_name='main expertise')
    facebook = models.CharField(max_length=255, null=True, blank=True, verbose_name='facebook')
    twitter = models.CharField(max_length=255, null=True, blank=True, verbose_name='tweeter')
    linkedin = models.CharField(max_length=255, null=True, blank=True, verbose_name='linkedin')
    youtube = models.CharField(max_length=255, null=True, blank=True, verbose_name='youtube')
    instagram = models.CharField(max_length=255, null=True, blank=True, verbose_name='instagram')
    owner_expert_at = models.ManyToManyField(OwnerExpertAt, blank=True, verbose_name='owner expert at')
    owner_testimonial = models.ManyToManyField(OwnerTestimonial, blank=True, verbose_name='owner testimonial')
    owner_client = models.ManyToManyField(OwnerClient, blank=True, verbose_name='owner client')
    owner_certificate = models.ManyToManyField(OwnerCertificate, blank=True, verbose_name='owner certificate')
    owner_knowledge = models.ManyToManyField(OwnerKnowledge, blank=True, verbose_name='owner knowledge')
    owner_resume_subject = models.ManyToManyField(OwnerResumeSubject, blank=True, verbose_name='owner resume subject')

    def __str__(self):
        return self.first_name + " " + self.last_name

    # def get_absolute_url(self):
    #     return reverse('blog:blog-single', kwargs={'pid': self.id})

    class Meta:
        verbose_name = 'owner'
        verbose_name_plural = 'owner'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
