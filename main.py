#!/usr/bin/env python

from os import system
import locale
import curses
import sqlite3
import sys
import random
import datetime

#TODO
#calc_attributes
#add_quest
#Create attribute history calc incl. config item: last update
#Quest ADD and DISPLAY
#Can I get rid of attributes_o?
#Functionality for negative events (e.g., over-weight)
#Fix scaling on level chart if using
#Add check on Log_Quest() that quest is 'open'
#Add type - fixed for non-decay e.g., weight

#REMEMBER
#datetime.datetime.now().date().isoformat()

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
     file = open('.config', 'w')
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
     for k in attributes_o:
          box_attr.addstr(2+i, 2, k, curses.A_BOLD)
          box_attr.addstr(2+i, 2 + 3, " - ")
          box_attr.addstr(2+i, 2 + 6, str(attributes[k][1]))
          for j in range(0,20):
               if int(attributes[k][1]/5)>j:
                    screen.addstr(origin_attr[1]+i, origin_attr[0] + 9 + j, u'\u25AA'.encode('utf-8'))
                    pass
          i+=2

def display_menu():
     i=0
     for menu_item in menu:
          box_menu.addstr(2+i*2, 4, menu[i], curses.A_BOLD)
          i+=1
     if current_menu<=5:
          box_menu.addstr(2+current_menu*2, 2, u'\u2588'.encode('utf-8'))

def display_chart():
     i=0
     temp = 0
     box_chart.addstr(2, 2, attributes_l[attributes_o[current_chart]], curses.A_BOLD)
     for tick in attributes[attributes_o[current_chart]]:
          if 0: #LEVEL CHART -- MUST FIX SCALING
               if temp!=tick:
                    box_chart.addstr(dimensions_chart[1]-5-tick, 5+i, u'\u251C'.encode('utf-8'))
               # if tick < temp:
               #      box_chart.addstr(dimensions_chart[1]-5-tick, 2+i, u'\u2514'.encode('utf-8'))
               # elif tick > temp:
               #      box_chart.addstr(dimensions_chart[1]-5-tick, 2+i, u'\u250C'.encode('utf-8'))
               else:
                    box_chart.addstr(dimensions_chart[1]-5-tick, 5+i, u'\u2500'.encode('utf-8'))
          else: #BAR CHART
               scaling_factor = float(dimensions_chart[1]-8)/99
               for j in range(1,dimensions_chart[1]-8):
                    if float(tick) * scaling_factor > j:
                         box_chart.addstr(dimensions_chart[1]-4-j, 5+i, u'\u2592'.encode('utf-8'))

          temp = tick
          i+=1
     
     #AXES
     box_chart.addstr(4, 2, "99")
     for i in range(5,dimensions_chart[1]-4):
          box_chart.addstr(i, 3, u'\u2502'.encode('utf-8'))

     box_chart.addstr(dimensions_chart[1]-4, 3, "0")
     box_chart.addstr(dimensions_chart[1]-3, 3, u'\u2514'.encode('utf-8'))
     for i in range(1,75):
          box_chart.addstr(dimensions_chart[1]-3, 3+i, u'\u2500'.encode('utf-8'))

def display_quest_status():
     screen.addstr(origin_quests[1], origin_quests[0], "ACTIVE QUESTS", curses.A_BOLD)

def load_db():
     con = None

     try:
          con = sqlite3.connect('char.db')
         
          cur = con.cursor()

          cur.execute("DROP TABLE IF EXISTS quests")
          cur.execute("DROP TABLE IF EXISTS completes")
          cur.execute("CREATE TABLE quests(name TEXT, date_created TEXT, style TEXT, status TEXT, description BLOB, cha_val INT, dex_val INT, int_val INT, str_val INT, vit_val INT, wis_val INT, wll_val INT)")
          cur.execute("CREATE TABLE completes(quest_id INT, date_completed TEXT)")

          if ADD_TEST_DATA:
               for i in range(0,499):
                    query = """INSERT INTO quests
                         (name, date_created, style, status, description, cha_val, dex_val, int_val, str_val, vit_val, wis_val, wll_val)
                         VALUES
                         (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)
                         """
                    str_date = str(random.randint(8,12))+"/"+str(random.randint(1,30))+"/2013"
                    if random.randint(0,6)<3:
                         status_str = 'open'
                    elif random.randint(0,2) == 1:
                         status_str = 'persistent'
                    else:
                         status_str = 'closed'
                    if random.randint(1,4)<3:
                         style_str = 'decay'
                    else:
                         style_str = 'fixed'
                    data =  ['test'+str(i), datetime.datetime.strptime(str_date, '%m/%d/%Y').date().isoformat(),style_str,status_str,'test',random.randint(0,20),random.randint(0,20),random.randint(0,20),random.randint(0,20),random.randint(0,20),random.randint(0,20),random.randint(0,20)]
                    cur.execute(query, data)       

          con.commit() 

          if ADD_TEST_DATA:
               for i in range(1,100):
                    log_quest(random.randint(1,499)) 
               con.commit                  
         
     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database--")
     finally:
          if con:
               con.close()

