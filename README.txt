____________________________________________________________________________________________________
Communication Contract for Microservice
____________________________________________________________________________________________________

A. In order to programmatically REQUEST data from the microservice, we utilize
   the "subprocess" module in Python. First, make sure you "import subprocess"
   at the top of your main program. Second, in order to request a random number
   within a specfic range from the microservice, make a call similar to this in
   your main program:

   subprocess.run(["python", "Z:/CS361/assignment_8/microservice.py", str(1), str(10)])
                                                ^                       ^        ^
                                     file path of microservice         min      max

   That's it! Make sure you keep the min and max numbers you want in str(), since
   that is what the function expects.
____________________________________________________________________________________________________

B. In order to programmatically RECEIVE data from the microservice, simply open
   and read the file that the microservice wrote the random number to. Here's
   what that might look like in your main program:

   file = open('Z:/CS361/assignment_8/random_num.txt', 'r+')
   random_number = file.read()
   file.close

   The file in which the micro service writes the random number to can be
   changed on line 23 of the micro service program in the open() function.
   That's it!
____________________________________________________________________________________________________

C. UML Sequence Diagram:
   https://docs.google.com/drawings/d/1L0JPAlr0mhH-rd4Gx60bW13Z2l6NDVf71_-o22mWLN8/edit?usp=sharing
____________________________________________________________________________________________________
