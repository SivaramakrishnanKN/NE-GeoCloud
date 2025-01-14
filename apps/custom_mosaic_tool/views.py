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


class DataCubeVisualization(DataCubeVisualization):

    """
    Create a Visualizer which shows all ingested data
    """
    tool_name = 'Cloud Coverage'
    tool_inputs = 3
    tool_satellites = {'Landsat_5', 'Landsat_7', 'GPM'}


class GetIngestedData(GetIngestedAreas):

    pass
