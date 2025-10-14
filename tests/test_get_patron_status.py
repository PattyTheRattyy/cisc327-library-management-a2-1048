
import pytest
from library_service import (
    get_patron_status_report
)

# positive
def test_patron_status_no_borrowing():
    """Test patron status that has never borrowed"""
    status = get_patron_status_report("654321")
    
    assert status['borrowed_books'] == []
    assert status['late_fees'] == 0.0
    assert status['borrowed_books_count'] == 0
    assert status['borrow_history'] == []

# positive
def test_patron_status_no_fees():
    """Test patron status with no fees"""
    status = get_patron_status_report("123456")
    
    assert status['borrowed_books'] == [1234, 5678]
    assert status['late_fees'] == 0.0
    assert status['borrowed_books_count'] == 2
    assert status['borrow_history'] == [6543, 1234, 5678]

# negative
def test_patron_that_does_not_exist():
    """Test with a patron that does not exist"""
    status = get_patron_status_report("209049")
    
    assert status['borrowed_books'] == []
    assert status['late_fees'] == 0.0
    assert status['borrowed_books_count'] == 0
    assert status['borrow_history'] == []

# negative
def test_patron_invalid_ID():
    """Test with an invalid patron ID"""
    status = get_patron_status_report("abcdef")
    
    assert status['borrowed_books'] == []
    assert status['late_fees'] == 0.0
    assert status['borrowed_books_count'] == 0
    assert status['borrow_history'] == []

# positive
def test_patron_with_fees():
    """Test patron with late fees"""
    status = get_patron_status_report("2090493431431")
    
    assert status['borrowed_books'] == [4335]
    assert status['late_fees'] == 3.5
    assert status['borrowed_books_count'] == 1
    assert status['borrow_history'] == [4335]