def add_quest():
     print PENDING

def log_quest(rowid):
     con = None

     try:
          con = sqlite3.connect('char.db')
          cur = con.cursor()
          query = """UPDATE quests SET status = 'closed' WHERE rowid = ? AND status = 'open'"""
          data = [rowid]
          cur.execute(query,data)
          con.commit()

          query = """INSERT INTO completes
               (quest_id, date_completed)
               VALUES
               (?, ?)
               """
          str_date = str(random.randint(8,12))+"/"+str(random.randint(1,30))+"/2013"
          data =  [rowid, datetime.datetime.strptime(str_date, '%m/%d/%Y').date().isoformat()]
          cur.execute(query, data)
          con.commit()
     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database--")
     finally:
          if con:
               con.close()
     #Add entry to table completed

     #CLOSE if status = 'open'

def calc_attributes():
     con = None
     hist = []

     #FOR EACH DATE IN LAST 100
          #FOR EACH DECAY COMPLETE -- AGGREGATE IMPACT UNTIL < 1 (LINEAR DECAY 1 MONTH)
          #FOR EACH FIXED COMPLETE -- ORDER BY QUEST_ID, DATE_COMPLETED DESC AND THEN LOOK ONLY FOR FIRST ENTRY FOR EA. QUEST_ID
     try:
          con = sqlite3.connect('char.db')
          cur = con.cursor()

          for i in range(0, 100)
               hist[i] = 0
               cur.execute("SELECT * FROM completes WHERE style = 'decay'")
               con.commit()
               c_rows = cur.fetchall()
               for c_row in c_rows:
                    query = """SELECT * FROM quests WHERE rowid = ?"""
                    data = [c_rows[0]]
                    cur.execute(query,data)
                    q_row = cur.fetchone()
                    


     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database--")
     finally:
          if con:
               con.close()

#GLOBAL VARIABLES
config = {}
attributes = {'INT': [11,10,13], 'VIT': [12,10], 'STR': [13,11], 'WIS': [25,23], 'WLL': [15,21], 'DEX': [30,40], 'CHA': [15,17]}
attributes_o = ['INT', 'VIT', 'STR', 'WIS', 'WLL', 'DEX', 'CHA'] #ORDERED
attributes_l = {'INT': 'INTELLIGENCE', 'VIT':'VITALITY', 'STR':'STRENGTH', 'WIS':'WISDOM', 'WLL':'WILLPOWER', 'DEX':'DEXTERITY', 'CHA':'CHARISMA'} #LONG NAME
menu = ["QUESTS", "SKILLS", "ATTRIBUTES", "SETTINGS", "SAVE & EXIT", "EXIT"]
origin_attr = [5, 35]
origin_portrait = [10, 3]
origin_menu = [5, 52]
origin_chart = [38, 35]
origin_quests = [38, 5]
origin_error = [3, 3]
dimensions_chart = [80, 32]

ADD_TEST_DATA = 1

x=0
run = 1
current_menu = 0
current_chart = 0

#INITIALIZATION
screen = curses.initscr()
screen.clear()
screen.keypad(1)

load_config()
load_db()
#load_char()
#save_char()

#MAIN LOOP
while run == 1:
     screen.clear()
     screen.border(0)
     box_attr = curses.newwin(17, 32, origin_attr[1]-2, origin_attr[0]-2)
     box_attr.box()
     box_menu = curses.newwin(15, 32, origin_menu[1]-2, origin_menu[0]-2)
     box_menu.box()
     box_chart = curses.newwin(dimensions_chart[1], dimensions_chart[0], origin_chart[1]-2, origin_chart[0]-2)
     box_chart.box()
  
     screen.refresh()

     display_attr()
     box_attr.refresh()

     display_menu()
     box_menu.refresh()

     display_chart()
     box_chart.refresh()

     #ascii_char()
     display_quest_status()

     cmd = screen.getch()

     if cmd == curses.KEY_DOWN and current_menu < len(menu)-1: current_menu+=1
     elif cmd == curses.KEY_UP and current_menu > 0: current_menu-=1
     elif cmd == curses.KEY_LEFT:
          if current_chart == 0: current_chart = len(attributes_o)-1
          else: current_chart-=1
     elif cmd == curses.KEY_RIGHT:
          if current_chart == len(attributes_o)-1: current_chart = 0
          else: current_chart+=1
     elif cmd == ord('\n'):
          if menu[current_menu] == "LOG QUEST": pass
          elif menu[current_menu] == "EXIT": run = 0
     if cmd == ord('x'): run = 0
     #username = get_param("Enter the username")

#save_char()
save_config()
screen.keypad(0)
curses.endwin()