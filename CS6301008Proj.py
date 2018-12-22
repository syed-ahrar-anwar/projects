#Syed Ahrar Anwar
#Project - CS 6301.008
#Predicting IPv6 addresses
#Language: Python 3 
#Requirements: Numpy

import numpy
punctuation = "."


#Training function: this function's primary goal is to establish probabilities 
#for each hex character at every position in a 32-bit IPv6 address. 
#First, it reads the addresses in the training file into a list, and sets up 
#counter lists for each hex character for every position. It then iterates through
#each address in the list to count the number of times a particular character appears
#at a certain position in the set. Then, it divides the elements in the counter
#lists with the total number of addresses to determine the probabilities for when 
#a certain hex character appears at a certain position at each position

def probfunc (filename):
    #initialising variables
    global zero
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global a
    global b
    global c
    global d
    global e
    global f
    global zeroprob
    global oneprob
    global twoprob
    global threeprob
    global fourprob
    global fiveprob
    global sixprob
    global sevenprob
    global eightprob
    global nineprob
    global aprob
    global bprob
    global cprob
    global dprob
    global eprob
    global fprob  
    
    #reading set of addresses from training file to list
    x = []
    file = open(filename, encoding='utf-8-sig')
    for line in file:
        newtext = ""
        text = line.rstrip('\n')
        for char in text:
            if char not in punctuation:
                newtext = newtext + char
        x.append(newtext)
        
    #initialising count lists for each hex character at each position  
    zero   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    one    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    two    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    three  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    four   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    five   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    six    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    seven  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    eight  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nine   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    a      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    b      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    d      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    e      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    f      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    #iterating through each address in the list of addresses and counting
    #the number of times a character appears at a certain position and updating 
    #the count list for each character
    countx = len(x)
    
    for i in x:
        k = 0
        for j in i:
            
            if   j == '0':
                zero[k]  += 1
                
            elif j == '1':
                one[k]   += 1
                
            elif j == '2':
                two[k]   += 1
                
            elif j == '3':
                three[k] += 1
                
            elif j == '4':
                four[k]  += 1
                
            elif j == '5':
                five[k]  += 1
                
            elif j == '6':
                six[k]   += 1
                
            elif j == '7':
                seven[k] += 1
                
            elif j == '8':
                eight[k] += 1
                
            elif j == '9':
                nine[k]  += 1
                
            elif j == 'a':
                a[k]     += 1
                
            elif j == 'b':
                b[k]     += 1
                
            elif j == 'c':
                c[k]     += 1
                
            elif j == 'd':
                d[k]     += 1
                
            elif j == 'e':
                e[k]     += 1
                
            elif j == 'f':
                f[k]     += 1
                
            k += 1

    #dividing count lists by number of addresses in the list of addresses to develop 
    #probabilities for each character at each position
    zeroprob  = [x/countx for x in zero ]
    oneprob   = [x/countx for x in one  ]
    twoprob   = [x/countx for x in two  ]
    threeprob = [x/countx for x in three]
    fourprob  = [x/countx for x in four ]
    fiveprob  = [x/countx for x in five ]
    sixprob   = [x/countx for x in six  ]
    sevenprob = [x/countx for x in seven]
    eightprob = [x/countx for x in eight]
    nineprob  = [x/countx for x in nine ]
    aprob     = [x/countx for x in a    ]
    bprob     = [x/countx for x in b    ]
    cprob     = [x/countx for x in c    ]
    dprob     = [x/countx for x in d    ]
    eprob     = [x/countx for x in e    ]
    fprob     = [x/countx for x in f    ]
    
    
#Test function: this function is the one that predicts the IPv6 address. It does
#so by first reading the addresses from the test file into a list. Then, to account
#for changes in network ranges and prefixes in the test set, it sets the counters
#for the first 8 positions for each hex character in the lists established in the
#training function to 0 and then iterates over each address in the test list to
#count the number of times a character appears at a certain position in the first
#8 positions. Then, it updates the probability lists from the training function
#with the probabilities of the first 8 positions for each hex character, by
#dividing the updated count of the first 8 positions by the number of addresses.
#Then, it predicts a character at each position of a 32-bit IPv6 address using 
#the probabilties of each hex character appearing at that position. It then saves 
#those predictions in a list and formats the contents into an IPv6 address format.
#It uses a for loop to repeat the prediction process as many times as signified in
#the 'times' argument for the test function, and collects all the predicted addresses
#into a list
   
