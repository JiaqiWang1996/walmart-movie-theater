# walmart-movie-theater

How to run project:
`./main.py -i \<inputfile> `

Run in Testing Mode
`./main.py -t`

How to run tests:
`pytest`

## How it works
The algorithm being used a greedy algorithm that trys to minimize the amount of buffer space created so that as many customers can watch the movie as possible.


## Assumptions
* If the movie Theater is unable to accommidate for the entire reservation request it will output "cannot fulfill reservation"
* The reservation requests that are first have priority
* All seats have the same value and customers only care about having a seat
* The number of reservations will be less than 1000
* Each reservation will have 0 < seats <= 20
* Once a reservation is made you can't change the seats

## Things to work on in the future
* If we can change the seats on the fly use backtracing to reorganize the seats. Similar to the N-Queens Problem.
* If there is preference for what seat a customer would like allow the user to input it. Center Seats are normally more valuable in a movie theaters.
* Allow for reservations to be broken up for more optimized sitting