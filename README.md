## What is Hackblogs?

Hackblogs is DVCS based blog system for hackers. 
A little explanation of the above sentence:

1. DVCS - your blog posts will be on Github/Bitbucket. You do not communicate with/use anything but git/hg and Github/Bitbucket
2. blog system - your blog is hosted statically (meaning HTML and CSS files) on our server
3. for hackers - you will write posts in rST, Markdown and similar formats, and will use DVCS to publish them so it's expected of you to find your way around with this tools


### Basically, it works like this:

1. Create repository on Github/Bitbucket that will host your blog posts
   - for now, repository needs to be public, in future we will also support private repos
2. Set commit POST hook to point to Hackblogs server
   - you can do this in Admin panel 
3. Push blog posts to your repository
   - you can write them in rST, Markdown, HTML or TXT format
4. Go to your_username.hackblo.gs to see you blog.
   - Hackblogs is intended to be used as a service, which means you blog will be hosted on our server


Project is still in  early development stage.
Some info on www.hackblo.gs
