from array import array
import pandas as pd
import numpy as np
import csv 
class Preprossing:
   
    #method to read the csv file and make the classification=

    def read_csv_data(self):
        with open(self.aaaa.csv, newline='') as csvfile:
                mydata = csv.reader(csvfile, delimiter=' ', quotechar='|')
                array = list(mydata)

        
    data= pd.read_csv(array,header=None,names=['mark1','mark2','finalresult'])
    print(data.head(10))
    accepted=data[data['finalresult'].isin([1])]
    rejected=data[data['finalresult'].isin([0])]   
    print('the accepted students is \n',accepted)
    print('the rejected students is \n',rejected)



#make object f from the class and running the methods of the class
f = Preprossing()
f.read_csv_data()