import re 

def prepocess_text(text:str)->str:

   text=text.lower()

   text=" ".join(text.split())

   text= re.sub(r"[^\w\s]","",text)

   return text
