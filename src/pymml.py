#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.history import History
from src.kbd_input import KbdInput
from src.char_buffer import CharBuffer

def main():
  history = History(127)
  buf = CharBuffer(1024 * 4)
  kbd = KbdInput(buf, history)
  kbd.start_read_loop()

if (__name__ == '__main__'): 
    main()