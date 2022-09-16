# BetterPrint
Simple Python module to print stuff in a prettier way


## Install

The module uses colorama to display colors, but in an easier way, and with the possibility to box the text.

- Linux:
   
      sudo pip3 install pybprint
    

- Windows:
   
      pip3 install pybprint



## Usage

Download module 
Import the module in your script and use it

- Parameters:
   - .bprint()
      - text     --> Your text to log (default "")
      - inBox    --> If True the text will be printed out in a box, this will ignore colors (default False)
      - boxSize  --> The width of the box in wich the text will be printed (default 100)

- Printing

        import pybprint as p
        
        #Print something in a box
        p.bprint(f'''This is a boxed text in a 50 characters long box! The cool thing is that i don't have to worry about new lines as it does it by itself!
      I could even go on a new line and there would be no problems!''', True, 50)
     ![Image](<https://i.imgur.com/6HvO151.png>)

        #Print something with colors and styling
        p.bprint(f'''\n<|fr>And this is some red text <|fb>that's now magically blue <|bw>and is now on a white background <|fB>as it turns black! <|sb>And now it's brigher!''')
     ![Image](<https://i.imgur.com/pbEV7ek.png>)


## COLORS/STYLING CHEATSHEET

To apply colors/styling to your text you should use this markers:

   - Foreground Colors:
      - "<|fr>" -> RED
      - "<|fg>" -> GREEN
      - "<|fb>" -> BLUE
      - "<|fw>" -> WHITE
      - "<|fy>" -> YELLOW
      - "<|fm>" -> MAGENTA
      - "<|fc>" -> CYAN
      - "<|fB>" -> BLACK
      - "<|fR>" -> RESET

   - Background Colors:
      - "<|br>" -> RED
      - "<|bg>" -> GREEN
      - "<|bb>" -> BLUE
      - "<|bw>" -> WHITE
      - "<|by>" -> YELLOW
      - "<|bm>" -> MAGENTA
      - "<|bc>" -> CYAN
      - "<|bB>" -> BLACK
      - "<|bR>" -> RESET

   - Styling Options:
      - "<|sd>" -> DIM
      - "<|sn>" -> NORMAL
      - "<|sb>" -> BRIGHT


## TO DO

As of now you can't use styling in a to-box text.
