# crud_app
My plan for Project 2 was to create a food nutrition app and my aim was to reach the bare minimum in requirements.
I started off by creating a plan on how I was going to do this project. 

I wanted to keep it as simple as I can and down
the track, if I had enough time, make it look half-decent. I broke it down by starting off with making the app work with a standard log in, out out system that stores in the information in a database. Once successfully logged in, be brought to the main page where foods can be read. 

As this site is accessed, it is also possible for foods to be added with the inputs for name, calories, protein, carbs, 
and an image_url to be added so anybody on the page can expand its overall content. Alternatively, if a food has any errors, it can be edited
to suit the correct amount. If there is a duplicate food or too many foods displayed at once, any and all of the listings can be deleted individually.

There is also an option to like which I did not get working so it's just for show. I wanted to implement a calorie amount search to filter for foods based 
on user input. The input and button is there, however it does not work. Aside from the content and input options, the only other main feature is the page will
randomly generate a background colour every time it is loaded and will change with every refresh as well.

At current point in time, all CRUD features work with both of my additional features. This is basic, but at the sufficient MVP target.


Bugs:

> On load of server, this error gets returned, it has not affected anything that I can see, and does not show errors on page or in inspect console: 

127.0.0.1 - - [27/Jun/2023 10:32:27] "GET / HTTP/1.1" 302 -
GET
ImmutableMultiDict([])

> Currently the sort by new does not work. However, it does not create errors and still refreshes the page.

Features to Add:

> Stylise the layout to be more aesthetic and professional
> Add more options for nutrition in foods
> Have a better display of the foods and their contents, currently there is no mention of calories, protein or carbohydrates when they display, only their numbers.

Notes:

> I have changed my database to use float numbers instead of text, the order of the foods in the database when using the sort by feature were not properly ordered.

> After changing the database for Calories, Protein and Carbohydrates, I have changed the form to make it take numbers, not text as if letters are put in, it creates errors. This applies to edit and the create functions.



