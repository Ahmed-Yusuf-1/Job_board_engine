def clean_text(text):
    special = "!.,()?"

    for i in special:
        text = text.replace(i, "")
    return text.lower().split(" ")
        
            

test = clean_text("Customer! Support Agent (Remote)")
print(test)