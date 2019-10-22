# Accounting-Game
A family friend approached me to create an interactive accounting game for their final PGCE presentation. This was created in one night.

Game was created using pyGame and Python 2.7. The app was delivered to the client as an x64 executable created using cx-Freeze.
These files are not included here, only the main .py file and required image and font files are included.


Issues:
Since the entire game runs off a while loop without any timer, the game speed will vary based on the speed of the PC. This was an oversight during development due to the time constraint. 


How it works:
The pygame window is initalized and 3 variables are created storing the balloon images( balloon1, balloon2, balloon3 ).
A list of questions as well as a list with answers are initialized. The lists matchup so the answer to question[i] will be stored at answer[i]. This is a multiple choice game with choices being a,b or c. 

The main game loop is an infinite while loop. The exit conditions are met if the balloons reach a certain y value(the spiked roof) or if the user answers question 9 correctly. Since the questions are answered sequentially this means the user has answered all questions correctly. 

During each loop the y location of each of the 3 balloons is decremented by 1. Fonts and pictures are all rendered using the pygame blit() function. An event handler then checks if the left mosue button is pressed and if so it checks to see if the click happened within ( x - 60 , x + 150 ) and ( y - 600, y + 550) for each balloon. These ranges mean that a user must press the letter in the center of each balloon, clicks are not registered for simply pressing any portion of the balloon.
I noticed that by taking more time to click(as more precision is required) I ended up getting more answers correct as it gave my brain time to correct me if the first answer I thought of was incorrect.

If a user clicks the wrong button the while loop exits and a lose screen is displayed. If the user selects the correct answer then all balloons are reset to their start positions and the question counter is incremented allowing the user to move on to the next question.

This goes on until the user gives an incorrect answer or if they answer all 9 questions correctly.

Improvements for the future:

* Add in difficulty levels by decreasing how quickly balloons move up the screen thereby giving a user less time to answer.
* Improve the score calculator to take into account how quickly an answer was answered.
* Adding more questions and an Hitpoint system so a user doesn't automatically lose after answering 1 question incorrectly.
* Randomize the order in which questions appear, this would require some checking to make sure that the answers still match up to the     questions based on index. A dictionary could be implemented but it would requrie extra code as dictionarys can't be reshuffled.
* Add a time limiter so that the game runs at 60 fps, this will ensure all systems experience the same game and will aid in implementing   the difficulty functions.
* Slight change to the exit conditions to use list size in the checks rather than the hard-coded 9.
* Split the program up into functions as the code is difficult to read and edit in it's current state.
