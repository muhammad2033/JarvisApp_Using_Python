import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib



# Import necessary libraries
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class JarvisApp(App):
    def __init__(self, **kwargs):
        super(JarvisApp, self).__init__(**kwargs)
        self.query_input = None
        self.output_label = None

    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a label for output
        self.output_label = Label(text="Jarvis: Hello!", font_size=20)
        layout.add_widget(self.output_label)

        # Create a text input for user queries
        self.query_input = TextInput(font_size=20, multiline=False)
        layout.add_widget(self.query_input)

        # Create a button to trigger user queries
        query_button = Button(text="Ask Jarvis", on_press=self.process_query)
        layout.add_widget(query_button)

        # Schedule the initial wishMe function
        Clock.schedule_once(self.wish_me, 0)

        return layout

    def wish_me(self, dt):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.output_label.text = "Jarvis: Good Morning!"
        elif 12 <= hour < 18:
            self.output_label.text = "Jarvis: Good Afternoon!"
        else:
            self.output_label.text = "Jarvis: Good Evening!"
        self.output_label.text += "\nJarvis: How may I help you?"

    def process_query(self, instance):
        # Get user input from the text input
        query = self.query_input.text.lower()

        # Process the query
        if 'wikipedia' in query:
            self.output_label.text = "Jarvis: Searching Wikipedia..."
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            self.output_label.text = f"Jarvis: According to Wikipedia\n{results}"
            speak(results)
        # Add more query processing here...

    def speak(self, audio):
        # Implement the speak function as in your original code
        engine.say(audio)
        engine.runAndWait()



if __name__ == "__main__":
    JarvisApp().run()
