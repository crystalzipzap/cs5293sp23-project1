import pytest
from redactor import redact_name, redact_email_address, redact_gender, redact_date, redact_phone_number, redact_address

@pytest.fixture(scope='module')
def text():
    signature = "Crystal Schmidt(she/her/hers)\nComputer Science\nUniversity of Oklahoma\ncschmidt@ou.edu| (123) 456-7890 \n "
    out_of_office_message = "I will be out of the office on May 5th 2023. Please visit 110 W. Boyd St. Rm. 150 if you need anything. "
    text = signature + out_of_office_message 
    return text

def test_redact_name(text):
    redacted_text, stats, count = redact_name(text)
    print(redacted_text)
    assert "█" in redacted_text
    assert count == 1

def test_redact_email_address(text):
    redacted_text, stats, count = redact_email_address(text)
    print(redacted_text)
    assert "█" in redacted_text
    assert count == 1

def test_redact_gender(text):
    redacted_text, stats, count = redact_gender(text)
    print(redacted_text)
    assert "█" in redacted_text
    assert count == 3

def test_redact_date(text):
    redacted_text, stats, count = redact_date(text)
    print(redacted_text)
    assert "█" in redacted_text
    assert count == 1

def test_redact_phone_number(text):
    #text = '(123) 456-7890' 
    redacted_text, stats, count = redact_phone_number(text)
    print(redacted_text)
    assert "█" in redacted_text
    assert count == 1

def test_redact_address(text):
    redacted_text, stats, count = redact_address(text)
    print(redacted_text)
    assert "█" in redacted_text
    assert count == 1