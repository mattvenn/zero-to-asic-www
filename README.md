# Setting up the *Zero to ASIC* Webpage Repository for Edits
1. Install [Hugo](https://gohugo.io/installation/) on your machine if you haven't already
2. Fork Matt Venn's [zero-to-asic-www repository](https://github.com/mattvenn/zero-to-asic-www)
3. Recursively clone your fork into a folder on your machine: `git clone --recursive <https://github.com/<githubusername>/<githubreponame>.git> `. This will create a new folder `<githubreponame>`.
4. From the command line or powershell, navigate into the folder with the cloned repository, and test the website: 
      * Enter `hugo server`. If you receive an error in the terminal indicating `render of page failed`, you likely forgot to add `--recursive` to `git clone`
      * Open a web browser and enter `localhost:1313` as the URL. The Zero to ASIC website should load.

## Getting Started with Edits
* **Verify edits:** Check any changes first locally using `hugo server` and going to `localhost:1313` in your browser before making a pull request
* **Blog Posts:** Create new markdown files in the `content/post/` directory 
   * For a blog post to appear in the *Related* sidebar, it needs to include the tag "course" in the markdown file header
* **Images:** Most  images are stored in the `static` directory
* **Linking to Other Site Pages:** Use relative paths for hyperlinks going to other pages from the website. For example, to link to a terminology page, use `[wordofinterest](/terminology/wordofinterest)` rather than `[wordofinterest](https://zerotoasiccourse.com/terminology/wordofinterest)`

## Submitting Changes
1. Push changes from your local repository to your fork
2. Submit a pull request at the [zero-to-asic-www](https://github.com/mattvenn/zero-to-asic-www) repository


# github actions

https://docs.github.com/en/actions/security-guides/encrypted-secrets


https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/#part-3-the-details


https://docs.github.com/en/actions/learn-github-actions/events-that-trigger-workflows

# secrets

gpg --symmetric --cipher-algo AES256 my_secret.json

shell script to decrypt: decrypt.sh
