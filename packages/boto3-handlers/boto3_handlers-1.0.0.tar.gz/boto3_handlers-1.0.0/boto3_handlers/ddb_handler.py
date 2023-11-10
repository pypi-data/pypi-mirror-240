# Setup logging
import logging
logger = logging.getLogger(__name__)

import boto3, os

class DynamoDBHandler:
    """
    A generic class for handling AWS DynamoDB operations using Boto3.

    :type table_name: string
    :param table_name: Name of DynamoDB Table
    :type region: string
    :param region: Region for AWS client to be invoked. Relies on 'AWS_REGION' environment variable
    :type dynamodb: boto3.client
    :param dynamodb: AWS Boto3 client handler for DynamoDB table
    """

    def __init__(self, table_name):
        """
        Initialize the DynamoDBHandler.

        :type table_name: string
        :param table_name: Name of DynamoDB Table
        """

        self.table_name = table_name
        self.region = os.environ["AWS_REGION"]
        self.dynamodb = boto3.client('dynamodb', region_name=self.region)

    def put_item(self, item):

        response = self.dynamodb.put_item(
            TableName=self.table_name,
            Item=item,
        )

        logger.debug(f"{response=}")

        return response

    def batch_put_items(self, items):

        request_items = {
            self.table_name: [
                {'PutRequest': {'Item': item}} for item in items
            ]
        }

        response = self.dynamodb.batch_write_item(
            RequestItems=request_items,
        )

        logger.debug(f"{response=}")

        return response