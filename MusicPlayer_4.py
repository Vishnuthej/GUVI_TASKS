class Music_Player():
    def __init__(self):
        self.playlist = []
        self.song_details ={}
        
    def create_playlist(self, playlist_name):
        self.playlist.append(playlist_name) 
        self.song_details[playlist_name] = []
        return True
    
    def delete_playlist(self, playlist_name):
        self.playlist.remove(playlist_name)
        return True
    
    def add_song(self, palylist_name, song_name):
        if palylist_name in self.playlist:
           self.song_details [palylist_name].append(song_name)
        else:
           print ("Playlist does not exist")
        return
    def delete_song(self, playlist_name, song_name):
        if playlist_name in self.playlist:
           if song_name in self.song_details[playlist_name]:
               self.song_details[playlist_name].remove(song_name)
           else: 
               print("song does not exist in playlist")
               
        else:
           print("Playlist does not exist in playlist")
        return
    def play_song(self, playlist_name, song_name):
        if playlist_name in self.playlist:
           if song_name in self.song_details[playlist_name]:
               print(song_name)
           else: 
               print("song does not exist in playlist")
               
        else:
           print("Playlist does not exist in playlist")
        return
if __name__ == "__main__":
    MP3 = Music_Player()
    MP3.create_playlist("PL1")
    print("1")
    MP3.create_playlist("PL2")
    print("2")
    MP3.add_song("PL1", "S1")
    MP3.add_song("PL1", "S2")
    MP3.add_song("PL1", "S3")
    MP3.add_song("PL2", "S4")
    
    MP3.delete_song("PL3", "S1")
    print("PL3 is not there")

    MP3.play_song("PL1", "S2")
    print("playing song S2")






           
           
           
           
""" temp = []
            temp.append(song_name)
            temp_dict = {}
            temp_dict[palylist_name] = temp

        
        
    def play_songs(self, playlist_name, song_name):
        if playlist in range(playlist_name):
            pri"""
            


   
    
   


"""playlist_name = [playlist_1, playlist_2, playlist_3]
        if playlist_name in range(playlist_name) :
            if song_name in range(playlist_name):
                print ("song is already added to this playlist")
            else:
                playlist_name =+ song_name"""