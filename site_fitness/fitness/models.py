from django.contrib.postgres.fields import ArrayField

from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    date_delete = models.DateTimeField(null=True, blank=True)
    is_group = models.BooleanField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class SportServices(models.IntegerChoices):
        TOWEL = 1
        WATER_BOTTLE = 2
        SAUNA = 3
        PERSONAL_LOCKER = 4
        DISPOSABLE_SLIPPERS = 5

    sport_services = ArrayField(models.IntegerField(choices=SportServices.choices), null=True, blank=True)
    description = models.TextField()
    group_status_changing = models.BooleanField(default=True, null=True, blank=True)
    max_clients = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('Service', on_delete=models.PROTECT, null=True, blank=True)
    photos = models.ManyToManyField('ServicePhoto', null=True, blank=True)
    advantages = models.ManyToManyField('Advantage', null=True, blank=True)
    visits = models.ManyToManyField('Visit', through='VisitService', null=True, blank=True)
    subscriptions = models.ManyToManyField('Subscription', null=True, blank=True)
    discounts = models.ManyToManyField('Discount', through='DiscountService', null=True, blank=True)


    def __str__(self):
        return self.name

class ServicePhoto(models.Model):
    photo_path = models.ImageField(upload_to="photos/")
    date_delete = models.DateTimeField(null=True, blank=True)


class Advantage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo_path = models.ImageField(upload_to="photos/", null=True, blank=True)
    date_delete = models.DateTimeField(null=True, blank=True)


class Visit(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_individual = models.BooleanField(null=True, blank=True)
    date_cancel = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    client = models.ForeignKey('Client', on_delete=models.PROTECT)


class VisitService(models.Model):
    visit = models.ForeignKey('Visit', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    phone = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    photo_path = models.ImageField(upload_to="photos/", null=True, blank=True)
    is_hourly = models.BooleanField(null=True, blank=True)

    class SportCategories(models.IntegerChoices):
        MASTER_OF_SPORTS_OF_INTERNATIONAL_CLASS = 1
        MASTER_OF_SPORTS = 2
        CANDIDATE_FOR_MASTER_OF_SPORTS = 3
        WITHOUT_A_SPORTS_CATEGORY = 4

    sport_category = models.IntegerField(choices=SportCategories.choices)
    date_delete = models.DateTimeField(null=True, blank=True)
    text_for_visit = models.TextField(null=True, blank=True)
    passwd = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    services = models.ManyToManyField('Service', null=True, blank=True)
    roles = models.ManyToManyField('Role', null=True, blank=True)


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    mail = models.CharField(max_length=255, verbose_name='Почта')
    date_of_birth = models.DateTimeField(verbose_name='Дата рождения')
    photo_path = models.ImageField(upload_to="photos/", null=True, verbose_name='Фото', blank=True)
    comment = models.TextField(null=True, blank=True)
    subscriptions = models.ManyToManyField('Subscription', through='ClientSubscription', null=True, blank=True)
    groups = models.ManyToManyField('Group', null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']


class Application(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=255, verbose_name='Телефон')

    class Status(models.IntegerChoices):
        REFUSED = 1
        WAITING_CALL = 2
        COMPLETED = 3
    date_create = models.DateTimeField(auto_now_add=True)
    date_complete = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=Status.choices, default=2)


class ClientSubscription(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True)


class Feedback(models.Model):
    main_phrase = models.CharField(max_length=255)
    photo_path = models.ImageField(upload_to="photos/", null=True, blank=True )

    class Marks(models.IntegerChoices):
        BAD = 1
        NOT_SATISFACTORY = 2
        SATISFACTORY = 3
        GOOD = 4
        EXCELLENT = 5

    mark = models.IntegerField(choices=Marks.choices)
    date_create = models.DateTimeField(auto_now_add=True)
    date_approve = models.DateTimeField(null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.PROTECT)
    service = models.ForeignKey('Service', on_delete=models.PROTECT, null=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=True, blank=True)


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    description = ArrayField(models.CharField(max_length=250), null=True, blank=True)
    date_delete = models.DateTimeField(null=True, blank=True)


class Group(models.Model):
    service = models.ForeignKey('Service', on_delete=models.PROTECT)
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Favourites(models.Model):
    client = models.ForeignKey('Client', on_delete=models.PROTECT)
    service = models.ForeignKey('Service', on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)


class Discount(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo_path = models.ImageField(upload_to="photos/", null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_delete = models.DateTimeField(null=True, blank=True)
    is_visible = models.BooleanField(default=True)
    is_fixed = models.BooleanField()
    discount_amount_absolute = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_amount_percent = models.IntegerField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)


class DiscountService(models.Model):
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)


class Role(models.Model):
    name = models.CharField(max_length=255)
    date_delete = models.DateTimeField(null=True, blank=True)
    permissions = models.ManyToManyField('Permission')
    place = models.ForeignKey('Service', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

class ServiceTimetable(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE)


class EmployeeTimetable(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)


class GroupTimetable(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE)