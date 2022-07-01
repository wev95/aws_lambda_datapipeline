
def activate(client, pipeline_id):
  client.activate_pipeline(pipelineId=pipeline_id)

def get_definition(client, pipeline_id):
  return client.get_pipeline_definition(pipelineId=pipeline_id)
  
def delete(client, old_pipeline_id):
  client.delete_pipeline(pipelineId=old_pipeline_id)

def put_definition(client, new_pipeline_id, definition):
  client.put_pipeline_definition(
    pipelineId=new_pipeline_id, 
    pipelineObjects=definition['pipelineObjects'],  
    parameterObjects=definition['parameterObjects'],
    parameterValues=definition['parameterValues']
  )

def create(client, old_pipeline_id, pipeline_name):
  response_create = client.create_pipeline(
    name = pipeline_name, 
    uniqueId = old_pipeline_id, 
    description = "asurion financial reconciliation file data pipeline"  
  )

  return response_create

def find(client, pipeline_name):
  pipelines = client.list_pipelines()['pipelineIdList']

  for pip in pipelines:
    if pip['name'] == pipeline_name:
      return pip

  return None