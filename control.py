#!/usr/bin/python3

import os
from gi.repository import Playerctl, GLib
from subprocess import call

player = Playerctl.Player(player_name='spotify')

def on_metadata(player, e):
    if 'xesam:artist' in e.keys() and 'xesam:tital' in e.keys():
        print('Now Playing: ')
        print('{artist} - {title}'.format(artist=e['xesam:artist'][0], title=e['xesam:title']))

def on_play(player):
    print('Playing at volume {}'.format(player.get_title()))
    
def on_pause(player):
    print('Paused the song: {}'.format(player.get_title()))
    cmd = 'espeak "{} is now paused"'.format(player.get_title())
    os.system(cmd)

player.on('play', on_play)
player.on('pause', on_pause)
player.on('metadata', on_metadata)

#start playing music
player.play()

#wait for events
main = GLib.MainLoop()
main.run()

