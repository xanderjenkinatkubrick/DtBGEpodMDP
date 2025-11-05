'''
test_converter.py

tests functionality of the "currency_converter" package

'''

import pytest

from converter import converter

def test_converter_same_curr() -> None:
    # Arrange
    input_value_1 = 'USD'
    input_value_2 = 'USD'
    input_value_3 = 100

    expected_output = input_value_3
    
    # Act
    actual_output = converter(input_value_1, input_value_2, input_value_3)

    # Assert
    assert actual_output == expected_output

def test_converter_neg_curr() -> None:
    # Arrange
    input_value_1 = 'USD'
    input_value_2 = 'GBP'
    input_value_3 = -100

    expected_output = ValueError
    
    # Act and Assert
    with pytest.raises(expected_output):
        converter(input_value_1, input_value_2, input_value_3)



