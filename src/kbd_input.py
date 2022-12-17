from readchar import readkey, key
from ansi_escapes import ansiEscapes
from src.char_buffer import CharBuffer

import sys

class KbdInput:
  def __init__(self, buf: CharBuffer):
    self.buf = buf
  
  def start_read_loop(self):
    while (True):
      self.handle_input(readkey())
  
  def handle_input(self, seq):
    if (seq == '\n'):
      pass
    elif (seq == key.BACKSPACE): # Backspace
      self.write(ansiEscapes.cursorBackward(1))
      self.write(ansiEscapes.eraseEndLine)
      # self.buf.pop() # TODO
    elif (seq == key.LEFT):
      self.write(ansiEscapes.cursorBackward(1))
    elif (seq == key.RIGHT):
      self.write(ansiEscapes.cursorForward(1))
    elif (seq[0] == key.ESC):
      pass
    else:
      # self.buf.append(seq)
      self.write(seq)
  
  def write(self, seq):
      print(seq, end='', flush=True)


