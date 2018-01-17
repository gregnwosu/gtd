#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

GOOGLE_CAL_URL = 'https://calendar.google.com/calendar/ical/'
CALENDARS = {
   'Maya&Cyra': 's5idc92chck1cpdl1g8peinsbs%40group.calendar.google.com/private-9ba0daef54392b7f7d7935af67c8acd9/basic.ics',
    'Domestic': '57jh52va6e1c1fpcpm4sc0hlv4%40group.calendar.google.com/private-0844715e5ca0ac0e2458cb7978e8e81b/basic.ics',
  'esta': 'os1meevo7574q3m04scoeea3q4%40group.calendar.google.com/private-c59c7d4fece0d7b3734366d0f4f59ba6/basic.ics',
  'esta2': 'esta.orchard%40gmail.com/public/basic.ics',
  'health&fitness':'l45q00pio1felphepk9r0uuh3s%40group.calendar.google.com/private-adeca8dce2371b37a6bd92ca374c03e0/basic.ics',
  'social': 'cnnkfps66o516p2qj8opq4b3bc%40group.calendar.google.com/private-9cdb83fd547e366f45175cf2c19b2abf/basic.ics'
  }


def main():
    for name, address in CALENDARS.items():
        print("loading " + name)
        with open("/Users/greg/gtd/calendars/imported/ical/%s-google-calendar.ics"
                  % name, "w") as fd:
            fd.write(requests.get(GOOGLE_CAL_URL + address).text)


if __name__ == '__main__':
    main()
