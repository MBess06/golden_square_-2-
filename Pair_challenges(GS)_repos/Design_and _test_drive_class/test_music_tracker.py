from lib.music_tracker import *
# """
# Given a song 
# Returns it in the list
# """
# track = music_tracker(list)
# track.add("let it go!")
# track.view_list() => list = ["let it go!"]

def test_adding_song():
    track = music_tracker()
    track.add("Let it go!")
    assert track.view_list() == ["Let it go!"]


# """
# Given an empty song argument
# Returns "Please enter a song title"
# """
# track = music_tracker(list)
# track.add("")
# track.view_list() => "Please enter a song title"
    
def test_no_song_title():
    track = music_tracker()
    assert track.add("") == "Please enter a song title"

# """
# Given you view the list before adding any songs
# Return should be empty
# """
# track.view_list() => list = []
    
def test_view_empty_list():
    track = music_tracker()
    assert track.view_list() == []

# """
# Given you add more songs
# Return more than one song in list 
# """
# track = music_tracker(list)
# track.add("let it go!")
# track.view_list() => list = ["let it go!"]

# track.add("Hakuna matata")
# track.view_list() => list = ["let it go!", "Hakuna matata"]
    
def test_adding_more_songs():
    track = music_tracker()
    track.add("Let it go!")
    track.add("Hakuna matata")
    assert track.view_list() == ["Let it go!","Hakuna matata"]