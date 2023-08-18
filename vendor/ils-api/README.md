# What is this?

The ILS API is defined through the OpenAPI standard, therefore you can leverage from code generation to get client code
generated for you, on your language of choice (in this case Python).

You do not need to worry about this, since Neoception® will do it's best to keep the ILS API backwards compatible, but
if there are some new functionality that could be interesting for you then it is just a matter of running the provided
script to update the client code. 

# How to update?

## Requirements

- docker
- be online (Internet access) and able to access https://api.ils.neoception.dev/v3/api-docs/

## Procedure

- run `./genclient.sh`