""" Python Code to calculate the average score of a student
and determine what program the student will be admitted to """

def studentAverage():

    print("\nPython command line interface application to calculate the average score of a\nstudent and determine what program the student will be admitted to\n")
    print("Input scores and separate with space\n")

    # this line takes in the scores
    scoresInput = input("Press enter when you are done: ")

    # scores will be split and stored in a list
    scores = []

    # initialize total and average score to 0
    totalScores = 0
    average = 0

    # initialize number of test to 0
    totalTests = 0

    # check if score is inputed
    if scoresInput !=  "":
        # split the scores and remove the space
        scoresSplit = scoresInput.split()

        # loop to store scores in list
        for a in scoresSplit:
            scores.append(int(a))
    else:
        print("\nNo scores inputed\n")
        # restart function if no scores inputed
        return studentAverage()

    # set number of tests to be lenght of scores list
    totalTests = len(scores)
    
    # loop through elements and add
    for b in range(0, len(scores)):
        totalScores += scores[b]

    # calculate average score
    average = totalScores / totalTests

    # print results 
    print("\nTotal number of tests taken = " + str(totalTests))
    print("Your total score = " + str(totalScores))
    print("Your average score = " + str(average))

    # check if average meets requirements
    if average >= 70:
        print("\nCongratulations, you have been admitted to Tier 1 of the program.\n")

        # exit or continue using app
        myexit = int(input("Input -1 then press enter to exit or input 1 then press enter to continue using application:\n"))
        if myexit == -1:
            exit()
        else: 
            return studentAverage()
    else:
         print("\nSorry, your average score did not meet requirement for Tier 1,\nbut you have been admitted to Tier 2 of the program.\n")
         
         # exit or continue using app
         myexit = int(input("Input -1 then press enter to exit or input 1 then press enter to continue using application:\n"))
         if myexit == -1:
            exit()
         else: 
            return studentAverage()

x = studentAverage()       
 


