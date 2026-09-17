from app.chatbot.engine import msg_process


def test_greeting():
   result=msg_process("Hello")
   assert result["intent"] == "greeting"

def test_password_reset():
   result=msg_process("I forgot my password")
   assert result["intent"]=="password_reset"

def test_login_problem():
   result=msg_process("I cannot login")
   assert result["intent"]=="login_problem"

def test_unknown_message():
   result=msg_process("What is weather")
   assert result["intent"]=="unknown"

   