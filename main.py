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

def load_config():
     file = open('.config', 'r')
     for line in file:
          colon_index = line.find(":")
          line_key = line[:colon_index]
          line_value = line[colon_index+1:]
          config[line_key.strip()]=line_value.strip() 
     file.close()

def save_config():
     file = open(".config", "w")
     for k, v in config.iteritems():
          file.write(k + ":" + v + "\n")
     file.close()

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
          j = 0
          for j in range(0,20):
               if int(int(v)/5)>j:
                    screen.addstr(origin_attr[1]+i, origin_attr[0] + 9 + j, u'\u25AA'.encode('utf-8'))
          i+=2

def display_menu():
     i = 0
     for menu_item in menu:
          screen.addstr(origin_menu[1]+i*2, origin_menu[0]+2, menu[i], curses.A_BOLD)
          i+=1
     if current_menu<=5:
          screen.addstr(origin_menu[1]+current_menu*2, origin_menu[0], u'\u2588'.encode('utf-8'))

def display_chart():
     i=0
     chart_origin_y = origin_chart[1]+dimensions_chart[1]
     for tick in test_INT:
          screen.addstr(chart_origin_y-tick, origin_chart[1]+10+i+69-len(test_INT), u'\u2588'.encode('utf-8'))
          i+=1

#GLOBAL VARIABLES
config = {}
attributes = {'INT': '99', 'VIT': '22', 'STR': '12', 'WIS': '10', 'POW': '30', 'DEX': '29'}
menu = ["QUESTS", "SKILLS", "ATTRIBUTES", "SETTINGS", "SAVE & EXIT", "EXIT"]
test_INT = [10,11,13,12,15,17,20,21,22,20,19,17,20,25,24,22,24,24,20,21,22,19]
origin_attr = [5, 35]
origin_portrait = [10, 3]
origin_menu = [5, 50]
origin_chart = [38, 35]
dimensions_chart = [80, 32]

run = 1
current_menu = 0

#INITIALIZATION
screen = curses.initscr()
screen.keypad(1)
load_config()
#load_char()
#save_char()

#MAIN LOOP
while run == 1:
     screen.clear()
     screen.border(0)
     #box_portrait = curses.newwin(35, 50, origin_portrait[1]-3, origin_portrait[0]-3)
     #box_portrait.box()
     box_attr = curses.newwin(15, 32, origin_attr[1]-2, origin_attr[0]-2)
     box_attr.box()
     box_menu = curses.newwin(17, 32, origin_menu[1]-2, origin_menu[0]-2)
     box_menu.box()
     box_chart = curses.newwin(dimensions_chart[1], dimensions_chart[0], origin_chart[1]-2, origin_chart[0]-2)
     box_chart.box()
  
     screen.refresh()
     #box_portrait.refresh()
     box_attr.refresh()
     box_menu.refresh()
     box_chart.refresh()
     display_attr()
     display_menu()
     display_chart()
     ascii_char()

     cmd = screen.getch()

     if cmd == curses.KEY_DOWN and current_menu < len(menu)-1: current_menu+=1
     elif cmd == curses.KEY_UP and current_menu > 0: current_menu-=1
     elif cmd == ord('\n'):
          if menu[current_menu] == "LOG QUEST": pass
          elif menu[current_menu] == "EXIT": run = 0
     if cmd == ord('x'): run = 0
     #username = get_param("Enter the username")

#save_char()
save_config()
stdscr.keypad(0)
curses.endwin()