
from .preprocessing import tokenize


STOP_WORDS = {
    "i", "am", "the", "a", "an",
    "is", "are", "to", "my", "me",
    "please", "can", "could", "would",
    "you", "do", "does", "it", "this",
    "that", "of", "for", "in", "on",
    "with", "have", "what", "your"
}


SYNONYMS = {
    # Password-related words
    "forgot": "forgot",
    "forgotten": "forgot",
    "forget": "forgot",
    "lost": "forgot",

    # Login-related words
    "login": "login",
    "signin": "login",
    "sign": "login",
    "signing": "login",

    # Problem-related words
    "problem": "problem",
    "issue": "problem",
    "error": "problem",
    "failure": "problem",

    # Support-related words
    "help": "support",
    "support": "support",
    "agent": "support",
    "human": "support",

    # Ticket-related words
    "ticket": "ticket",
    "request": "ticket",

    # Working-hours-related words
    "working": "working",
    "available": "working",
    "open": "working"
}


def remove_stop_words(tokens: list[str]) -> list[str]:


    return [
        token
        for token in tokens
        if token not in STOP_WORDS
    ]


def normalize_synonyms(tokens: list[str]) -> list[str]:


    return [
        SYNONYMS.get(token, token)
        for token in tokens
    ]


def preprocess(text: str) -> list[str]:


    tokens = tokenize(text)

    tokens = remove_stop_words(tokens)

    tokens = normalize_synonyms(tokens)

    return tokens
