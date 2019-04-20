import aqgFunction
import sys

# Main Function
def main():
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()
    #inputText = readFile.read()
    filehandle = open(sys.argv[1], 'r')
    inputText = filehandle.read()

    print("------INPUT TEXT------\n\n")
    print(inputText,'\n')

    #inputText = '''I am Saurabh'''

    questionList = aqg.aqgParse(inputText)
    aqg.display(questionList)

    #aqg.DisNormal(questionList)
    return 0

if __name__ == "__main__":
    main()
