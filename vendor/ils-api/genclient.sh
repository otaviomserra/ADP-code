#!/usr/bin/env bash

rm -rf output
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate \
    -i https://api.ils.neoception.dev/v3/api-docs/ \
    -l python \
    -o /local/output \
    -DpackageName=core.ils.client

BASE_DIR=../../core/ils

rm -rf $BASE_DIR/client/*

cp -r output/core/ils/client $BASE_DIR
cp output/README.md $BASE_DIR/client/
cp -r output/docs $BASE_DIR/client/

