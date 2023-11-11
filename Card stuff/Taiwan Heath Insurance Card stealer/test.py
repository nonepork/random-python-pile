from smartcard.System import readers

# define the APDUs used in this script
SelectAPDU = [ 0x00, 0xA4, 0x04, 0x00, 0x10, 0xD1, 0x58, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x11, 0x00 ]

ReadProfileAPDU = [ 0x00, 0xca, 0x11, 0x00, 0x02, 0x00, 0x00 ]

# get all the available readers
r = readers()
print ("Available readers:", r)

reader = r[0]
print ("Using:", reader)

connection = reader.createConnection()
connection.connect()

data, sw1, sw2 = connection.transmit(SelectAPDU)
print ("Select Applet: %02X %02X" % (sw1, sw2))

data, sw1, sw2 = connection.transmit(ReadProfileAPDU)
print ("Command: %02X %02X" % (sw1, sw2))
print  ('Card Number : %s' % ''.join(chr(i) for i in data[0:12]))

# 讀卡機讀取進來的的資料的確是12～31這些byte，big5為雙位元字，所以在data中大概是前6～8個
# 在python3中，字串都是以bytes儲存的，你要顯示出來，只需要decode時指定正確的編碼就行了
print("name: {}".format(bytes(data[12:32]).decode("big5")))

print  ('ID Number : %s' % ''.join(chr(i) for i in data[32:42]))
print  ('Birthday : %s' % ''.join(chr(i) for i in data[43:49]))
print  ('Sex : %s' % ''.join(chr(i) for i in data[49:50]))
print  ('Card Date : %s' % ''.join(chr(i) for i in data[51:57]))
