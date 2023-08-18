# What is this?

The ILS Event API exposes business events with a specific `json` payload and this structure must ensure that customers depending on it have backwards compatibility ensured. Such contract is defined through a [protocol buffer](https://developers.google.com/protocol-buffers) description.

You do not need to worry or modify it.

> ⚠️ Actually you definitely should not modify anything.
> 
> In case a new event is made available, of your interest, a new `proto` file will be made available. You can then use the instructions documented bellow to update the generated code.

To your convenience, the code was already generated for you. You are strongly advised to deserialize the `json` payload this way and not *blindly* navigate through the data structure.

# How to update?

> ⚠️ If you are here, it is because you know what you are doing and really need to update the generated code.

## Requirements

- [protoc](https://grpc.io/docs/protoc-installation/) 

## Procedure

- replace the provided `proto` files
- run `./genproto.sh` (optionally you can run the `protoc` commands on your shell, if not using `bash`)
