#!/usr/bin/env python3

from aws_cdk import core as cdk

from stacks.network_stack import NetworkStack
from stacks.sagemaker_stack import SageMakerStack
from stacks.data_storage_stack import DataStorageStack
from stacks.api_stack import APIStack
from stacks.appsync_stack import AppSyncStack
from stacks.analytics_visualization_stack import AnalyticsVisualizationStack
from stacks.security_stack import SecurityComplianceStack

app = cdk.App()

network_stack = NetworkStack(app, "NetworkStack")

sagemaker_stack = SageMakerStack(app, "SageMakerStack",
                                  vpc=network_stack.vpc)

data_storage_stack = DataStorageStack(app, "DataStorageStack")

api_stack = APIStack(app, "APIStack",
                     sagemaker_endpoint=sagemaker_stack.sagemaker_endpoint)

appsync_stack = AppSyncStack(app, "AppSyncStack",
                             data_storage=data_storage_stack.table)

analytics_visualization_stack = AnalyticsVisualizationStack(app, "AnalyticsVisualizationStack",
                                                             data_storage=data_storage_stack.bucket)

security_compliance_stack = SecurityComplianceStack(app, "SecurityComplianceStack")

app.synth()

