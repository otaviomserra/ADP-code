# core.ils.client.KanbanControlCycleApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_kanban_card_to_carrier**](KanbanControlCycleApi.md#assign_kanban_card_to_carrier) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId}/cards:associate-carrier/{carrierId} | Assign a free Kanban Card, from a specific Kanban Control Cycle, to a Carrier.
[**associate_lane_to_kanban_control_cycle**](KanbanControlCycleApi.md#associate_lane_to_kanban_control_cycle) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:associate-lane/{laneId} | Associate a Lane to a Kanban Control Cycle.
[**associate_lane_to_kanban_control_cycle1**](KanbanControlCycleApi.md#associate_lane_to_kanban_control_cycle1) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:associate-lane/{address}:by-address | Associate a Lane to a Kanban Control Cycle.
[**create_kanban_control_cycle**](KanbanControlCycleApi.md#create_kanban_control_cycle) | **POST** /v1beta1/kanban/control-cycles | Create a new Kanban Control Cycle.
[**dissociate_lane_to_kanban_control_cycle**](KanbanControlCycleApi.md#dissociate_lane_to_kanban_control_cycle) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:dissociate-lane/{laneId} | Dissociate a Lane from a Kanban Control Cycle.
[**dissociate_lane_to_kanban_control_cycle1**](KanbanControlCycleApi.md#dissociate_lane_to_kanban_control_cycle1) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes:dissociate-lane/{address}:by-address | Dissociate a Lane from a Kanban Control Cycle.
[**get_kanban_control_cycle_by_external_id**](KanbanControlCycleApi.md#get_kanban_control_cycle_by_external_id) | **GET** /v1beta1/kanban/control-cycles/{externalId}:by-external-id | Get Kanban Control Cycle by External Id.
[**get_kanban_control_cycle_by_id**](KanbanControlCycleApi.md#get_kanban_control_cycle_by_id) | **GET** /v1beta1/kanban/control-cycles/{controlCycleId} | Get Kanban Control Cycle by Id.
[**get_kanban_control_cycle_cards**](KanbanControlCycleApi.md#get_kanban_control_cycle_cards) | **GET** /v1beta1/kanban/control-cycles/{controlCycleId}/cards | Get all Kanban Cards of a Kanban Control Cycle.
[**get_kanban_control_cycle_lanes**](KanbanControlCycleApi.md#get_kanban_control_cycle_lanes) | **GET** /v1beta1/kanban/control-cycles/{controlCycleId}/lanes | Get all Lanes assigned to a Kanban Control Cycle.
[**get_kanban_control_cycles**](KanbanControlCycleApi.md#get_kanban_control_cycles) | **GET** /v1beta1/kanban/control-cycles | Get all Kanban Control Cycles, paginated.
[**remove_card_from_kanban_control_cycle**](KanbanControlCycleApi.md#remove_card_from_kanban_control_cycle) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId}/cards/{cardId} | Remove a card from a Kanban Control Cycle.
[**remove_kanban_control_cycle**](KanbanControlCycleApi.md#remove_kanban_control_cycle) | **DELETE** /v1beta1/kanban/control-cycles/{controlCycleId} | Remove a Kanban Control Cycle.
[**update_kanban_control_cycle**](KanbanControlCycleApi.md#update_kanban_control_cycle) | **PUT** /v1beta1/kanban/control-cycles/{controlCycleId} | Update a Kanban Control Cycle.

# **assign_kanban_card_to_carrier**
> KanbanControlCycleCard assign_kanban_card_to_carrier(control_cycle_id, carrier_id, organisation_id=organisation_id, create_card_if_none_free=create_card_if_none_free)

Assign a free Kanban Card, from a specific Kanban Control Cycle, to a Carrier.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
carrier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Carrier's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
create_card_if_none_free = true # bool | By default the operation fails if there are no free Kanban Cards, enable to create a forcefully create a new one. (optional)

try:
    # Assign a free Kanban Card, from a specific Kanban Control Cycle, to a Carrier.
    api_response = api_instance.assign_kanban_card_to_carrier(control_cycle_id, carrier_id, organisation_id=organisation_id, create_card_if_none_free=create_card_if_none_free)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->assign_kanban_card_to_carrier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **carrier_id** | [**str**](.md)| The Carrier&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **create_card_if_none_free** | **bool**| By default the operation fails if there are no free Kanban Cards, enable to create a forcefully create a new one. | [optional] 

### Return type

[**KanbanControlCycleCard**](KanbanControlCycleCard.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_lane_to_kanban_control_cycle**
> DefaultResponse associate_lane_to_kanban_control_cycle(control_cycle_id, lane_id, organisation_id=organisation_id)

Associate a Lane to a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
lane_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Lane's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Associate a Lane to a Kanban Control Cycle.
    api_response = api_instance.associate_lane_to_kanban_control_cycle(control_cycle_id, lane_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->associate_lane_to_kanban_control_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
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

# **associate_lane_to_kanban_control_cycle1**
> DefaultResponse associate_lane_to_kanban_control_cycle1(control_cycle_id, address, organisation_id=organisation_id)

Associate a Lane to a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
address = 'address_example' # str | The Lane's address.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Associate a Lane to a Kanban Control Cycle.
    api_response = api_instance.associate_lane_to_kanban_control_cycle1(control_cycle_id, address, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->associate_lane_to_kanban_control_cycle1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **address** | **str**| The Lane&#x27;s address. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kanban_control_cycle**
> KanbanControlCycle create_kanban_control_cycle(body, organisation_id=organisation_id)

Create a new Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.KanbanControlCycleCreateBody() # KanbanControlCycleCreateBody | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Create a new Kanban Control Cycle.
    api_response = api_instance.create_kanban_control_cycle(body, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->create_kanban_control_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KanbanControlCycleCreateBody**](KanbanControlCycleCreateBody.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**KanbanControlCycle**](KanbanControlCycle.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dissociate_lane_to_kanban_control_cycle**
> DefaultResponse dissociate_lane_to_kanban_control_cycle(control_cycle_id, lane_id, organisation_id=organisation_id)

Dissociate a Lane from a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
lane_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Lane's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Dissociate a Lane from a Kanban Control Cycle.
    api_response = api_instance.dissociate_lane_to_kanban_control_cycle(control_cycle_id, lane_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->dissociate_lane_to_kanban_control_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
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

# **dissociate_lane_to_kanban_control_cycle1**
> DefaultResponse dissociate_lane_to_kanban_control_cycle1(control_cycle_id, address, organisation_id=organisation_id)

Dissociate a Lane from a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
address = 'address_example' # str | The Lane's address.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Dissociate a Lane from a Kanban Control Cycle.
    api_response = api_instance.dissociate_lane_to_kanban_control_cycle1(control_cycle_id, address, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->dissociate_lane_to_kanban_control_cycle1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **address** | **str**| The Lane&#x27;s address. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kanban_control_cycle_by_external_id**
> KanbanControlCycle get_kanban_control_cycle_by_external_id(external_id, organisation_id=organisation_id)

Get Kanban Control Cycle by External Id.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
external_id = 'external_id_example' # str | The Kanban Control Cycle's external id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get Kanban Control Cycle by External Id.
    api_response = api_instance.get_kanban_control_cycle_by_external_id(external_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->get_kanban_control_cycle_by_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**| The Kanban Control Cycle&#x27;s external id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**KanbanControlCycle**](KanbanControlCycle.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kanban_control_cycle_by_id**
> KanbanControlCycle get_kanban_control_cycle_by_id(control_cycle_id, organisation_id=organisation_id)

Get Kanban Control Cycle by Id.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get Kanban Control Cycle by Id.
    api_response = api_instance.get_kanban_control_cycle_by_id(control_cycle_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->get_kanban_control_cycle_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**KanbanControlCycle**](KanbanControlCycle.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kanban_control_cycle_cards**
> KanbanControlCycleCardList get_kanban_control_cycle_cards(control_cycle_id, organisation_id=organisation_id)

Get all Kanban Cards of a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get all Kanban Cards of a Kanban Control Cycle.
    api_response = api_instance.get_kanban_control_cycle_cards(control_cycle_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->get_kanban_control_cycle_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**KanbanControlCycleCardList**](KanbanControlCycleCardList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kanban_control_cycle_lanes**
> LaneList get_kanban_control_cycle_lanes(control_cycle_id, organisation_id=organisation_id)

Get all Lanes assigned to a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Get all Lanes assigned to a Kanban Control Cycle.
    api_response = api_instance.get_kanban_control_cycle_lanes(control_cycle_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->get_kanban_control_cycle_lanes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**LaneList**](LaneList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kanban_control_cycles**
> KanbanControlCyclePaginatedList get_kanban_control_cycles(organisation_id=organisation_id, page=page, size=size, sort=sort)

Get all Kanban Control Cycles, paginated.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"name,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["name,DESC"])

try:
    # Get all Kanban Control Cycles, paginated.
    api_response = api_instance.get_kanban_control_cycles(organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->get_kanban_control_cycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;name,DESC&quot;]]

### Return type

[**KanbanControlCyclePaginatedList**](KanbanControlCyclePaginatedList.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_card_from_kanban_control_cycle**
> DefaultResponse remove_card_from_kanban_control_cycle(control_cycle_id, card_id, organisation_id=organisation_id)

Remove a card from a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
card_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Card's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Remove a card from a Kanban Control Cycle.
    api_response = api_instance.remove_card_from_kanban_control_cycle(control_cycle_id, card_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->remove_card_from_kanban_control_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **card_id** | [**str**](.md)| The Card&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_kanban_control_cycle**
> DefaultResponse remove_kanban_control_cycle(control_cycle_id, organisation_id=organisation_id)

Remove a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Remove a Kanban Control Cycle.
    api_response = api_instance.remove_kanban_control_cycle(control_cycle_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->remove_kanban_control_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kanban_control_cycle**
> KanbanControlCycle update_kanban_control_cycle(body, control_cycle_id, organisation_id=organisation_id)

Update a Kanban Control Cycle.

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
api_instance = core.ils.client.KanbanControlCycleApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.KanbanControlCycleUpdateBody() # KanbanControlCycleUpdateBody | 
control_cycle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Kanban Control Cycle's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Update a Kanban Control Cycle.
    api_response = api_instance.update_kanban_control_cycle(body, control_cycle_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KanbanControlCycleApi->update_kanban_control_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KanbanControlCycleUpdateBody**](KanbanControlCycleUpdateBody.md)|  | 
 **control_cycle_id** | [**str**](.md)| The Kanban Control Cycle&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**KanbanControlCycle**](KanbanControlCycle.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

