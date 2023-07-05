import peer
import time
import clipboard

if __name__ == "__main__":
    # Create a peer in a separate thread
    peer1 = peer.Peer("10.113.18.56", 6000)
    peer1.connect("10.113.18.56", 5000)

    # Store the previous clipboard content
    previous_clipboard_content = ""

    while True:
        # Get the current clipboard content
        clipboard_content = clipboard.paste()

        # Check if the clipboard content has changed
        if clipboard_content != previous_clipboard_content:
            # Send the clipboard content to the connected peer
            peer1.send_data(clipboard_content)

            # Update the previous clipboard content
            previous_clipboard_content = clipboard_content

        # Sleep for a short duration
        time.sleep(0.5)
