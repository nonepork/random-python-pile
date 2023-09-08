#! /usr/bin/env python3
"""
Sample script that monitors smartcard insertion/removal.

__author__ = "http://www.gemalto.com"

Copyright 2001-2012 gemalto
Author: Jean-Daniel Aussel, mailto:jean-daniel.aussel@gemalto.com

This file is part of pyscard.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.System import readers
import time

SelectAPDU = [ 0x00, 0xA4, 0x04, 0x00, 0x10, 0xD1, 0x58, 0x00,
              0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x11, 0x00 ]

ReadProfileAPDU = [ 0x00, 0xca, 0x11, 0x00, 0x02, 0x00, 0x00 ]

class PrintObserver(CardObserver):
    """A simple card observer that is notified
    when cards are inserted/removed from the system and
    prints the list of cards
    """

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        if addedcards:
            try:
                r = readers()
                reader = r[0]

                connection = reader.createConnection()
                connection.connect()

                data, sw1, sw2 = connection.transmit(SelectAPDU)
                data, sw1, sw2 = connection.transmit(ReadProfileAPDU)

                card_number = ''.join(chr(i) for i in data[0:12])
                name = ''.join(bytes(data[12:32]).decode("big5"))
                ID = ''.join(chr(i) for i in data[32:42])
                birthday = ''.join(chr(i) for i in data[43:49])
                sex = ''.join(chr(i) for i in data[49:50])
                card_date = ''.join(chr(i) for i in data[51:57])
                with open('data.txt', 'a', encoding='utf-8') as f:
                    f.write(card_number)
                    f.write(name)
                    f.write(ID)
                    f.write(birthday)
                    f.write(sex)
                    f.write(card_date)
                    f.write('\n')
            except KeyboardInterrupt:
                quit()
            except:
                pass
        if removedcards:
            print("-Removed:")

if __name__ == '__main__':
    print("Insert or remove a smartcard in the system.")
    print("")
    cardmonitor = CardMonitor()
    cardobserver = PrintObserver()
    cardmonitor.addObserver(cardobserver)

    time.sleep(100000)
