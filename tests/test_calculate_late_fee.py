import pytest
from library_service import (
    calculate_late_fee_for_book
)

# positive
def test_calculate_fee_7_days():
    """Test calculating fee when book is 7 days late"""
    result = calculate_late_fee_for_book("654321", 1)
    
    assert result['fee_amount'] == 3.5
    assert result['days_overdue'] == 7
    assert "late fee" in result['status'].lower()

# negative
def test_calculation_when_book_is_not_borrowed():
    """Test calculating fee when book is not borrowed"""
    result = calculate_late_fee_for_book("123456", 2)
    
    assert result['fee_amount'] == 0.0
    assert result['days_overdue'] == 0
    assert "not borrowed" in result['status'].lower()


# postive
def test_calculate_fee_30_days():
    """Test calculating fee when book is 30 days late"""
    result = calculate_late_fee_for_book("431498", 3)
    
    
    assert result['fee_amount'] == 15.0
    assert result['days_overdue'] == 30
    assert "late fee" in result['status'].lower()


# postive
def test_calculate_fee_9_days():
    """Test calculating fee when book is 9 days late"""
    result = calculate_late_fee_for_book("431455", 4)
    
    
    assert result['fee_amount'] == 5.5
    assert result['days_overdue'] == 9
    assert "late fee" in result['status'].lower()


# negative
def test_calculate_fee_when_book_does_not_exist():
    """Test calculating fee when book does not exist"""
    result = calculate_late_fee_for_book("807773", 5)
    

    assert result['fee_amount'] == 0.0
    assert result['days_overdue'] == 0
    assert "does not exist" in result['status'].lower()

