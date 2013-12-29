#!/usr/bin/env python

from os import system
import locale
import curses
import sqlite3
import sys
import random
import datetime

#For Activate/Deactivate/Log make sure the SQL returns any data -- maybe no options to pick from

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

def display_attr():
     i=0
     for k in attributes_o:
          box_attr.addstr(2+i, 2, k, curses.A_BOLD)
          box_attr.addstr(2+i, 2 + 3, " - ")
          if len(attributes[k]) > 0:
               box_attr.addstr(2+i, 2 + 6, str(int(attributes[k][len(attributes[k])-1])))
               for j in range(0,20):
                    if int(attributes[k][len(attributes[k])-1]/5)>j:
                         screen.addstr(origin_attr[1]+i, origin_attr[0] + 9 + j, u'\u25AA'.encode('utf-8'))
          else:
               box_attr.addstr(2+i, 2 + 6, "0")
          i+=2

def display_menu():
     i=0
     for menu_item in menu_tree[menu_level]:
          box_menu.addstr(2+i*2, 4, menu_tree[menu_level][i], curses.A_BOLD)
          i+=1
     if current_menu<=len(menu_tree[menu_level]):
          box_menu.addstr(2+current_menu*2, 2, u'\u25BA'.encode('utf-8'))

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
                         box_chart.addstr(dimensions_chart[1]-4-j, 77-i, u'\u2592'.encode('utf-8'))

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
     screen.addstr(origin_quests[1], origin_quests[0], "ACTIVE", curses.A_BOLD)

def load_db():
     con = None

     try:
          con = sqlite3.connect('char.db')
         
          cur = con.cursor()

          cur.execute("DROP TABLE IF EXISTS quests")
          cur.execute("DROP TABLE IF EXISTS completes")
          cur.execute("CREATE TABLE quests(name TEXT, date_created TEXT, style TEXT, status TEXT, icon TEXT, description BLOB, cha_val INT, dex_val INT, int_val INT, str_val INT, vit_val INT, wis_val INT, wll_val INT)")
          cur.execute("CREATE TABLE completes(quest_id INT, date_completed TEXT, buff_bool TEXT)")

          if ADD_TEST_DATA:
               for i in range(0,499):
                    query = """INSERT INTO quests
                         (name, date_created, style, status, icon, description, cha_val, dex_val, int_val, str_val, vit_val, wis_val, wll_val)
                         VALUES
                         (?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?)
                         """
                    str_date = str(random.randint(11,12))+"-"+str(random.randint(1,30))+"-2013"
                    if random.randint(0,6)<3:
                         status_str = 'open'
                    elif random.randint(0,2) == 1:
                         status_str = 'persistent'
                    else:
                         status_str = 'closed'
                    style_str = 'decay'
                    data =  ['test'+str(i), datetime.datetime.strptime(str_date, '%m-%d-%Y').date().isoformat(),style_str,status_str,"u'\u266B'",'test',random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)]
                    cur.execute(query, data)       

          con.commit() 

          if ADD_TEST_DATA:
               for i in range(1,100):
                    log_quest('quest',random.randint(1,499)) 
               con.commit                  
               calc_attributes()
         
     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database--")
     finally:
          if con:
               con.close()

