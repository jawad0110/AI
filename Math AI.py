import tkinter as tk
import speech_recognition as sr
import pyttsx3
import sympy as sp

#The Calculator
class Calculator:
    def __init__(self):
        self.engine = pyttsx3.init()

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return self.say("Error: Cannot divide by zero.")

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Algebraic functions
    def solve_algebraic_equation(self, user_question):
        # Define the variable
        x = sp.symbols('x')

        # Create the equation object
        equation = sp.Eq(sp.sympify(user_question), 0)

        # Solve the equation
        result = sp.solve(equation, x)
        
        result_str = str(result).replace('-', ' minus ')

        # Print the solutions
        response = f"The solution is {result_str}"
        self.say(response)
        return response
    
# Plus, minus, multiply and divide functions
    def solve_math_question(self, user_question):
        
        # Initialize variables
        num1 = ""
        num2 = ""
        operator = ""

        # Iterate through the characters in the input
        for char in user_question:
            if char.isdigit() or char == '.':
                # Append to the current number being parsed
                if operator == "":
                    num1 += char
                else:
                    num2 += char
            elif char in ['+', '-', '*', '/']:
                # Set the operator
                operator = char
                
            elif char == '-':
                # If the character is '-', replace it with "minus"
                operator = 'minus'
                num1 += ' '  # Add a space to separate "minus" from the number

        try:
            # Convert the parsed strings to numbers
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            return self.say("Error: Invalid numbers in the question.")

        # Perform the operation
        if operator == '+':
            result = self.add(num1, num2)
        elif operator == '-':
            result = self.subtract(num1, num2)
        elif operator == '*':
            result = self.multiply(num1, num2)
        elif operator == '/':
            result = self.divide(num1, num2)
        else:
            return self.say("Error: Invalid operator. Please use '+', '-', '*', or '/'.")

        response = f"The solution is {result}"
        self.say(response)
        return response


# Example usage
def usage():
    if __name__ == "__main__":
        calculator = Calculator()

        # Get user question through voice input
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            calculator.say("Speak your math question:")
            audio = recognizer.listen(source)

        try:
            user_question = recognizer.recognize_google(audio)
            
            if 'x' in user_question:
                calculator.solve_algebraic_equation(user_question)
                
            else:
                # Solve the math question and provide the answer in voice
                calculator.solve_math_question(user_question)

        except sr.UnknownValueError:
            calculator.say("Sorry, I could not understand your question.")
        except sr.RequestError as e:
            calculator.say(f"Could not request results from Google Speech Recognition service; {e}")


#The GUI
def on_button_click():
    label.config(text="Done!")
    usage()  # Call the imported function

# Create the main window
window = tk.Tk()

# Set the window title
window.title("AI Calculator")

# Set the window size
window.geometry("400x300")

# Add a label to the window
label = tk.Label(window, text="AI Calculator")
label.pack(pady=20)

# Add a button to the window
button = tk.Button(window, text="Start", command=on_button_click)
button.pack()

# Run the main loop
window.mainloop()
