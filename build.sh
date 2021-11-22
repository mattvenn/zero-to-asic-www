HUGO_ENV=production hugo
#cd public
#git add *
#git commit -m 'update'
#git push --force
tar -czf z2a.tar.gz public
scp z2a.tar.gz matt@zerotoasiccourse.com:/tmp/