def add_quest(quest_type):
     val_array = [0,0,0,0,0,0,0]

     if quest_type == 'quest':
          style_str = 'decay'
          icon_str = "u'\u2588'"
     else:
          status_str = 'persistent'
          style_str = 'fixed'

     attempt = 1
     while attempt == 1:
          screen.clear()
          screen.border(0)
          if quest_type == 'quest':
               screen.addstr(2, 2, "What is the quest?")
          else:
               screen.addstr(2,2, "What is this buff or debuff?")
          screen.refresh()
          name_str = screen.getstr(10, 10, 60)
          if len(name_str)>0:
               attempt = 0

     if quest_type == 'quest':
          attempt = 1
          menu_step = 0
          while attempt == 1:
               screen.clear()
               screen.border(0)
               screen.addstr(2, 2, "Is this a persistent quest?")
               screen.addstr(4, 4, "Persistent")
               screen.addstr(6, 4, "One-time")
               screen.addstr(4+menu_step%2*2, 2, u'\u25BA'.encode('utf-8'))
               screen.addstr(1, 1, '')

               screen.refresh()

               cmd = screen.getch()

               if cmd == curses.KEY_DOWN or cmd == curses.KEY_UP:
                    menu_step+=1
               elif cmd == ord('\n'):
                    if menu_step%2 == 0:
                         status_str = 'persistent'
                    else:
                         status_str = 'open'
                    attempt = 0

     if quest_type == 'buff':
          attempt = 1
          menu_step = 0
          while attempt == 1:
               screen.clear()
               screen.border(0)
               screen.addstr(2, 2, "Choose an icon for this buff or debuff")
               j = 0
               for icon in icon_list:
                    buff_cmd = "screen.addstr(4+j%8*2, 4+(j/8)*10, "+icon+".encode('utf-8'))"
                    exec buff_cmd
                    j+=1
               screen.addstr(4+menu_step%8*2, 2+(menu_step/8)*10, u'\u25BA'.encode('utf-8'))

               screen.addstr(1, 1, '')

               screen.refresh()

               cmd = screen.getch()

               if cmd == curses.KEY_DOWN and menu_step < len(icon_list):
                    menu_step+=1
               elif cmd == curses.KEY_UP and menu_step > 0:
                    menu_step-=1
               elif cmd == ord('\n'):
                    icon_str = icon_list[menu_step]
                    attempt = 0

     attempt = 1
     menu_step = 0
     while attempt == 1:
          screen.clear()
          screen.border(0)
          screen.addstr(2, 2, "Configure attribute impact")

          attributes_sorted = attributes_o
          attributes_sorted.sort()

          for i in range (0,7):
               screen.addstr(4, 4+i*8, attributes_sorted[i])
               screen.addstr(6, 4+i*8, str(val_array[i]))
          screen.addstr(4, 3+menu_step*8, u'\u2588'.encode('utf-8'))
          screen.refresh()

          cmd = screen.getch()

          if cmd == curses.KEY_DOWN and val_array[menu_step] > 0 and quest_type == 'quest':
               val_array[menu_step]-=1
          elif cmd == curses.KEY_DOWN:
               val_array[menu_step]-=1
          elif cmd == curses.KEY_UP:
               val_array[menu_step]+=1
          elif cmd == curses.KEY_RIGHT and menu_step < 7:
               menu_step += 1
          elif cmd == curses.KEY_LEFT and menu_step > 0:
               menu_step -= 1
          elif cmd == ord('\n'):
               attempt = 0

     con = None

     try:
          con = sqlite3.connect('char.db')
          cur = con.cursor()

          query = """INSERT INTO quests
               (name, date_created, style, status, icon, description, cha_val, dex_val, int_val, str_val, vit_val, wis_val, wll_val)
               VALUES
               (?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?)
               """
          data =  [name_str, datetime.datetime.today().date().isoformat(),style_str,status_str,icon_str,'',val_array[0], val_array[1], val_array[2], val_array[3], val_array[4], val_array[5], val_array[6]]
          cur.execute(query, data)       
          con.commit()               
     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error adding quest to database--")
     finally:
          if con:
               con.close()

