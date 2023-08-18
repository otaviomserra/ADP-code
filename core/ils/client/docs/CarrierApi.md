# core.ils.client.CarrierApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dissociate_card_from_carrier**](CarrierApi.md#dissociate_card_from_carrier) | **DELETE** /v1beta1/kanban/carriers/{carrierId}:dissociate-card | Remove the association between the specified Carrier and a Kanban Card.

# **dissociate_card_from_carrier**
> DefaultResponse dissociate_card_from_carrier(carrier_id, organisation_id=organisation_id)

Remove the association between the specified Carrier and a Kanban Card.

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
api_instance = core.ils.client.CarrierApi(core.ils.client.ApiClient(configuration))
carrier_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The Carrier's id.
organisation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Target Organisation / Sub Organisation, user's base level applied by default. (optional)

try:
    # Remove the association between the specified Carrier and a Kanban Card.
    api_response = api_instance.dissociate_card_from_carrier(carrier_id, organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierApi->dissociate_card_from_carrier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_id** | [**str**](.md)| The Carrier&#x27;s id. | 
 **organisation_id** | [**str**](.md)| Target Organisation / Sub Organisation, user&#x27;s base level applied by default. | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

[token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

