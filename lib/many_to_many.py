from datetime import datetime

class Author:

    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Name must be a string")

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books (self):
        return [contract.book for contract in Contract.all_contracts if contract.author == self]

    def sign_contract(self, book, date, royalties):
        if  isinstance(book, Book):
            new_contract = Contract(self, book, date, royalties)
            return new_contract
        else:
            raise Exception ("The book must be an instance of Book class.")
    
    def total_royalties(self):
        royalty_list = [contract.royalties for contract in Contract.all_contracts if contract.author== self]
        return sum(royalty_list)  
        
class Book:

    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("Title must be a string.")

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors (self):
        return [contract.author for contract in Contract.all_contracts if contract.book == self]

class Contract:

    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @property
    def author (self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an instance of Author class.")

    @property
    def book (self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book must be an instance of Book class.")
    
    @property
    def date (self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Date must be a string")

    @property
    def royalties (self):
        return self._royalties

    @royalties.setter
    def royalties (self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Royalties must be an integer")

    @classmethod
    def contracts_by_date(cls, date):

        target_date = datetime.strptime(date, "%d/%m/%Y")

        def get_datetime(date_str):
            return datetime.strptime(date_str, "%d/%m/%Y")
            

        filtered_contracts = [contract for contract in cls.all_contracts if get_datetime(contract.date) == target_date]
        
        sorted_contracts = sorted(filtered_contracts, key = lambda contract: get_datetime(contract.date))

        return sorted_contracts


