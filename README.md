# Lab1_IPP

   For this laboratory, I have chosen to work with Django framework.
I admit that the task raised a lot of questions for me. There were many things I wasn't familiar with. 
Beginning with "What is an oAuth service and how it works?" until "How the final product should look like?"
Some of the global questions that appeared in my head are:

1. How should the application's model look like?
2. Which are the conditions for a user to be able to use this service?
3. How is guaranteed the confidentiality of the user's data?
4. Can the same user login from more than one application at the same time and what should happen then?
5. How can be an instance defined?
6. How much time is a token viable?
7. What is a GET and POST request and how can I implement them in my app?
8. How are the register/login requests processed using the browser?
9. How the data will be transmited through the application?
10. How to validate  user's data?


###How I made the system work?

1. Separating the system's attributes by implementing each request in a different view.
2. Thinking about and creating the right model of the database in order 
to make the data storage possible and accesible for every operation performed.
3. Allowing views to process incoming data by getting it and parsing as json's.
4. Applying filters for every request in order to validate data.
5. Building the logic of the entire API according to the given format for inputs and outputs and also - specified codes


###Which would be some future improvements?

1. Build another function(view) for password recovery.
2. Improve security by storing hashes of the passwords.
3. Another point, discussed also during the lessons- define the lifetime of the tokens.
4. Make possible the manipulation of data from command line(thing that I've tried to do, but I'm missing something).
