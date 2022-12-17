import sys
from src.history import History
from src.char_buffer import CharBuffer

class AutoCompletion:

  def __init__(self, buf: CharBuffer, history: History):
    self.buf = buf
    self.history = history
  
  def get_candiates(self):
    val = self.buf.to_string()
    if len(val) > 0:
      return self.history.get_candiates(val)
    return []