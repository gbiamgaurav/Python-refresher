
import os 
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

class NLPModel:
    def get_model(self):
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        return model
    
class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.first_menu()

    def first_menu(self):
        first_input = input("""
                            Hi! How would you like to proceed?
                            1. Not a member? Register
                            2. Already a member? Login
                            3. Bhai galti se aa gaya kya?Exit """)
        
        if first_input == "1":

            # Register
            self.__register() 
        elif first_input == "2":

            # Login
            self.__login()
        elif first_input == "3":

            print("Thank You for using our service!")
        else:
            exit()


    def second_menu(self):
        
        second_input = input("""
                                What do you want to do now?
                                1. Sentiment Analysis
                                2. Language Translation
                                3. Language Detection """)
        
        if second_input == "1":
            # Sentiment Analysis
            self.__sentiment_analysis()

        elif second_input == "2":
            self.__language_translation()

        elif second_input == "3":
            self.__language_detection()

        else:
            exit()


    def __register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.__database:
            print("Email already exists")
        else:
            self.__database[email] = [name, password]
            print("Registration successful. Now you can Login!")
            self.__database
            self.second_menu()

    def __login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login Successful")
                self.first_menu()
            else:
                print("Invalid credentials")
                self.__login()
        else:
            print("User email not found. Please register first.")
            self.first_menu()

    def __sentiment_analysis(self):
          user_text = input("Enter your text: ")
          model = super().get_model()
          response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
          result = response.text
          print(result) 
          self.second_menu()


    def __language_translation(self):
          user_text = input("Enter your text: ")
          user_language = input("Enter the language you want to translate into: ")
          user_language = user_language.lower()
          model = super().get_model()
          response = model.generate_content(f"Give me the translation of this sentence: {user_text} into {user_language}.")
          result = response.text
          print(result)
          self.second_menu() 


    def __language_detection(self):
          user_text = input("Enter your text: ")
          model = super().get_model()
          response = model.generate_content(f"Give me the language of this sentence: {user_text}")
          result = response.text
          print(result)
          self.second_menu() 



if __name__ == "__main__":
    app = NLPApp()