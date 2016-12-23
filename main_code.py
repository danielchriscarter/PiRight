import logic
from pygame_output import PygameOutput
#from terminal_output import TerminalOutput

quiz = logic.Quiz("./data/questions.csv")

if __name__ == "__main__":
    Window = PygameOutput(quiz, [24,23,25,18]) #Replace with real button numbers
    Window.Main()







#terminal = TerminalOutput(quiz)
#terminal.printAllQuestions()
#quiz.calculateTotalTime()
#print ("Total Time: " + "%.2f" % quiz.totalTime + "s")
