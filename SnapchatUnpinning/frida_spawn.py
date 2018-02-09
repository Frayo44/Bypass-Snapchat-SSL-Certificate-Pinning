import frida, sys, re
import codecs, time

'''
Running example:
python ./frida_spawn.py ./ca.crt 
'''

APP_NAME = "com.snapchat.android"

if(len(sys.argv)) < 2:
    print("Usage: ./frida_spawn.py [plain text certificate in PEM format]")
    quit()


def on_message(message, data):
    if message['type'] == 'error':
        print(message['stack'])


with codecs.open("./snapchat_unpinning.js", 'r', encoding='utf8') as f:
    jscode  = f.read()
    device  = frida.get_usb_device(timeout=5)
    pid     = device.spawn([APP_NAME])
    session = device.attach(pid)
    print ("pid: {}".format(pid))
    script  = session.create_script(jscode)  
    print ("[*] Intercepting ...")
    script.on('message', on_message)
    script.load()

    with open(sys.argv[1]) as file:
        script.post({'type': 'input', 'payload': file.read()})

    device.resume(APP_NAME)
    sys.stdin.read()
