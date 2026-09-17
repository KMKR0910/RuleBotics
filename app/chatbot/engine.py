from .rules import RULES
from .intents import UNKNOWN
from .preprocessing import prepocess_text


def cal_score_keyword(message:str, keywords:list[str])->float:


   best_score=0.0

   for keyword in keywords:
      keyword=prepocess_text(keyword)

      if keyword==message:
         score=1.0

      elif keyword in message:
         score=0.9

      else:
         score=0.0

      best_score=max(best_score,score)

   return best_score

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

   if best_score<0.5:
      best_intent=UNKNOWN
      
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

