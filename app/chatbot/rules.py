from .intents import (
   GREETING,
   PASSWORD_RESET,
   LOGIN_PROBLEM,
   TICKET_CREATE,
   TICKET_STATUS,
   HUMAN_SUPPORT,
   GOODBYE, SYSTEM_ERROR,
   WORKING_HOURS
)

RULES = {

   GREETING:{
      "keywords":[
         "hello",
         "hi",
         "hey",
         "good morning"
         "good afternoon",
         "good evening"
      ],
      "response" :"Hello! How can I help you"
   },

   PASSWORD_RESET:{
      "keywords":[
      "forgot pw",
      "forgot password",
      "reset password",
      "password forgot",
      "password forgotten",
      "lost pw",
      "lost password",
      "change pw",
      "change password"

      ],
      "response":"You can reset your password from the account settings"
      },
      LOGIN_PROBLEM:{
         "keywords":[
            "can not login",
            "can't login",
            "cant login",
            "login failed",
            "lgin not corrected",
            "unable to login",

         ],
         "response":("Kindly please check your username and password."
         "If stil problen occured, Add a support ticket.")
      },

      SYSTEM_ERROR:{
         "keywords":[
            "error in system",
            "system error",
            "app error",
            "application not support",
            "application error",
            "app is not working",
            "web app isnt working",
            "web app is not working"
            "web app not support",
            "application error",
            
         ],
         "response":(
            "You're experincing a system problem "
            "I can help you to create a support ticket."

         )
      },

      WORKING_HOURS:{
         "keywords":[
            "working hours",
            "operating hours"
            "office hours",
            "support hours",
            "working hour",
            "opening hours",
            "opening hour",
            "what time are you open",
            "when are you open",
            "what is ofiice time",
            
         ],
         "response":(
            "Our help desk support team is avaliable from "
            "9:30 AM to 5:30 PM, Monday to Sunday"
         )
      },
      HUMAN_SUPPORT:{
         "keywords":[
            "human",
            "In person",
            "person",
            "agent",
            "support staff",
            "talk to someone",
            "talk to person",
            "human support",
            
         ],
         "response":(
            "Sure,I can contact to support agent to solve your problem"
         )
      },

      GOODBYE:{
         "keywords":[
            "bye",
            "goddbye",
            "good bye",
            "see you",
            "see you again",
            "see you later"
         ],
         "response":(
            "Goodbye! Have a nice day. "
         )
      }
}