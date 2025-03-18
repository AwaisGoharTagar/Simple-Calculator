import streamlit as st

def smart_calculator():
    st.title("🧮 Simple Calculator")
    
    # Operation selection
    operation = st.selectbox("Select an operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])
    
    # User input for numbers
    num1 = st.number_input("Enter first number:", format="%.2f")
    num2 = st.number_input("Enter second number:", format="%.2f")
    
    # Calculation logic
    result = None
    if st.button("Calculate"):
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (*)":
            result = num1 * num2
        elif operation == "Division (/)":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero!")
                
    # Display result
    if result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    smart_calculator()

# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Initialize session state for expression, history, memory, and toggle states
#     if "expression" not in st.session_state:
#         st.session_state.expression = ""
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     if "memory" not in st.session_state:
#         st.session_state.memory = 0
#     if "toggles" not in st.session_state:
#         st.session_state.toggles = {btn: False for btn in ["MC", "MR", "M+", "M-", "sin", "cos", "tan", "log", "sqrt", "x^y", "(", ")"]}
    
#     # Custom CSS for responsive calculator layout with colored buttons
#     st.markdown(
#         """
#         <style>
#             .calculator {
#                 display: grid;
#                 grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
#                 gap: 10px;
#                 width: 100%;
#                 max-width: 400px;
#                 margin: auto;
#                 padding: 20px;
#                 background-color: #282c34;
#                 border-radius: 10px;
#                 text-align: center;
#             }
#             .calc-btn {
#                 padding: 15px;
#                 font-size: 18px;
#                 font-weight: bold;
#                 color: white;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#                 text-align: center;
#             }
#             .calc-btn.number { background-color: #4CAF50; }
#             .calc-btn.operator { background-color: #FF9800; }
#             .calc-btn.function { background-color: #2196F3; }
#             .calc-btn.clear { background-color: #F44336; }
#             .calc-btn.active { background-color: #FFD700; }
#             .calc-btn:hover { opacity: 0.8; }
#             .stTextInput input {
#                 font-size: 24px;
#                 text-align: right;
#                 padding: 10px;
#                 width: 100%;
#             }
#             @media (max-width: 480px) {
#                 .calculator {
#                     grid-template-columns: repeat(4, 1fr);
#                 }
#             }
#         </style>
#         """, unsafe_allow_html=True
#     )
    
#     st.title("🧮 Advanced Smart Calculator")
    
#     # Display calculator screen
#     st.text_input("", st.session_state.expression, key="display", disabled=True)
    
#     # Calculator buttons with categories for coloring
#     buttons = [
#         ("MC", "function"), ("MR", "function"), ("M+", "function"), ("M-", "function"),
#         ("sin", "function"), ("cos", "function"), ("tan", "function"), ("log", "function"),
#         ("sqrt", "function"), ("x^y", "function"), ("(", "operator"), (")", "operator"), 
#         ("C", "clear"),("⌫", "function"),("/", "operator"),("*", "operator"),
#         ("7", "number"), ("8", "number"), ("9", "number"), ("-", "operator"),
#         ("4", "number"), ("5", "number"), ("6", "number"), ("+", "operator"),
#         ("1", "number"), ("2", "number"), ("3", "number"), ("=", "operator"), 
#         ("0", "number"), (".", "number")
#     ]
    
#     # Layout for calculator
#     cols = st.columns(4)
#     for i, (btn, category) in enumerate(buttons):
#         with cols[i % 4]:
#             btn_class = "calc-btn " + category + (" active" if st.session_state.toggles.get(btn, False) else "")
#             if st.button(btn, key=btn, help=btn, use_container_width=True):
#                 if btn in st.session_state.toggles:
#                     st.session_state.toggles[btn] = not st.session_state.toggles[btn]
#                 elif btn == "=":
#                     try:
#                         result = str(eval(st.session_state.expression))
#                         st.session_state.history.append(f"{st.session_state.expression} = {result}")
#                         st.session_state.expression = result
#                     except:
#                         st.session_state.expression = "Error"
#                 elif btn == "C":
#                     st.session_state.expression = ""
#                 elif btn == "⌫":  # Backspace button
#                     st.session_state.expression = st.session_state.expression[:-1]
#                 elif btn == "sqrt":
#                     st.session_state.expression = str(math.sqrt(float(st.session_state.expression)))
#                 elif btn == "x^y":
#                     st.session_state.expression += "**"
#                 elif btn == "sin":
#                     st.session_state.expression = str(math.sin(math.radians(float(st.session_state.expression))))
#                 elif btn == "cos":
#                     st.session_state.expression = str(math.cos(math.radians(float(st.session_state.expression))))
#                 elif btn == "tan":
#                     st.session_state.expression = str(math.tan(math.radians(float(st.session_state.expression))))
#                 elif btn == "log":
#                     st.session_state.expression = str(math.log10(float(st.session_state.expression)))
#                 elif btn == "M+":
#                     st.session_state.memory = float(st.session_state.expression)
#                 elif btn == "M-":
#                     st.session_state.memory = 0
#                 elif btn == "MR":
#                     st.session_state.expression += str(st.session_state.memory)
#                 elif btn == "MC":
#                     st.session_state.memory = 0
#                 else:
#                     st.session_state.expression += btn
    
#     # Display Calculation History
#     if st.session_state.history:
#         st.subheader("📜 Calculation History")
#         for entry in st.session_state.history[-5:]:
#             st.text(entry)

# if __name__ == "__main__":
#     smart_calculator()





# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Initialize session state for expression, history, and memory
#     if "expression" not in st.session_state:
#         st.session_state.expression = ""
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     if "memory" not in st.session_state:
#         st.session_state.memory = 0
    
#     # Custom CSS for calculator layout
#     st.markdown(
#         """
#         <style>
#             .calculator {
#                 display: grid;
#                 grid-template-columns: repeat(4, 1fr);
#                 gap: 10px;
#                 width: 320px;
#                 margin: auto;
#                 padding: 20px;
#                 background-color: #282c34;
#                 border-radius: 10px;
#                 text-align: center;
#             }
#             .calc-btn {
#                 padding: 15px;
#                 font-size: 18px;
#                 font-weight: bold;
#                 color: white;
#                 background-color: #4CAF50;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#                 text-align: center;
#             }
#             .calc-btn:hover {
#                 background-color: #45a049;
#             }
#             .stTextInput input {
#                 font-size: 24px;
#                 text-align: right;
#                 padding: 10px;
#             }
#         </style>
#         """, unsafe_allow_html=True
#     )
    
#     st.title("🧮 Advanced Smart Calculator")
    
#     # Display calculator screen
#     st.text_input("", st.session_state.expression, key="display", disabled=True)
    
#     # Calculator buttons
#     buttons = [
#         "MC", "MR", "M+", "M-",
#         "7", "8", "9", "/",
#         "4", "5", "6", "*",
#         "1", "2", "3", "-",
#         "0", ".", "=", "+",
#         "C", "(", ")", "⌫",
#         "sin", "cos", "tan", "log",
#         "sqrt", "x^y"
#     ]
    
#     # Layout for calculator
#     cols = st.columns(4)
#     for i, btn in enumerate(buttons):
#         with cols[i % 4]:
#             if st.button(btn, key=btn, help=btn, use_container_width=True):
#                 if btn == "=":
#                     try:
#                         result = str(eval(st.session_state.expression))
#                         st.session_state.history.append(f"{st.session_state.expression} = {result}")
#                         st.session_state.expression = result
#                     except:
#                         st.session_state.expression = "Error"
#                 elif btn == "C":
#                     st.session_state.expression = ""
#                 elif btn == "⌫":  # Backspace button
#                     st.session_state.expression = st.session_state.expression[:-1]
#                 elif btn == "sqrt":
#                     st.session_state.expression = str(math.sqrt(float(st.session_state.expression)))
#                 elif btn == "x^y":
#                     st.session_state.expression += "**"
#                 elif btn == "sin":
#                     st.session_state.expression = str(math.sin(math.radians(float(st.session_state.expression))))
#                 elif btn == "cos":
#                     st.session_state.expression = str(math.cos(math.radians(float(st.session_state.expression))))
#                 elif btn == "tan":
#                     st.session_state.expression = str(math.tan(math.radians(float(st.session_state.expression))))
#                 elif btn == "log":
#                     st.session_state.expression = str(math.log10(float(st.session_state.expression)))
#                 elif btn == "M+":
#                     st.session_state.memory = float(st.session_state.expression)
#                 elif btn == "M-":
#                     st.session_state.memory = 0
#                 elif btn == "MR":
#                     st.session_state.expression += str(st.session_state.memory)
#                 elif btn == "MC":
#                     st.session_state.memory = 0
#                 else:
#                     st.session_state.expression += btn
    
#     # Display Calculation History
#     if st.session_state.history:
#         st.subheader("📜 Calculation History")
#         for entry in st.session_state.history[-5:]:
#             st.text(entry)

# if __name__ == "__main__":
#     smart_calculator()



# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Initialize session state for expression, history, and memory
#     if "expression" not in st.session_state:
#         st.session_state.expression = ""
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     if "memory" not in st.session_state:
#         st.session_state.memory = 0
    
#     st.title("🧮 Advanced Smart Calculator")
    
#     # Display calculator screen
#     st.text_input("Expression", st.session_state.expression, key="display", disabled=True)
    
#     # Calculator buttons
#     buttons = [
#         "7", "8", "9", "/",
#         "4", "5", "6", "*",
#         "1", "2", "3", "-",
#         "0", ".", "=", "+",
#         "C", "(", ")", "⌫",
#         "sin", "cos", "tan", "log",
#         "sqrt", "x^y", "M+", "M-",
#         "MR", "MC"
#     ]
    
#     # Layout for calculator
#     cols = st.columns(4)
#     for i, btn in enumerate(buttons):
#         with cols[i % 4]:
#             if st.button(btn, key=btn):
#                 if btn == "=":
#                     try:
#                         result = str(eval(st.session_state.expression))
#                         st.session_state.history.append(f"{st.session_state.expression} = {result}")
#                         st.session_state.expression = result
#                     except:
#                         st.session_state.expression = "Error"
#                 elif btn == "C":
#                     st.session_state.expression = ""
#                 elif btn == "⌫":  # Backspace button
#                     st.session_state.expression = st.session_state.expression[:-1]
#                 elif btn == "sqrt":
#                     st.session_state.expression = str(math.sqrt(float(st.session_state.expression)))
#                 elif btn == "x^y":
#                     st.session_state.expression += "**"
#                 elif btn == "sin":
#                     st.session_state.expression = str(math.sin(math.radians(float(st.session_state.expression))))
#                 elif btn == "cos":
#                     st.session_state.expression = str(math.cos(math.radians(float(st.session_state.expression))))
#                 elif btn == "tan":
#                     st.session_state.expression = str(math.tan(math.radians(float(st.session_state.expression))))
#                 elif btn == "log":
#                     st.session_state.expression = str(math.log10(float(st.session_state.expression)))
#                 elif btn == "M+":
#                     st.session_state.memory = float(st.session_state.expression)
#                 elif btn == "M-":
#                     st.session_state.memory = 0
#                 elif btn == "MR":
#                     st.session_state.expression += str(st.session_state.memory)
#                 elif btn == "MC":
#                     st.session_state.memory = 0
#                 else:
#                     st.session_state.expression += btn
    
#     # Display Calculation History
#     if st.session_state.history:
#         st.subheader("📜 Calculation History")
#         for entry in st.session_state.history[-5:]:
#             st.text(entry)

# if __name__ == "__main__":
#     smart_calculator()



# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Initialize session state for expression, history, and dark mode
#     if "expression" not in st.session_state:
#         st.session_state.expression = ""
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     if "dark_mode" not in st.session_state:
#         st.session_state.dark_mode = False
    
#     # Dark Mode Toggle
#     st.session_state.dark_mode = st.checkbox("Dark Mode", value=st.session_state.dark_mode)
    
#     # Custom CSS for dark/light mode
#     dark_mode_style = """
#         <style>
#             body {background-color: #121212; color: white;}
#             .stTextInput input {background-color: #333; color: white;}
#             .calc-btn {background-color: #444; color: white;}
#             .calc-btn:hover {background-color: #666;}
#         </style>
#     """
#     light_mode_style = """
#         <style>
#             body {background-color: white; color: black;}
#             .stTextInput input {background-color: #fff; color: black;}
#             .calc-btn {background-color: #4CAF50; color: white;}
#             .calc-btn:hover {background-color: #45a049;}
#         </style>
#     """
    
#     if st.session_state.dark_mode:
#         st.markdown(dark_mode_style, unsafe_allow_html=True)
#     else:
#         st.markdown(light_mode_style, unsafe_allow_html=True)
    
#     st.title("🧮 Smart Calculator")
    
#     # Display calculator screen
#     st.text_input("Expression", st.session_state.expression, key="display", disabled=True)
    
#     # Calculator buttons
#     buttons = [
#         "7", "8", "9", "/",
#         "4", "5", "6", "*",
#         "1", "2", "3", "-",
#         "0", ".", "=", "+",
#         "C"
#     ]
    
#     # Layout for calculator
#     cols = st.columns(4)
#     for i, btn in enumerate(buttons):
#         with cols[i % 4]:
#             if st.button(btn, key=btn):
#                 if btn == "=":
#                     try:
#                         result = str(eval(st.session_state.expression))
#                         st.session_state.history.append(f"{st.session_state.expression} = {result}")
#                         st.session_state.expression = result
#                     except:
#                         st.session_state.expression = "Error"
#                 elif btn == "C":
#                     st.session_state.expression = ""
#                 else:
#                     st.session_state.expression += btn
    
#     # Display Calculation History
#     if st.session_state.history:
#         st.subheader("📜 Calculation History")
#         for entry in st.session_state.history[-5:]:
#             st.text(entry)

# if __name__ == "__main__":
#     smart_calculator()


# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Initialize session state for expression, history, and dark mode
#     if "expression" not in st.session_state:
#         st.session_state.expression = ""
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     if "dark_mode" not in st.session_state:
#         st.session_state.dark_mode = False
    
#     # Dark Mode Toggle
#     st.session_state.dark_mode = st.checkbox("Dark Mode", value=st.session_state.dark_mode)
    
#     # Custom CSS for dark/light mode
#     dark_mode_style = """
#         <style>
#             body {background-color: #121212; color: white;}
#             .stTextInput input {background-color: #333; color: white;}
#             .calc-btn {background-color: #444; color: white;}
#             .calc-btn:hover {background-color: #666;}
#         </style>
#     """
#     light_mode_style = """
#         <style>
#             body {background-color: white; color: black;}
#             .stTextInput input {background-color: #fff; color: black;}
#             .calc-btn {background-color: #4CAF50; color: white;}
#             .calc-btn:hover {background-color: #45a049;}
#         </style>
#     """
    
#     if st.session_state.dark_mode:
#         st.markdown(dark_mode_style, unsafe_allow_html=True)
#     else:
#         st.markdown(light_mode_style, unsafe_allow_html=True)
    
#     st.title("🧮 Smart Calculator")
    
#     # Display calculator screen
#     st.text_input("Expression", st.session_state.expression, key="display", disabled=True)
    
#     # Calculator buttons
#     buttons = [
#         "7", "8", "9", "/",
#         "4", "5", "6", "*",
#         "1", "2", "3", "-",
#         "0", ".", "=", "+",
#         "C"
#     ]
    
#     # Layout for calculator
#     cols = st.columns(4)
#     for i, btn in enumerate(buttons):
#         with cols[i % 4]:
#             if st.button(btn, key=btn):
#                 if btn == "=":
#                     try:
#                         result = str(eval(st.session_state.expression))
#                         st.session_state.history.append(f"{st.session_state.expression} = {result}")
#                         st.session_state.expression = result
#                     except:
#                         st.session_state.expression = "Error"
#                 elif btn == "C":
#                     st.session_state.expression = ""
#                 else:
#                     st.session_state.expression += btn
    
#     # Display Calculation History
#     if st.session_state.history:
#         st.subheader("📜 Calculation History")
#         for entry in st.session_state.history[-5:]:
#             st.text(entry)

# if __name__ == "__main__":
#     smart_calculator()


# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Custom CSS for calculator layout
#     st.markdown(
#         """
#         <style>
#             .calculator {
#                 display: grid;
#                 grid-template-columns: repeat(4, 1fr);
#                 gap: 10px;
#                 width: 300px;
#                 margin: auto;
#                 padding: 20px;
#                 background-color: #282c34;
#                 border-radius: 10px;
#                 text-align: center;
#             }
#             .calc-btn {
#                 padding: 15px;
#                 font-size: 18px;
#                 font-weight: bold;
#                 color: white;
#                 background-color: #4CAF50;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#             }
#             .calc-btn:hover {
#                 background-color: #45a049;
#             }
#             .stTextInput input {
#                 font-size: 20px;
#                 text-align: center;
#             }
#         </style>
#         """, unsafe_allow_html=True
#     )
    
#     st.title("🧮 Smart Calculator")
    
#     # Initialize session state for expression and history
#     if "expression" not in st.session_state:
#         st.session_state.expression = ""
#     if "history" not in st.session_state:
#         st.session_state.history = []
    
#     # Display calculator screen
#     st.text_input("Expression", st.session_state.expression, key="display", disabled=True)
    
#     # Calculator buttons
#     buttons = [
#         "7", "8", "9", "/",
#         "4", "5", "6", "*",
#         "1", "2", "3", "-",
#         "0", ".", "=", "+",
#         "C"
#     ]
    
#     # Layout for calculator
#     cols = st.columns(4)
#     for i, btn in enumerate(buttons):
#         with cols[i % 4]:
#             if st.button(btn, key=btn):
#                 if btn == "=":
#                     try:
#                         result = str(eval(st.session_state.expression))
#                         st.session_state.history.append(f"{st.session_state.expression} = {result}")
#                         st.session_state.expression = result
#                     except:
#                         st.session_state.expression = "Error"
#                 elif btn == "C":
#                     st.session_state.expression = ""
#                 else:
#                     st.session_state.expression += btn
    
#     # Display Calculation History
#     if st.session_state.history:
#         st.subheader("📜 Calculation History")
#         for entry in st.session_state.history[-5:]:
#             st.text(entry)
    
#     # Dark Mode Toggle
#     if st.checkbox("Dark Mode"):
#         st.markdown('<style>body {background-color: #121212; color: white;}</style>', unsafe_allow_html=True)

# if __name__ == "__main__":
#     smart_calculator()


# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Custom CSS for calculator layout
#     st.markdown(
#         """
#         <style>
#             .calculator {
#                 display: grid;
#                 grid-template-columns: repeat(4, 1fr);
#                 gap: 10px;
#                 width: 300px;
#                 margin: auto;
#                 padding: 20px;
#                 background-color: #282c34;
#                 border-radius: 10px;
#                 text-align: center;
#             }
#             .calc-btn {
#                 padding: 15px;
#                 font-size: 18px;
#                 font-weight: bold;
#                 color: white;
#                 background-color: #4CAF50;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#             }
#             .calc-btn:hover {
#                 background-color: #45a049;
#             }
#             .stTextInput input {
#                 font-size: 20px;
#                 text-align: center;
#             }
#         </style>
#         """, unsafe_allow_html=True
#     )
    
#     st.title("🧮 Smart Calculator")
    
#     # Initialize session state for expression
#     if "expression" not in st.session_state:
#         st.session_state.expression = ""
    
#     # Display calculator screen
#     st.text_input("Expression", st.session_state.expression, key="display", disabled=True)
    
#     # Calculator buttons
#     buttons = [
#         "7", "8", "9", "/",
#         "4", "5", "6", "*",
#         "1", "2", "3", "-",
#         "0", ".", "=", "+",
#         "C"
#     ]
    
#     # Layout for calculator
#     cols = st.columns(4)
#     for i, btn in enumerate(buttons):
#         with cols[i % 4]:
#             if st.button(btn, key=btn):
#                 if btn == "=":
#                     try:
#                         st.session_state.expression = str(eval(st.session_state.expression))
#                     except:
#                         st.session_state.expression = "Error"
#                 elif btn == "C":
#                     st.session_state.expression = ""
#                 else:
#                     st.session_state.expression += btn
    
#     # Dark Mode Toggle
#     if st.checkbox("Dark Mode"):
#         st.markdown('<style>body {background-color: #121212; color: white;}</style>', unsafe_allow_html=True)

# if __name__ == "__main__":
#     smart_calculator()


# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Custom CSS for calculator layout
#     st.markdown(
#         """
#         <style>
#             .calculator {
#                 display: grid;
#                 grid-template-columns: repeat(4, 1fr);
#                 gap: 10px;
#                 width: 300px;
#                 margin: auto;
#                 padding: 20px;
#                 background-color: #282c34;
#                 border-radius: 10px;
#                 text-align: center;
#             }
#             .calc-btn {
#                 padding: 15px;
#                 font-size: 18px;
#                 font-weight: bold;
#                 color: white;
#                 background-color: #4CAF50;
#                 border: none;
#                 border-radius: 5px;
#                 cursor: pointer;
#             }
#             .calc-btn:hover {
#                 background-color: #45a049;
#             }
#             .stTextInput input {
#                 font-size: 20px;
#                 text-align: center;
#             }
#         </style>
#         """, unsafe_allow_html=True
#     )
    
#     st.title("🧮 Smart Calculator")
    
#     # Number input as a calculator display
#     expression = st.text_input("Enter Calculation", "")
    
#     # Calculator buttons
#     buttons = [
#         "7", "8", "9", "/",
#         "4", "5", "6", "*",
#         "1", "2", "3", "-",
#         "0", ".", "=", "+"
#     ]
    
#     # Layout for calculator
#     col1, col2, col3, col4 = st.columns(4)
#     button_values = {}
    
#     for i, btn in enumerate(buttons):
#         with (col1 if i % 4 == 0 else col2 if i % 4 == 1 else col3 if i % 4 == 2 else col4):
#             if st.button(btn, key=btn):
#                 button_values[btn] = True
    
#     # Evaluate expression
#     if "=" in button_values:
#         try:
#             result = eval(expression)
#             st.success(f"Result: {result}")
#         except Exception as e:
#             st.error("Invalid Expression")
    
#     # Dark Mode Toggle
#     if st.checkbox("Dark Mode"):
#         st.markdown('<style>body {background-color: #121212; color: white;}</style>', unsafe_allow_html=True)

# if __name__ == "__main__":
#     smart_calculator()


# import streamlit as st
# import math

# def smart_calculator():
#     st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
    
#     # Custom CSS for better UI
#     st.markdown(
#         """
#         <style>
#             body {background-color: #1e1e2f; color: white;}
#             .stApp {background-color: #282c34; padding: 20px; border-radius: 10px;}
#             .stButton>button {background-color: #4CAF50; color: white; font-size: 16px;}
#         </style>
#         """, unsafe_allow_html=True
#     )
    
#     st.title("🧮 Smart Calculator")
    
#     # Operation selection
#     operation = st.selectbox("Select an operation:", [
#         "Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)", 
#         "Square Root (√)", "Power (x^y)"
#     ])
    
#     # User input for numbers
#     num1 = st.number_input("Enter first number:", format="%.2f")
#     num2 = None
#     if operation not in ["Square Root (√)"]:
#         num2 = st.number_input("Enter second number:", format="%.2f")
    
#     # Calculation logic
#     result = None
#     history = st.session_state.get("history", [])
    
#     if st.button("Calculate"):
#         if operation == "Addition (+)":
#             result = num1 + num2
#         elif operation == "Subtraction (-)":
#             result = num1 - num2
#         elif operation == "Multiplication (*)":
#             result = num1 * num2
#         elif operation == "Division (/)":
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 st.error("Cannot divide by zero!")
#         elif operation == "Square Root (√)":
#             if num1 >= 0:
#                 result = math.sqrt(num1)
#             else:
#                 st.error("Cannot calculate square root of a negative number!")
#         elif operation == "Power (x^y)":
#             result = math.pow(num1, num2)
        
#         if result is not None:
#             st.success(f"Result: {result}")
#             history.append(f"{operation}: {num1} {('' if num2 is None else f'and {num2}')} = {result}")
#             st.session_state.history = history
    
#     # Display Calculation History
#     if history:
#         st.subheader("📜 Calculation History")
#         for entry in history[-5:]:
#             st.text(entry)
    
#     # Dark Mode Toggle
#     if st.checkbox("Dark Mode"):
#         st.markdown('<style>body {background-color: #121212; color: white;}</style>', unsafe_allow_html=True)

# if __name__ == "__main__":
#     smart_calculator()


