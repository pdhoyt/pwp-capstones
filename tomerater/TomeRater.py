class User():
    # constructor for User class, takes name & email as args and creates empty dict for books read
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
    # returns email for User instance
        return self.email

    def change_email(self, address):
    # takes new email address and asigns it to the User instance email address
        self.email = address
        return self.email

    def __repr__(self):
    # string representation of instance of User class
        return "User: {}, Email: {}, Books Read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
    # check to see if User instance matches and existing User instance by comparing name and email
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
    # takes book and rating with default of None, and adds to the book dict for the instance.
        self.books[book] = rating

    def get_avg_rating(self):
    # creates counter variables and sets to zero then loops through books dict and for each value adds 1 to n.  Calculates average rating by dividing total n by length of the dict.
        avg_rating = 0
        count = 0
        for value in self.books.values():
            if value == None:
                continue
            elif value != None:
                avg_rating += value
                count += 1
        return avg_rating / count

class Book():
    # constructor for Book class, takes title & isbn as args and creates empty list for ratings
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
    # string representation for instance of Book class
        try:
            average = sum(self.ratings)/len(self.ratings)
            return "{} - ISBN {} - has an average rating of {} with a total of {} ratings.".format(self.title, self.isbn, average, len(self.ratings))
        except ZeroDivisionError:
            return "{} - ISBN {} - has no current ratings.".format(self.title, self.isbn)

    def get_title(self):
    # returns title of Book instance
        return self.title

    def get_isbn(self):
    # returns isbn of Book instance
        return self.isbn

    def set_isbn(self, new_isbn):
    # takes new_isbn as arg and updates the isbn of a Book instance
        self.isbn = new_isbn
        print("ISBN for {} has been updated to {}.".format(self.title, self.isbn))
        return self.isbn

    def add_rating(self, rating):
    # takes rating as an arg and checks for valid rating.  If valid, appends to rating list.  if not prints and error message.
        if rating >=0 and rating <=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
    # takes other_book arg and compares it to Book instance.  Returns True of title and isbn are the same.
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        avg_rating = 0
        count = 0
        for i in self.ratings:
            avg_rating += i
            count += 1
        return avg_rating / count

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
# creates a Fiction subclass of Book object that inherits title and isbn from Book class and takes additional author arg.
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
    # returns author of Fiction instance
        return self.author

    def __repr__(self):
    # string representation for Fiction instance.
        return "{} by {}, ISBN: {}.".format(self.title, self.author, self.isbn)

class Non_Fiction(Book):
# creates a Non_Fiction subclass of Book object that inherits title and isbn from Book class and takes additional subject and level args.
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
    # retunrs subject of Non_Fiction instance
        return self.subject

    def get_level(self):
    # returns level of Non_Fiction instance
        return self.level

    def __repr__(self):
    # string representation of Non_Fiction instance
        return "{}, a {} manual on {}, ISBN: {}.".format(self.title, self.level, self.subject, self.isbn)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        novel = Fiction(title, author, isbn)
        return novel

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            elif book not in self.books.keys():
                self.books[book] = 1
        elif email not in self.users.keys():
            return "No user with email {}!".format(email)

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[user.email] = user
        if user_books is not None:
            for i in user_books:
                self.add_book_to_user(i, email, None)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def get_most_read_book(self):
        largest_key = None
        largest_value = float("-inf")
        for key, value in self.books.items():
            if value > largest_value:
                largest_value = value
                largest_key = key
        return largest_key.get_title()

    def highest_rated_book(self):
        largest_key = 0
        for key in self.books.keys():
            if key.get_average_rating() > largest_key:
                largest_key = key.get_average_rating()
        return largest_key

    def most_positive_user(self):
        largest_value = 0
        user = None
        for value in self.users.values():
            if value.get_avg_rating() > largest_value:
                largest_values = value.get_avg_rating()
                user = value
        return user.name
