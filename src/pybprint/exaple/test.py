import pybprint 


pybprint.bprint(f'''This is a boxed text in a 50 characters long box! The cool thing is that i don't have to worry about new lines as it does it by itself!
I could even go on a new line and there would be no problems!''', True, 50)

pybprint.bprint(f'''\n<|fr>And this is some red text <|fb>that's now magically blue <|bw>and is now on a white background <|fB>as it turns black! <|sb>And now it's brigher!''')