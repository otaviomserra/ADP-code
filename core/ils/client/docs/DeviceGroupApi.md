# core.ils.client.DeviceGroupApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device_group_by_id**](DeviceGroupApi.md#delete_device_group_by_id) | **DELETE** /v1/core/device-groups/{deviceGroupId} | Delete a Device Group by id.
[**get_detailed_device_group_by_id**](DeviceGroupApi.md#get_detailed_device_group_by_id) | **GET** /v1/core/device-groups/{deviceGroupId}:detailed | Get a Device Group by id, detailed.
[**get_device_group_by_id**](DeviceGroupApi.md#get_device_group_by_id) | **GET** /v1/core/device-groups/{deviceGroupId} | Get a Device Group by id.
[**get_device_group_settings_by_device_id**](DeviceGroupApi.md#get_device_group_settings_by_device_id) | **GET** /v1/core/device-groups/{deviceGroupId}/settings | Get all Settings of a Device Group by id.
[**get_device_groups**](DeviceGroupApi.md#get_device_groups) | **GET** /v1/core/device-groups | Get all Device Groups, paginated.
[**get_device_tags_by_device_id1**](DeviceGroupApi.md#get_device_tags_by_device_id1) | **GET** /v1/core/device-groups/{deviceGroupId}/tags | Get all Tags of a Device Group by id.
[**remove_device_group_tag**](DeviceGroupApi.md#remove_device_group_tag) | **DELETE** /v1/core/device-groups/{deviceGroupId}/tags/{tag} | Remove a Tag from Device Group, if assigned already.
[**update_device_group_name**](DeviceGroupApi.md#update_device_group_name) | **PATCH** /v1/core/device-groups/{deviceGroupId}:rename | Rename a Device Group.
[**update_device_group_settings**](DeviceGroupApi.md#update_device_group_settings) | **PATCH** /v1/core/device-groups/{deviceGroupId}/settings | Update Settings of a Device Group.
[**update_device_group_tag**](DeviceGroupApi.md#update_device_group_tag) | **PATCH** /v1/core/device-groups/{deviceGroupId}/tags/{tag} | Add a Tag to a Device Group, if not assigned already.
[**update_device_group_tags**](DeviceGroupApi.md#update_device_group_tags) | **PUT** /v1/core/device-groups/{deviceGroupId}/tags | Replace all Tags of a Device Group.

# **delete_device_group_by_id**
> DefaultResponse delete_device_group_by_id(device_group_id)

Delete a Device Group by id.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.

try:
    # Delete a Device Group by id.
    api_response = api_instance.delete_device_group_by_id(device_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->delete_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_detailed_device_group_by_id**
> DeviceGroupDetailed get_detailed_device_group_by_id(device_group_id, organisation_id=organisation_id)

Get a Device Group by id, detailed.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get a Device Group by id, detailed.
    api_response = api_instance.get_detailed_device_group_by_id(device_group_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->get_detailed_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroupDetailed**](DeviceGroupDetailed.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_by_id**
> DeviceGroup get_device_group_by_id(device_group_id, organisation_id=organisation_id)

Get a Device Group by id.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get a Device Group by id.
    api_response = api_instance.get_device_group_by_id(device_group_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->get_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_settings_by_device_id**
> DeviceGroupTagsList get_device_group_settings_by_device_id(device_group_id, organisation_id=organisation_id)

Get all Settings of a Device Group by id.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get all Settings of a Device Group by id.
    api_response = api_instance.get_device_group_settings_by_device_id(device_group_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->get_device_group_settings_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroupTagsList**](DeviceGroupTagsList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups**
> DeviceGroupPaginatedList get_device_groups(organisation_id=organisation_id, page=page, size=size, sort=sort)

Get all Device Groups, paginated.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"timestamp,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["timestamp,DESC"])

try:
    # Get all Device Groups, paginated.
    api_response = api_instance.get_device_groups(organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->get_device_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;timestamp,DESC&quot;]]

### Return type

[**DeviceGroupPaginatedList**](DeviceGroupPaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_tags_by_device_id1**
> DeviceGroupTagsList get_device_tags_by_device_id1(device_group_id, organisation_id=organisation_id)

Get all Tags of a Device Group by id.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get all Tags of a Device Group by id.
    api_response = api_instance.get_device_tags_by_device_id1(device_group_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->get_device_tags_by_device_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroupTagsList**](DeviceGroupTagsList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_device_group_tag**
> DeviceGroup remove_device_group_tag(device_group_id, tag, organisation_id=organisation_id)

Remove a Tag from Device Group, if assigned already.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.
tag = 'tag_example' # str | The tag to remove from the Device Group.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Remove a Tag from Device Group, if assigned already.
    api_response = api_instance.remove_device_group_tag(device_group_id, tag, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->remove_device_group_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 
 **tag** | **str**| The tag to remove from the Device Group. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_name**
> DeviceGroup update_device_group_name(device_group_id, name, organisation_id=organisation_id)

Rename a Device Group.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.
name = 'name_example' # str | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Rename a Device Group.
    api_response = api_instance.update_device_group_name(device_group_id, name, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->update_device_group_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 
 **name** | **str**|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_settings**
> DeviceGroup update_device_group_settings(body, device_group_id, organisation_id=organisation_id)

Update Settings of a Device Group.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.DeviceGroupUpdateSettingsBody() # DeviceGroupUpdateSettingsBody | 
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Update Settings of a Device Group.
    api_response = api_instance.update_device_group_settings(body, device_group_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->update_device_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroupUpdateSettingsBody**](DeviceGroupUpdateSettingsBody.md)|  | 
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_tag**
> DeviceGroup update_device_group_tag(device_group_id, tag, organisation_id=organisation_id)

Add a Tag to a Device Group, if not assigned already.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.
tag = 'tag_example' # str | The tag to add to the Device Group.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Add a Tag to a Device Group, if not assigned already.
    api_response = api_instance.update_device_group_tag(device_group_id, tag, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->update_device_group_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 
 **tag** | **str**| The tag to add to the Device Group. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_tags**
> DeviceGroup update_device_group_tags(device_group_id, tags, organisation_id=organisation_id)

Replace all Tags of a Device Group.

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
api_instance = core.ils.client.DeviceGroupApi(core.ils.client.ApiClient(configuration))
device_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device Group's id.
tags = ['tags_example'] # list[str] | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Replace all Tags of a Device Group.
    api_response = api_instance.update_device_group_tags(device_group_id, tags, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupApi->update_device_group_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | [**str**](.md)| The Device Group&#x27;s id. | 
 **tags** | [**list[str]**](str.md)|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

