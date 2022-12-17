import sys
from readchar import readkey, key
from ansi_escapes import ansiEscapes
from src.history import History
from src.char_buffer import CharBuffer
from src.auto_completion import AutoCompletion

class KbdInput:
  def __init__(self, buf: CharBuffer, history: History):
    self.buf = buf
    self.history = history
    self.auto_completion = AutoCompletion(buf, history)
  
  def start_read_loop(self):
    while (True):
      self.handle_input(readkey())
  
  def handle_input(self, seq):
    if (seq == '\n'):
      cmd = self.buf.to_string()
      print('input:' + cmd)
      self.history.add(cmd)
      self.buf.clear()
    elif (seq == key.BACKSPACE): # Backspace
      try:
        self.buf.delete()
        self.write(ansiEscapes.cursorBackward(1))
        self.write(ansiEscapes.eraseEndLine)
      except:
        pass # TODO
    elif (seq == key.LEFT):
      try:
        self.buf.move_backward()
        self.write(ansiEscapes.cursorBackward(1))
      except:
        pass # TODO
    elif (seq == key.RIGHT):
      try:
        self.buf.move_forward()
        self.write(ansiEscapes.cursorForward(1))
      except:
        pass
    elif (seq[0] == key.ESC):
      pass # TODO
    else:
      try:
        self.buf.insert(seq)
        candiates = self.auto_completion.get_candiates()
        if len(candiates) > 0:
          print('candidates: ' + '\n'.join(candiates))
        self.write(seq)
      except:
        pass # TODO
  
  def write(self, seq):
      print(seq, end='', flush=True)


