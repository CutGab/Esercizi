import random 

class LotteryMachine:

    def __init__(self, mylist):

        self.mylist = mylist
        self.winning_ticket = []

    
    def roll (self):

        i = 0
        self.winning_ticket = []

        while i < 4:
            
            ticketroll = random.choice(self.mylist)
            self.winning_ticket.append(ticketroll)
            i += 1

        return self.winning_ticket
    
    def winning (self):
        
        print(f"The winning ticket is the following: {self.winning_ticket}")


lotteria1 = LotteryMachine ([1,2,3,4,5,6,7,8,9,10,"a","b","c","d"])

lotteria1.roll()

lotteria1.winning()