#!/bin/bash
cp README.md docs/index.md
# TODO: generate openapi.json
# https://github.com/tiangolo/fastapi/issues/1173#issuecomment-605664503
mkdocs build --verbose
