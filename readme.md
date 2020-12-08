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
Commit any changes you want deployed to the master branch. Run `./deploy.sh`. This will build the `/dist` directory and copy it (along with other necessary assets) to the `/docs` folder which github-pages uses to display the site. Commit the updated `/docs` directory and push the changes. It can take around 10m to deploy and sometimes I've found github-pages can have a weird intermediary state where it's only half updated and things break. Once the page is finally updated you might need to hard refresh to see all the changes (cmd + shift + R).