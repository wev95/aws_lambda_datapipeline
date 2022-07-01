import os
import json
import boto3
import botocore.exceptions
from config.logger_utils import logger
import service.pipeline_service as pipeline_service

def main(event, context):
    logger.info("started asurion-financial-reconciliation-file-data-pipeline-lambda")
    
    start_data_pipeline()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Starting datapipeline.')
    }

def start_data_pipeline():
  pipeline_name = os.getenv('DATAPIPELINE_NAME')

  client = boto3.client('datapipeline', region_name=os.getenv('REGION'))

  pipeline_id_delete = pipeline_service.find(client, pipeline_name)

  if pipeline_id_delete == None:

    try:
        old_pipeline_id = pipeline_id_delete['id']
      
        definition = pipeline_service.get_definition(client, old_pipeline_id)
        pipeline_service.delete(client, old_pipeline_id)

        new_pipeline = pipeline_service.create(client, old_pipeline_id, pipeline_name)
        
        new_pipeline_id = new_pipeline['pipelineId']
        
        pipeline_service.put_definition(client, new_pipeline_id, definition)

        pipeline_service.activate(client, new_pipeline_id)

        logger.info("{ DataPipelineName: %s DataPipelineId: %s Message: Successfully activated. }", pipeline_name, new_pipeline_id)
    except botocore.exceptions.ClientError as ex:
        logger.error(ex)
        raise ex
  else:
    logger.info("%s DataPipeline não encontrado.", pipeline_name)