def log_quest(quest_type, rowid):

     if rowid >= 0:
          is_test_data = 1
     else: 
          is_test_data = 0

     con = None

     try:
          con = sqlite3.connect('char.db')
          cur = con.cursor()
          if not is_test_data:
               if quest_type == 'buff':
                    query = """SELECT c_sub.quest_id, q.name, q.icon
                         from quests q
                         inner join (
                              select c1.* from completes c1
                              where c1.buff_bool = 0
                              and not exists (
                                   select c2.* from completes c2
                                   where c2.quest_id = c1.quest_id
                                   and c2.buff_bool = 1
                                   and c2.date_completed >= c1.date_completed)) c_sub
                         on q.rowid = c_sub.quest_id;
                         """
               elif quest_type == 'quest':
                    query = """SELECT rowid, * FROM quests WHERE style = 'decay' ORDER BY name"""
               elif quest_type == 'buff_off':
                    query = """SELECT c_sub.quest_id, q.name, q.icon
                         from quests q
                         inner join (
                              select c1.* from completes c1
                              where c1.buff_bool = 1
                              and not exists (
                                   select c2.* from completes c2
                                   where c2.quest_id = c1.quest_id
                                   and c2.buff_bool = 0
                                   and c2.date_completed >= c1.date_completed)) c_sub
                         on q.rowid = c_sub.quest_id;
                         """
               cur.execute(query)
               con.commit()

               c_rows = cur.fetchall()

               attempt = 1
               menu_step = 0
               while attempt == 1:
                    screen.clear()
                    screen.border(0)

                    if quest_type == 'buff':
                         screen.addstr(2, 2, "Which buff should be activated?")
                    elif quest_type == 'quest':
                         screen.addstr(2, 2, "Which quest did you complete?")
                    elif quest_type == 'buff_off':
                         screen.addstr(2, 2, "Which buff should be deactivated?")


                    i = 0
                    for c_row in c_rows:
                         if quest_type == 'buff':
                              buff_cmd = "screen.addstr(4+i*2,4, "+c_row[5]+".encode('utf-8'))"
                         elif quest_type == 'buff_off':
                              buff_cmd = "screen.addstr(4+i*2,4, "+c_row[2]+".encode('utf-8'))"
                         elif quest_type == 'quest':
                              buff_cmd = "pass"
                         exec buff_cmd
                         screen.addstr(4+i*2, 6, c_row[1])
                         i+=1

                    screen.addstr(4+menu_step%8*2, 2+(menu_step/8)*10, u'\u25BA'.encode('utf-8'))
                    screen.addstr(1, 1, '')
                    screen.refresh()

                    cmd = screen.getch()

                    if cmd == curses.KEY_DOWN and menu_step < len(c_rows)-1:
                         menu_step+=1
                    elif cmd == curses.KEY_UP and menu_step > 0:
                         menu_step-=1
                    elif cmd == ord('\n'):
                         if quest_type == 'buff_off' and 1: #CHANGE TO CATCH NO OPTION INSTANCES
                              return
                         else:
                              rowid = c_rows[menu_step][0]
                              attempt = 0

          query = """UPDATE quests SET status = 'closed' WHERE rowid = ? AND status = 'open'""" #will only affect quests are others are status = 'persistent'
          data = [int(rowid)]
          cur.execute(query,data)
          con.commit()

          if quest_type == 'buff' or quest_type == 'buff_off':
               query = """INSERT INTO completes
                    (quest_id, date_completed, buff_bool)
                    VALUES
                    (?, ?, ?)
                    """
          elif quest_type == 'quest':
               query = """INSERT INTO completes
                    (quest_id, date_completed)
                    VALUES
                    (?, ?)
                    """
          if is_test_data:
               str_date = str(random.randint(8,12))+"/"+str(random.randint(1,30))+"/2013"
               act_date = datetime.datetime.strptime(str_date, '%m/%d/%Y').date().isoformat()
          else: act_date = datetime.datetime.today().date().isoformat()
          if quest_type == 'quest':
               data =  [int(rowid), act_date]
          elif quest_type == 'buff':
               data = [int(rowid), act_date, 1]
          elif quest_type == 'buff_off':
               data = [int(rowid), act_date, 0]
          cur.execute(query, data)
          con.commit()
     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database--")
     finally: 
          if con:
               con.close()
          if not ADD_TEST_DATA:
               calc_attributes()

def display_buffs():
     global buff_list
     box_buffs.addstr(2,2, "BUFFS")
     box_buffs.addstr(6,2, "DEBUFFS")

     try:
          con = sqlite3.connect('char.db')
          cur = con.cursor()

          buff_i = 0
          buff_row = 0
          debuff_i = 0
          debuff_row = 0
          for k,v in buff_list.items():
               buff_check = 0
               debuff_check = 0
               if int(v[0]) == 1:
                    query = """SELECT * FROM quests WHERE rowid = ?"""
                    data = [k]
                    cur.execute(query,data)
                    con.commit()
                    q_row = cur.fetchone()

                    for j in range (0, 7):
                         if q_row[6+j] > 0:
                              buff_check = 1
                         if q_row[6+j] < 0:
                              debuff_check = 1

                    if buff_i > 8:
                         buff_row = 1
                    if debuff_i > 8:
                         debuff_row = 1
                    
                    if buff_check:
                         buff_cmd = "box_buffs.addstr(2+buff_row*2,11+2*buff_i-buff_row*18, "+q_row[4]+".encode('utf-8'))"
                         exec buff_cmd
                         buff_i += 1
                    if debuff_check:
                         buff_cmd = "box_buffs.addstr(2+debuff_row*2,11+2*debuff_i-debuff_row*18, "+q_row[4]+".encode('utf-8'))"
                         exec buff_cmd
                         debuff_i += 1
                    if buff_i > 14 or debuff_i > 14:
                         break

     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database for listing buffs--")
     finally:
          if con:
               con.close()

