class History:

  def __init__(self, size):
    """Store buffer in given storage."""
    self.buffer = [None]*size
    self.low = 0
    self.high = 0
    self.size = size
    self.count = 0

  def is_empty(self):
    """Determines if buffer is empty."""
    return self.count == 0

  def is_full(self):
    """Determines if buffer is full."""
    return self.count == self.size

  def __len__(self):
    """Returns number of elements in buffer."""
    return self.count

  def add(self, value):
    """Adds value to buffer, overwrite as needed."""
    if self.is_full():
      self.low = (self.low + 1) % self.size
    else:
      self.count += 1
    self.buffer[self.high] = value
    self.high = (self.high + 1) % self.size

  def remove(self):
    """Removes oldest value from non-empty buffer."""
    if self.count == 0:
        raise Exception ("no histories")
    value = self.buffer[self.low]
    self.low = (self.low + 1) % self.size
    self.count -= 1
    return value
  
  def get_last(self):
    if self.count == 0:
        raise Exception ("no histories")
    return self.buffer[self.high]


  def __iter__(self):
    """Return elements in the circular buffer in order using iterator."""
    idx = self.low
    num = self.count
    while num > 0:
      yield self.buffer[idx]
      idx = (idx + 1) % self.size
      num -= 1

  def __repr__(self):
    """String representation of circular buffer."""
    if self.is_empty():
        return 'cb:[]'

    return 'cb:[' + ','.join(map(str,self)) + ']'