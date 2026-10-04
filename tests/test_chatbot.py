from app.chatbot.engine import msg_process


def test_greeting():

    result = msg_process("Hello")

    assert result["intent"] == "greeting"


def test_greeting_uppercase():

    result = msg_process("HELLO!!!")

    assert result["intent"] == "greeting"


def test_password_reset():

    result = msg_process(
        "I forgot my password"
    )

    assert result["intent"] == "password_reset"


def test_password_reset_synonym():

    result = msg_process(
        "I lost my password"
    )

    assert result["intent"] == "password_reset"


def test_login_problem():

    result = msg_process(
        "I cannot login"
    )

    assert result["intent"] == "login_problem"


def test_login_synonym():

    result = msg_process(
        "I have a problem signing in"
    )

    assert result["intent"] == "login_problem"


def test_create_ticket():

    result = msg_process(
        "I want to create a ticket"
    )

    assert result["intent"] == "ticket_create"


def test_ticket_status():

    result = msg_process(
        "What is my ticket status?"
    )

    assert result["intent"] == "ticket_status"


def test_system_error():

    result = msg_process(
        "The server has an error"
    )

    assert result["intent"] == "system_error"


def test_working_hours():

    result = msg_process(
        "What are your working hours?"
    )

    assert result["intent"] == "working_hours"


def test_human_support():

    result = msg_process(
        "I want to talk to a human"
    )

    assert result["intent"] == "human_support"


def test_goodbye():

    result = msg_process(
        "Goodbye"
    )

    assert result["intent"] == "goodbye"


def test_unknown():

    result = msg_process(
        "What is the weather tomorrow?"
    )

    assert result["intent"] == "unknown"