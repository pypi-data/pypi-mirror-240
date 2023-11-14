'''
Date         : 2022-10-25 15:44:41
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-11-13 11:00:19
LastEditors  : BDFD
Description  : 
FilePath     : \execdata\__init__.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''

from execdata import templateproj
from .eda.data_conversion import *
from .eda import _data_mining, _data_preprocess, _standardization, _feature_selection
# from execdata.standardization import encode
from .model import _model_evaluate
from .graph import _data_analysis_graph, _data_mining_graph
