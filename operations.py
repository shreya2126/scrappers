import json  
data=json.load(open("quotes.json"))
new=json.dumps(data)
for obj in data:
     
     print(obj['image'],("  "),obj["say"],("  "),obj["author"]) 
     print("\n")
     print("******")
     print("\n")
     
