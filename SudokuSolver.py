



def setUpBoard(op, given1, given2, given3):
    # Easy1
    #given1 = '036100052100240000405000080'
    #given2 = '070480265200000008658027010'
    #given3 = '060000809000093006740002530'

    #Easy2
    #given1 = '080010095900028100007000034'
    #given2 = '030106489090000010561904020'
    #given3 = '210000300009230001370060040'

    #Medium1
    #given1 = '500300061030580097000900043'
    #given2 = '000005000308000406000200000'
    #given3 = '710002000890014030240003008'

    #Hard1
    #given1 = '800005010005080004300107000'
    #given2 = '200060000057020340000070002'
    #given3 = '000809007500040200040700003'

    #Evil
    #given1 = '000009800000450060906008000'
    #given2 = '800060005010805070600090002'
    #given3 = '000900704030047000002500000'

    #Evil2
    #given1 = '000000304802100000060094020'
    #given2 = '050047900000000000007650040'
    #given3 = '010520070000009602504000000'

    #Evil3
    given1 = '005320006200894000000000030'
    given2 = '400000800027000540008000009'
    given3 = '060000000000716008300058100'


    given1 = userInput(given1)
    given2 = userInput(given2)
    given3 = userInput(given3)

    for i in range(0,81):
        op[i] = [' ',[], [1,2,3,4,5,6,7,8,9],i]

    for i in range(0,27):
        op[i][0] = given1[i]

    j = 0
    for i in range(27,54):
        op[i][0] = given2[j]
        j += 1

    j = 0
    for i in range(54,81):
        op[i][0] = given3[j]
        j += 1

    for i in range(0,81):
        if op[i][0] in [1,2,3,4,5,6,7,8,9]:
            op[i][2] = []


