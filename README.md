# WnCC Website

The official website for [WnCC: www.wncc-iitb.org](https://www.wncc-iitb.org) resides in this repository.  
This website is completely static and runs on jekyll.

## Content: 

### [Wiki](http://wncc-iitb.org/wiki/)  
WnCC's own wiki. Containing wide-ranging articles, references and guides for everyone and especially beginners. Join the community, read, request, contribute and share!

### [SoC- Seasons of Code](http://wncc-iitb.org/soc/)  
Seasons of Code is a programme launched by the WnCC, along the lines of GSoC without much greenery though. The incentive is similar to ITSP, based on the current form of it, the fundamental difference is that one can choose from the ideas offered by mentors who are senior undergrads, doctorate students or professors, and in some exceptional cases, startups.

### [Showcase](http://wncc-iitb.org/showcase/)  
Some of the best projects, made by us. These could be hackathon ideas, applications that make your life easier or purely for fun, hobby projects.

### [Events](http://wncc-iitb.org/events/)  
A list of events that are planned and are coming soon.

## Contribution guidelines:

##### If you want a page to be added/edited: 
Please open a PR to WnCC:master.

##### If you are a mentor, and want to update your SoC page:
Please create a PR to WnCC:master. All content you add will go to your project page. Keep a brief introduction regarding the page at the start followed by a *newline* `<!--break-->` *newline* and further by more content. Everything prior to the break will appear in the short project description in the main SoC page under "List of Projects". Don't forget to update the list of mentees. You may also want to keep your project page updated with where the project is headed and what all has been accomplished.

##### If adding an event/showcase/soc-project:
Add a relevant image to the `_images` folder and resize it if needed using the `resize.py` script. If it doesn't need to be resized add it to the ignored list inside `resize.py`. If in doubt or unable to do the above, mention it in the PR.

##### If you are a collaborator:
Please (jekyll) build and push to the master. Server is on auto-deploy and reflects everything built and pushed to production. **Do not forget to cherry-pick the last commits from master to gh-pages. The gh-pages website is: [http://nihal111.github.io/WnCC/](http://nihal111.github.io/WnCC/) which serves as a backup to the main website. Also checkout production and merge it with master.** If you don't want to do the above, just create a PR with the change to WnCC:master.
