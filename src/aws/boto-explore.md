###First call to boto3.resource('s3')
>>>s3 = boto3.resource('s3')
('s3',)
Entering boto3 session init method
enter Botocore Session object initiation
enter register components
enter lazy_register_component method in botocore.session.ComponentLocator
args: credential_provider, <bound method Session._create_credential_resolver of <botocore.session.Session object at 0x10ed4ce10>>
{}
{'credential_provider': <bound method Session._create_credential_resolver of <botocore.session.Session object at 0x10ed4ce10>>}
exit lazy_register_component method in botocore.session.ComponentLocator
enter lazy_register_component method in botocore.session.ComponentLocator
args: data_loader, <function Session._register_data_loader.<locals>.<lambda> at 0x10e1eeb70>
{}
{'credential_provider': <bound method Session._create_credential_resolver of <botocore.session.Session object at 0x10ed4ce10>>, 'data_loader': <function Session._register_data_loader.<locals>.<lambda> at 0x10e1eeb70>}
exit lazy_register_component method in botocore.session.ComponentLocator
enter lazy_register_component method in botocore.session.ComponentLocator
args: endpoint_resolver, <function Session._register_endpoint_resolver.<locals>.create_default_resolver at 0x10ed8ed08>
{}
{'endpoint_resolver': <function Session._register_endpoint_resolver.<locals>.create_default_resolver at 0x10ed8ed08>}
exit lazy_register_component method in botocore.session.ComponentLocator
enter register_component method in botocore.session.ComponentLocator
args: event_emitter, <botocore.hooks.EventAliaser object at 0x10e1eddd8>
exit register_component method in botocore.session.ComponentLocator
enter register_component method in botocore.session.ComponentLocator
args: response_parser_factory, <botocore.parsers.ResponseParserFactory object at 0x10ed4cda0>
exit register_component method in botocore.session.ComponentLocator
enter register_component method in botocore.session.ComponentLocator
args: exceptions_factory, <botocore.errorfactory.ClientExceptionsFactory object at 0x10ed8f518>
exit register_component method in botocore.session.ComponentLocator
enter register_component method in botocore.session.ComponentLocator
args: config_store, <botocore.configprovider.ConfigValueStore object at 0x10ed8f6a0>
exit register_component method in botocore.session.ComponentLocator
enter lazy_register_component method in botocore.session.ComponentLocator
args: monitor, <bound method Session._create_csm_monitor of <botocore.session.Session object at 0x10ed4ce10>>
{'exceptions_factory': <botocore.errorfactory.ClientExceptionsFactory object at 0x10ed8f518>}
{'endpoint_resolver': <function Session._register_endpoint_resolver.<locals>.create_default_resolver at 0x10ed8ed08>, 'monitor': <bound method Session._create_csm_monitor of <botocore.session.Session object at 0x10ed4ce10>>}
exit lazy_register_component method in botocore.session.ComponentLocator
exit register components
<botocore.session.SessionVarDict object at 0x10edb1e48>
<botocore.session.SessionVarDict object at 0x10edb1e48>
exit Botocore Session object initiation
after session object initiation
User agent name: Botocore
botocore_info: Botocore/1.17.44
component of type: <class 'botocore.hooks.EventAliaser'>
event emitter component: <botocore.hooks.EventAliaser object at 0x10e1eddd8>
['emit', 'emit_until_response', 'register', 'register_first', 'register_last', 'unregister']
{'aws_access_key_id': 'ASIAZTKLPTSFRJ6JVXTR', 'aws_secret_access_key': 'hl56bA2uCHQFOPTAMjTKUV56MBWkaAmWkD/gXPJY', 'aws_session_token': 'FwoGZXIvYXdzEAkaDMcQuOJO4kYVM+lkACKCAv51aUz5V/qQhrxPCzIhJylKAM7G6SPbZT/ccLVeD96dgLlw8bi2I2mIhCEVmJdMsCSmhQdWUaLpLplYLwakoj93JCJUlevdARjq2pJjrPbxPC113Glney8Bj/ywbaYu07zuPlaAlBP6bfq/EuZrA7orp0d8AdF9oHXzwyRItaj3rO+wIRFYMpdgW9EmeiWXfaA1IMwOmx8VUyaWDI5BSBm0AHUPxvptxhnBh+iT8v0wdtZGQETRz9y0ETGumY1cqInRTPfQAWF16vxFhg//Xe+ZWJL7hgXqY+ssY66Zk45c3Fhy8+TE2GlzGJ+WjJOCU9aJJpRKBOZ0NPCXb6Gmat30ZSirgNiBBjIr09AvPEi2zp1OuqpLWa/8RDUxf8C9ZSOdNG583084YMgXCw5GXKW8ePRM1Q==', 'aws_security_token': 'FwoGZXIvYXdzEAkaDMcQuOJO4kYVM+lkACKCAv51aUz5V/qQhrxPCzIhJylKAM7G6SPbZT/ccLVeD96dgLlw8bi2I2mIhCEVmJdMsCSmhQdWUaLpLplYLwakoj93JCJUlevdARjq2pJjrPbxPC113Glney8Bj/ywbaYu07zuPlaAlBP6bfq/EuZrA7orp0d8AdF9oHXzwyRItaj3rO+wIRFYMpdgW9EmeiWXfaA1IMwOmx8VUyaWDI5BSBm0AHUPxvptxhnBh+iT8v0wdtZGQETRz9y0ETGumY1cqInRTPfQAWF16vxFhg//Xe+ZWJL7hgXqY+ssY66Zk45c3Fhy8+TE2GlzGJ+WjJOCU9aJJpRKBOZ0NPCXb6Gmat30ZSirgNiBBjIr09AvPEi2zp1OuqpLWa/8RDUxf8C9ZSOdNG583084YMgXCw5GXKW8ePRM1Q=='}
Type of loader: <class 'botocore.loaders.Loader'>
['BUILTIN_DATA_PATH', 'BUILTIN_EXTRAS_TYPES', 'CUSTOMER_DATA_PATH', 'FILE_LOADER_CLASS', 'determine_latest_version', 'extras_types', 'file_loader', 'list_api_versions', 'list_available_services', 'load_data', 'load_service_model', 'search_paths']
['/Users/SMarya/.aws/models', '/Users/SMarya/WORK/nike-enablon-etl/venv/lib/python3.6/site-packages/botocore/data', '/Users/SMarya/WORK/nike-enablon-etl/venv/lib/python3.6/site-packages/boto3/data']
In boto3.utls.lazy_call: full_name: boto3.s3.inject.inject_s3_transfer_methods, kwargs: {}
In boto3.utls.lazy_call: full_name: boto3.s3.inject.inject_bucket_methods, kwargs: {}
In boto3.utls.lazy_call: full_name: boto3.s3.inject.inject_object_methods, kwargs: {}
In boto3.utls.lazy_call: full_name: boto3.s3.inject.inject_object_summary_methods, kwargs: {}
In boto3.utls.lazy_call: full_name: boto3.dynamodb.transform.register_high_level_interface, kwargs: {}
In boto3.utls.lazy_call: full_name: boto3.dynamodb.table.register_table_methods, kwargs: {}
In boto3.utls.lazy_call: full_name: boto3.ec2.createtags.inject_create_tags, kwargs: {}
In boto3.utls.lazy_call: full_name: boto3.ec2.deletetags.inject_delete_tags, kwargs: {'event_emitter': <botocore.hooks.EventAliaser object at 0x10e1eddd8>}
Exiting boto3 session init method
in boto3 session resource function call s3
in load service model
service_name: s3 ,type_name: resources-1, api_version: None
in list_available_services
in <generator object Loader._potential_locations at 0x10edd1200>
known_services:
possible_path: /Users/SMarya/WORK/nike-enablon-etl/venv/lib/python3.6/site-packages/botocore/data/s3
possible_path: /Users/SMarya/WORK/nike-enablon-etl/venv/lib/python3.6/site-packages/boto3/data/s3
before load data in Load Service model
call to load data
after load data in Load Service model
call to load data
end of Load Service model
type of resource: <class 'collections.OrderedDict'>
we have dict loaded from data/s3/json file, odict_keys(['service', 'resources'])
keys of keys: odict_keys(['CreateBucket']), odict_keys(['Create', 'Delete', 'DeleteObjects', 'PutObject'])
api_version: 2006-03-01
before client creation
enter create_client botocore
after getting data loader, event emitter, response parser
1
credentials
<botocore.credentials.EnvProvider object at 0x10edd4f28>
<botocore.credentials.AssumeRoleProvider object at 0x10ee1def0>
<botocore.credentials.AssumeRoleWithWebIdentityProvider object at 0x10ee1deb8>
<botocore.credentials.SSOProvider object at 0x10ee1de80>
<botocore.credentials.SharedCredentialProvider object at 0x10ee1de10>
<botocore.credentials.ProcessProvider object at 0x10ee1ddd8>
<botocore.credentials.ConfigProvider object at 0x10ee1dda0>
<botocore.credentials.OriginalEC2Provider object at 0x10ee1dfd0>
<botocore.credentials.BotoProvider object at 0x10ee1dd68>
<botocore.credentials.ContainerProvider object at 0x10ee1dba8>
<botocore.credentials.InstanceMetadataProvider object at 0x10ee1df98>
before
1
_fetch_metadata_token
_fetch_metadata_token2
_fetch_metadata_token3
_fetch_metadata_token4: 0
sending rereuest
AWSHTTPConnectionPool(host='169.254.169.254', port=80)
sending rereuest2
sending rereuest3
1
sending rereuest
AWSHTTPConnectionPool(host='169.254.169.254', port=80)
sending rereuest2
sending rereuest3
after
over
1
2
call to load data
2
before client_creator create client in botocore
IN botocore.client create_client method 1
IN botocore.client create_client method A
IN botocore.client create_client method B
in load service model
service_name: s3 ,type_name: service-2, api_version: 2006-03-01
in list_available_services
in <generator object Loader._potential_locations at 0x10edd1468>
known_services:
before load data in Load Service model
call to load data
after load data in Load Service model
call to load data
end of Load Service model
Service Model init method
IN botocore.client create_client method C
service_model: ServiceModel(s3)
service_model type: <class 'botocore.model.ServiceModel'>
in create client class method
IN _handler of lazy call, module: boto3.s3.inject, function_name: inject_s3_transfer_methods
in inject s3 trasnfer methods
None
IN botocore.client create_client method 10
IN botocore.client create_client method 3
<botocore.loaders.Loader object at 0x10edb5198>
call to load data
IN botocore.client create_client method 4
exit create_client botocore
after client creation
config: <botocore.config.Config object at 0x10edd4e80>
type of cls loaded from s3 json definition: <class 'boto3.resources.factory.s3.ServiceResource'>
type of cls created from s3 json definition: <class 'boto3.resources.factory.s3.ServiceResource'>
  
  
  
