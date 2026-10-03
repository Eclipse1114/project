import streamlit as st
import random

st.markdown("""
  <style>
    .stApp {
      background-color: rgb(250, 100, 170);
      color: blue;
    }

    button {
      background-color: rgb(140, 165, 235) !important;
      color: black !important;
    }

    .stAppHeader {
      visibility: hidden;
    }

    .stAppToolbar {
      visibility: visible;
    }
  </style>
""", unsafe_allow_html=True)

st.set_page_config(
  page_title="Maria's app"
)

truths = [
    "What's the most embarrassing thing you've done recently?",
    "What's a weird habit you have that almost nobody knows about?",
    "What's the dumbest thing you've ever argued about?",
    "What's a food you absolutely refuse to eat?",
    "What's the weirdest thing you've ever Googled?",
    "What's a song you're embarrassed to admit you like?",
    "What's the most useless talent you have?",
    "What's the strangest dream you remember having?",
    "What's something you've always wanted to try?",
    "What's the funniest misunderstanding you've ever had?",
    "What's the last thing that made you laugh really hard?",
    "What's a fictional character you would absolutely hate to live with?",
    "What's the weirdest nickname you've ever had?",
    "What's something you believed as a kid that turned out to be completely false?",
    "What's your most irrational fear?",
    "What's the most chaotic thing you've done because you were bored?",
    "What's one thing you're surprisingly good at?",
    "What's the worst haircut you've ever had?",
    "What's the most embarrassing autocorrect you've ever sent?",
    "What's something you could talk about for hours?",
    "What's the strangest compliment you've ever received?",
    "What's a popular thing that you just don't understand the hype around?",
    "What's the most childish thing you still enjoy?",
    "What's one thing on your bucket list?",
    "If you could instantly master one skill, what would it be?"
]

dares = [
    "Send a picture of the closest object to you right now.",
    "Change your profile picture to something ridiculous for 10 minutes.",
    "Send the next message using only emojis.",
    "Try to say the alphabet backwards.",
    "Send a voice message saying something completely random in your most dramatic voice.",
    "Draw a cat in under 30 seconds and send it.",
    "Send a picture of your current view.",
    "Type a sentence with your eyes closed and send whatever you typed.",
    "Speak in an exaggerated accent for your next three messages.",
    "Send a picture of the weirdest object within reach.",
    "Make up a completely fake fact and try to convince me it's real.",
    "Write a five-word story and send it.",
    "Send a voice message humming the first song that comes to mind.",
    "Balance something harmless on your head for 10 seconds.",
    "Describe what you're doing like you're narrating a nature documentary.",
    "Use your non-dominant hand to write your name and send a picture.",
    "Send a message where every word starts with the same letter.",
    "Make up a terrible superhero and explain their power.",
    "Try to make me laugh using only one sentence.",
    "Take a completely normal object and give it an absurd name.",
    "Send three emojis that describe your day and explain them.",
    "Invent a ridiculous conspiracy theory about an everyday object.",
    "Try to draw yourself from memory without looking at yourself.",
    "Write a dramatic two-sentence obituary for a fictional character.",
    "For your next message, talk like an overly dramatic movie villain."
]

message = "Press Truth to reveal something about yourself, or Dare to test your luck with a challenge!"

with st.container(horizontal=True, gap="small"):
    truth = st.button("Truth")
    dare = st.button("Dare")

if truth:
    message = random.choice(truths)

elif dare:
    message = random.choice(dares)

st.write(message)
