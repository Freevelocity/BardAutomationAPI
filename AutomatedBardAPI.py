from bardapi import Bard



import os
import csv
import random


loopcounter = 0 
os.environ["_BARD_API_KEY"] = "Your Own KEY From Bard"
websites =[]
BardsResponse = []
SummerizedBardResponse = []

DifferentStartingVariations  = ["Amazing how", "Its really cool how", "Interesting how", "I really love how"]

with open('MWsites.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file) 

        next(csv_reader)

        for line in csv_reader:
            websites.append(line[0])

    

for website in websites:

    message = "I want to sell a service to the following website \"{}\" as a Digital Ads Expert, can you please go through their website and come up with a personalized first line, in one sentence to two sentences. Start with \"{}\" and make the prompt understandable for an 18-year old high schooler, do not make it salesy and do not include promotional sentences. Make it casual and something similar to something you would say when meeting someone at a coffee shop. Base the complement of the following website. Do no include information that is not listed in the following website and you don't need to explain just give the options".format(website,DifferentStartingVariations[random.randint(0,len(DifferentStartingVariations) - 1)])
    bard = Bard(timeout=100)
    BardsResponse.append(Bard().get_answer(str(message))['content'])
    
    #message2 = "Can you summarize all of the points into 1-2 lines\n{}".format(BardsResponse[loopcounter])
    #SummerizedBardResponse.append(Bard().get_answer(str(message2))['content'])
    loopcounter = loopcounter + 1
    print(loopcounter)


CombinedList = list(zip(websites, BardsResponse))
with open('BardResponses.csv','w',newline="" ) as csv_fileWrite:
        csv_writer = csv.writer(csv_fileWrite, delimiter=",")
        csv_writer.writerows(CombinedList)
