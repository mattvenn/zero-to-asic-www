HUGO_ENV=production hugo
cd public
git add *
git commit -m 'update'
git push
