import pytest
from library_service import (
    borrow_book_by_patron
)

# positive
def test_borrow_book_valid_input():
    """Test borrowing a book with valid input."""
    success, message = borrow_book_by_patron("654321", 1)
    
    assert success == True
    assert "successfully borrowed" in message.lower()

# negative
def test_borrow_book_too_many_borrowed():
    """Test borrowing a book with too many borrowed books. (assuming patron is currently borrowing 5 books already)"""
    success, message = borrow_book_by_patron("123456", 2)
    
    
    assert success == False
    assert "borrow limit" in message.lower()


# positive
def test_borrow_book_valid_input2():
    """Test borrowing a book with valid input. (book exists, under borrow limit, valid patron ID)"""
    success, message = borrow_book_by_patron("456123", 3)
    
    assert success == True
    assert "successfully borrowed" in message.lower()


# negative
def test_borrow_book_does_not_exist():
    """Test borrowing a book that does not exist. (Assuming no book with id 9341039840193840 exists)"""
    success, message = borrow_book_by_patron("987651", 9341039840193840) 
    
    
    assert success == False
    assert "does not exist" in message


# negative
def test_borrow_book_no_available_copies():
    """Test borrowing a book with no available copies. (assuming this book has no available copies)"""
    success, message = borrow_book_by_patron("673123", 4)
    
    
    assert success == False
    assert "no available copies" in message


