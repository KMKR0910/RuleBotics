from .rules import RULES
from .intents import UNKNOWN
from .preprocessing import prepocess_text


def cal_score_keyword(message:str, keywords:list[str])->float:


   matched_keywords=0

   for keyword in keywords:
      keyword= prepocess_text(keyword)

      if keyword in message:
         matched_keywords +=1

   if len(keyword)==0:
      return 0.0

   
   return matched_keywords/len(keyword)

def intent_detect(message:str)->dict:

   message= prepocess_text(message)

   best_intent= UNKNOWN
   best_score=0.0

   for intent, rule in RULES.items():
      keywords=rule["keywords"]

      score=cal_score_keyword(message,keywords)

      if score>best_score:
         best_score=score
         best_intent=intent

      
   return{
      "intent":best_intent,
      "confidence":round(best_score,2)
   }

def generate_response(intent:str)-> str:

   if intent in RULES:
      return RULES[intent]["response"]

   return(
      "I don't understand your question."
      "Please kindly explain your question diffrently."
   )

def msg_process(message:str)->dict:

   result=intent_detect(message)

   intent = result["intent"]
   confidence= result["confidence"]

   response= generate_response(intent)

   return{
      "intent":intent,
      "confidence":confidence,
      "response":response
   }

