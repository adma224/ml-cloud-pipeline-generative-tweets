"""

Under construction ....

"""

from aws_cdk import (
    core,
    aws_rds as rds,
    aws_secretsmanager as secretsmanager,
    aws_ec2 as ec2,
    aws_s3 as s3
)

from network_stack import NetworkStack

class DataStorageStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.data_bucket = s3.Bucket(self, "DataBucket",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )

        self.bucket_name = self.data_bucket.bucket_name

        self.db_credentials_secret = secretsmanager.Secret(self, "DBCredentialsSecret",
            description="Credentials for Aurora Serverless DB",
            secret_name="auroraServerlessCredentials"
        )

        self.database = rds.ServerlessCluster(self, "AuroraServerlessDB",
            engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc=vpc,
            credentials=rds.Credentials.from_secret(self.db_credentials_secret),  # Use credentials from Secrets Manager
            default_database_name="MyDatabase"
        )

vpc = NetworkStack.vpc  # Make sure this is the correct reference
data_storage_stack = DataStorageStack(app, "DataStorageStack", vpc=vpc)
