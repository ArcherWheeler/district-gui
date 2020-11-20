#!/bin/sh
set -euxo pipefail

rm -rf dist
parcel build --public-url . index.html
mv dist docs
echo "redistrictingproject.com" > CNAME