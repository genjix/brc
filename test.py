from _brc import *

def started(ec):
    print ec

def newtx(tx_hash):
    print "tx:", tx_hash.encode("hex")

b = Broadcaster()
b.start(1, 10, 4, newtx, started)
# To broadcast a tx use:
#   b.broadcast(raw_tx)
# Where raw_tx is the raw tx data bytes.
raw_input()
# You must stop otherwise exception is thrown.
b.stop()

