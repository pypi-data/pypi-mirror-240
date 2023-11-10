# ##################################################################
#
# Copyright 2022 Teradata. All rights reserved.
# TERADATA CONFIDENTIAL AND TRADE SECRET
#
# Primary Owner: pt186002@teradata.com
# Secondary Owner:
#
# This file defines constants related to tdapiclient library
# ##################################################################

from enum import Enum


class TDApiClientConstants(Enum):
    SG_MODULE_LIST = ["sagemaker.mxnet.estimator",
                      "sagemaker", "sagemaker.sklearn.estimator",
                      "sagemaker.chainer", "sagemaker.huggingface",
                      "sagemaker.pytorch", "sagemaker.rl.estimator",
                      "sagemaker.tensorflow", "sagemaker.estimator",
                      "sagemaker.xgboost.estimator", "sagemaker.image_uris"]
    AZ_MODULE_LIST = ["azureml.core", "azureml.train.automl"]
    VX_MODULE_LIST = ["google.cloud.aiplatform"]