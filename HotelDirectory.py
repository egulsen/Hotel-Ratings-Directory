"""
Binary Search Trees
Written By: Elifnaz Gulsen
"""

"""
This function reads in the file provided, and divides into a list of lists 
input: none
output: returns list of lists 
"""
def readFile():
    file = open("hotels.txt",'r')
    lst2 = []
    for line in file:
         lst =[i.strip() for i in line.split(',')]
         lst2.append(lst)
    file.close()
    return lst2
#Modified/ used the code after lst = .... from the website below:
#https://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
#Author: Sean Vieira
#Date: November 1st 2010
"""
This function adds a new node to the tree by comparing the hotel ID
Input: Binary search tree
Output: Modified BST with new node added
"""
def addNewID(tree,val):
    #if tree empty, add new node
    if tree == None:
        return {"data":val, "left": None, "right": None}
    elif float(val[0]) < float(tree["data"][0]):
        tree["left"] = addNewID(tree["left"],val)
        return tree
    elif float(val[0]) > float(tree["data"][0]):
        tree["right"] = addNewID(tree["right"],val)
        return tree
    else: #same data value ignored
        return tree

"""
This function finds the average of any one of the scores the user decides to
choose from. We use the sumBST() and numNodes() functions as helper functions.
Input: Binary Search Tree, and userCrit, the score the user wants the avg. of
Output: Integer value representing the average of user criteria
"""
def findAvg(tree,userCrit):
    val = sumBST(tree,userCrit)
    nodes = numNodes(tree)
    avg = val/nodes
    return avg
    

"""
This function prints out the listings of all hotel ID numbers that
are greater than or equal to the min acceptable score provided by the
user.
Input: userCrit(user criterion), minScore(the min score user will accept)
Output: all the hotel ID numbers that satisfy the min score
"""
def printCrit(tree,userCrit,minScore):
    if tree == None:
        return
    printCrit(tree['left'],userCrit,minScore)
    printCrit(tree['right'],userCrit,minScore)
    #compare min score with the index user wants to check,
    #if our min score smaller or equal to data value, then print the hotel ID
    #which would be data[0] 
    if minScore <= float(tree['data'][userCrit]):
       print("Hotel no: ",tree['data'][0])
        
    
"""
This function sums up the data values in a given user criteria in the BST
Input: Binary Search Tree, userCrit, the criteria the user chooses
Output: sum of the data values of chosen criteria
"""
def sumBST(tree,userCrit):
    if tree == None:
        theSum = 0
        return theSum
    else:
        left = sumBST(tree['left'],userCrit)
        right = sumBST(tree['right'],userCrit)

        theSum = float(tree['data'][userCrit]) + left + right
        return theSum
#I used / modified the above code from the following website:
#http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/12-Recursion/sum-bintree.html
#Written by: Shun Yan Cheung
#Date: Unknown

"""
This function returns the number of nodes in a binary search tree
Input: Binary Search Tree
Output: Integer value representing number of nodes
"""
def numNodes(tree):
    if tree is None:
        return 0
    else:
        return  1 + numNodes(tree['left']) + numNodes(tree['right'])
    
#I used/ modified the above code segment from the following website:
#https://stackoverflow.com/questions/19187901/counting-number-of-nodes-in-a-binary-search-tree    
#Written by: Vaibhav Desai
#Date: October 4th 2013

"""
This function returns the number of hotels that got a less than 70% rating
on the overall avg. satisfaction criteria
Input: Binary Search Tree
Output: integer representing number of hotels 
"""
def countSeventy(tree):
    calcVal = (70 * 65) / 100
    if tree == None:
        return 0
    count = countSeventy(tree['left']) + countSeventy(tree['right'])
    #since we want to find avg. satisfaction we have to check data[7]
    if float(tree['data'][7]) <= calcVal:
        count += 1
        return count 
    else:
        return count
    

"""
This function finds the scores for a hotel the user wishes to inquire about
Input: tree (our BST), hotelID ( the hotel the user wants to know about)
Output: Either a string stating the hotel wasn't found or the scores of the
found hotel in string format
"""
def findHotel(tree,hotelID):
    if tree == None:
        print("Sorry, the hotel you are looking for doesn't exist")
        
    elif hotelID == float(tree['data'][0]):
        print("Hotel ID:",int(tree['data'][0]))
        print("Preferred Location Score:",float(tree['data'][1]),"/25")
        print("Reputation Score:",float(tree['data'][2]),"/25")
        print("Cleanliness and Comfort Score:",float(tree['data'][3]),"/15")
        print("Amenities Score:",float(tree['data'][4]),"/20")
        print("Price(Budget) Score:",float(tree['data'][5]),"/20")
        print("Luxury Score:",float(tree['data'][6]),"/35")
        print("Overall Average Satisfaction of Guests:",float(tree['data'][7]),"/65")
        
    elif hotelID < float(tree['data'][0]):
        return findHotel(tree['left'],hotelID)
    else:
        return findHotel(tree['right'],hotelID)


