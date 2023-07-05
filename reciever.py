import peer
import time

if __name__ == "__main__":
    # create a peer in a separate thread
    peer1 = peer.Peer("10.113.18.56", 5000)
    peer1.start()
