
from movie import MovieTheater

def test_no_reservations():
    m = MovieTheater([])
    m.greedy_assignment()
    assert m.output() == ''

def test_one_reservation():
    m = MovieTheater(["R001 1"])
    m.greedy_assignment()
    assert "\n" not in m.output()

def test_one_reservation_twenty_seat():
    m = MovieTheater(["R001 20"])
    m.greedy_assignment()
    assert m.output().count(',') == 19

def test_one_reservation_x_seat():
    for k in range(1, 21):
        m = MovieTheater(["R001 %d" % k])
        m.greedy_assignment()
        assert m.output().count(',') == k - 1

def test_x_reservation_1_seat():
    for k in range(1, 11):
        m = MovieTheater(["R%03d 1" % x for x in range(1,k+1)])
        m.greedy_assignment()
        assert m.output().count('\n') == k - 1

def test_full_seats():
    m = MovieTheater(["R%03d 20" % x for x in range(1,6)])
    m.greedy_assignment()
    print(m)
    print(m.output())

def test_buf_count():
    m = MovieTheater([])
    assert m.count_buffer(0,0,2) ==  5
    assert m.count_buffer(3,3,2) ==  10