def calc_attributes():
     con = None
     global buff_list
     impact_array = []
     buff_list = {}
     attr_hist = [[],[],[],[],[],[],[]]

     attributes['CHA'] = []
     attributes['DEX'] = []
     attributes['INT'] = []
     attributes['STR'] = []
     attributes['VIT'] = []
     attributes['WIS'] = []
     attributes['WLL'] = []

     try:
          con = sqlite3.connect('char.db')
          cur = con.cursor()

          #Build buff table -- append to set key = quest_id and value = [], then build that out
          cur.execute("""SELECT DISTINCT completes.quest_id
               FROM completes
               INNER JOIN quests ON completes.quest_id = quests.rowid
               WHERE quests.style = 'fixed' and completes.buff_bool = 1
               ORDER BY completes.quest_id""") #all entries for
          con.commit()
          c_rows = cur.fetchall()
          for c_row in c_rows:
               buff_list[c_row[0]] = []

          for k, v in buff_list.items():
               query = """SELECT * FROM completes WHERE quest_id = ? ORDER BY date_completed ASC"""
               data = [k]
               cur.execute(query,data)
               con.commit()
               c_rows = cur.fetchall()

               daily_status = 0
               for i in range (0, 73):
                    for c_row in c_rows:
                         days_since = (datetime.datetime.today()-datetime.datetime.strptime(c_row[1], "%Y-%m-%d" )).days
                         if days_since == i:
                              daily_status = c_row[2]
                    buff_list[k].append(daily_status)

          for i in range(0, 73):
               #QUESTS
               for j in range (0, 7):
                   attr_hist[j].append(0)            
               cur.execute("SELECT completes.* FROM completes INNER JOIN quests ON completes.quest_id = quests.rowid WHERE quests.style = 'decay'")
               con.commit()
               c_rows = cur.fetchall()
               for c_row in c_rows:
                    decay_scaler = 0
                    #IF COMPLETE TOOK PLACE ON OR BEFORE DAY IN QUESTION AND < 30 DAYS AGO
                    days_since = (datetime.datetime.today()-datetime.datetime.strptime(c_row[1], "%Y-%m-%d" )).days
                    if (days_since >= i) and (days_since - i < decay_days):
                         decay_scaler = float(decay_days-days_since-i)/float(decay_days)
                         query = """SELECT * FROM quests WHERE rowid = ?"""
                         data = [c_row[0]]
                         cur.execute(query,data)
                         q_row = cur.fetchone()
                         for j in range (0, 7):
                              attr_hist[j][i] += (float(q_row[6+j])*decay_scaler)

               #BUFFS
               for k, v in buff_list.items():
                    buff_active = 0
                    debuff_active = 0
                    query = """SELECT * FROM quests WHERE rowid = ?"""
                    data = [k]
                    cur.execute(query,data)
                    con.commit()
                    q_row = cur.fetchone()
                    for j in range (0, 7):
                         attr_hist[j][i] += float(q_row[6+j])*float(v[i]) #attribute value * daily_status array from buff_list

               attributes['CHA'].append(min(attr_hist[0][i],99))
               attributes['DEX'].append(min(attr_hist[1][i],99))
               attributes['INT'].append(min(attr_hist[2][i],99))
               attributes['STR'].append(min(attr_hist[3][i],99))
               attributes['VIT'].append(min(attr_hist[4][i],99))
               attributes['WIS'].append(min(attr_hist[5][i],99))
               attributes['WLL'].append(min(attr_hist[6][i],99))

          config['last_calc'] = str(datetime.datetime.today().date().isoformat())

     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database--")
     finally:
          if con:
               con.close()

#SYSTEM VARS
config = {}
attributes = {'INT': [], 'VIT': [], 'STR': [], 'WIS': [], 'WLL': [], 'DEX': [], 'CHA': []}
attributes_o = ['INT', 'VIT', 'STR', 'WIS', 'WLL', 'DEX', 'CHA'] #ORDERED
attributes_l = {'INT': 'INTELLIGENCE', 'VIT':'VITALITY', 'STR':'STRENGTH', 'WIS':'WISDOM', 'WLL':'WILLPOWER', 'DEX':'DEXTERITY', 'CHA':'CHARISMA'} #LONG NAME
buffs = []
debuffs = []
buff_list = {}
menu_tree = {'top':["QUESTS", "BUFFS", "SETTINGS", "EXIT"], 'quests':["LOG QUEST", "ADD QUEST", "REMOVE QUEST", "MAIN MENU"], 'buffs':["ACTIVATE BUFF", "DEACTIVATE BUFF", "ADD BUFF", "REMOVE BUFF", "MAIN MENU"]}

