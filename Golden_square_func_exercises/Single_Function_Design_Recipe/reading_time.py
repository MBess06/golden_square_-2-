'''
As a user
So that I can manage my time
I want to see an estimate of reading time for a text,
assuming that I can read 200 words a minute.
'''

def reading_time(text_len):
    if text_len is None:
        raise Exception("No text length given. 0 minutes")
    time = text_len / 200
    result = round(time)
    return f"It will take {result} minutes to read this text"