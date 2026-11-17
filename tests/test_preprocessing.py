
from app.chatbot.preprocessing import clean_text, tokenize
from app.chatbot.nlp import (
    remove_stop_words,
    normalize_synonyms,
    preprocess
)


def test_clean_text_lowercase():
    assert clean_text("HELLO") == "hello"


def test_clean_text_punctuation():
    assert clean_text("Hello!!!") == "hello"


def test_clean_text_extra_spaces():
    assert clean_text("hello    world") == "hello world"


def test_tokenize():
    assert tokenize("hello world") == ["hello", "world"]


def test_tokenize_empty_text():
    assert tokenize("   ") == []


def test_remove_stop_words():
    tokens = ["i", "forgot", "my", "password"]

    assert remove_stop_words(tokens) == ["forgot", "password"]


def test_normalize_synonyms():
    tokens = ["forgotten", "issue", "agent"]

    assert normalize_synonyms(tokens) == [
        "forgot",
        "problem",
        "support"
    ]


def test_preprocess():
    result = preprocess("I have a problem signing in!")

    assert result == ["problem", "login"]
