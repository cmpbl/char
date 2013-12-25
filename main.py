#!/usr/bin/env python

from os import system
import locale
import curses

locale.setlocale(locale.LC_ALL, '')

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def ascii_char():
     if 0:
          screen.addstr( origin_portrait[1]+0, origin_portrait[0], u'              \u2588\u2588\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+1, origin_portrait[0], u'             \u2588\u2591\u2591\u2591\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+2, origin_portrait[0], u'           \u2588\u2591\u2591\u2591\u2592\u2588\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+3, origin_portrait[0], u'         \u2588\u2588\u2591\u2591\u2591\u2592\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+4, origin_portrait[0], u'       \u2588\u2588\u2591\u2591\u2591\u2591\u2592\u2592\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+5, origin_portrait[0], u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+6, origin_portrait[0], u'\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2592\u2592\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+7, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2591\u2591\u2591\u2591\u2592\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+8, origin_portrait[0], u'  \u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2591\u2591\u2591\u2591\u2592\u2588    '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+9, origin_portrait[0], u'    \u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+10, origin_portrait[0], u'   \u2588 \u2584  \u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+11, origin_portrait[0], u'   \u2588 \u2588  \u2584   \u2588\u2588\u2592\u2592\u2592\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+12, origin_portrait[0], u'   \u2592\u2592   \u2588    \u2592\u2588\u2588\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+13, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592   \u2592 \u2592\u2592\u2588\u2593\u2588\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+14, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+15, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+16, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+17, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2593\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+18, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2593\u2593\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+19, origin_portrait[0], u' \u2588 \u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2593\u2593\u2593\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+20, origin_portrait[0], u' \u2588 \u2588\u2593\u2593\u2588\u2588\u2588\u2588\u2593\u2593\u2593\u2588\u2588\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+21, origin_portrait[0], u'  \u2588\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2588\u2593\u2588  \u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+22, origin_portrait[0], u'   \u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588   \u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+23, origin_portrait[0], u' \u2588\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588\u2588\u2588    '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+24, origin_portrait[0], u'\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+25, origin_portrait[0], u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+26, origin_portrait[0], u'       \u2588\u2588\u2588\u2593\u2593\u2593\u2593\u2588    '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+27, origin_portrait[0], u'          \u2588\u2588\u2588\u2588     '.encode('utf-8'))
     else:
          screen.addstr( origin_portrait[1]+0, origin_portrait[0], u'         \u2588\u2588\u2588\u2588    '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+1, origin_portrait[0], u'    \u2588\u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2588\u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+2, origin_portrait[0], u'    \u2588\u2592\u2592\u2592\u2592\u2588\u2592\u2592\u2592\u2592\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+3, origin_portrait[0], u'  \u2588\u2592\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2592\u2592\u2592\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+4, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+5, origin_portrait[0], u' \u2588\u2588\u2592\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+6, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+7, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2592\u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+8, origin_portrait[0], u' \u2588\u2588\u2592\u2588      \u2588\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+9, origin_portrait[0], u'  \u2588\u2592\u2588       \u2588\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+10, origin_portrait[0], u'   \u2588 \u2584       \u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+11, origin_portrait[0], u'   \u2588 \u2588  \u2584    \u2588\u2592\u2592\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+12, origin_portrait[0], u'   \u2592\u2592   \u2588   \u2588\u2588\u2592\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+13, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592   \u2592 \u2592\u2592\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+14, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+15, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+16, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2591\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+17, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2591\u2591\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+18, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2591\u2591\u2591\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+19, origin_portrait[0], u' \u2588 \u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2588\u2591\u2588\u2591\u2591\u2591\u2588'.encode('utf-8'))
          screen.addstr( origin_portrait[1]+20, origin_portrait[0], u' \u2588 \u2588\u2591\u2591\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2588\u2588\u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+21, origin_portrait[0], u'  \u2588\u2588\u2588\u2588\u2591\u2591\u2588\u2588\u2588\u2591\u2588  \u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+22, origin_portrait[0], u'   \u2588\u2591\u2591\u2588\u2588\u2588\u2591\u2591\u2588   \u2588 '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+23, origin_portrait[0], u' \u2588\u2588\u2591\u2591\u2591\u2591\u2588\u2591\u2591\u2591\u2591\u2588\u2588\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+24, origin_portrait[0], u'\u2588  \u2588\u2591\u2591\u2591\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+25, origin_portrait[0], u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2588\u2588\u2588\u2588\u2591\u2588  '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+26, origin_portrait[0], u'       \u2588\u2588\u2588   \u2588   '.encode('utf-8'))
          screen.addstr( origin_portrait[1]+27, origin_portrait[0], u'          \u2588\u2588\u2588\u2588'.encode('utf-8'))

def load_char():
     print PENDING

def save_char():
     print PENDING

def update_attr():
     print PENDING

def display_attr():
     i=0
     for k, v in attributes.iteritems():
          screen.addstr(origin_attr[1]+i, origin_attr[0], k, curses.A_BOLD)
          screen.addstr(origin_attr[1]+i, origin_attr[0] + 3, " - ")
          screen.addstr(origin_attr[1]+i, origin_attr[0] + 6, v)
          i=i+2
     screen.addstr(origin_attr[1]+15, origin_attr[0], "4 - Exit")

#GLOBAL VARIABLES
x = 0
attributes = {'INT': '10', 'VIT': '53', 'STR': '23', 'WIS': '53', 'POW': '33', 'DEX': '22'}
origin_attr = [35,5]
origin_portrait = [5,5]

#INITIALIZATION
#load_char()
#save_char()

#MAIN LOOP
while x != ord('4'):
     screen = curses.initscr()

     screen.clear()
     screen.border(0)
     box_portrait = curses.newwin(35, 50, origin_portrait[1]-3, origin_portrait[0]-3)
     box_portrait.box()
     box_attr = curses.newwin(20, 12, origin_attr[1]-2, origin_attr[0]-2)
     box_attr.box()
  

     screen.refresh()
     box_portrait.refresh()
     box_attr.refresh() 
     display_attr()
     ascii_char()

     x = screen.getch()

     if x == ord('1'):
          username = get_param("Enter the username")
          homedir = get_param("Enter the home directory, eg /home/nate")
          groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
          shell = get_param("Enter the shell, eg /bin/bash:")
          curses.endwin()
     if x == ord('2'):
          curses.endwin()
          execute_cmd("ls -al")
     if x == ord('3'):
          curses.endwin()
          execute_cmd("df -h")

#save_char()
curses.endwin()