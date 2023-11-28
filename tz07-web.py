# tz07-web.py
import sys

myHTML = '''     
<form method="POST">
  Enter your input: <input type="text" name="user_input">
  <input type="submit" value="Submit">
</form>
'''

def myRunPy(input_value):
    # Process the input and return the result
    # return f"Processed: {input_value}"
    return myHTML + input_value

if __name__ == "__main__":
    input_value = sys.argv[1]  # Get input from command line argument
    result = myRunPy(input_value)
    print(result)
