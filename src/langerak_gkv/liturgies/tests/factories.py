from datetime import time, date, timedelta

import factory
import factory.fuzzy

from ..models import Liturgy, MailRecipient, Service
from langerak_gkv.users.tests.factories import UserFactory


class ServiceFactory(factory.django.DjangoModelFactory):

    name = factory.Iterator(['Morning', 'Noon'])
    time = factory.Iterator([time(9, 30), time(14, 00)])

    class Meta:
        model = Service
        django_get_or_create = ('time',)


class LiturgyFactory(factory.django.DjangoModelFactory):

    date = factory.fuzzy.FuzzyDate(date.today(), date.today() + timedelta(days=14))
    service = factory.SubFactory(ServiceFactory)
    preacher = factory.fuzzy.FuzzyText(length=15)

    class Meta:
        model = Liturgy


class MailRecipientFactory(factory.django.DjangoModelFactory):

    liturgy = factory.SubFactory(LiturgyFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = MailRecipient
