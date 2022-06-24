from os import mkdir, path, system, name
from yaml import safe_load
from console.utils import set_title
from pypresence import Presence
import threading
import time

default_values = '''#
# Open-Source Project by haxvzje (ch1zuru_#7376)
#
# Access to create your own Applications here:
# https://discord.com/developers/applications
#
cdrp:
  # Please leave it blank if you don't need something below
  # Please replace your own APPLICATION_ID here
  application_id: 989923268456751124
  details: Details => Custom Discord Rich Presence is cool !
  state: State => Custom Discord Rich Presence is cool !
  large_image: image key
  small_image: image key
  large_image_text: text
  small_image_text: text

  # Time Elapsed Count (true/false)
  time_elapsed: true

  # RPC refresh time (in seconds)
  refresh_time: 15
'''

if path.exists('config.yml'):
    settings = safe_load(open('config.yml', 'r', errors='ignore'))
else:
    open('config.yml', 'w').write(default_values)
    settings = safe_load(open('config.yml', 'r', errors='ignore'))

clear = lambda: system('cls' if name == 'nt' else 'clear')
version = '1.0-releaase'
threading_break = False
set_title(f'Custom Discord Rich Presence | build {version} | by haxvzje')

def Main():
    logo() # Call logo() function
    rpc() # Call rpc() function
    input("\nPress enter to exit...")

def logo():
    ascii_logo = ''' 
   ▄████████ ████████▄     ▄████████    ▄███████▄ 
   ███    ███ ███   ▀███   ███    ███   ███    ███ 
   ███    █▀  ███    ███   ███    ███   ███    ███ 
   ███        ███    ███  ▄███▄▄▄▄██▀   ███    ███ 
   ███        ███    ███ ▀▀███▀▀▀▀▀   ▀█████████▀  
   ███    █▄  ███    ███ ▀███████████   ███        
   ███    ███ ███   ▄███   ███    ███   ███        
   ████████▀  ████████▀    ███    ███  ▄████▀      
                         ███    ███              '''
    clear()
    print(ascii_logo)
    print(f"\n   Author: haxvzje (ch1zuru_#7376)\n   Build: {version}\n\n\n\n")

def rpc():
    t = threading.Thread(target=title_session)
    t.start()
    print("   Please make sure your Discord Client is up and running!\n   Don't forget to visit config.yml to edit the parameters you want!")
    try:
        RPC = Presence(CDRP.application_id)
        RPC.connect()
        if CDRP.time_elapsed:
            RPC.update(state=CDRP.state, details=CDRP.details, large_image=CDRP.large_image, small_image=CDRP.small_image, large_text=CDRP.large_image_text, small_text=CDRP.small_image_text, start=int(time.time()))
        else:
            RPC.update(state=CDRP.state, details=CDRP.details, large_image=CDRP.large_image, small_image=CDRP.small_image, large_text=CDRP.large_image_text, small_text=CDRP.small_image_text)
        print("\n\n   Custom Discord Rich Presence has been launched!\n   If you want to stop using CDRP just close this window!")
        while True:
            time.sleep(15)
    except Exception as e:
        print("\n\nError: " + e)

def title_session():
    sension_time  = 0
    while True:
        set_title(f'Custom Discord Rich Presence | build {version} | by haxvzje | session_time: {sension_time}s')
        sension_time+=1
        time.sleep(1)
        if threading_break:
            break

class CDRP:
    application_id = str(settings['cdrp']['application_id'])
    state = str(settings['cdrp']['state'])
    details = str(settings['cdrp']['details'])
    large_image = str(settings['cdrp']['large_image'])
    small_image = str(settings['cdrp']['small_image'])
    large_image_text = str(settings['cdrp']['large_image_text'])
    small_image_text = str(settings['cdrp']['small_image_text'])
    time_elapsed = bool(settings['cdrp']['time_elapsed'])
    refresh_time = int(settings['cdrp']['refresh_time'])

Main() # Run Main() function