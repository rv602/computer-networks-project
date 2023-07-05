import peer
import time

if __name__ == "__main__":
    # create a peer in a separate thread
    peer1 = peer.Peer("10.113.18.210", 6000)
    peer1.connect("10.113.18.210", 5000)

    while True:
        peer1.send_data("Hello from peer1")
        time.sleep(1)
