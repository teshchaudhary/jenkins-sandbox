import boto3

def create_glue_crawler():
    client = boto3.client('glue')

    response = client.create_crawler(
        Name='my-crawler',
        Role='AWSGlueServiceRole',
        DatabaseName='jenkins-database',
        Targets={
            'S3Targets': [
                {
                    'Path': 's3://jenkins-bucket-98741/'
                },
            ]
        },
        Schedule='',
        SchemaChangePolicy={
            'UpdateBehavior': 'UPDATE_IN_DATABASE',
            'DeleteBehavior': 'LOG'
        },
        RecrawlPolicy={
            'RecrawlBehavior': 'CRAWL_EVERYTHING'
        }
    )

    print(response)

if __name__ == "__main__":
    create_glue_crawler()
