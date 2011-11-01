# What is Hackblogs?

Hackblogs is **DVCS based blog system for hackers**.   
A little explanation of the above sentence:

1. DVCS - your blog posts will be on Github/Bitbucket. You do not communicate
    with/use anything but git/hg and Github/Bitbucket
2. blog system - your blog is hosted statically (meaning HTML and CSS files)
    on our server
3. for hackers - you will write posts in rST, Markdown and similar formats
    and will use DVCS to publish them so it's expected of you to find your
    way around with this tools


### It works like this:

1. Create repository on Github/Bitbucket that will host your blog posts
   - for now, repository needs to be public, in future we will also support
   private repos
2. Set commit POST hook to point to Hackblogs server
   - you can do this in Admin panel 
3. Push blog posts to your repository
   - you can write them in rST, Markdown, HTML or TXT format
4. Go to your\_username.hackblo.gs to see you blog.
   - Hackblogs is intended to be used as a service, which means you blog
   will be hosted on our server

Project is still in  early development stage.  
Some info on www.hackblo.gs  

## Architectural overview

System has 2 main components:

1. Request listener
2. Request processor

They communicate over Celery queue; first component puts requests for
processing in queue, second component pulls and processes them.

#### 1. Request listener

Basically, this compoment listens and parses requests from DVCS.

1. Listen for POST requests from DVCS notifying us of new commits to 
    repository that has blog posts
2. Parse JSON payload and assemble Request object
3. Put Request object to queue for processing by other component

#### 2. Request processor

This component pulls Request objects from queue and processes them.

1. Pull Request object from queue
2. Extract modified, added and deleted filenames from Request
3. Pull modified and added files from DVCS
4. Do any conversions (rST to HTML, Markdown to HTML...) on modified and added
files if necessary
5. Publih modified and added files (copy to folder from where nginx will serve
them)
6. Remove deleted files