###Subsequent call to boto3.resource('s3')


>>>s3 = boto3.resource('s3')
('s3',)
in boto3 session resource function call s3
type of resource: <class 'collections.OrderedDict'>
we have dict loaded from data/s3/json file, odict_keys(['service', 'resources'])
keys of keys: odict_keys(['CreateBucket']), odict_keys(['Create', 'Delete', 'DeleteObjects', 'PutObject'])
api_version: 2006-03-01
before client creation
enter create_client botocore
after getting data loader, event emitter, response parser
1
credentials
<botocore.credentials.EnvProvider object at 0x10edd4f28>
<botocore.credentials.AssumeRoleProvider object at 0x10ee1def0>
<botocore.credentials.AssumeRoleWithWebIdentityProvider object at 0x10ee1deb8>
<botocore.credentials.SSOProvider object at 0x10ee1de80>
<botocore.credentials.SharedCredentialProvider object at 0x10ee1de10>
<botocore.credentials.ProcessProvider object at 0x10ee1ddd8>
<botocore.credentials.ConfigProvider object at 0x10ee1dda0>
<botocore.credentials.OriginalEC2Provider object at 0x10ee1dfd0>
<botocore.credentials.BotoProvider object at 0x10ee1dd68>
<botocore.credentials.ContainerProvider object at 0x10ee1dba8>
<botocore.credentials.InstanceMetadataProvider object at 0x10ee1df98>
before
1
_fetch_metadata_token
_fetch_metadata_token2
_fetch_metadata_token3
_fetch_metadata_token4: 0
sending rereuest
AWSHTTPConnectionPool(host='169.254.169.254', port=80)
sending rereuest2
sending rereuest3
1
sending rereuest
AWSHTTPConnectionPool(host='169.254.169.254', port=80)
sending rereuest2
sending rereuest3
after
over
1
2
2
before client_creator create client in botocore
IN botocore.client create_client method 1
IN botocore.client create_client method A
IN botocore.client create_client method B
Service Model init method
IN botocore.client create_client method C
service_model: ServiceModel(s3)
service_model type: <class 'botocore.model.ServiceModel'>
in create client class method
IN _handler of lazy call, module: boto3.s3.inject, function_name: inject_s3_transfer_methods
in inject s3 trasnfer methods
None
IN botocore.client create_client method 10
IN botocore.client create_client method 3
<botocore.loaders.Loader object at 0x10edb5198>
IN botocore.client create_client method 4
exit create_client botocore
after client creation
config: <botocore.config.Config object at 0x10edd4e80>
type of cls loaded from s3 json definition: <class 'boto3.resources.factory.s3.ServiceResource'>
type of cls created from s3 json definition: <class 'boto3.resources.factory.s3.ServiceResource'>
