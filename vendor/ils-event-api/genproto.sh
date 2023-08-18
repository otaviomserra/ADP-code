#!/usr/bin/env bash
protoc --proto_path=proto --python_out=../../ core/ils/external/types.proto
protoc --proto_path=proto --pyi_out=../../ core/ils/external/types.proto
protoc --proto_path=proto --python_out=../../ core/ils/external/organisation_event.proto
protoc --proto_path=proto --pyi_out=../../ core/ils/external/organisation_event.proto
