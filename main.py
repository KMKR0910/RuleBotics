from app.chatbot.engine import msg_process

def main():


   print()
   print("   RuleBotics Help Desk Chatbot")

   print("Type 'exit' to close the RuleBotics.")

   while True:

      user_input=input("You:")

      if user_input.lower().strip()=="exit":

         print("RuleBotics: Goodbye! See you again")
         break

      if not user_input.lower().strip():
         print("RuleBotics: Please enter a message.")
         continue

      result= msg_process(user_input)

      print(f"Intent :{result['intent']}")
      print(f"Confidence: {result['confidence']}")
      print()
      print(f"RuleBotics:{result['response']}")



if __name__ == "__main__":
   main()

            


            
