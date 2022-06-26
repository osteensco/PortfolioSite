# PortfolioSite

    A project to place all of my projects.




###### Backend

    This site was built with Python and Django. I only found it necessary to use only one app for my 
    approach. The main page of the site is meant to provide a high level overview of my skillset, 
    projects, and experience. Additionally, I wanted to provide the option to take a deeper dive into 
    how I implemented different technologies and the approach I took for each project. Because Django 
    is great for building out scalable content on web apps I decided to use it for building a portfolio 
    site quickly where I could easily add content as my professional capabilities continue to grow. The 
    sections I have where scalability is necessary are technologies and projects. I established a many 
    to many relationship between these two tables in the database to allow visitors a choice in how the 
    information they were looking for was organized. The structure is built in a way where a visitor 
    can browse by project and see what technologies where used for each or browse by technology and see 
    what projects used that technology.


###### Frontend

    The frontend utilizes bootstrap and a CSS stylesheet I wrote myself. Bootstrap is a great template 
    that provides an excellent starting point, but I wanted to add my own additions as I learned more 
    about CSS. One example of my own CSS would be the Navbar at the top of every page. This can be found 
    in the base.html file.