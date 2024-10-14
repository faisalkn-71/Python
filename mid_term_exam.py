class Star_Cinema:
    # Class attribute to store list of hall objects
    hall_list = []

    # Method to add a Hall object to the hall_list
    @classmethod
    def entry_hall(cls, hall_obj):
        cls.hall_list.append(hall_obj)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        # Initialize instance attributes and insert into Star_Cinema's hall_list
        self.__seats = {}  # Private: stores seats for each show (show_id as key)
        self.__show_list = []  # Private: stores list of shows as tuples
        self.__rows = rows  # Private: number of rows in the hall
        self.__cols = cols  # Private: number of columns in the hall
        self.__hall_no = hall_no  # Private: hall number
        Star_Cinema.entry_hall(self)

    # Method to add a show with id, movie_name, and time
    def entry_show(self, show_id, movie_name, show_time):
        # Create a tuple with show information and add to show_list
        show_info = (show_id, movie_name, show_time)
        self.__show_list.append(show_info)
        
        # Create 2D list of seats (initially free) and add to seats dictionary
        seat_arrangement = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seat_arrangement

    # Method to book seats for a specific show
    def book_seats(self, show_id, seat_list):
        # Check if show exists
        if show_id not in self.__seats:
            raise ValueError("Invalid show ID.")
        
        # Try to book seats
        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                raise ValueError(f"Invalid seat location: ({row}, {col}).")
            if self.__seats[show_id][row][col] == 'Booked':
                raise ValueError(f"Seat ({row}, {col}) is already booked.")
            self.__seats[show_id][row][col] = 'Booked'

    # Method to view the list of shows
    def view_show_list(self):
        if not self.__show_list:
            print("No shows available.")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    # Method to view available seats for a specific show
    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            raise ValueError("Invalid show ID.")
        
        print(f"Available seats for show ID {show_id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == 'Free':
                    print(f"Seat ({row}, {col}) is Free.")

# Example usage
try:
    # Create Hall object
    hall1 = Hall(5, 5, 'Hall 1')

    # Add a show
    hall1.entry_show('S1', 'Movie 1', '10:00 AM')
    
    # View shows
    hall1.view_show_list()
    
    # Book some seats
    hall1.book_seats('S1', [(0, 0), (1, 1), (2, 2)])
    
    # View available seats
    hall1.view_available_seats('S1')

except ValueError as e:
    print(e)
