**What is Hackblogs?**
Hackblogs is DVCS based blog system. It's in early development stage.
Basically, it works like this:

1. Create repository on Github/Bitbucket that will host your blog posts
   - for now, repository needs to be public, in future we will also support private repos
2. Set commit POST hook to point to Hackblogs server
   - you can do this in Admin panel 
3. Push blog posts to your repository
   - you can write them in rST, Markdown, HTML or TXT format
4. Go to your_username.hackblo.gs to see you blog.
   - Hackblogs is intended to be used as a service, which means you blog will be hosted on our server

Some info on www.hackblo.gs
