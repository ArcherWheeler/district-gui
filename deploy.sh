#!/bin/sh
set -euxo pipefail

rm -rf docs
npm run predeploy
cp -R pages/assets dist
mv dist docs
echo "redistrictingproject.com" > docs/CNAME