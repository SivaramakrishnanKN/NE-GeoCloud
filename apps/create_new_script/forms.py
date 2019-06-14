# Define form for collecting user-defined
# script's parameters

from django import forms
from django.db.models import Q

from apps.data_cube_manager.models import DatasetType


def validate_product_sources(product_sources, num_input_products):
    if len(product_sources) != num_input_products:
        raise forms.ValidationError(('Number of products chosen did not match \
            specified number of products'))


class GetParametersForm(forms.Form):

    script_name = forms.CharField(label='Script Name',
                                  max_length=20,
                                  help_text='Give name for new application')
    num_input_products = forms.IntegerField(label='Number of Products',
                                            min_value=0,
                                            help_text='Give number of products \
                                                       this application works \
                                                       with')
    product_sources = forms.MultipleChoiceField(label='Product Sources',
                                                help_text='Select product\
                                                sources',
                                                validators=[
                                                    validate_product_sources])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dataset_types = DatasetType.objects.using('agdc').filter(
            Q(definition__has_keys=['managed']) & Q(definition__has_keys=[
                'measurements']))

        choices = ["All", *sorted(set([dataset_type.metadata['platform'][
            'code'] for dataset_type in dataset_types]))]
        self.fields['product_sources'].choices = (
            (product_sources, product_sources) for product_sources in choices)
