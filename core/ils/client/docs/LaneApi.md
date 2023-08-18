# core.ils.client.LaneApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lane**](LaneApi.md#get_lane) | **GET** /v1beta1/kanban/lanes/{laneId} | Get a Lane by id.
[**get_lane_by_address**](LaneApi.md#get_lane_by_address) | **GET** /v1beta1/kanban/lanes/{address}:by-address | Get a Lane by address.
[**get_lane_stock_trigger**](LaneApi.md#get_lane_stock_trigger) | **GET** /v1beta1/kanban/lanes/{laneId}/triggers:stock | Get a Lane&#x27;s Stock Trigger.
[**get_lanes**](LaneApi.md#get_lanes) | **GET** /v1beta1/kanban/lanes | Get all Lanes, paginated.
[**get_lanes_carriers**](LaneApi.md#get_lanes_carriers) | **GET** /v1beta1/kanban/lanes/{laneId}/carriers | Get all Carriers currently allocated to a Lane, paginated.
[**get_lanes_carriers1**](LaneApi.md#get_lanes_carriers1) | **GET** /v1beta1/kanban/lanes/carriers | Get all Carriers currently allocated to all Lanes, paginated.
[**remove_lane_stock_trigger**](LaneApi.md#remove_lane_stock_trigger) | **DELETE** /v1beta1/kanban/lanes/{laneId}/triggers:stock | Remove a Lane&#x27;s Stock Trigger.
[**set_lane_stock_trigger**](LaneApi.md#set_lane_stock_trigger) | **PUT** /v1beta1/kanban/lanes/{laneId}/triggers:stock/{threshold} | Set a Lane&#x27;s Stock Trigger.

# **get_lane**
> Lane get_lane(lane_id, organisation_id=organisation_id)

Get a Lane by id.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
lane_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Lane's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get a Lane by id.
    api_response = api_instance.get_lane(lane_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->get_lane: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lane_id** | [**str**](.md)| The Lane&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**Lane**](Lane.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lane_by_address**
> Lane get_lane_by_address(address, organisation_id=organisation_id)

Get a Lane by address.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
address = 'address_example' # str | The Lane's address.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get a Lane by address.
    api_response = api_instance.get_lane_by_address(address, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->get_lane_by_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The Lane&#x27;s address. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**Lane**](Lane.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lane_stock_trigger**
> LaneTrigger get_lane_stock_trigger(lane_id, organisation_id=organisation_id)

Get a Lane's Stock Trigger.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
lane_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Lane's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get a Lane's Stock Trigger.
    api_response = api_instance.get_lane_stock_trigger(lane_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->get_lane_stock_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lane_id** | [**str**](.md)| The Lane&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**LaneTrigger**](LaneTrigger.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lanes**
> LanePaginatedList get_lanes(organisation_id=organisation_id, page=page, size=size, sort=sort)

Get all Lanes, paginated.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"address,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["address,DESC"])

try:
    # Get all Lanes, paginated.
    api_response = api_instance.get_lanes(organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->get_lanes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;address,DESC&quot;]]

### Return type

[**LanePaginatedList**](LanePaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lanes_carriers**
> CarrierPaginatedList get_lanes_carriers(lane_id, organisation_id=organisation_id, page=page, size=size, sort=sort)

Get all Carriers currently allocated to a Lane, paginated.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
lane_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Lane's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"id,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,DESC"])

try:
    # Get all Carriers currently allocated to a Lane, paginated.
    api_response = api_instance.get_lanes_carriers(lane_id, organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->get_lanes_carriers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lane_id** | [**str**](.md)| The Lane&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,DESC&quot;]]

### Return type

[**CarrierPaginatedList**](CarrierPaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lanes_carriers1**
> LaneCarrierPaginatedList get_lanes_carriers1(organisation_id=organisation_id, page=page, size=size, sort=sort)

Get all Carriers currently allocated to all Lanes, paginated.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"id,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["id,DESC"])

try:
    # Get all Carriers currently allocated to all Lanes, paginated.
    api_response = api_instance.get_lanes_carriers1(organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->get_lanes_carriers1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;id,DESC&quot;]]

### Return type

[**LaneCarrierPaginatedList**](LaneCarrierPaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_lane_stock_trigger**
> DefaultResponse remove_lane_stock_trigger(lane_id, organisation_id=organisation_id)

Remove a Lane's Stock Trigger.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
lane_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Lane's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Remove a Lane's Stock Trigger.
    api_response = api_instance.remove_lane_stock_trigger(lane_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->remove_lane_stock_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lane_id** | [**str**](.md)| The Lane&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_lane_stock_trigger**
> LaneTrigger set_lane_stock_trigger(lane_id, threshold, organisation_id=organisation_id)

Set a Lane's Stock Trigger.

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
api_instance = core.ils.client.LaneApi(core.ils.client.ApiClient(configuration))
lane_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Lane's id.
threshold = 56 # int | The Stock Threshold value for the Trigger.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Set a Lane's Stock Trigger.
    api_response = api_instance.set_lane_stock_trigger(lane_id, threshold, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaneApi->set_lane_stock_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lane_id** | [**str**](.md)| The Lane&#x27;s id. | 
 **threshold** | **int**| The Stock Threshold value for the Trigger. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**LaneTrigger**](LaneTrigger.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

