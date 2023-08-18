# core.ils.client.DeviceApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_device_by_id**](DeviceApi.md#delete_device_by_id) | **DELETE** /v1/core/devices/{deviceId} | Delete a Device by id.
[**get_detailed_device_by_id**](DeviceApi.md#get_detailed_device_by_id) | **GET** /v1/core/devices/{deviceId}:detailed | Get a Device by id, detailed.
[**get_device_by_id**](DeviceApi.md#get_device_by_id) | **GET** /v1/core/devices/{deviceId} | Get a Device by id.
[**get_device_settings_by_device_id**](DeviceApi.md#get_device_settings_by_device_id) | **GET** /v1/core/devices/{deviceId}/settings | Get all Settings of a Device by id.
[**get_device_tags_by_device_id**](DeviceApi.md#get_device_tags_by_device_id) | **GET** /v1/core/devices/{deviceId}/tags | Get all Tags of a Device by id.
[**get_devices**](DeviceApi.md#get_devices) | **GET** /v1beta1/core/devices | Get all Devices, paginated.
[**get_devices1**](DeviceApi.md#get_devices1) | **GET** /v1/core/devices | Get all Devices, paginated.
[**remove_device_tag**](DeviceApi.md#remove_device_tag) | **DELETE** /v1/core/devices/{deviceId}/tags/{tag} | Remove a Tag from Device, if assigned already.
[**update_device_name**](DeviceApi.md#update_device_name) | **PATCH** /v1/core/devices/{deviceId}:rename | Rename a Device.
[**update_device_settings**](DeviceApi.md#update_device_settings) | **PATCH** /v1/core/devices/{deviceId}/settings | Update Settings of a Device.
[**update_device_tag**](DeviceApi.md#update_device_tag) | **PATCH** /v1/core/devices/{deviceId}/tags/{tag} | Add a Tag to a Device, if not assigned already.
[**update_device_tags**](DeviceApi.md#update_device_tags) | **PUT** /v1/core/devices/{deviceId}/tags | Replace all Tags of a Device.

# **delete_device_by_id**
> DefaultResponse delete_device_by_id(device_id)

Delete a Device by id.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.

try:
    # Delete a Device by id.
    api_response = api_instance.delete_device_by_id(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->delete_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_detailed_device_by_id**
> DeviceDetailed get_detailed_device_by_id(device_id, organisation_id=organisation_id)

Get a Device by id, detailed.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get a Device by id, detailed.
    api_response = api_instance.get_detailed_device_by_id(device_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_detailed_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceDetailed**](DeviceDetailed.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> Device get_device_by_id(device_id, organisation_id=organisation_id)

Get a Device by id.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get a Device by id.
    api_response = api_instance.get_device_by_id(device_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_settings_by_device_id**
> DeviceTagsList get_device_settings_by_device_id(device_id, organisation_id=organisation_id)

Get all Settings of a Device by id.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get all Settings of a Device by id.
    api_response = api_instance.get_device_settings_by_device_id(device_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_settings_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceTagsList**](DeviceTagsList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_tags_by_device_id**
> DeviceTagsList get_device_tags_by_device_id(device_id, organisation_id=organisation_id)

Get all Tags of a Device by id.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Get all Tags of a Device by id.
    api_response = api_instance.get_device_tags_by_device_id(device_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_device_tags_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DeviceTagsList**](DeviceTagsList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> DevicePaginatedList get_devices(organisation_id=organisation_id, type=type, page=page, size=size, sort=sort)

Get all Devices, paginated.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
type = 'type_example' # str |  (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"id,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,DESC"])

try:
    # Get all Devices, paginated.
    api_response = api_instance.get_devices(organisation_id=organisation_id, type=type, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)|  | [optional] 
 **type** | **str**|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,DESC&quot;]]

### Return type

[**DevicePaginatedList**](DevicePaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices1**
> DevicePaginatedList get_devices1(organisation_id=organisation_id, page=page, size=size, sort=sort)

Get all Devices, paginated.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"timestamp,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["timestamp,DESC"])

try:
    # Get all Devices, paginated.
    api_response = api_instance.get_devices1(organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_devices1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;timestamp,DESC&quot;]]

### Return type

[**DevicePaginatedList**](DevicePaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_device_tag**
> Device remove_device_tag(device_id, tag, organisation_id=organisation_id)

Remove a Tag from Device, if assigned already.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.
tag = 'tag_example' # str | The tag to remove from the Device.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Remove a Tag from Device, if assigned already.
    api_response = api_instance.remove_device_tag(device_id, tag, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->remove_device_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 
 **tag** | **str**| The tag to remove from the Device. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_name**
> Device update_device_name(device_id, name, organisation_id=organisation_id)

Rename a Device.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.
name = 'name_example' # str | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Rename a Device.
    api_response = api_instance.update_device_name(device_id, name, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->update_device_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 
 **name** | **str**|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_settings**
> Device update_device_settings(body, device_id, organisation_id=organisation_id)

Update Settings of a Device.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.DeviceUpdateSettingsBody() # DeviceUpdateSettingsBody | 
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Update Settings of a Device.
    api_response = api_instance.update_device_settings(body, device_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->update_device_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceUpdateSettingsBody**](DeviceUpdateSettingsBody.md)|  | 
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_tag**
> Device update_device_tag(device_id, tag, organisation_id=organisation_id)

Add a Tag to a Device, if not assigned already.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.
tag = 'tag_example' # str | The tag to add to the Device.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Add a Tag to a Device, if not assigned already.
    api_response = api_instance.update_device_tag(device_id, tag, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->update_device_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 
 **tag** | **str**| The tag to add to the Device. | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_tags**
> Device update_device_tags(device_id, tags, organisation_id=organisation_id)

Replace all Tags of a Device.

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
api_instance = core.ils.client.DeviceApi(core.ils.client.ApiClient(configuration))
device_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Device's id.
tags = ['tags_example'] # list[str] | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Replace all Tags of a Device.
    api_response = api_instance.update_device_tags(device_id, tags, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->update_device_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| The Device&#x27;s id. | 
 **tags** | [**list[str]**](str.md)|  | 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

