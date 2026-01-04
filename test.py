def clean_text(text):
    special = "!.,()?"
    text = text.replace("/", " ")

    for i in special:
        text = text.replace(i, "")
    return text.lower().split(" ")
        
            

test = clean_text("Customer! Support Agent (Remote)")
print(test)