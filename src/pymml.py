#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.kbd_input import KbdInput
from src.char_buffer import CharBuffer

def main():
  buf = CharBuffer(1024 * 4)
  kbd = KbdInput(buf)
  kbd.start_read_loop()

if (__name__ == '__main__'): 
    main()