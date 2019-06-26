# Copyright 2016 United States Government as represented by the Administrator
# of the National Aeronautics and Space Administration. All Rights Reserved.
#
# Portion of this code is Copyright Geoscience Australia, Licensed under the
# Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License
# at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# The CEOS 2 platform is licensed under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django import forms
from django.core.validators import RegexValidator, validate_comma_separated_integer_list, validate_slug
from django.core import validators
from django.db.models import Q

import re
import datetime

from apps.dc_algorithm.utils import logical_xor
from apps.data_cube_manager.models import DatasetType


class VisualizationForm(forms.Form):
    """Form meant to validate all metadata fields for an ingestion configuration file."""
    
    def __init__(self, product_number, *args, **kwargs):
        satellites = kwargs.pop('satellites')
        #product_number = kwargs.pop('number')
        super(VisualizationForm, self).__init__(*args, **kwargs)
        
        dataset_types = DatasetType.objects.using('agdc').filter(
            Q(definition__has_keys=['managed']) & Q(definition__has_keys=['measurements']))

        # The below line gets all dataset_types from the database which have measurement
        #choices = ["All", *sorted(set([dataset_type.metadata['platform']['code'] for dataset_type in dataset_types]))]
        self.fields['start_date_%s' % product_number] = forms.CharField(
            label='Start Date',
            error_messages={'required': 'Start date is required.'},
            widget=forms.DateInput(attrs={
            'class': 'datepicker field-divided onchange_filter',
            'placeholder': '01/01/2010',
            'onchange': "update_shown_cubes(%d)" %product_number
        }))
        self.fields['end_date_%s' % product_number] = forms.DateField(
            label='End Date',
            error_messages={'required': 'End date is required.'},
            widget=forms.DateInput(attrs={
                'class': 'datepicker field-divided onchange_filter',
                'placeholder': '01/02/2010',
                'onchange': "update_shown_cubes(%d)" %product_number
        }))
        self.fields['platform_%s' % product_number] = forms.MultipleChoiceField(
            label="Source Dataset Type",
            help_text="Select a platform to filter Data Cubes",
            widget=forms.Select(attrs={'class': "onchange_refresh",
                                   'onchange': "update_shown_cubes(%d)" %product_number
                                   }))
        self.fields['platform_%s' % product_number].choices = ((satellite, satellite) for satellite in satellites)
        
