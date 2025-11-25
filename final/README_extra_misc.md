# metro_simulator.py bonus stuff

For the bonus i added various assistance functions like 

- Fully functional ascii metro graph with search feature 

works same as old 2d game rendering (i think this is the fastest way to render 2d graphs too (in python.)) uses coordinates hashmap basically key is coordinate pair (x,y) and value is location now a grid is rendered but grid is fixed to terminal size columns and rows(lines for shutil ui) incrementation of ou1 and ou2 is done to the rendered coords and that is it for the zoom in zoom out i changed the scale when creating hashmap basically earlier i calculated by multiplying with 1000 as the SCALE but if i reduce it by some ratio like 0.8 or inc by 1.25 the gap b/w stations dec/inc as the hashmap is recreated 

Search feature also works the same uses value pair to find keypair basically searches value then sets the x+ou1, y+ou2  = value_x, value_y

the caption function just enables disables the printing of the text part using if case 

- Metro search feature with suggestions and details

search any metro on any line affiliated with dmrc works by using a custom input function rather than using input inbuilt, i used the input_key() function i created to take single input and return it then just append it to idk i.e. an empty list and search the list with metro data for `idk in i[1] for i in metro_data` works this way and prints it simply 


- fully colored menu 

fully colored everything using ansi escape codes and it works on all terminals using an reset code too (might not work as intended if your terminal only supports 24bit colors).

- Interactive Menu

colored menu with heading and details, using a list to iterate using key presses for incrementing or decrementing the index for the list to color (`>> xyz name <<` this part) 




