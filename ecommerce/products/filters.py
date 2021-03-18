import django_filters
from .models import *
from django_filters import CharFilter

class PersonFilter(django_filters.FilterSet):
    email_contains =CharFilter(field_name='email',
                               lookup_expr='icontains')
    firstname_contains =CharFilter(field_name='firstname',
                               lookup_expr='icontains')
    class Meta:
        model = Person
        fields = ''
