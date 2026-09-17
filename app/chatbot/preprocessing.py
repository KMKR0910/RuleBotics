import re 

def prepocess_text(text:str)->str:

   text=text.lower()

   text=" ".join(text.split())

   text= re.sub(r"[^\w\s]","",text)

   return text


def tokenize(text:str)-> list[str]:
   text=prepocess_text(text)
   return text.split()