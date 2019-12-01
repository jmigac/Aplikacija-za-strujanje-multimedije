import vlc

url = 'http://mr2.juricamigac.com/windows.mp3'

vlc = vlc.Instance()
vlcPlayer = instance.media_player_new()
pjesma = vlc.media_new(url)
vlcPlayer.set_media(media)
vlcPlayer.play()