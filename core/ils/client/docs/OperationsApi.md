# core.ils.client.OperationsApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_blink_operation**](OperationsApi.md#request_blink_operation) | **PUT** /v1/core/operations/set-light | Broadcast a Blink operation to all eligible Devices and/or Device Groups.
[**request_configure_put_to_light_for_lanes**](OperationsApi.md#request_configure_put_to_light_for_lanes) | **PUT** /v1beta1/kanban/operations/put-to-light:configure | Configure Put To Light for specified Lanes.
[**request_put_to_light_for_carrier**](OperationsApi.md#request_put_to_light_for_carrier) | **PUT** /v1beta1/kanban/operations/put-to-light | Broadcast a Put To Light request for the specified Carrier.
[**request_rfid_scan_operation**](OperationsApi.md#request_rfid_scan_operation) | **PUT** /v1/core/operations/rfid-scan | Broadcast a RFID Scan operation to all eligible Devices and/or Device Groups.
[**request_set_image_operation**](OperationsApi.md#request_set_image_operation) | **PUT** /v1beta1/kanban/operations/set-image | Broadcast a Set Image operation to all eligible Device
[**request_set_image_operation1**](OperationsApi.md#request_set_image_operation1) | **PUT** /v1/core/operations/set-image | Broadcast a Set Image operation to all eligible Device and/or Device Groups.
[**request_set_light**](OperationsApi.md#request_set_light) | **PUT** /v1beta1/kanban/operations/set-light | Broadcast a Set Light request for the specified Lanes or Devices.
[**request_test_me_device_group_operation**](OperationsApi.md#request_test_me_device_group_operation) | **GET** /v1/core/operations/test-me-device-group | Finds all eligible Device Groups for the given criteria. Nothing gets broadcast to targets.
[**request_test_me_device_operation**](OperationsApi.md#request_test_me_device_operation) | **GET** /v1/core/operations/test-me-device | Finds all eligible Devices for the given criteria. Nothing gets broadcast to targets.

# **request_blink_operation**
> DefaultResponse request_blink_operation(device_ids=device_ids, device_tags=device_tags, device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id)

Broadcast a Blink operation to all eligible Devices and/or Device Groups.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
device_ids = ['device_ids_example'] # list[str] |  (optional)
device_tags = ['device_tags_example'] # list[str] |  (optional)
device_group_ids = ['device_group_ids_example'] # list[str] |  (optional)
device_group_tags = ['device_group_tags_example'] # list[str] |  (optional)
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Broadcast a Blink operation to all eligible Devices and/or Device Groups.
    api_response = api_instance.request_blink_operation(device_ids=device_ids, device_tags=device_tags, device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_blink_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_tags** | [**list[str]**](str.md)|  | [optional] 
 **device_group_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_group_tags** | [**list[str]**](str.md)|  | [optional] 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_configure_put_to_light_for_lanes**
> DefaultResponse request_configure_put_to_light_for_lanes(body, organisation_id=organisation_id)

Configure Put To Light for specified Lanes.

Configure the behavior of a put to light by for example enabling put to light validation.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.ConfigurePutToLightOperationBody() # ConfigurePutToLightOperationBody | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Configure Put To Light for specified Lanes.
    api_response = api_instance.request_configure_put_to_light_for_lanes(body, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_configure_put_to_light_for_lanes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigurePutToLightOperationBody**](ConfigurePutToLightOperationBody.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_put_to_light_for_carrier**
> DefaultResponse request_put_to_light_for_carrier(body, organisation_id=organisation_id)

Broadcast a Put To Light request for the specified Carrier.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.PutToLightOperationBody() # PutToLightOperationBody | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Broadcast a Put To Light request for the specified Carrier.
    api_response = api_instance.request_put_to_light_for_carrier(body, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_put_to_light_for_carrier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutToLightOperationBody**](PutToLightOperationBody.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_rfid_scan_operation**
> DefaultResponse request_rfid_scan_operation(device_ids=device_ids, device_tags=device_tags, device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id)

Broadcast a RFID Scan operation to all eligible Devices and/or Device Groups.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
device_ids = ['device_ids_example'] # list[str] |  (optional)
device_tags = ['device_tags_example'] # list[str] |  (optional)
device_group_ids = ['device_group_ids_example'] # list[str] |  (optional)
device_group_tags = ['device_group_tags_example'] # list[str] |  (optional)
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Broadcast a RFID Scan operation to all eligible Devices and/or Device Groups.
    api_response = api_instance.request_rfid_scan_operation(device_ids=device_ids, device_tags=device_tags, device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_rfid_scan_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_tags** | [**list[str]**](str.md)|  | [optional] 
 **device_group_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_group_tags** | [**list[str]**](str.md)|  | [optional] 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_set_image_operation**
> DefaultResponse request_set_image_operation(body, organisation_id=organisation_id)

Broadcast a Set Image operation to all eligible Device

In order to broadcast an image to a device you must be aware of the following: Images must be encoded in Base64; the color depth must be 8-bit; The resolution of the image depends on the device itself; The color model of the image also depends on the device itself (binary images are always supported). If your devices are e-ink displays it will be very common that they have binary+1 screens. This means the only colors they support are black/white+1 (no shades of grey). WARNING: low resolution binary screens in conjunction with images that were rendered with antialiasing will result in degradation of the image once it is sent to the display. You are strongly advised to render images without antialiasing to not experience surprises.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.SetImageOperationBody() # SetImageOperationBody | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Broadcast a Set Image operation to all eligible Device
    api_response = api_instance.request_set_image_operation(body, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_set_image_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetImageOperationBody**](SetImageOperationBody.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_set_image_operation1**
> DefaultResponse request_set_image_operation1(device_ids=device_ids, device_tags=device_tags, device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id)

Broadcast a Set Image operation to all eligible Device and/or Device Groups.

In order to broadcast an image to a device you must be aware of the following: Images must be encoded in Base64; the color depth must be 8-bit; The resolution of the image depends on the device itself; The color model of the image also depends on the device itself (binary images are always supported). If your devices are e-ink displays it will be very common that they have binary+1 screens. This means the only colors they support are black/white+1 (no shades of grey). WARNING: low resolution binary screens in conjunction with images that were rendered with antialiasing will result in degradation of the image once it is sent to the display. You are strongly advised to render images without antialiasing to not experience surprises.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
device_ids = ['device_ids_example'] # list[str] |  (optional)
device_tags = ['device_tags_example'] # list[str] |  (optional)
device_group_ids = ['device_group_ids_example'] # list[str] |  (optional)
device_group_tags = ['device_group_tags_example'] # list[str] |  (optional)
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Broadcast a Set Image operation to all eligible Device and/or Device Groups.
    api_response = api_instance.request_set_image_operation1(device_ids=device_ids, device_tags=device_tags, device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_set_image_operation1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_tags** | [**list[str]**](str.md)|  | [optional] 
 **device_group_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_group_tags** | [**list[str]**](str.md)|  | [optional] 
 **organisation_id** | [**str**](.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_set_light**
> DefaultResponse request_set_light(body, organisation_id=organisation_id, lane_ids=lane_ids, device_ids=device_ids)

Broadcast a Set Light request for the specified Lanes or Devices.

Broadcasting light requests for devices has some caveats you need to be aware of. Not all devices that are supported have the same abilities. Some devices are able to display more colors than others; some devices are able to keep a light turned on indefinitely, others have only hardcoded intervals of time that can be used; some devices are able to keep a steady light and blink, others are only able to blink; some devices can be ordered to turn the light off (by sending the BLACK color) others you will need to wait for it to stop by itself.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
body = core.ils.client.SetLightOperationBody() # SetLightOperationBody | 
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)
lane_ids = ['lane_ids_example'] # list[str] | The Lane's id's. (optional)
device_ids = ['device_ids_example'] # list[str] | The Device's id's. (optional)

try:
    # Broadcast a Set Light request for the specified Lanes or Devices.
    api_response = api_instance.request_set_light(body, organisation_id=organisation_id, lane_ids=lane_ids, device_ids=device_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_set_light: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetLightOperationBody**](SetLightOperationBody.md)|  | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 
 **lane_ids** | [**list[str]**](str.md)| The Lane&#x27;s id&#x27;s. | [optional] 
 **device_ids** | [**list[str]**](str.md)| The Device&#x27;s id&#x27;s. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_test_me_device_group_operation**
> DefaultResponse request_test_me_device_group_operation(device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id, page=page, size=size, sort=sort)

Finds all eligible Device Groups for the given criteria. Nothing gets broadcast to targets.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
device_group_ids = ['device_group_ids_example'] # list[str] |  (optional)
device_group_tags = ['device_group_tags_example'] # list[str] |  (optional)
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"tags,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["tags,DESC"])

try:
    # Finds all eligible Device Groups for the given criteria. Nothing gets broadcast to targets.
    api_response = api_instance.request_test_me_device_group_operation(device_group_ids=device_group_ids, device_group_tags=device_group_tags, organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_test_me_device_group_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_group_tags** | [**list[str]**](str.md)|  | [optional] 
 **organisation_id** | [**str**](.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;tags,DESC&quot;]]

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_test_me_device_operation**
> DefaultResponse request_test_me_device_operation(device_ids=device_ids, device_tags=device_tags, organisation_id=organisation_id, page=page, size=size, sort=sort)

Finds all eligible Devices for the given criteria. Nothing gets broadcast to targets.

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
api_instance = core.ils.client.OperationsApi(core.ils.client.ApiClient(configuration))
device_ids = ['device_ids_example'] # list[str] |  (optional)
device_tags = ['device_tags_example'] # list[str] |  (optional)
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
size = 10 # int | The size of the page to be returned (optional) (default to 10)
sort = ['[\"tags,DESC\"]'] # list[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional) (default to ["tags,DESC"])

try:
    # Finds all eligible Devices for the given criteria. Nothing gets broadcast to targets.
    api_response = api_instance.request_test_me_device_operation(device_ids=device_ids, device_tags=device_tags, organisation_id=organisation_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->request_test_me_device_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ids** | [**list[str]**](str.md)|  | [optional] 
 **device_tags** | [**list[str]**](str.md)|  | [optional] 
 **organisation_id** | [**str**](.md)|  | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] [default to [&quot;tags,DESC&quot;]]

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

