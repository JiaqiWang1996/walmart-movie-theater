#!/usr/bin/python3

import unittest

from movie import MovieTheater

class TestMovie(unittest.TestCase):

    def test_no_reservations(self):
        myMovie = MovieTheater([])
        output = myMovie.output()
        self.assertEqual(output, "", "There Should be no output when there are no reservations")
    
    def test_one_reservation_one_seat(self):
        myMovie = MovieTheater(["R001 1"])
        output = myMovie.output()
        lines = output.split("\n")
        self.assertEqual(len(lines), 1, "There Should only be one output line")
        number_seats_alloc = len(lines[0].split(","))
        self.assertEqual(number_seats_alloc, 1, "There should only be one allocated seat")

    def test_one_reservation_x_seat(self):
        for i in range(1, 11):
            myMovie = MovieTheater(["R001 %d" % i])
            output = myMovie.output()
            lines = output.split("\n")
            self.assertEqual(len(lines), 1, "There Should only be one output line")
            number_seats_alloc = len(lines[0].split(","))
            self.assertEqual(number_seats_alloc, i, "There should only be %d allocated seat/s" % i)

    def test_x_reservation_1_seat(self):
        for i in range(1, 50):
            myMovie = MovieTheater(["R00%d 1" % i])
            output = myMovie.output()
            lines = output.split("\n")
            self.assertEqual(len(lines), i, "There Should only be %d output line/s" % i)
    

if __name__ == '__main__':
    unittest.main()