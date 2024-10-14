class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

    @classmethod
    def view_halls(self):
        for hall in self.__hall_list:
            print(f"Hall No: {hall._Hall__hall_no}, Rows: {hall._Hall__rows}, Columns: {hall._Hall__cols}")
            hall.view_show_list()

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_tuple = (show_id, movie_name, time)
        self.__show_list.append(show_tuple)
        
        seats = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seats

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Error: Invalid Show ID.")
            return

        seats = self.__seats[show_id]

        for row, col in seat_list:
            if row >= self.__rows or col >= self.__cols or row < 0 or col < 0:
                print(f"Error: Invalid seat ({row}, {col}).")
                return
            if seats[row][col] == 'Booked':
                print(f"Error: Seat ({row}, {col}) is already booked.")
                return

        for row, col in seat_list:
            seats[row][col] = 'Booked'
        print(f"Seats {seat_list} successfully booked for show {show_id}.")


    def view_show_list(self):
        if not self.__show_list:
            print("No shows available.")
        else:
            print(f"Shows running in Hall {self.__hall_no}:")
            for show in self.__show_list:
                print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")


    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Error: Invalid Show ID.")
            return
        
        seats = self.__seats[show_id]
        print(f"Available seats for show {show_id} in Hall {self.__hall_no}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(f"({row},{col}): {seats[row][col]}", end=" | ")
            print()



    
hall_1 = Hall(5, 5, 1)
hall_2 = Hall(4, 6, 2)


hall_1.entry_show("101", "Toofan", "10:00 AM")
hall_1.entry_show("102", "3 idiots", "2:00 PM")
    
hall_2.entry_show("103", "Home Alone", "12:00 PM")

 
while True:
    print("\n==== Cinema Ticket Counter System ====")
    print("1. View all shows")
    print("2. View available seats")
    print("3. Book seats")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        Star_Cinema.view_halls()

    elif choice == '2':
        hall_no = int(input("Enter hall number: "))
        show_id = input("Enter show ID: ")
        if hall_no == 1:
            hall_1.view_available_seats(show_id)
        elif hall_no == 2:
            hall_2.view_available_seats(show_id)

    elif choice == '3':
        hall_no = int(input("Enter hall number: "))
        show_id = input("Enter show ID: ")
        seats_to_book = []
        n = int(input("Enter number of seats to book: "))
        for _ in range(n):
            row = int(input("Enter seat row: "))
            col = int(input("Enter seat column: "))
            seats_to_book.append((row, col))

        if hall_no == 1:
            hall_1.book_seats(show_id, seats_to_book)
        elif hall_no == 2:
            hall_2.book_seats(show_id, seats_to_book)

    elif choice == '4':
        break

    else:
        print("Invalid choice, please try again.")