"""
Main function starts program execution
Input:None
"""
def main():
    tree = None
    nodeList = readFile()
    #Create our BST
    for i in nodeList:
        tree = addNewID(tree,i)
        
    print("Welcome to the Hotel Ratings Directory")
    print("")
    cond= True
    while cond:
        userIn = input("""
                       Would you like to:
                       
         1) Manually Input the Hotel ID and all it's other scores
         2) Find the average of any of the scores
         3) Find  suitable hotels based on criteria and minimum requirement
         4) Find the number of hotels that have a less than 70% rating on
            overall satisfaction
         5) Look up scores for a given hotel
         6) Quit

         Please input 1, 2, 3, 4, 5 or 6 for given options : """)
        print("")

        if userIn == "1":
             userAdd = input("Enter the hotel ID and all it's components using commas in between:")
             print("")
             userList = list(map(float,userAdd.split(',')))
             #To create a list out of user input, I modified the line of code above from:
             #https://stackoverflow.com/questions/29358402/python-turning-user-input-into-a-list
             #Written by: Marcin
             #Date: March 31st 2015
             tree = addNewID(tree,userList)
             print("Successfully added Hotel to the directory")
             print("")

        elif userIn == "2":
            user_crit = input("""
            Please choose from the following options:
       
              1) Preferred location score
              2) Reputation score
              3) Cleanliness and comfort score
              4) Amenities score
              5) Price (Budget) score
              6) Luxury score
              7) Overall average satisfaction of guests

            Enter the criteria you wish to find the average(Enter 1,2,3,4,5,6 or 7):""")
            if user_crit == "1":
                findAvg1 = findAvg(tree,int(user_crit))
                print("Average score of choice 1: ",'%.2f'%(findAvg1))
            elif user_crit == "2":
                findAvg2 = findAvg(tree,int(user_crit))
                print("Average score of choice 2: ",'%.2f'%(findAvg2))
            elif user_crit == "3":
                findAvg3 = findAvg(tree,int(user_crit))
                print("Average score of choice 3: ",'%.2f'%(findAvg3))
            elif user_crit == "4":
                findAvg4 = findAvg(tree,int(user_crit))
                print("Average score of choice 4: ",'%.2f'%(findAvg4))
            elif user_crit == "5":
                findAvg5 = findAvg(tree,int(user_crit))
                print("Average score of choice 5: ",'%.2f'%(findAvg5))
            elif user_crit == "6":
                findAvg6 = findAvg(tree,int(user_crit))
                print("Average score of choice 6: ",'%.2f'%(findAvg6))
            else:
                findAvg7 = findAvg(tree,int(user_crit))
                print("Average score of choice 7: ",'%.2f'%(findAvg7))
                            

        elif userIn == "3":
            criteria = input("""

            Please choose from the following options:
       
              1) Preferred location score
              2) Reputation score
              3) Cleanliness and comfort score
              4) Amenities score
              5) Price (Budget) score
              6) Luxury score
              7) Overall average satisfaction of guests

            Enter the criteria you wish to look for(Enter 1,2,3,4,5,6 or 7):""")
            
            minScore = input("Please enter the minimum acceptable score (out of 100): ")
            print("")
            minScore = float(minScore)
            criteria = int(criteria)
            if criteria == 1:
                calculate_1 = (minScore * 25) / 100
                print("Hotels that satisfy the criteria:")
                print("")
                calcCrit = printCrit(tree,criteria,calculate_1)
            elif criteria == 2:
                calculate_2 = (minScore * 25) / 100
                print("Hotels that satisfy the criteria:")
                print("")
                calcCrit2 = printCrit(tree,criteria,calculate_2)
            elif criteria == 3:
                calculate_3 = (minScore * 15) / 100
                print("Hotels that satisfy the criteria:")
                print("")
                calcCrit3 = printCrit(tree,criteria,calculate_3)
            elif criteria == 4:
                calculate_4 = (minScore * 20) / 100
                print("Hotels that satisfy the criteria:")
                print("")
                calcCrit4 = printCrit(tree,criteria,calculate_4)
            elif criteria == 5:
                calculate_5 = (minScore * 20) / 100
                print("Hotels that satisfy the criteria:")
                print("")
                calcCrit5 = printCrit(tree,criteria,calculate_5)
            elif criteria == 6:
                calculate_6 = (minScore * 35) / 100
                print("Hotels that satisfy the criteria:")
                print("")
                calcCrit6 = printCrit(tree,criteria,calculate_6)
            else:
                calculate_7 = (minScore * 65) / 100
                print("Hotels that satisfy the criteria:")
                print("")
                calcCrit7 = printCrit(tree,criteria,calculate_7)
                

        elif userIn == "4":
            disp = countSeventy(tree)
            print("Number of hotels that have less than 70% rating:",disp)

        elif userIn == "5":
            userin = input("Enter the hotel ID you are inquiring about:")
            print("")
            userFind = findHotel(tree,float(userin))

        elif userIn == "6":
            cond = False
            
        elif userIn not in ["1","2","3","4","5","6"]:
            print("Please input either 1,2,3,4,5 or 6")
            print("")
            
        else:
            print("Please input either 1, 2 , 3, 4 , 5 or 6")
            print("")
            
            

main()

        
    
