

class MovieTheater:

    def __init__(self):
        self.seats = [['s'] * 20 for _ in range(10)]

    def __str__(self):
        s = "\t[[     SCREEN     ]]\n\t--------------------\n"

        for i, row in enumerate(self.seats):
            s += chr(65+i) + "\t" + "".join(row) + "\n"
        return s