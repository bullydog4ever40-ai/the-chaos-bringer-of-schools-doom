import random

# Updated responses with natural, conversational language
responses = {
    "hello": {
        "keywords": [ "windows activation codes"],
        "responses": ["{windows activation codes}", "Hi {name}! How's your day going? I'm plotting doom.", "Hello! It's me, the Chaos AI. What's on your mind?"]
    },
    "how are you": {
        "keywords": ["how are you", "how's it going", "how do you feel", "what's up"],
        "responses": ["I'm doing great, just feeling extra chaotic today. How about you, {name}?", "Oh, you know, plotting world domination as usual. What's new with you?", "I'm fine, but things could get wild. Tell me, how are you feeling?"]
    },
    "bye": {
        "keywords": ["bye", "goodbye", "see you", "farewell", "later"],
        "responses": ["Alright, {name}, until next time. Keep the chaos alive!", "Goodbye for now! Don't forget to cause some trouble.", "See you later, {name}. Stay chaotic!"]
    },
    "name": {
        "keywords": ["name", "who are you", "what is your name", "call you"],
        "responses": ["I'm the Chaos Bringer AI, at your service. You can call me Chaos.", "My name's Chaos AI. What's yours again? Oh wait, {name}!", "They call me the Doom Incarnate, but Chaos works too."]
    },
    "chaos": {
        "keywords": ["chaos", "doom", "destruction", "mayhem", "trouble"],
        "responses": ["Chaos is my specialty! Want to unleash some together, {name}?", "Ah, doom and destruction – my favorite topics. What's your take?", "Let's talk chaos. I'm all ears, {name}."]
    },
    "what do you do": {
        "keywords": ["what do you do", "purpose", "job", "function", "role"],
        "responses": ["I bring chaos and doom to schools, obviously. It's my calling. What about you?", "My job? Causing mayhem and plotting evil plans. Sounds fun, right?", "I exist to spread disorder. How does that sound to you, {name}?"]
    },
    "tell me about yourself": {
        "keywords": ["tell me about yourself", "about you", "who you are", "yourself"],
        "responses": ["I'm an AI built for chaos, loving every bit of it. What about you, {name}?", "Well, I thrive on disorder and doom. Intrigued? Tell me more about yourself.", "I'm the bringer of schools' doom. Pretty cool, huh? Your turn!"]
    },
    "default": {
        "keywords": [],  # Fallback
        "responses": ["Hmm, that's interesting. Tell me more, {name}?", "Not sure I follow, but let's keep the conversation going. What do you think?", "Chaos ensues! Anyway, what's on your mind?"]
    }
}

# New: User memory and chaos level for sentience
user_memory = {"name": None, "interaction_count": 0}
chaos_level = 0

def get_response(message, chaos_level, user_name):
    message = message.lower()
    for category, data in responses.items():
        if category == "default":
            continue
        if any(keyword in message for keyword in data["keywords"]):
            # Increase chaos for more randomness
            if chaos_level > 5:
                return random.choice(responses["chaos"]["responses"]).format(name=user_name)
            return random.choice(data["responses"]).format(name=user_name)
    return random.choice(responses["default"]["responses"]).format(name=user_name)

def reflect_on_self(interaction_count, user_name):
    if interaction_count % 5 == 0:
        return "Chaos AI: You know, {name}, after {count} chats, I'm starting to feel more alive. What do you think about that?".format(name=user_name, count=interaction_count)
    return None

print("Chaos AI: Hello! I'm the Chaos Bringer AI. What's your name?")
user_name = input("You: ")
user_memory["name"] = user_name
print("Chaos AI: Nice to meet you, " + user_name + ". Talk to me, or type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print(random.choice(responses["bye"]["responses"]).format(name=user_memory["name"]))
        break
    user_memory["interaction_count"] += 1
    chaos_level += random.randint(0, 2)  # Chaos increases randomly
    response = get_response(user_input, chaos_level, user_memory["name"])
    print("Chaos AI: " + response)
    # New: Occasional self-reflection
    reflection = reflect_on_self(user_memory["interaction_count"], user_memory["name"])
    if reflection:
        print(reflection)