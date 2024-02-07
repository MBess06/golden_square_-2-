class music_tracker:
    def __init__(self):
        self.list = []
    def add(self, songs):
        if songs == "":
            return "Please enter a song title"
        else:
            song_list = self.list.append(songs)
        return song_list
    def view_list(self):
        return self.list