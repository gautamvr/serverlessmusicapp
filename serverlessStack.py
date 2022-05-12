from aws_cdk import (
    aws_dynamodb as _dynamodb,
    aws_kinesis as _kinesis,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    aws_apigateway as _apigateway,
    core
)


class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        my_table= _dynamodb.Table(self,id='dynamoTable',table_name='testcdktable'
                                  ,partition_key=_dynamodb.Attribute(name='lastname',type=_dynamodb.AttributeType.STRING))    
                                  
        my_stream= _kinesis.Stream(self,id='kinesistream',stream_name='cdkkinesisstream')
        
        my_bucket= _s3.Bucket(self,id='s3bucket',bucket_name='rajcdkbucket')
        
        my_lambda= _lambda.Function(self,id='lambdafunction',runtime=_lambda.Runtime.PYTHON_3_7,
                    handler='hello.handler', 
                    code= _lambda.Code.asset('lambdacode')) 
                    
        my_api = _apigateway.LambdaRestApi(self,id='lambdaapi',rest_api_name='cdkapi',handler=my_lambda)
        
        api_with_method = _apigateway.RestApi(self,id='restapi',rest_api_name='cdkrestapi_music')
        #music = api_with_method.root.addResource('music')
        #music.addMethod('GET')
        music = api_with_method.root.add_resource('music')
        music.add_method('GET') 
        music.add_method("DELETE", _apigateway.HttpIntegration("http://aws.amazon.com"))
