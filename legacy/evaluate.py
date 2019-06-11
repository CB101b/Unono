def evalCard(userchoice, player, playStack):
        
    currentCard = playStack[-1] #Get the last card from the stack	
    if currentCard == "wild" or "wild+":
        return(1)

    currentCardArray = currentCard.split("#") #Splits the card data in two
    currentCardColor = currentCardArray[0] #Sets a new variable with only the color of the card
    currentCardNumber = currentCardArray[1] #Sets a new variable with only the number of the card
	
    userchoiceArray = userchoice.split("#") #Same as above but with the userchoice
    userchoiceColor = userchoiceArray[0]
    userchoiceNumber = userchoiceArray[1] 
	
    if userchoiceNumber == currentCardNumber or userchoiceColor == currentCardColor: #Checks if the number of the two cards the same are
        return(1)
    else: 
        return(0)
