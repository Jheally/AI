# AI
Here it is:

Title: SwearJar Bot

Authors: Jharna Patel, Lucy Hartley

Date Due: May 21, 2026

Date Submitted: May 22, 2026

High Concept: A Raspberry Pi that listens for swear words, tracks how often they are said, and emails a report to the user.

Problem or Purpose: People often swear without realizing how much. This project tracks it automatically like a swear jar but without needing to put money in it.

Target User: Families, students, or anyone who wants to track their language habits.

Models Used: Google Speech Recognition for transcription. Claude by Anthropic for confirming swear words and predicting others the user likely says.

Local Inference Design: Audio recording and word matching runs on the Pi. Transcription and AI analysis are done over the internet through APIs.

Prompting and Logic: The Pi records audio, transcribes it, checks it against a swear word list with severity scores from 1 to 5, sends flagged words to Claude to confirm them, and logs the results. Claude also predicts other swear words the user probably says.

User Interaction: The user speaks near the mic. The terminal shows what was detected and the running score. Email reports are sent on a schedule.

How to Run: Install sounddevice, scipy, SpeechRecognition, and anthropic using pip. Add your Anthropic API key and Gmail App Password to the config section. Run swear_jar.py in Thonny or the terminal.

Hardware: Raspberry Pi 5, laptop for remote access, microphone.

What Works Well: Transcription is accurate in quiet environments. The severity scores make it more interesting than just counting. Claude correctly ignores false positives like the word shoot in a sports context.

Known Issues: Requires internet. Background noise causes errors. Whisper and PyTorch could not be installed on the Pi due to missing ARM builds so Google Speech Recognition was used instead.

Future Improvements: Add a web dashboard. Add text to speech so the Pi calls out swears out loud. Support multiple user profiles.

Honor Statement: This is our own original work. All outside help is listed below. Signed: Jharna Patel, Lucy Hartley.

AI Disclosure: Claude was used to help debug errors, rewrite code, and help write this document.

References: Anthropic docs, SpeechRecognition library docs, Raspberry Pi documentation, Gmail App Passwords guide.

Reflection: We spent about 1 to 2 weeks on this. The biggest challenge was getting speech recognition to work on the Pi. Whisper and PyTorch would not install due to missing ARM support so we switched to Google Speech Recognition which worked immediately. We learned how to record audio on a Pi, use the Claude API, and adapt when a plan does not work on the target hardware. 

I spent about 1–2 weeks working on this project. The biggest challenge was honestly getting the speech recognition stuff to actually work on the Raspberry Pi. At first I wanted to use Whisper with PyTorch because it would run more locally, but I kept running into installation errors and missing ARM builds on the Pi. I spent a long time trying random fixes and debugging before realizing it just was not going to work well on the hardware I had. Eventually I switched to Google Speech Recognition instead, and it worked almost immediately and was way more reliable.

Another issue I had was false positives where the program would think normal words were swear words. I used Claude to help check the context of detected words so it could ignore words that only sounded like swears or were used normally, like “shoot” during sports conversations. That made the results a lot more accurate.

I learned a lot from this project honestly. I learned how to record audio on a Raspberry Pi, work with APIs, use AI models inside a project, and debug Linux/Python package issues. I also learned that sometimes the original idea does not work exactly how you planned and you have to adapt and find another solution instead of wasting time forcing something that will not run on the device.


