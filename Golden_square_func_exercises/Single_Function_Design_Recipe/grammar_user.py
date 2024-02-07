def check_grammar(text):
    if isinstance(text, str) == False or text == "":
        return "No text provided."
    elif text.capitalize() in text and any(c in ".?!" for c in text):
        return True
    else:
        return False 


