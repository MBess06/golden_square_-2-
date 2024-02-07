def make_snippet(string):
    diary = string.split()
    if len(diary) > 5 :
        five = diary[:5]
        return f"{' '.join(five)} ..."
    else:
        return string