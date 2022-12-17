import pytest
from src.char_buffer import CharBuffer

def test_empty_buf():
  buf = CharBuffer(100)
  assert buf.count == 0
  assert buf.cursor == 0
  assert buf.is_full() == False 
  assert buf.is_empty() == True
  assert buf.to_string() == ''

def test_insert():
  buf = CharBuffer(100)
  buf.insert('a')
  assert buf.count == 1
  assert buf.cursor == 1
  assert buf.is_full() == False 
  assert buf.is_empty() == False 
  assert buf.to_string() == 'a'

def test_insert_unicode():
  buf = CharBuffer(100)
  buf.insert('中')
  assert buf.count == 1
  assert buf.cursor == 1
  assert buf.is_full() == False 
  assert buf.is_empty() == False 
  assert buf.to_string() == '中'

def test_full_buf():
  buf = CharBuffer(1)
  buf.insert('a')
  assert buf.count == 1
  assert buf.cursor == 1
  assert buf.is_full() == True 
  assert buf.is_empty() == False 
  assert buf.to_string() == 'a'

def test_input_not_a_char():
  buf = CharBuffer(100)
  with pytest.raises(Exception):
    buf.insert('')
  with pytest.raises(Exception):
    buf.insert('ab')