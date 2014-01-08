#!/usr/bin/env python

from os import system
import locale
import curses
import sqlite3
import sys
import random
import datetime

#testing merge

locale.setlocale(locale.LC_ALL, '')

def refresh_main_interface():
     screen.refresh()

     ascii_char()
     box_portrait.refresh()

     display_buffs()
     box_buffs.box()
     box_buffs.refresh()

     display_attr()
     box_attr.box()
     box_attr.refresh()

     display_menu()
     box_menu.box()
     box_menu.refresh()

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def ascii_char():
     if 0:
          box_portrait.addstr( origin_portrait[1]+0, origin_portrait[0], u'              \u2588\u2588\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+1, origin_portrait[0], u'             \u2588\u2591\u2591\u2591\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+2, origin_portrait[0], u'           \u2588\u2591\u2591\u2591\u2592\u2588\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+3, origin_portrait[0], u'         \u2588\u2588\u2591\u2591\u2591\u2592\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+4, origin_portrait[0], u'       \u2588\u2588\u2591\u2591\u2591\u2591\u2592\u2592\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+5, origin_portrait[0], u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2591\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+6, origin_portrait[0], u'\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2592\u2592\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+7, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2591\u2591\u2591\u2591\u2592\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+8, origin_portrait[0], u'  \u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2591\u2591\u2591\u2591\u2592\u2588    '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+9, origin_portrait[0], u'    \u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+10, origin_portrait[0], u'   \u2588 \u2584  \u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+11, origin_portrait[0], u'   \u2588 \u2588  \u2584   \u2588\u2588\u2592\u2592\u2592\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+12, origin_portrait[0], u'   \u2592\u2592   \u2588    \u2592\u2588\u2588\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+13, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592   \u2592 \u2592\u2592\u2588\u2593\u2588\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+14, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+15, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+16, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+17, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2593\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+18, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2593\u2593\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+19, origin_portrait[0], u' \u2588 \u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2588\u2593\u2593\u2593\u2593\u2593\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+20, origin_portrait[0], u' \u2588 \u2588\u2593\u2593\u2588\u2588\u2588\u2588\u2593\u2593\u2593\u2588\u2588\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+21, origin_portrait[0], u'  \u2588\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2588\u2593\u2588  \u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+22, origin_portrait[0], u'   \u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588   \u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+23, origin_portrait[0], u' \u2588\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588\u2588\u2588    '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+24, origin_portrait[0], u'\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+25, origin_portrait[0], u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2593\u2593\u2593\u2593\u2593\u2593\u2593\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+26, origin_portrait[0], u'       \u2588\u2588\u2588\u2593\u2593\u2593\u2593\u2588    '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+27, origin_portrait[0], u'          \u2588\u2588\u2588\u2588     '.encode('utf-8'))
     else:
          box_portrait.addstr( origin_portrait[1]+0, origin_portrait[0], u'         \u2588\u2588\u2588\u2588    '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+1, origin_portrait[0], u'    \u2588\u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2588\u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+2, origin_portrait[0], u'    \u2588\u2592\u2592\u2592\u2592\u2588\u2592\u2592\u2592\u2592\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+3, origin_portrait[0], u'  \u2588\u2592\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2592\u2592\u2592\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+4, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+5, origin_portrait[0], u' \u2588\u2588\u2592\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+6, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+7, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2592\u2588\u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+8, origin_portrait[0], u' \u2588\u2588\u2592\u2588      \u2588\u2592\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+9, origin_portrait[0], u'  \u2588\u2592\u2588       \u2588\u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+10, origin_portrait[0], u'   \u2588 \u2584       \u2592\u2592\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+11, origin_portrait[0], u'   \u2588 \u2588  \u2584    \u2588\u2592\u2592\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+12, origin_portrait[0], u'   \u2592\u2592   \u2588   \u2588\u2588\u2592\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+13, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592   \u2592 \u2592\u2592\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+14, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+15, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2588\u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+16, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2591\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+17, origin_portrait[0], u' \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2591\u2591\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+18, origin_portrait[0], u'  \u2588\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2592\u2588\u2591\u2591\u2591\u2591\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+19, origin_portrait[0], u' \u2588 \u2588\u2588\u2588\u2592\u2592\u2592\u2592\u2588\u2591\u2588\u2591\u2591\u2591\u2588'.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+20, origin_portrait[0], u' \u2588 \u2588\u2591\u2591\u2588\u2588\u2588\u2588\u2591\u2591\u2591\u2588\u2588\u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+21, origin_portrait[0], u'  \u2588\u2588\u2588\u2588\u2591\u2591\u2588\u2588\u2588\u2591\u2588  \u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+22, origin_portrait[0], u'   \u2588\u2591\u2591\u2588\u2588\u2588\u2591\u2591\u2588   \u2588 '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+23, origin_portrait[0], u' \u2588\u2588\u2591\u2591\u2591\u2591\u2588\u2591\u2591\u2591\u2591\u2588\u2588\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+24, origin_portrait[0], u'\u2588  \u2588\u2591\u2591\u2591\u2588\u2591\u2591\u2591\u2591\u2591\u2591\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+25, origin_portrait[0], u'\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2591\u2588\u2588\u2588\u2588\u2591\u2588  '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+26, origin_portrait[0], u'       \u2588\u2588\u2588   \u2588   '.encode('utf-8'))
          box_portrait.addstr( origin_portrait[1]+27, origin_portrait[0], u'          \u2588\u2588\u2588\u2588'.encode('utf-8'))

     box_portrait.addstr( origin_portrait[1]+29, origin_portrait[0], "Level 29 Human", curses.A_BOLD)     
     screen.addstr(0,0, "") 

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
               box_attr.addstr(2+i, 2 + 6, str(int(attributes[k][0])))
               #box_attr.addstr(2+i, 2 + 6, str(int(attributes[k][len(attributes[k])-1])))
               for j in range(0,20):
                    if int(attributes[k][0]*20/99)>j:
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
     global attributes
     i=0
     box_chart.addstr(2, 2, attributes_l[attributes_o[current_chart]], curses.A_BOLD)
     for tick in attributes[attributes_o[current_chart]]:
          scaling_factor = float(dimensions_chart[1]-8)/99
          for j in range(1,dimensions_chart[1]-8):
               if float(tick) * scaling_factor > j:
                    box_chart.addstr(dimensions_chart[1]-4-j, 77-i, u'\u2592'.encode('utf-8'))
          i+=1
     
     #AXES
     box_chart.addstr(4, 2, "99")
     for i in range(5,dimensions_chart[1]-4):
          box_chart.addstr(i, 3, u'\u2502'.encode('utf-8'))
     box_chart.addstr(dimensions_chart[1]-4, 3, "0")
     box_chart.addstr(dimensions_chart[1]-3, 3, u'\u2514'.encode('utf-8'))
     for i in range(1,75):
          box_chart.addstr(dimensions_chart[1]-3, 3+i, u'\u2500'.encode('utf-8'))

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
                         buff_cmd = "box_buffs.addstr(6+debuff_row*2,11+2*debuff_i-debuff_row*18, "+q_row[4]+".encode('utf-8'))"
                         exec buff_cmd
                         debuff_i += 1
                    if buff_i > 14 or debuff_i > 14:
                         break

     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database for listing buffs--")
     finally:
          if con:
               con.close()

def display_quest_status():
     screen.addstr(origin_quests[1], origin_quests[0], "ACTIVE", curses.A_BOLD)

def load_db():
     con = None

     try:
          con = sqlite3.connect('char.db')
         
          cur = con.cursor()

          if CLEAN_START:
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

def feature_list_buffs():
     global buff_list

     try:
          con = sqlite3.connect('char.db')
          cur = con.cursor()

          box_feature.addstr(4,4, "BUFFS", curses.A_BOLD)

          i = 0
          for k,v in buff_list.items():
               if int(v[0]) == 1:
                    query = """SELECT * FROM quests WHERE rowid = ? and
                         (cha_val > 0 or int_val > 0 or vit_val > 0 or str_val > 0 or wis_val > 0 or dex_val > 0 or wll_val > 0)"""
                    data = [k]
                    cur.execute(query,data)
                    con.commit()
                    q_row = cur.fetchone()

                    if q_row:
                         buff_cmd = "box_feature.addstr(6+i*5,5, "+q_row[4]+".encode('utf-8'))"
                         exec buff_cmd
                         box_feature.addstr(6+i*5, 7, q_row[0])
                         for j in range (0, 7):
                             box_feature.addstr(6+i*5+2, 7+j*8, attributes_o[j] + "(" + str(q_row[6+j]) + ")")

                    i+=1

          box_feature.addstr(6+i*5,4, "DEBUFFS", curses.A_BOLD)

          for k,v in buff_list.items():
               if int(v[0]) == 1:
                    query = """SELECT * FROM quests WHERE rowid = ? and
                         (cha_val < 0 or int_val < 0 or vit_val < 0 or str_val < 0 or wis_val < 0 or dex_val < 0 or wll_val < 0)"""
                    data = [k]
                    cur.execute(query,data)
                    con.commit()
                    q_row = cur.fetchone()

                    if q_row:
                         buff_cmd = "box_feature.addstr(4+i*5-1,5, "+q_row[4]+".encode('utf-8'))"
                         exec buff_cmd
                         box_feature.addstr(4+i*5-1, 7, q_row[0])
                         for j in range (0, 7):
                             box_feature.addstr(4+i*5+1, 7+j*8, attributes_o[j] + "(" + str(q_row[6+j]) + ")")
                             
                    i+=1

     except sqlite3.Error, e:
          screen.addstr(origin_error[1], origin_error[0], "--Error loading database for listing buffs--")
     finally:
          if con:
               con.close()   

def feature_chart_multi():
     attr_i = 0
     for k,v in attributes.items():

          #ATTR LABELS
          box_feature.addstr(7+10*attr_i, 3, k, curses.A_BOLD)

          #VALUES
          i=0
          for tick in v:
               scaling_factor = float(dimensions_feature[1])/99/len(attributes_o)
               if i < 68:
                    for j in range(1,8):
                         if float(tick) * scaling_factor > j:
                              pass
                              box_feature.addstr(10-j+10*attr_i, 76-i, u'\u2592'.encode('utf-8'))
               i+=1
          
          #AXES
          for i in range(4+dimensions_feature[1]/len(attributes_o)*attr_i-1,dimensions_feature[1]/len(attributes_o)*attr_i+11):
               box_feature.addstr(i, 8, u'\u2502'.encode('utf-8'))
          box_feature.addstr(dimensions_feature[1]/len(attributes_o)*attr_i+10, 8, u'\u2514'.encode('utf-8'))

          for i in range(1,69):
               box_feature.addstr(dimensions_feature[1]/len(attributes_o)*attr_i+10, 8+i, u'\u2500'.encode('utf-8'))

          attr_i += 1

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
          box_feature.clear()
          if quest_type == 'quest':
               box_feature.addstr(2, 2, "What is the quest?")
          else:
               box_feature.addstr(2,2, "What is this buff or debuff?")
          
          refresh_main_interface()
          box_feature.box()
          box_feature.refresh()
          name_str = box_feature.getstr(10, 10, 60)

          try:
               con = sqlite3.connect('char.db')
               cur = con.cursor()

               query = """SELECT * FROM quests
                    WHERE name = ? and (status = 'open' or status = 'persistent')
                    """
               data =  [name_str]
               cur.execute(query, data)       
               con.commit()
               q_rows = cur.fetchall()
          except sqlite3.Error, e:
               screen.addstr(origin_error[1], origin_error[0], "--Error adding quest to database--")
          finally:
               if con:
                    con.close()

          if len(q_rows) > 0:
               box_alert.addstr(2,2,"A quest or buff with that name already exists.")
               box_alert.refresh()
               cmd = screen.getch()
          elif len(name_str)>0:
               attempt = 0

     if quest_type == 'quest':
          attempt = 1
          menu_step = 0
          while attempt == 1:
               screen.clear()
               box_feature.clear()
               box_feature.box()
               box_feature.addstr(2, 2, "Is this a persistent quest?")
               box_feature.addstr(4, 4, "Persistent")
               box_feature.addstr(6, 4, "One-time")
               box_feature.addstr(4+menu_step%2*2, 2, u'\u25BA'.encode('utf-8'))
               box_feature.addstr(1, 1, '')

               refresh_main_interface()

               box_feature.refresh()

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
               box_feature.clear()
               box_feature.box()
               box_feature.addstr(2, 2, "Choose an icon for this buff or debuff")
               j = 0
               for icon in icon_list:
                    buff_cmd = "box_feature.addstr(4+j%8*2, 4+(j/8)*10, "+icon+".encode('utf-8'))"
                    exec buff_cmd
                    j+=1
               box_feature.addstr(4+menu_step%8*2, 2+(menu_step/8)*10, u'\u25BA'.encode('utf-8'))

               screen.addstr(1, 1, '')

               refresh_main_interface()

               box_feature.refresh()

               cmd = screen.getch()

               if cmd == curses.KEY_DOWN and menu_step < len(icon_list)-1:
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
          box_feature.clear()
          box_feature.box()
          box_feature.addstr(2, 2, "Configure attribute impact")

          attributes_sorted = attributes_o
          attributes_sorted.sort()

          for i in range (0,7):
               box_feature.addstr(4, 4+i*8, attributes_sorted[i])
               box_feature.addstr(6, 4+i*8, str(val_array[i]))
          box_feature.addstr(4, 3+menu_step*8, u'\u2588'.encode('utf-8'))
          
          refresh_main_interface()

          box_feature.refresh()

          cmd = screen.getch()

          if cmd == curses.KEY_DOWN and val_array[menu_step] > 0 and quest_type == 'quest':
               val_array[menu_step]-=1
          elif cmd == curses.KEY_DOWN:
               val_array[menu_step]-=1
          elif cmd == curses.KEY_UP:
               val_array[menu_step]+=1
          elif cmd == curses.KEY_RIGHT and menu_step < 6:
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
          if quest_type == 'buff':
               query = """SELECT rowid from quests where name = ? and date_created = ?"""
               data = [name_str, datetime.datetime.today().date().isoformat()]
               cur.execute(query, data)       
               con.commit() 
               q_row = cur.fetchone()
               query = """INSERT INTO completes
                    (quest_id, date_completed, buff_bool)
                    VALUES
                    (?, ?, ?)
                    """       
               data = [q_row[0],datetime.datetime.today().date().isoformat(),0]
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

               if len(c_rows)==0 and quest_type == 'buff':
                    box_alert.addstr(2,2,"You have not added any buffs or debuffs to activate, or they are all currently active.")
                    box_alert.refresh()
                    cmd = screen.getch()
                    return
               elif len(c_rows) == 0 and quest_type == 'buff_off':
                    box_alert.addstr(2,2,"There are no buffs or debuffs eligible for removal.")
                    box_alert.refresh()
                    cmd = screen.getch()
                    return
               elif len(c_rows) == 0 and quest_type == 'quest':
                    box_alert.addstr(2,2,"There are currently no open quests.")
                    box_alert.refresh()
                    cmd = screen.getch()
                    return

               attempt = 1
               menu_step = 0
               while attempt == 1:
                    screen.clear()

                    if quest_type == 'buff':
                         prompt_string = "Which buff should be activated?"
                    elif quest_type == 'quest':
                         prompt_string = "Which quest did you complete?"
                    elif quest_type == 'buff_off':
                         prompt_string = "Which buff should be deactivated?"

                    box_feature.clear()
                    screen.refresh()

                    i = 0
                    for c_row in c_rows:
                         if quest_type == 'buff':
                              buff_cmd = "box_feature.addstr(4+i*2,4, "+c_row[2]+".encode('utf-8'))"
                         elif quest_type == 'buff_off':
                              buff_cmd = "box_feature.addstr(4+i*2,4, "+c_row[2]+".encode('utf-8'))"
                         elif quest_type == 'quest':
                              buff_cmd = "pass"
                         exec buff_cmd
                         box_feature.addstr(4+i*2, 6, c_row[1])
                         i+=1

                    box_feature.addstr(4+menu_step%8*2, 2+(menu_step/8)*10, u'\u25BA'.encode('utf-8'))
                    box_feature.addstr(1, 1, '')

                    refresh_main_interface()

                    box_feature.addstr(2,2,prompt_string)
                    box_feature.box()
                    box_feature.refresh()

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

def calc_attributes():
     global attributes
     global buff_list

     con = None
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
               #populates a dictionary with a key for every buff that has ever been active, value is an empty array which will become the daily array
               buff_list[c_row[0]] = []

          for k, v in buff_list.items():
               query = """SELECT * FROM completes WHERE quest_id = ? ORDER BY date_completed ASC"""
               data = [k]
               cur.execute(query,data)
               con.commit()
               c_rows = cur.fetchall()

               daily_status = 0
               temp_array = []
               for i in reversed(range (0, 73)):
                    for c_row in c_rows:
                         days_since = (datetime.datetime.today()-datetime.datetime.strptime(c_row[1], "%Y-%m-%d" )).days
                         if days_since == i:
                              daily_status = c_row[2]
                    temp_array.append(daily_status)
               buff_list[k] = temp_array[::-1]

          for i in range(0, 73):
               #QUESTS
               for j in range (0, 7): #append a new day slot to each of 7 attributes
                   attr_hist[j].append(0)            
               cur.execute("SELECT completes.* FROM completes INNER JOIN quests ON completes.quest_id = quests.rowid WHERE quests.style = 'decay'")
               con.commit()
               c_rows = cur.fetchall()
               for c_row in c_rows:
                    decay_scaler = 0
                    #IF COMPLETE TOOK PLACE ON OR BEFORE DAY IN QUESTION AND < 30 DAYS AGO
                    days_since = (datetime.datetime.today()-datetime.datetime.strptime(c_row[1], "%Y-%m-%d" )).days
                    if (days_since >= i) and (days_since - i < decay_days):
                         decay_scaler = float(decay_days-(days_since-i))/float(decay_days)
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

               attributes['CHA'].append(max(min(attr_hist[0][i],99),0))
               attributes['DEX'].append(max(min(attr_hist[1][i],99),0))
               attributes['INT'].append(max(min(attr_hist[2][i],99),0))
               attributes['STR'].append(max(min(attr_hist[3][i],99),0))
               attributes['VIT'].append(max(min(attr_hist[4][i],99),0))
               attributes['WIS'].append(max(min(attr_hist[5][i],99),0))
               attributes['WLL'].append(max(min(attr_hist[6][i],99),0))

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
buff_list = {}
menu_tree = {'top':["QUESTS", "BUFFS", "VIEWS", "EXIT"], 'quests':["LOG QUEST", "ADD QUEST", "MAIN MENU"], 'buffs':["ACTIVATE BUFF", "DEACTIVATE BUFF", "ADD BUFF", "MAIN MENU"], 'views':["OVERVIEW", "LIST BUFFS", "ATTRIBUTES"]}
icon_list = ["u'\u263A'","u'\u263C'","u'\u2642'","u'\u2665'","u'\u2666'","u'\u266B'", "u'\u2707'","u'\u221E'", "u'\u2126'", "u'\u2302'", "u'\u273F'", "u'\u2709'","u'\u2602'", "u'\u262F'", "u'\u2605'", "u'\u265E'", "u'\u224B'", "u'\u2646'", "u'\u260E'","u'\u265A'","u'\u00BB'","u'\uFF04'","u'\u2622'","u'\u27B3'"]

#LAYOUT VARS [x, y] notation which is reversed [row, col]
origin_attr = [5, 47]
origin_portrait = [10, 3]
origin_menu = [5, 64]
origin_chart = [38, 36]
origin_quests = [38, 5]
origin_error = [3, 3]
origin_buffs = [5, 36]
origin_feature = [38, 5]
origin_alert = [40,30]
dimensions_chart = [80, 43]
dimensions_feature = [80, 74]

#CONFIG
ADD_TEST_DATA = 0
DEBUGGING = 0
CLEAN_START = 0
decay_days = 30

#OPERATING VARS
x=0
run = 1
menu_level = 'top'
current_menu = 0
current_chart = 0
current_feature = 'chart_multi'

#INITIALIZATION
screen = curses.initscr()
screen.clear()
screen.keypad(1)

load_config()
load_db()

calc_attributes()

while run == 1:
     if DEBUGGING:
          calc_attributes()

     screen.clear()
     box_portrait = curses.newwin(100,100, 0, 0)
     box_attr = curses.newwin(17, 32, origin_attr[1]-2, origin_attr[0]-2)
     box_attr.box()
     box_menu = curses.newwin(15, 32, origin_menu[1]-2, origin_menu[0]-2)
     box_menu.box()
     box_chart = curses.newwin(dimensions_chart[1], dimensions_chart[0], origin_chart[1]-2, origin_chart[0]-2)
     box_chart.box()
     box_buffs = curses.newwin(11, 32, origin_buffs[1]-2, origin_buffs[0]-2)
     box_buffs.box()
     box_feature = curses.newwin(dimensions_feature[1], dimensions_feature[0], origin_feature[1]-2, origin_feature[0]-2)
     box_feature.box()
     box_alert = curses.newwin(15,45,origin_alert[1],origin_alert[0])
     box_alert.box()

     screen.refresh()

     refresh_main_interface()

     if current_feature == 'chart_single':
          display_chart()
          display_quest_status()
          box_chart.refresh()
     elif current_feature == 'chart_multi':
          feature_chart_multi()
          box_feature.refresh()
     elif current_feature == 'list_buffs':
          feature_list_buffs()
          box_feature.refresh()

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
          elif menu_tree[menu_level][current_menu] == "VIEWS":
               menu_level = 'views'
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
          elif menu_tree[menu_level][current_menu] == "LIST BUFFS":
               current_feature = 'list_buffs'
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
          elif menu_tree[menu_level][current_menu] == "OVERVIEW":
               current_feature = 'chart_single'
               menu_level = 'top'
               current_menu = 0 
          elif menu_tree[menu_level][current_menu] == "ATTRIBUTES":
               current_feature = 'chart_multi'
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