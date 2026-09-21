from .intents import (
    GREETING,
    PASSWORD_RESET,
    LOGIN_PROBLEM,
    TICKET_CREATE,
    TICKET_STATUS,
    HUMAN_SUPPORT,
    GOODBYE,
    SYSTEM_ERROR,
    WORKING_HOURS,
    THANKYOU
)


RULES = {

    GREETING: {
        "keywords": {
            "hello": 1.0,
            "hi": 1.0,
            "hey": 1.0,
            "good morning": 1.0,
            "good afternoon": 1.0,
            "good evening": 1.0,
            "morning": 0.9,
            "afternoon": 0.9,
            "evening": 0.9,
            "hello rulebotics": 1.0
        },
        "response": "Hello! How can I help you?"
    },


    PASSWORD_RESET: {
        "keywords": {
            "forgot pw": 1.0,
            "forgot password": 1.0,
            "forgot my password": 1.0,
            "reset password": 1.0,
            "password forgot": 0.9,
            "password forgotten": 1.0,
            "lost pw": 1.0,
            "lost password": 1.0,
            "change pw": 0.9,
            "change password": 1.0,
            "lose password": 0.8,
            "loses pw": 0.8
        },
        "response": (
            "You can reset your password from the account settings."
        )
    },


    LOGIN_PROBLEM: {
        "keywords": {
            "cannot login": 1.0,
            "can not login": 1.0,
            "can't login": 1.0,
            "cant login": 1.0,
            "login failed": 1.0,
            "login problem": 1.0,
            "login issue": 1.0,
            "login not working": 1.0,
            "unable to login": 1.0,
            "cant access the login": 0.9
        },
        "response": (
            "Kindly check your username and password. "
            "If the problem still occurs, add a support ticket."
        )
    },


    SYSTEM_ERROR: {
        "keywords": {
            "error in system": 1.0,
            "system error": 1.0,
            "app error": 1.0,
            "application not support": 0.9,
            "application error": 1.0,
            "app is not working": 1.0,
            "web app isnt working": 1.0,
            "web app is not working": 1.0,
            "web app not support": 0.9,
            "error in application": 1.0
        },
        "response": (
            "You're experiencing a system problem. "
            "I can help you create a support ticket."
        )
    },


    WORKING_HOURS: {
        "keywords": {
            "working hours": 1.0,
            "operating hours": 1.0,
            "office hours": 1.0,
            "support hours": 1.0,
            "working hour": 0.9,
            "opening hours": 1.0,
            "opening hour": 0.9,
            "what time are you open": 1.0,
            "when are you open": 1.0,
            "what is office time": 1.0
        },
        "response": (
            "Our help desk support team is available from "
            "9:30 AM to 5:30 PM, Monday to Sunday."
        )
    },


    HUMAN_SUPPORT: {
        "keywords": {
            "human": 1.0,
            "in person": 1.0,
            "person": 0.9,
            "agent": 1.0,
            "support staff": 1.0,
            "talk to someone": 1.0,
            "talk to person": 1.0,
            "human support": 1.0
        },
        "response": (
            "Sure, I can connect you with a support agent "
            "to help solve your problem."
        )
    },


    GOODBYE: {
        "keywords": {
            "bye": 1.0,
            "goodbye": 1.0,
            "good bye": 1.0,
            "see you": 1.0,
            "see you again": 1.0,
            "see you later": 1.0
        },
        "response": (
            "Goodbye! Have a nice day."
        )
    },


    THANKYOU: {
        "keywords": {
            "thanks": 1.0,
            "thanks for your help": 1.0,
            "thank for your support": 1.0,
            "thank": 0.9,
            "thank for support": 1.0
        },
        "response": (
            "You're welcome! Come again if you need any support."
        )
    },


    TICKET_CREATE: {
        "keywords": {
            "create ticket": 1.0,
            "open ticket": 1.0,
            "new ticket": 1.0,
            "raise ticket": 1.0,
            "submit ticket": 1.0,
            "create a support ticket": 1.0
        },
        "response": (
            "Sure, I can help you create a support ticket."
        )
    },


    TICKET_STATUS: {
        "keywords": {
            "ticket status": 1.0,
            "check ticket": 1.0,
            "ticket progress": 1.0,
            "ticket update": 1.0,
            "status of my ticket": 1.0
        },
        "response": (
            "Please provide your ticket number so I can check "
            "the status of your ticket."
        )
    }

}