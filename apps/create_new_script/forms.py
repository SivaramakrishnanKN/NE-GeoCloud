# Define form for collecting user-defined
# script's parameters

from django import forms
from django.db.models import Q

from apps.data_cube_manager.models import DatasetType


def validate_product_sources(product_sources, num_input_products):
    if not len(product_sources) == num_input_products:
        raise forms.ValidationError(('Number of products chosen did not match \
            specified number of products'))


def validate_param_name(sourcefile, param_name):
    with open(sourcefile) as notebook:
        for line in notebook:
            for word in line.split():
                if param_name in word:
                    return True
    return False


class GetProductDetailsForm(forms.Form):

    script_name = forms.CharField(label='Script Name',
                                  max_length=20,
                                  required=True,
                                  help_text='Give name for new application')
    script_details = forms.CharField(label='Script Details',
                                     max_length=300,
                                     required=True,
                                     help_text='Provide a small description of\
                                     your algorithm')
    num_input_products = forms.IntegerField(label='Number of Products',
                                            min_value=0,
                                            required=True,
                                            help_text='Give number of products \
                                                       this application works \
                                                       with')
    # product_sources = forms.MultipleChoiceField(label='Product Sources',
    #                                             help_text='Select product\
    #                                             sources',
    #                                             validators=[
    #                                                 validate_product_sources])
    script = forms.FileField(
        label='Script',
        required=True,
        allow_empty_file=False,
        widget=forms.ClearableFileInput(attrs={'class': 'chip',
            'style': 'width:250px',
            'placeholder': "None",
            'name' : 'script'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dataset_types = DatasetType.objects.using('agdc').filter(
            Q(definition__has_keys=['managed']) & Q(definition__has_keys=[
                'measurements']))

        # choices = ["All", *sorted(set([dataset_type.metadata['platform'][
        #     'code'] for dataset_type in dataset_types]))]
        # self.fields['product_sources'].choices = (
        #     (product_sources, product_sources) for product_sources in choices)


class GetHyperParametersForm(forms.Form):

    parameter_name = forms.CharField(label='Parameter Name',
                                     max_length=20,
                                     help_text='This is the name as seen by the\
                                     script users',
                                     validators=[
                                        validate_param_name])
    parameter_variable = forms.CharField(label='Varaible name',
                                         max_length=30,
                                         help_text='This is the name of the corresponding\
                                         variable in the script')
    param_min_value = forms.IntegerField(label='Min paramater value',
                                         help_text='Provide minimum value for\
                                         paramater tuning')
    param_max_value = forms.IntegerField(label='Max paramater value',
                                         help_text='Provide maximum value for\
                                         paramater tuning')
    details = forms.CharField(label='Details',
                              max_length=150,
                              help_text='Give details for given parmeter\
                              (optional)',
                              required=False)
