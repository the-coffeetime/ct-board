import factory
from field.models import Fields


class FieldsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fields

    name = 'Test Field'
