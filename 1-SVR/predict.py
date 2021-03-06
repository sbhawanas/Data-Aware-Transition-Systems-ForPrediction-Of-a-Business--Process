"""
authors : Bhavna Singh (18134501003)
          Ritik Pal (18134501025)

"""
"""
In this file we are calculating the result 
by finding their MAPE and RMSPE values
"""
# we import our model by importing  the train.py file
import train
import math
# we store the Predicted and actual values of remaining time in P, A respectively
Predicted,Actual=train.makeprediction()

NumberOfEvent=0
MAPE=0		
RMSEP=0
for i in range(len(Actual)):
	if Actual[i]==0:
		# if its the last event in the trace then we don't calculate the remaining time for it
		continue
	NumberOfEvent+=1
	#  we calculate the MAPE and RMSPE values 
	MAPE+=abs(Actual[i]-Predicted[i])/Actual[i]
	RMSEP+=(abs(Actual[i]-Predicted[i])/Actual[i])*(abs(Actual[i]-Predicted[i])/Actual[i])

MAPE=MAPE/NumberOfEvent
RMSEP=math.sqrt(RMSEP/NumberOfEvent)
print(100*MAPE,100*RMSEP)