# spam filter of sms using using 'or'

comment = input("Enter the comment: ")

if ("Make a lot of money" in comment or 
    "buy now" in comment or 
    "subscribe this" in comment or 
    "click this" in comment):
    print("This comment is a spam")
else:
    print("This comment is not a spam")