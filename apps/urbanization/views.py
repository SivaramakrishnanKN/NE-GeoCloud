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

from apps.dc_algorithm.views import DataCubeVisualization, GetIngestedAreas
from django.shortcuts import render
from django.views import View
import json
import os
import subprocess


class DataCubeVisualization(DataCubeVisualization):

    """
    Create a Visualizer which shows all ingested data
    """
    tool_name = 'Urbanization'
    tool_inputs = 1
    tool_satellites = ['All', 'LANDSAT_5', 'LANDSAT_7', 'LANDSAT_8']
    tool_parameters = []

class GetIngestedData(GetIngestedAreas):

    pass

class OutputView(View):
    def post(self, request):

        if request.method == 'POST':
            lat_min = request.POST.get('lat_min')
            lat_max = request.POST.get('lat_max')
            long_min = request.POST.get('long_min')
            long_max = request.POST.get('long_max')
            product = request.POST.get('product')
            platform = request.POST.get('platform')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date') 
            
            cmd = 'python /home/localuser/Datacube/NE-GeoCloud/Scripts/urbanization.py ' + lat_min + ' ' + lat_max + ' ' + long_min + ' ' + long_max + ' ' + product + ' ' + platform + ' ' + start_date + ' ' + end_date 
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = p.communicate()
            context = {
                        'lat_min': lat_min,
                        'lat_max': lat_max,
                        'long_min': long_min,
                        'long_max': long_max,
                        'product': product,
                        'platform': platform,
                        'start_date': start_date,
                        'end_date': end_date,
                        'out' : out,
                        'err' : err
            }
            return render(request, 'urbanization/output.html', context)
            
        else:
            return HttpResponseBadRequest('Only POST requests are allowed')
    