def testfunc (filenametest, times):

    #reading set of addresses from test file into list
    x = []
    file = open(filenametest, encoding='utf-8-sig')
    for line in file:
        newtext = ""
        text = line.rstrip('\n')
        for char in text:
            if char not in punctuation:
                newtext = newtext + char
        x.append(newtext)
     
    #setting the first 8 elements in the count lists for each character to 0
    zero[0:7]   = [0,0,0,0,0,0,0,0]
    one[0:7]    = [0,0,0,0,0,0,0,0]
    two[0:7]    = [0,0,0,0,0,0,0,0]
    three[0:7]  = [0,0,0,0,0,0,0,0]
    four[0:7]   = [0,0,0,0,0,0,0,0]
    five[0:7]   = [0,0,0,0,0,0,0,0]
    six[0:7]    = [0,0,0,0,0,0,0,0]
    seven[0:7]  = [0,0,0,0,0,0,0,0]
    eight[0:7]  = [0,0,0,0,0,0,0,0]
    nine[0:7]   = [0,0,0,0,0,0,0,0]
    a[0:7]      = [0,0,0,0,0,0,0,0]
    b[0:7]      = [0,0,0,0,0,0,0,0]
    c[0:7]      = [0,0,0,0,0,0,0,0]
    d[0:7]      = [0,0,0,0,0,0,0,0]
    e[0:7]      = [0,0,0,0,0,0,0,0]
    f[0:7]      = [0,0,0,0,0,0,0,0]


    #iterating through each address in the list of addresses and counting
    #the number of times a character appears at a certain position in the first 8 positions 
    #and updating the count list for each character
    countx = len(x)
    for i in x:
        k = 0
        for j in i:
            if k < 8:
                
                if   j == '0':
                    zero[k]  += 1
                
                elif j == '1':
                    one[k]   += 1
                
                elif j == '2':
                    two[k]   += 1
                
                elif j == '3':
                    three[k] += 1
                
                elif j == '4':
                    four[k]  += 1
                
                elif j == '5':
                    five[k]  += 1
                
                elif j == '6':
                    six[k]   += 1
                
                elif j == '7':
                    seven[k] += 1
                
                elif j == '8':
                    eight[k] += 1
                
                elif j == '9':
                    nine[k]  += 1
                
                elif j == 'a':
                    a[k]     += 1
                
                elif j == 'b':
                    b[k]     += 1
                
                elif j == 'c':
                    c[k]     += 1
                
                elif j == 'd':
                    d[k]     += 1
                
                elif j == 'e':
                    e[k]     += 1
                
                elif j == 'f':
                    f[k]     += 1
                
                k += 1

    #dividing count lists by number of addresses in the list of addresses to develop 
    #probabilities for each character at each position in the first 8 positions and
    #updating the list of probabilities for each character
    zeroprob[0:7]  = [x/countx for x in zero[0:7] ]
    oneprob[0:7]   = [x/countx for x in one[0:7]  ]
    twoprob[0:7]   = [x/countx for x in two[0:7]  ]
    threeprob[0:7] = [x/countx for x in three[0:7]]
    fourprob[0:7]  = [x/countx for x in four[0:7] ]
    fiveprob[0:7]  = [x/countx for x in five[0:7] ]
    sixprob[0:7]   = [x/countx for x in six[0:7]  ]
    sevenprob[0:7] = [x/countx for x in seven[0:7]]
    eightprob[0:7] = [x/countx for x in eight[0:7]]
    nineprob[0:7]  = [x/countx for x in nine[0:7] ]
    aprob[0:7]     = [x/countx for x in a[0:7]    ]
    bprob[0:7]     = [x/countx for x in b[0:7]    ]
    cprob[0:7]     = [x/countx for x in c[0:7]    ]
    dprob[0:7]     = [x/countx for x in d[0:7]    ]
    eprob[0:7]     = [x/countx for x in e[0:7]    ]
    fprob[0:7]     = [x/countx for x in f[0:7]    ]   
    
    #predicting a character at each position in 32-bit address from the probabilities 
    #of all the hex characters appearing at a certain position and assigning them to a list.
    #The number of addresses predicted is signified by the variable 'times' which the for loop
    #loops to make that many predictions. The final list is a collection of all the
    #predicted addresses
    
    finallist = []
    for i in range(times):
        final = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
        final[0]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[0], oneprob[0], twoprob[0], threeprob[0], fourprob[0], fiveprob[0], sixprob[0], sevenprob[0], eightprob[0], nineprob[0], aprob[0], bprob[0], cprob[0], dprob[0], eprob[0], fprob[0]])
        final[1]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[1], oneprob[1], twoprob[1], threeprob[1], fourprob[1], fiveprob[1], sixprob[1], sevenprob[1], eightprob[1], nineprob[1], aprob[1], bprob[1], cprob[1], dprob[1], eprob[1], fprob[1]])
        final[2]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[2], oneprob[2], twoprob[2], threeprob[2], fourprob[2], fiveprob[2], sixprob[2], sevenprob[2], eightprob[2], nineprob[2], aprob[2], bprob[2], cprob[2], dprob[2], eprob[2], fprob[2]])
        final[3]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[3], oneprob[3], twoprob[3], threeprob[3], fourprob[3], fiveprob[3], sixprob[3], sevenprob[3], eightprob[3], nineprob[3], aprob[3], bprob[3], cprob[3], dprob[3], eprob[3], fprob[3]])
        final[4]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[4], oneprob[4], twoprob[4], threeprob[4], fourprob[4], fiveprob[4], sixprob[4], sevenprob[4], eightprob[4], nineprob[4], aprob[4], bprob[4], cprob[4], dprob[4], eprob[4], fprob[4]])
        final[5]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[5], oneprob[5], twoprob[5], threeprob[5], fourprob[5], fiveprob[5], sixprob[5], sevenprob[5], eightprob[5], nineprob[5], aprob[5], bprob[5], cprob[5], dprob[5], eprob[5], fprob[5]])
        final[6]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[6], oneprob[6], twoprob[6], threeprob[6], fourprob[6], fiveprob[6], sixprob[6], sevenprob[6], eightprob[6], nineprob[6], aprob[6], bprob[6], cprob[6], dprob[6], eprob[6], fprob[6]])
        final[7]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[7], oneprob[7], twoprob[7], threeprob[7], fourprob[7], fiveprob[7], sixprob[7], sevenprob[7], eightprob[7], nineprob[7], aprob[7], bprob[7], cprob[7], dprob[7], eprob[7], fprob[7]])    
        final[8]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[8], oneprob[8], twoprob[8], threeprob[8], fourprob[8], fiveprob[8], sixprob[8], sevenprob[8], eightprob[8], nineprob[8], aprob[8], bprob[8], cprob[8], dprob[8], eprob[8], fprob[8]])
        final[9]  = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[9], oneprob[9], twoprob[9], threeprob[9], fourprob[9], fiveprob[9], sixprob[9], sevenprob[9], eightprob[9], nineprob[9], aprob[9], bprob[9], cprob[9], dprob[9], eprob[9], fprob[9]])
        final[10] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[10], oneprob[10], twoprob[10], threeprob[10], fourprob[10], fiveprob[10], sixprob[10], sevenprob[10], eightprob[10], nineprob[10], aprob[10], bprob[10], cprob[10], dprob[10], eprob[10], fprob[10]])
        final[11] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[11], oneprob[11], twoprob[11], threeprob[11], fourprob[11], fiveprob[11], sixprob[11], sevenprob[11], eightprob[11], nineprob[11], aprob[11], bprob[11], cprob[11], dprob[11], eprob[11], fprob[11]])
        final[12] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[12], oneprob[12], twoprob[12], threeprob[12], fourprob[12], fiveprob[12], sixprob[12], sevenprob[12], eightprob[12], nineprob[12], aprob[12], bprob[12], cprob[12], dprob[12], eprob[12], fprob[12]])
        final[13] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[13], oneprob[13], twoprob[13], threeprob[13], fourprob[13], fiveprob[13], sixprob[13], sevenprob[13], eightprob[13], nineprob[13], aprob[13], bprob[13], cprob[13], dprob[13], eprob[13], fprob[13]])
        final[14] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[14], oneprob[14], twoprob[14], threeprob[14], fourprob[14], fiveprob[14], sixprob[14], sevenprob[14], eightprob[14], nineprob[14], aprob[14], bprob[14], cprob[14], dprob[14], eprob[14], fprob[14]])
        final[15] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[15], oneprob[15], twoprob[15], threeprob[15], fourprob[15], fiveprob[15], sixprob[15], sevenprob[15], eightprob[15], nineprob[15], aprob[15], bprob[15], cprob[15], dprob[15], eprob[15], fprob[15]])       
        final[16] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[16], oneprob[16], twoprob[16], threeprob[16], fourprob[16], fiveprob[16], sixprob[16], sevenprob[16], eightprob[16], nineprob[16], aprob[16], bprob[16], cprob[16], dprob[16], eprob[16], fprob[16]])
        final[17] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[17], oneprob[17], twoprob[17], threeprob[17], fourprob[17], fiveprob[17], sixprob[17], sevenprob[17], eightprob[17], nineprob[17], aprob[17], bprob[17], cprob[17], dprob[17], eprob[17], fprob[17]])
        final[18] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[18], oneprob[18], twoprob[18], threeprob[18], fourprob[18], fiveprob[18], sixprob[18], sevenprob[18], eightprob[18], nineprob[18], aprob[18], bprob[18], cprob[18], dprob[18], eprob[18], fprob[18]])
        final[19] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[19], oneprob[19], twoprob[19], threeprob[19], fourprob[19], fiveprob[19], sixprob[19], sevenprob[19], eightprob[19], nineprob[19], aprob[19], bprob[19], cprob[19], dprob[19], eprob[19], fprob[19]])
        final[20] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[20], oneprob[20], twoprob[20], threeprob[20], fourprob[20], fiveprob[20], sixprob[20], sevenprob[20], eightprob[20], nineprob[20], aprob[20], bprob[20], cprob[20], dprob[20], eprob[20], fprob[20]])
        final[21] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[21], oneprob[21], twoprob[21], threeprob[21], fourprob[21], fiveprob[21], sixprob[21], sevenprob[21], eightprob[21], nineprob[21], aprob[21], bprob[21], cprob[21], dprob[21], eprob[21], fprob[21]])
        final[22] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[22], oneprob[22], twoprob[22], threeprob[22], fourprob[22], fiveprob[22], sixprob[22], sevenprob[22], eightprob[22], nineprob[22], aprob[22], bprob[22], cprob[22], dprob[22], eprob[22], fprob[22]])
        final[23] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[23], oneprob[23], twoprob[23], threeprob[23], fourprob[23], fiveprob[23], sixprob[23], sevenprob[23], eightprob[23], nineprob[23], aprob[23], bprob[23], cprob[23], dprob[23], eprob[23], fprob[23]])    
        final[24] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[24], oneprob[24], twoprob[24], threeprob[24], fourprob[24], fiveprob[24], sixprob[24], sevenprob[24], eightprob[24], nineprob[24], aprob[24], bprob[24], cprob[24], dprob[24], eprob[24], fprob[24]])
        final[25] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[25], oneprob[25], twoprob[25], threeprob[25], fourprob[25], fiveprob[25], sixprob[25], sevenprob[25], eightprob[25], nineprob[25], aprob[25], bprob[25], cprob[25], dprob[25], eprob[25], fprob[25]])
        final[26] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[26], oneprob[26], twoprob[26], threeprob[26], fourprob[26], fiveprob[26], sixprob[26], sevenprob[26], eightprob[26], nineprob[26], aprob[26], bprob[26], cprob[26], dprob[26], eprob[26], fprob[26]])
        final[27] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[27], oneprob[27], twoprob[27], threeprob[27], fourprob[27], fiveprob[27], sixprob[27], sevenprob[27], eightprob[27], nineprob[27], aprob[27], bprob[27], cprob[27], dprob[27], eprob[27], fprob[27]])
        final[28] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[28], oneprob[28], twoprob[28], threeprob[28], fourprob[28], fiveprob[28], sixprob[28], sevenprob[28], eightprob[28], nineprob[28], aprob[28], bprob[28], cprob[28], dprob[28], eprob[28], fprob[28]])
        final[29] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[29], oneprob[29], twoprob[29], threeprob[29], fourprob[29], fiveprob[29], sixprob[29], sevenprob[29], eightprob[29], nineprob[29], aprob[29], bprob[29], cprob[29], dprob[29], eprob[29], fprob[29]])
        final[30] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[30], oneprob[30], twoprob[30], threeprob[30], fourprob[30], fiveprob[30], sixprob[30], sevenprob[30], eightprob[30], nineprob[30], aprob[30], bprob[30], cprob[30], dprob[30], eprob[30], fprob[30]])
        final[31] = numpy.random.choice(numpy.arange(0,16), p = [zeroprob[31], oneprob[31], twoprob[31], threeprob[31], fourprob[31], fiveprob[31], sixprob[31], sevenprob[31], eightprob[31], nineprob[31], aprob[31], bprob[31], cprob[31], dprob[31], eprob[31], fprob[31]]) 
        
    
        #replacing predicted characters greater than 9 with hex values and formatting the 
        #final predicted result
        for i in range(len(final)):
            if  final[i]  == 10:
                final[i] = 'a.'
            elif final[i] == 11:
                final[i] = 'b.'
            elif final[i] == 12:
                final[i] = 'c.'
            elif final[i] == 13:
                final[i] = 'd.'
            elif final[i] == 14:
                final[i] = 'e.'
            elif final[i] == 15:
                final[i] = 'f.'
            else:
                final[i] = str(final[i]) + '.'
    
        result = ''.join(final)
        result = result.rstrip('.')
   
        finallist.append(result)
        
    return finallist


