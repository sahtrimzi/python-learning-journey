marks ={
    "syed ali haider":90,
    "umar":85,
    "saif":88,
    "faizan":87,
    "hassan":82,
}
print(marks.items())  # print the items of the dictionary
print(marks.values()) # print the values of the dictionary
print(marks.keys())   # print the keys of the dictionary
marks.update({"syed ali haider":95})
print(marks)          # update the value of the key "syed ali haider"
print(marks.get("syed ali haider")) #print the value of the key "syed ali haider"

