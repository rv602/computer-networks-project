import peer
import time
# import clipboard

if __name__ == "__main__":
    # Create a peer in a separate thread
    peer1 = peer.Peer("10.113.18.210", 6001)
    peer1.start()
    # peer1.connect("10.113.18.210", 6000)

    time.sleep(1)

    # Create a peer in a separate thread
    peer2 = peer.Peer("10.113.18.210", 6002)
    peer2.connect("10.113.18.210", 6001)

    time.sleep(1)
    peer2.send_data("Hello from peer 2")

    peer1.send_data("Hello from peer 1")

    # Store the previous clipboard content
    previous_clipboard_content = ""

    # while True:
    #     # Get the current clipboard content
    #     clipboard_content = clipboard.paste()

    #     # Check if the clipboard content has changed
    #     if clipboard_content != previous_clipboard_content:
    #         # Send the clipboard content to the connected peer
    #         peer1.send_data(clipboard_content)

    #         # Update the previous clipboard content
    #         previous_clipboard_content = clipboard_content

    #     # Sleep for a short duration
    #     time.sleep(0.5)