#Hit rate function: calculates the percentage of predicted addresses that are
#the same as addresses in the test set

def hitrate(resultfile, inputfile):
    
    #reading the file of predicted addresses into a list
    x = []
    file1 = open(resultfile, encoding='utf-8-sig')
    for line in file1:
        newtext = ""
        text = line.rstrip('\n')
        for char in text:
            if char not in punctuation:
                newtext = newtext + char
        x.append(newtext)
    x = set(x)
      
    #reading the test file addresses into a list
    y = []
    file2 = open(inputfile, encoding='utf-8-sig')
    for line in file2:
        newtext = ""
        text = line.rstrip('\n')
        for char in text:
            if char not in punctuation:
                newtext = newtext + char
        y.append(newtext)
    y = set(y)
      
    #comparing the list of predicted addresses to test addresses to see how many are the same
    z = x.intersection(y)
    hits = len(z)
    
    #calculating percentage of predicted addresses that are the same as test addresses
    #and displaying the result
    rate = (hits/len(x))*100.0
    print ("Hits: ", hits)
    print ("Hit Rate (%): ", rate)   

    
#Main function: provides user functionality for the program
    
def main(): 
    #main function that lists all of the menu options
    print ("Please select an option: ")
    number = input("1: Run training set | 2: Predict using test set | 3: Calculate hit rate | 4: Exit ")
    
    #first option asks for name of training file then runs the training function
    if  number == '1':
        filename = input("Please enter the name of the training file: ")
        probfunc(filename)
        print ("Training successful")
        print ("--------------------")
        main()
        
    #second option asks for name of test file and number of predictions to make
    #as well as the name of file to write the results to before running the test function and
    #writing the results to a file
    elif number == '2':
        filenametest = input("Please enter the name of the test file: ")
        reps = input("How many IP addresses would you like to predict?: ")
        resultfile = input("Please enter the name of the file you wish to write the predictions to: ")
        reps = int(reps)
        result = testfunc(filenametest, reps)   
            
        with open(resultfile, 'w') as f:
            for item in result:
                f.write("%s\n" % item)
        f.close()
        
        print ("Success!")
        print ("--------------------")
        main()
        
    #third option asks for the names of the file of predicted addresses and the test file before 
    #running the hit rate function and displaying the hit rate
    elif number == '3':
        fileres = input("Please enter the name of the file with predicted addresses: ")
        fileinput = input("Please enter the name of the test file: ")
        hitrate (fileres, fileinput)
        print ("--------------------")
        main()
        
    #fourth option option exits the program
    elif number == '4':
        exit
         
    #error message for invalid entry
    else: 
        print("Error: Invalid entry")
        print ("--------------------")
        main()
        
        
#Main module: runs the main function
        
if __name__ == "__main__":
    main()
    

        




