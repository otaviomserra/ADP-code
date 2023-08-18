# core.ils.client.AboutApi

All URIs are relative to *https://api.ils.neoception.dev/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**about**](AboutApi.md#about) | **GET** /about | 

# **about**
> str about()



### Example
```python
from __future__ import print_function
import time
import core.ils.client
from core.ils.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = core.ils.client.AboutApi()

try:
    api_response = api_instance.about()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->about: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

