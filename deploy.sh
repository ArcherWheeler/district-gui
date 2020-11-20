#!/bin/sh
set -euxo pipefail

rm -rf docs
npm run predeploy
mv dist docs
echo "redistrictingproject.com" > docs/CNAME