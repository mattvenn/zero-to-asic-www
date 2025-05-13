# Contributing to the Zero to ASIC Website
1. Install hugo:
    * Linux: `snap install hugo`
    * Other platforms: https://gohugo.io/getting-started/installing/
2. Fork the [zero-to-asic-www](https://github.com/mattvenn/zero-to-asic-www) repository
3. Recursively clone your fork into a folder on your machine: `git clone --recursive <https://github.com/<githubusername>/<githubreponame>.git> `. This will create a new folder `<githubreponame>`.
4. From a command line, navigate into the folder with the cloned repository, and test the website: 
      * Enter `hugo server`. If you receive an error in the terminal indicating `render of page failed`, you likely forgot to add `--recursive` to `git clone`
      * Open a web browser and enter `localhost:1313` as the URL. The Zero to ASIC website should load.

## Getting Started with Edits
* **Blog Posts:** Create new markdown files in the `content/post/` directory 
   * For a blog post to appear in the *Related* sidebar, it needs to include the tag "course" in the markdown file header
* **Images:** Most  images are stored in the `static` directory
* **Linking to Other Site Pages:** Use relative paths for hyperlinks going to other pages from the website. For example, to link to a terminology page, use `[wordofinterest](/terminology/wordofinterest)` rather than `[wordofinterest](https://zerotoasiccourse.com/terminology/wordofinterest)`
* **Verify edits:** Check any changes first locally using `hugo server` and going to `localhost:1313` in your browser before making a pull request

## Submitting Changes
1. Push changes from your local repository to your fork
2. Submit a pull request


# github actions

https://docs.github.com/en/actions/security-guides/encrypted-secrets


https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/#part-3-the-details


https://docs.github.com/en/actions/learn-github-actions/events-that-trigger-workflows

# secrets

use encrypt.sh to encrypt
use decrypt.sh to decrypt

password in tweet-a-term bitwarden

**if testing, make sure to put password in single quotes!**
**single quotes!!!!**
