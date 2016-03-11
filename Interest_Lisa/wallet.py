'''
Created on Mar 10, 2016

@author: oashonibare
'''
import unittest


class Test(unittest.TestCase):

    def testCase1(self):
        print("-----------------Test Case 1-------------------------")
        portfolio1 = {'person': 1, 'wallet':1, 'cards':['visa','mc','discover']}
        #print(portfolio1['cards'])
        for card in portfolio1['cards']:
            card_amount = 100
            if card == 'visa':
                interest_rate = 10.0
                visa_interest = int((card_amount/100.0) * interest_rate)
                print("Interest for Visa card is %s"  %("$" + str(visa_interest) + ".00"))
            elif card == 'mc':
                interest_rate = 5.0
                mc_interest = int((card_amount/100.0) * interest_rate)
                print("Interest for MC card  is %s" %("$" + str(mc_interest)+ ".00"))
            elif card == 'discover':
                dis_interest = int(card_amount/100.0)
                print("Interest for Discover card is %s" %("$" + str(dis_interest)+ ".00"))
        cc_interest = int(visa_interest +  mc_interest + dis_interest) 
        
        print("First Test Case Person has %s interest " %("$" + str(cc_interest) + ".00"))
        
    def testCase2(self):
        print("-----------------Test Case 2-------------------------")
        card_amount = 100
        wallet1 = ['visa', 'discover']
        wallet2 =['mc']
        
        for card in wallet1:
            if card == 'visa':
                interest_rate = 10.0
                visa_interest = (card_amount/100.0) * interest_rate
            elif card == 'discover':
                interest_rate = 5.0
                mc_interest = (card_amount/100.0) * interest_rate
        wallet1_interest = int(visa_interest + mc_interest)
        print ("The interest for the first wallet is %s" %("$" +str(wallet1_interest))+".00")
        
        #  wallet 2
        for card in wallet2:
            if card == 'mc':
                interest_rate = 5.0
                mc_interest = (card_amount/100.0) * interest_rate
        wallet2_interest = int(mc_interest)
        print ("The interest for the second wallet is %s" %("$" + str(wallet2_interest) + ".00"))
        
        person_interest = int(wallet1_interest + wallet2_interest)
        print("Second Test Case Person has %s interest" %("$" +str(person_interest) +".00"))
        
    def testCase3(self):
        print("-----------------Test Case 3-------------------------")
        card_amount = 100
        person1 = ['mc', 'visa']
        person2 = ['visa','mc']
        
        for card in person1:
            if card == 'visa':
                interest_rate = 10.0
                visa_interest = (card_amount/100.0) * interest_rate
            elif card == 'mc':
                interest_rate = 5.0
                mc_interest = (card_amount/100.0) * interest_rate
        person1_interest=wallet_interest= int(visa_interest + mc_interest)
        
        print("Person 1 has one wallet, the wallet interest is %s therefore Person 1 Interest is %s" %("$"+ str(wallet_interest) +".00","$" + str(person1_interest) + ".00"))
        
        
        for card in person2:
            if card == 'visa':
                interest_rate = 10.0
                visa_interest = (card_amount/100.0) * interest_rate
            elif card == 'mc':
                interest_rate = 5.0
                mc_interest = (card_amount/100.0) * interest_rate
        person2_interest=wallet_interest= int(visa_interest + mc_interest)
        
        print("Person 2 has one wallet, the wallet interest is %s therefore Person 2 Interest is %s" %("$"+ str(wallet_interest) + ".00","$" + str(person2_interest)+ ".00"))
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()