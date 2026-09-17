from .preprocessing import tokenize

STOP_WORDS = {
    "i",
    "am",
    "the",
    "a",
    "an",
    "is",
    "are",
    "to",
    "my",
    "me",
    "please",
    "can",
    "could",
    "would",
    "you",
    "do",
    "does",
    "it",
    "this",
    "that",
    "of",
    "for",
    "in",
    "on",
    "with"
}

def remove_stop_words(tokens:list[str])->list[str]:

   return [
      token
      for token in tokens
      if token not in STOP_WORDS
   ]


SYNONYMS = {

    "forgot": "forgot",
    "forgotten": "forgot",
    "forget": "forgot",
    "lost": "forgot",

    "login": "login",
    "signin": "login",
    "sign": "login",

    "problem": "problem",
    "issue": "problem",
    "error": "problem",
    "failure": "problem",

    "help": "support",
    "support": "support",
    "agent": "support",
    "human": "support",

    "ticket": "ticket",
    "request": "ticket",

    "working": "working",
    "available": "working",
    "open": "working"
}


def normalize_synonyms(tokens:list[str])->list[str]:

    normalized_tokens=[]

    for token in tokens:

      normalized_token=SYNONYMS.get(
         token,
         token
      )

      normalized_tokens.append(normalized_token)

    return normalized_tokens


def preprocess(text:str)->list[str]:

   tokens=tokenize(text)

   tokens=remove_stop_words(tokens)

   tokens=normalize_synonyms(tokens)

   return tokens