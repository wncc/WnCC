The official website for [WnCC](www.wncc-iitb.org) resides in this repository.

###Instructions for Contributing to WnCC website:

#####If you want a page to be added/edited: 
Please open a PR to WnCC:development.

#####If you are a mentor, and want to update your SoC page:
Please create a PR to WnCC:development. All content you add will go to your project page. Keep a brief introduction regarding the page at the start followed by a `<!--break-->` and further by more content. Everything prior to the break will appear in the short project description in the main SoC page under "List of Projects". Don't forget to update the list of mentees. You may also want to keep your project page updated with where the project is headed and what all has been accomplished.

#####If adding an event/showcase/soc-project:
Add a relevant image to the `_images` folder and resize it if needed using the `resize.py` script. If it doesn't need to be resized add it to the ignored list inside `resize.py`. If in doubt or unable to do the above, mention it in the PR.

#####If you are a collaborator:
Please (jekyll) build and push to the master. Server is on auto-deploy and reflects everything built and pushed to master. **Do not forget to cherry-pick the last commits from master to gh-pages. Also checkout development and merge it with master.** If you don't want to do the above, just create a PR with the change to WnCC:development.