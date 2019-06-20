import time
import frida

device = frida.get_usb_device()

pid = device.spawn(["fm.castbox.audiobook.radio.podcast"])

device.resume(pid)

time.sleep(1)

session = device.attach(pid)

with open("s1.js") as f:
	script = session.create_script(f.read())
script.load()

raw_input()