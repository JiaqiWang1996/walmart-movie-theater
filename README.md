# walmart-movie-theater

How to run project:
>./main.py -i \<inputfile> -o \<outputfile>

How to run tests:
>./test.py

## Assumptions
* Parties Larger than 20 will make multiple reservations
* If the movie Theater is unable to accommidate for the entire reservation request it will output N/A for all of the assignments
* The reservation requests that are first have priority
* All of the reservations are recieved at the same time so that the algorithm can strategically fit the customers.
* All seats have the same value and customers only care about having a seat