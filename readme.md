# Setup
You'll need npm. I'd recommend using brew if you don't have it. (https://brew.sh/)

```
brew install node
npm install
```

To run locally (http://localhost:1234/):
```
npm run start
```

This app uses openlayers.org and bundles it into a single app as recommended with parcel.

# Update
add geojson to `district_plans` folder. Run:
```
npm run predeploy
```
Then commit the geojson files *and* the produced `dist` folder. After pushing you'll need to run
```
git subtree push --prefix dist origin gh-pages
```
which pushes a branch as a subtree so that github pages updates. The maps can then be viewed at archerwheeler.github.io/district-gui#STATE_NAME