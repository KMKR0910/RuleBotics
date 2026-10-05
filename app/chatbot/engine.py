from .rules import RULES
from .intents import UNKNOWN
from .preprocessing import prepocess_text
from rapidfuzz.fuzz import ratio


def cal_score_keyword(
    message_tokens: list[str],
    keywords: dict[str, float]
) -> float:

    message_text = " ".join(message_tokens)
    best_score = 0.0

    for keyword, weight in keywords.items():

        keyword_tokens = prepocess_text(keyword)
        keyword_text = " ".join(keyword_tokens)

        # Exact match
        if message_text == keyword_text:
            score = weight

        # Keyword/phrase exists inside the message
        elif keyword_text in message_text:
            score = weight * 0.95

        # Fuzzy matching
        else:
            similarity = ratio(
                message_text,
                keyword_text
            ) / 100

            score = similarity * weight

        if score > best_score:
            best_score = score

    return round(best_score, 2)
   
def intent_detect(message:str)->dict:

   message_tokens= prepocess_text(message)

   best_intent= UNKNOWN
   best_score=0.0

   for intent, rule in RULES.items():
      keywords=rule["keywords"]

      score=cal_score_keyword(message,keywords)

      if score>best_score:
         best_score=score
         best_intent=intent

   if best_score<0.7:
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

