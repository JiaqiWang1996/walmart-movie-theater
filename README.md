# walmart-movie-theater

How to run project:
>./main.py -i \<inputfile> 

Run in Testing Mode
>./main.py -t

How to run tests:
>pytest

## Assumptions
* If the movie Theater is unable to accommidate for the entire reservation request it will output "cannot fulfill reservation"
* The reservation requests that are first have priority
* All seats have the same value and customers only care about having a seat
* The number of reservations will be less than 1000
* Each reservation will have 0 < seats <= 20
* Once a reservation is made you can't change the seats