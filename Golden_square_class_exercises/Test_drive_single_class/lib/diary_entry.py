import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entry must have title or contents")
        self.title = title
        self.contents = contents
        self.read_so_far = 0
        # Parameters:
        #   title: string
        #   contents: string
        

    def format(self):
        return f"{self.title}: {self.contents}"
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        

    def count_words(self):
        contents_ls = self.format().split()
        return len(contents_ls)
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Can read this under a minute")
        contents_words = self.contents.split()
        words_per_min = len(contents_words)/wpm
        result = math.ceil(words_per_min)
        return result
        
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        can_read = wpm * minutes
        words = self.contents.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0

        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + can_read
        chunk = words[chunk_start: chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk)
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
