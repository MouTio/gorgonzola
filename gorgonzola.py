# -*- coding: utf-8 -*-
import urllib2
import datetime
import re


NEW_DAY = '<p>'
NEW_LINE = '<br />'

# today = (datetime.date.today()-datetime.timedelta(days = 4)).strftime('%d/%m/%Y')
today = datetime.date.today().strftime('%d/%m/%Y')
print 'Hoy es día =', today

portamivia_web = urllib2.urlopen("https://www.facebook.com/PORTAMI-VIA-128458703849924/").read()  # portamivia_web
# print 'portamivia_web=', portamivia_web


menu = ''

# cadena.find(sub[, start[, end]]) -> int
pos_today = portamivia_web.find(today)
pos_ini = portamivia_web.find('<p>', pos_today)
pos_end = portamivia_web.find('</p>', pos_ini)


for i in xrange(pos_ini, pos_end):
  menu += portamivia_web[i]

if re.search('Gorgonzola', menu, re.IGNORECASE):
  print 'HOY HAY GORGONZOLA!!!'
else:
  print 'Hoy no hay gorgonzola :('


title_ini = menu.find('<p>')+len(NEW_DAY)
title_end = menu.find(NEW_LINE, title_ini)
menu_title = menu[title_ini:title_end]
print menu_title

menu_end = len(menu)
num_lines = menu.count(NEW_LINE)
line_end = 0
for i in xrange(num_lines):
  line_menu = ''
  line_ini = menu.find(NEW_LINE, line_end)+len(NEW_LINE)
  line_end = menu.find(NEW_LINE, line_ini)
  if line_end == -1:
    line_end = menu_end
  line_menu = menu[line_ini:line_end]
  print line_menu

# print 'Menú del día=', menu


