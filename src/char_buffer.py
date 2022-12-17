class CharBuffer:

  def __init__(self, size):
    if size <= 0:
     raise Exception ("size should be positive") 
    self.buf = [""] * size
    self.size = size
    self.cursor = 0
    self.count = 0
  
  def is_empty(self):
    return self.count <= 0

  def is_full(self):
    return self.count >= self.size
  
  def at_head(self):
    return self.cursor <= 0

  def at_tail(self):
    return self.cursor >= self.count

  def insert(self, char):
    if self.is_full():
      raise Exception ("buffer is full")
    if not len(char) == 1:
      raise Exception ("{char} is not a char")
    if self.cursor < self.count:
      for ind in range(self.count, self.cursor, -1):
        self.buf[ind + 1] = self.buf[ind]
    elif self.cursor == self.count:
      pass
    else:
      raise Exception ("unknown error")  
    self.buf[self.cursor] = char
    self.cursor += 1
    self.count += 1

  # delete the char in front of cursor 
  def delete(self):
    if self.is_empty():
      raise Exception ("buffer is empty") 
    if self.at_head():
      raise Exception ("at head")
    if self.cursor < self.count:
      for ind in range(self.cursor, self.count, 1):
        self.buf[ind - 1] = self.buf[ind]
    elif self.cursor == self.count:
      pass
    else:
      raise Exception ("index {} is out of range {}".format(self.cursor, self.count))
    self.cursor -= 1
    self.count -= 1

  # delete the char after cursor 
  def delete_after_cursor(self):
    if self.is_empty():
      raise Exception ("buffer is empty") 
    if self.at_tail():
      raise Exception ("at tail")
    if self.cursor < self.count:
      for ind in range(self.cursor, self.count, 1):
        self.buf[ind] = self.buf[ind + 1]
      self.count -= 1
    else:
      raise Exception ("unknown error")  
  
  def move_backward(self):
    if self.at_head():
      raise Exception ("at head")
    self.cursor -= 1

  def move_forward(self):
    if self.at_tail():
      raise Exception ("at tail")
    self.cursor += 1
  
  def clear(self):
    self.cursor = 0
    self.count = 0

  def to_string(self):
    return ''.join(self.buf[0:self.count])