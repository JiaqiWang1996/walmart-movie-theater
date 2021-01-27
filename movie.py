

class MovieTheater:

    assignments = []

    def __init__(self, reservations):
        self.seats = [['s'] * 20 for _ in range(10)]
        self.reservations = [r.split() for r in reservations if len(r)]

    def printr(self):
        print(self.reservations)

    # Returns the string of the seat assignments in the requested format
    def output(self):
        return ""

    def __str__(self):
        s = "\t[[     SCREEN     ]]\n\t--------------------\n"

        for i, row in enumerate(self.seats):
            s += chr(65+i) + "\t" + "".join(row) + "\n"
        return s