def display(op):
    print("\n\n\n\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[0][0],op[1][0],op[2][0],op[3][0],op[4][0],op[5][0],op[6][0],op[7][0],op[8][0]))
    print("\t\t\t___________  ___________  ___________")
    print("\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[9][0],op[10][0],op[11][0],op[12][0],op[13][0],op[14][0],op[15][0],op[16][0],op[17][0]))
    print("\t\t\t___________  ___________  ___________")
    print("\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[18][0],op[19][0],op[20][0],op[21][0],op[22][0],op[23][0],op[24][0],op[25][0],op[26][0]))

    print("\n\n\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[27][0],op[28][0],op[29][0],op[30][0],op[31][0],op[32][0],op[33][0],op[34][0],op[35][0]))
    print("\t\t\t___________  ___________  ___________")
    print("\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[36][0],op[37][0],op[38][0],op[39][0],op[40][0],op[41][0],op[42][0],op[43][0],op[44][0]))
    print("\t\t\t___________  ___________  ___________")
    print("\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[45][0],op[46][0],op[47][0],op[48][0],op[49][0],op[50][0],op[51][0],op[52][0],op[53][0]))

    print("\n\n\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[54][0],op[55][0],op[56][0],op[57][0],op[58][0],op[59][0],op[60][0],op[61][0],op[62][0]))
    print("\t\t\t___________  ___________  ___________")
    print("\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} ".format(op[63][0],op[64][0],op[65][0],op[66][0],op[67][0],op[68][0],op[69][0],op[70][0],op[71][0]))
    print("\t\t\t___________  ___________  ___________")
    print("\t\t\t {} | {} | {}    {} | {} | {}    {} | {} | {} \n\n\n".format(op[72][0],op[73][0],op[74][0],op[75][0],op[76][0],op[77][0],op[78][0],op[79][0],op[80][0]))

def updateOptions(items):
    for item in items.values():
        for slot in item:
            if slot[0] == " ":
                for check in item:
                    if check[0] in [1,2,3,4,5,6,7,8,9]:
                        slot[1].append(check[0])
                slot[1] = list(set(slot[1]))
                for i in slot[1]:
                    if i in slot[2]:
                        slot[2].remove(i)
            else:
                slot[1] = []
                slot[2] = []

def chosenOnes(items):
    #Check if only 2 numbers can go in 2 boxes and eliminate from other boxes in that component other than those 2
    for item in items.values():
        chosen2 = []
        for box in item:   
            if box[0] == " ":
                if len(box[2]) == 2:
                    chosen2.append(box)  
        half = round(len(chosen2) / 2)
        
        for i in range(0,half):
            keep = []
            count = 0
            for pair in chosen2:
                if chosen2[i][2] == pair[2]:
                    count += 1
                    keep.append(pair[3])
            if count == 2:
                for box in item:
                    if box[0] == " " and box[3] not in keep:
                        # If the first number in the yes values of the first pair is in the yes 
                        # values of another square in that same section, add that number to that 
                        # square's no values and remove it from its yes values
                        if chosen2[i][2][0] in box[2]:
                            box[1].append(chosen2[i][2][0])
                            box[2].remove(chosen2[i][2][0])
                        if chosen2[i][2][1] in box[2]:
                            box[1].append(chosen2[i][2][1])
                            box[2].remove(chosen2[i][2][1])
    #Guesser
def guesser(op, boxes, rows, columns, correct): 
    guess = search(rows)
    print(guess)
    if guess != 0:
        for i in range(0,81):
            if op[i][3] == guess[0][3]:
                op[i][0] = op[i][2][0]
                return op[i][3]

 
def incorrect(correct, guess):
    for i in range(0,81):
        if op[i][3] in correct:
            op[i][0] = " "
    



def search(items):
    empty = 0
    temp = []
    for item in items.values():
        for square in item:
            if square[0] == " ":
                empty += 1
                temp.append(square)
        if empty == 2:
            return temp
        else:
            empty = 0
            temp = []
    return 0

def progressTracker(op):
    progress = []
    for item in range(0,81):
        if op[item][0] in [1,2,3,4,5,6,7,8,9]:
            progress.append(op[item][0])
    return progress


def uODriver(boxes, rows, columns):
    updateOptions(boxes)
    updateOptions(rows)
    updateOptions(columns)
    chosenOnes(boxes)
    chosenOnes(rows)
    chosenOnes(columns)
    
def lastManStanding(op):
    for i in range(0,81):
        if op[i][0] == " ":
            if len(op[i][2]) == 1:
                op[i][0] = op[i][2][0]
                op[i][1] = []
                op[i][2] = []
    uODriver(boxes, rows, columns)

#Check to see if there i only one number available to go in a row, box, or column
def elimination(items):
    for x in items.values():
        pos = []
        for item in x:  
            if item[0] == " ":
                for num in item[2]:
                    pos.append(num)
        pos = list(set(pos))
        for i in pos:
            counter = 0
            temp = 0
            for item in x:
                if i in item[2]:
                    counter += 1
                    temp = item
            if counter == 1:
                for item in x:
                    if item == temp:
                        item[0] = i
    

def eliminationDriver(boxes, rows, columns):
    elimination(boxes)
    elimination(rows)
    elimination(columns)
    uODriver(boxes, rows, columns)

def userInput(given):
    x1 = []
    for i in given:
        x1.append(int(i))
    for i in range(0,27):
        if x1[i] == 0:
            x1[i] = " "
    return x1

def completed(op):
    for i in range(0,81):
        if op[i][0] == " ":
            return False
    return True

def roadblock(past, present):
    if past == present:
        return True
    else:
        return False

def noMoves(op):
    counter = 0
    for i in range(0, 81):
        if op[i][2] == []:
            counter += 1
    if counter == 81:
        return True
    else:
        return False

def solve(op, boxes, rows, columns, correct):
    uODriver(boxes, rows, columns)
    past = []
    present = progressTracker(op)
    while( not completed(op) and not roadblock(past, present)):
        past = present
        lastManStanding(op)
        eliminationDriver(boxes, rows, columns)
        present = progressTracker(op)
    if not completed(op) and roadblock(past,present):
        print("Commence Guesser!\n")
        for i in range(0,81):
            if op[i] != " ":
                correct.append(op[i][3])
        while(noMoves(op) == False):
            g = guesser(op, boxes, rows, columns, correct)
            guesses


###################################################################################################
#                                            MAIN CODE
###################################################################################################

op = [0] * 81
print("Create your puzzle by entering the numbers from left to right, row by row. Enter a 0 for blanks.")
given1 = (input("Enter the numbers for the first 3 rows here:\n"))
given2 = (input("Enter the numbers for the middle 3 rows here:\n"))
given3 = (input("Enter the numbers for the last 3 rows here:\n"))
correct = []
setUpBoard(op, given1, given2, given3)

boxes = {'box1' : [op[0], op[1], op[2], op[9], op[10], op[11], op[18], op[19], op[20]],
             'box2' : [op[3], op[4], op[5], op[12], op[13], op[14], op[21], op[22], op[23]],
             'box3' : [op[6], op[7], op[8], op[15], op[16], op[17], op[24], op[25], op[26]],
             'box4' : [op[27], op[28], op[29], op[36], op[37], op[38], op[45], op[46], op[47]],
             'box5' : [op[30], op[31], op[32], op[39], op[40], op[41], op[48], op[49], op[50]],
             'box6' : [op[33], op[34], op[35], op[42], op[43], op[44], op[51], op[52], op[53]],
             'box7' : [op[54], op[55], op[56], op[63], op[64], op[65], op[72], op[73], op[74]],
             'box8' : [op[57], op[58], op[59], op[66], op[67], op[68], op[75], op[76], op[77]],
             'box9' : [op[60], op[61], op[62], op[69], op[70], op[71], op[78], op[79], op[80]]}

columns = {'col1' : [op[0], op[9], op[18], op[27], op[36], op[45], op[54], op[63], op[72]],
            'col2' : [op[1], op[10], op[19], op[28], op[37], op[46], op[55], op[64], op[73]],
            'col3' : [op[2], op[11], op[20], op[29], op[38], op[47], op[56], op[65], op[74]],
            'col4' : [op[3], op[12], op[21], op[30], op[39], op[48], op[57], op[66], op[75]],
            'col5' : [op[4], op[13], op[22], op[31], op[40], op[49], op[58], op[67], op[76]],
            'col6' : [op[5], op[14], op[23], op[32], op[41], op[50], op[59], op[68], op[77]],
            'col7' : [op[6], op[15], op[24], op[33], op[42], op[51], op[60], op[69], op[78]],
            'col8' : [op[7], op[16], op[25], op[34], op[43], op[52], op[61], op[70], op[79]],
            'col9' : [op[8], op[17], op[26], op[35], op[44], op[53], op[62], op[71], op[80]]}

rows = {'row1' : [op[0], op[1], op[2], op[3], op[4], op[5], op[6], op[7], op[8]],
        'row2' : [op[9], op[10], op[11], op[12], op[13], op[14], op[15], op[16], op[17]],
        'row3' : [op[18], op[19], op[20], op[21], op[22], op[23], op[24], op[25], op[26]],
        'row4' : [op[27], op[28], op[29], op[30], op[31], op[32], op[33], op[34], op[35]],
        'row5' : [op[36], op[37], op[38], op[39], op[40], op[41], op[42], op[43], op[44]],
        'row6' : [op[45], op[46], op[47], op[48], op[49], op[50], op[51], op[52], op[53]],
        'row7' : [op[54], op[55], op[56], op[57], op[58], op[59], op[60], op[61], op[62]],
        'row8' : [op[63], op[64], op[65], op[66], op[67], op[68], op[69], op[70], op[71]],
        'row9' : [op[72], op[73], op[74], op[75], op[76], op[77], op[78], op[79], op[80]]}

display(op)
solve(op, boxes, rows, columns, correct)
display(op)



for i in range(0,81):
    print("Box {}: Value - {}  Available - {}  Unavailable = {}".format(op[i][3], op[i][0], op[i][2], op[i][1]))
        


