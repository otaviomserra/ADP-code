# core.ils.client.IdentifierApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_enrichment_schema**](IdentifierApi.md#create_enrichment_schema) | **POST** /v1/core/identifiers/enrichment-schemas | Create a Schema.
[**delete_enrichment_by_identifier_id**](IdentifierApi.md#delete_enrichment_by_identifier_id) | **DELETE** /v1/core/identifiers/{identifierId}/enrichments | Delete all Enrichments of an Identifier.
[**delete_enrichment_by_key_name_and_value**](IdentifierApi.md#delete_enrichment_by_key_name_and_value) | **DELETE** /v1/core/identifiers/enrichments/{key}:{value}:by-key-and-value | Delete all enrichments from all identifiers where specific key and value are present.
[**find_enrichments_with_non_unique_values_by_key_name**](IdentifierApi.md#find_enrichments_with_non_unique_values_by_key_name) | **GET** /v1/core/identifiers/enrichments/{key}:non-unique-values-by-key | Find all enrichments by identifier, where values occurring more than once, for a specific key.
[**generate_identifier**](IdentifierApi.md#generate_identifier) | **PUT** /v1beta1/core/identifiers | Generate an identifier based on a code and salt (optional).
[**generate_identifier1**](IdentifierApi.md#generate_identifier1) | **POST** /v1/core/identifiers | Generate an identifier based on a code and salt (optional).
[**get_enrichment_schema**](IdentifierApi.md#get_enrichment_schema) | **GET** /v1/core/identifiers/enrichment-schemas/{name} | Get the Schema for a specific name.
[**get_enrichment_schemas**](IdentifierApi.md#get_enrichment_schemas) | **GET** /v1/core/identifiers/enrichment-schemas | Get all Schemas.
[**get_identifier_by_id**](IdentifierApi.md#get_identifier_by_id) | **GET** /v1/core/identifiers/{identifierId} | Get an Identifier by id.
[**get_identifiers**](IdentifierApi.md#get_identifiers) | **GET** /v1/core/identifiers | Get all identifiers, paginated.
[**patch_enrichment_by_identifier_id**](IdentifierApi.md#patch_enrichment_by_identifier_id) | **PATCH** /v1/core/identifiers/{identifierId}/enrichments | Add or Update specific Enrichments of an Identifier.
[**update_enrichment_by_identifier_id**](IdentifierApi.md#update_enrichment_by_identifier_id) | **PUT** /v1/core/identifiers/{identifierId}/enrichments | Override all Enrichments of an Identifier.
[**update_enrichment_schema**](IdentifierApi.md#update_enrichment_schema) | **PUT** /v1/core/identifiers/enrichment-schemas/{name} | Update the Schema for a specific name.

# **create_enrichment_schema**
> EnrichmentSchema create_enrichment_schema(body, organisation_id=organisation_id)

Create a Schema.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.EnrichmentSchemaCreateBody() # EnrichmentSchemaCreateBody | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Create a Schema.
    api_response = api_instance.create_enrichment_schema(body, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->create_enrichment_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrichmentSchemaCreateBody**](EnrichmentSchemaCreateBody.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**EnrichmentSchema**](EnrichmentSchema.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrichment_by_identifier_id**
> Identifier delete_enrichment_by_identifier_id(identifier_id, organisation_id=organisation_id)

Delete all Enrichments of an Identifier.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
identifier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Identifier's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Delete all Enrichments of an Identifier.
    api_response = api_instance.delete_enrichment_by_identifier_id(identifier_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->delete_enrichment_by_identifier_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | [**str**](.md)| The Identifier&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**Identifier**](Identifier.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrichment_by_key_name_and_value**
> DefaultResponse delete_enrichment_by_key_name_and_value(key, value, organisation_id=organisation_id)

Delete all enrichments from all identifiers where specific key and value are present.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
key = 'key_example' # str | The Enrichment's key.
value = 'value_example' # str | The Enrichment's value.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Delete all enrichments from all identifiers where specific key and value are present.
    api_response = api_instance.delete_enrichment_by_key_name_and_value(key, value, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->delete_enrichment_by_key_name_and_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Enrichment&#x27;s key. | 
 **value** | **str**| The Enrichment&#x27;s value. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_enrichments_with_non_unique_values_by_key_name**
> IdentifierEnrichmentsDuplicatedOccurrence find_enrichments_with_non_unique_values_by_key_name(key, organisation_id=organisation_id)

Find all enrichments by identifier, where values occurring more than once, for a specific key.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
key = 'key_example' # str | The Enrichment's key.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Find all enrichments by identifier, where values occurring more than once, for a specific key.
    api_response = api_instance.find_enrichments_with_non_unique_values_by_key_name(key, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->find_enrichments_with_non_unique_values_by_key_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Enrichment&#x27;s key. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**IdentifierEnrichmentsDuplicatedOccurrence**](IdentifierEnrichmentsDuplicatedOccurrence.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_identifier**
> Identifier generate_identifier(body, organisation_id=organisation_id)

Generate an identifier based on a code and salt (optional).

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.IdentifierCreate() # IdentifierCreate | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Generate an identifier based on a code and salt (optional).
    api_response = api_instance.generate_identifier(body, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->generate_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentifierCreate**](IdentifierCreate.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**Identifier**](Identifier.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_identifier1**
> Identifier generate_identifier1(body, organisation_id=organisation_id)

Generate an identifier based on a code and salt (optional).

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.IdentifierCreate() # IdentifierCreate | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Generate an identifier based on a code and salt (optional).
    api_response = api_instance.generate_identifier1(body, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->generate_identifier1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentifierCreate**](IdentifierCreate.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**Identifier**](Identifier.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrichment_schema**
> EnrichmentSchema get_enrichment_schema(name, organisation_id=organisation_id)

Get the Schema for a specific name.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
name = 'name_example' # str | The name of the Enrichment Schema.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get the Schema for a specific name.
    api_response = api_instance.get_enrichment_schema(name, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->get_enrichment_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Enrichment Schema. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**EnrichmentSchema**](EnrichmentSchema.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrichment_schemas**
> EnrichmentSchemaList get_enrichment_schemas(organisation_id=organisation_id)

Get all Schemas.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get all Schemas.
    api_response = api_instance.get_enrichment_schemas(organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->get_enrichment_schemas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**EnrichmentSchemaList**](EnrichmentSchemaList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identifier_by_id**
> Identifier get_identifier_by_id(identifier_id, organisation_id=organisation_id)

Get an Identifier by id.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
identifier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Identifier's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get an Identifier by id.
    api_response = api_instance.get_identifier_by_id(identifier_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->get_identifier_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | [**str**](.md)| The Identifier&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**Identifier**](Identifier.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identifiers**
> IdentifierPaginatedList get_identifiers(organisation_id=organisation_id, enrichment_value_contains=enrichment_value_contains, enrichment_key_name_contains=enrichment_key_name_contains, identifier_types=identifier_types, page=page, size=size, sort=sort)

Get all identifiers, paginated.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
enrichment_value_contains = 'enrichment_value_contains_example' # str | Search for results with a Value containing this string. (optional)
enrichment_key_name_contains = 'enrichment_key_name_contains_example' # str | Search for results with a Key Name containing this string. (optional)
identifier_types = ['identifier_types_example'] # list[str] | The expected Types of the Identifier. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"createTime,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["createTime,DESC"])

try:
    # Get all identifiers, paginated.
    api_response = api_instance.get_identifiers(organisation_id=organisation_id, enrichment_value_contains=enrichment_value_contains, enrichment_key_name_contains=enrichment_key_name_contains, identifier_types=identifier_types, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->get_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **enrichment_value_contains** | **str**| Search for results with a Value containing this string. | [optional] 
 **enrichment_key_name_contains** | **str**| Search for results with a Key Name containing this string. | [optional] 
 **identifier_types** | [**list[str]**](str.md)| The expected Types of the Identifier. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;createTime,DESC&quot;]]

### Return type

[**IdentifierPaginatedList**](IdentifierPaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_enrichment_by_identifier_id**
> Identifier patch_enrichment_by_identifier_id(body, identifier_id, organisation_id=organisation_id, schema_name=schema_name)

Add or Update specific Enrichments of an Identifier.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.IdentifierEnrichmentsUpdateBody() # IdentifierEnrichmentsUpdateBody | 
identifier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Identifier's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
schema_name = 'schema_name_example' # str | The name of the Schema to validate the Parameters. (optional)

try:
    # Add or Update specific Enrichments of an Identifier.
    api_response = api_instance.patch_enrichment_by_identifier_id(body, identifier_id, organisation_id=organisation_id, schema_name=schema_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->patch_enrichment_by_identifier_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentifierEnrichmentsUpdateBody**](IdentifierEnrichmentsUpdateBody.md)|  | 
 **identifier_id** | [**str**](.md)| The Identifier&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **schema_name** | **str**| The name of the Schema to validate the Parameters. | [optional] 

### Return type

[**Identifier**](Identifier.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_enrichment_by_identifier_id**
> Identifier update_enrichment_by_identifier_id(body, identifier_id, organisation_id=organisation_id, schema_name=schema_name)

Override all Enrichments of an Identifier.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.IdentifierEnrichmentsUpdateBody() # IdentifierEnrichmentsUpdateBody | 
identifier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Identifier's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
schema_name = 'schema_name_example' # str | The name of the Schema to validate the Parameters. (optional)

try:
    # Override all Enrichments of an Identifier.
    api_response = api_instance.update_enrichment_by_identifier_id(body, identifier_id, organisation_id=organisation_id, schema_name=schema_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->update_enrichment_by_identifier_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentifierEnrichmentsUpdateBody**](IdentifierEnrichmentsUpdateBody.md)|  | 
 **identifier_id** | [**str**](.md)| The Identifier&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **schema_name** | **str**| The name of the Schema to validate the Parameters. | [optional] 

### Return type

[**Identifier**](Identifier.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_enrichment_schema**
> EnrichmentSchema update_enrichment_schema(body, name, organisation_id=organisation_id)

Update the Schema for a specific name.

### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = core.ils.client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: user
configuration = core.ils.client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = core.ils.client.IdentifierApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.EnrichmentSchemaUpdateBody() # EnrichmentSchemaUpdateBody | 
name = 'name_example' # str | The name of the Enrichment Schema.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Update the Schema for a specific name.
    api_response = api_instance.update_enrichment_schema(body, name, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifierApi->update_enrichment_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrichmentSchemaUpdateBody**](EnrichmentSchemaUpdateBody.md)|  | 
 **name** | **str**| The name of the Enrichment Schema. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**EnrichmentSchema**](EnrichmentSchema.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