icon_list = ["u'\u263A'","u'\u263C'","u'\u2642'","u'\u2665'","u'\u2666'","u'\u266B'", "u'\u221E'", "u'\u2126'", "u'\u2302'", "u'\u273F'", "u'\u2691'" ,"u'\u2693'", "u'\u2602'", "u'\u262F'", "u'\u2605'", "u'\u265E'", "u'\u224B'", "u'\u2615'", "u'\u2646'"]

#LAYOUT VARS
origin_attr = [5, 46]
origin_portrait = [10, 3]
origin_menu = [5, 63]
origin_chart = [38, 35]
origin_quests = [38, 5]
origin_error = [3, 3]
origin_buffs = [5, 35]
dimensions_chart = [80, 43]

#CONFIG
ADD_TEST_DATA = 0
DEBUGGING = 0
decay_days = 30

#OPERATING VARS
x=0
run = 1
menu_level = 'top'
current_menu = 0
current_chart = 0

#INITIALIZATION
screen = curses.initscr()
screen.clear()
screen.keypad(1)

load_config()
load_db()
if (datetime.datetime.today()-datetime.datetime.strptime(config['last_calc'], "%Y-%m-%d" )).days > 0:
     calc_attributes()

while run == 1:
     if DEBUGGING:
          calc_attributes()

     screen.clear()
     screen.border(0)
     box_attr = curses.newwin(17, 32, origin_attr[1]-2, origin_attr[0]-2)
     box_attr.box()
     box_menu = curses.newwin(15, 32, origin_menu[1]-2, origin_menu[0]-2)
     box_menu.box()
     box_chart = curses.newwin(dimensions_chart[1], dimensions_chart[0], origin_chart[1]-2, origin_chart[0]-2)
     box_chart.box()
     box_buffs = curses.newwin(11, 32, origin_buffs[1]-2, origin_buffs[0]-2)
     box_buffs.box()
  
     screen.refresh()

     display_buffs()
     box_buffs.refresh()

     display_attr()
     box_attr.refresh()

     display_menu()
     box_menu.refresh()

     display_chart()
     box_chart.refresh()

     #ascii_char()
     display_quest_status()

     cmd = screen.getch()

     if cmd == curses.KEY_DOWN and current_menu < len(menu_tree[menu_level])-1: current_menu+=1
     elif cmd == curses.KEY_UP and current_menu > 0: current_menu-=1
     elif cmd == curses.KEY_LEFT:
          if current_chart == 0: current_chart = len(attributes_o)-1
          else: current_chart-=1
     elif cmd == curses.KEY_RIGHT:
          if current_chart == len(attributes_o)-1: current_chart = 0
          else: current_chart+=1
     elif cmd == ord('\n'):
          if menu_tree[menu_level][current_menu] == "QUESTS":
               menu_level = 'quests'
               current_menu = 0
          elif menu_tree[menu_level][current_menu] == "BUFFS":
               menu_level = 'buffs'
               current_menu = 0
          elif menu_tree[menu_level][current_menu] == "MAIN MENU":
               menu_level = 'top'
               current_menu = 0
          elif menu_tree[menu_level][current_menu] == "ADD QUEST":
               add_quest('quest')
               menu_level = 'top'
               current_menu = 0
          elif menu_tree[menu_level][current_menu] == "ADD BUFF":
               add_quest('buff')
               menu_level = 'top'
               current_menu = 0
          elif menu_tree[menu_level][current_menu] == "ACTIVATE BUFF":
               log_quest('buff', -1)
               menu_level = 'top'
               current_menu = 0 
          elif menu_tree[menu_level][current_menu] == "DEACTIVATE BUFF":
               log_quest('buff_off', -1)
               menu_level = 'top'
               current_menu = 0 
          elif menu_tree[menu_level][current_menu] == "LOG QUEST":
               log_quest('quest', -1)
               menu_level = 'top'
               current_menu = 0  
          elif menu_tree[menu_level][current_menu] == "REMOVE QUEST":
               #PENDING
               menu_level = 'top'
               current_menu = 0             
          elif menu_tree[menu_level][current_menu] == "EXIT": run = 0
     if cmd == ord('x'): run = 0

save_config()
screen.keypad(0)
curses.endwin()