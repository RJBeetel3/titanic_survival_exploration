#this code creates predictions for survivors of the titanic
import pandas

def predictions_3(data):
    
 
    """ Model with two features: 
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """
    
    predictions = []
    
    for _, passenger in data.iterrows():
        
        if passenger['Sex'] == 'female' or passenger['Age'] <= 10:
            predictions.append(1)
        
        else: 
            predictions.append(0)
        
    
    # Return our predictions
    return pandas.Series(predictions)
    
def predictions_4(data):
	
	predictions = []
	
	for _, passenger in data.iterrows():
		if passenger['Sex'] == 'female': 
			predictions.append(1)
		elif passenger['Age'] <= 10 and passenger['SibSp'] < 3:
			predictions.append(1)
		else:
			predictions.append(0)
						
	return pandas.Series(predictions)
	
def predictions_5(data):
	
	# Accuracy = 81.71%
	predictions = []
	
	for _, passenger in data.iterrows():
		if passenger['Sex'] == 'female' and passenger['SibSp'] < 3: # and passenger['Fare'] > 10 : 
			predictions.append(1)
		elif passenger['Sex'] == 'male' and passenger['Age'] <= 10 and passenger['SibSp'] < 3:
			predictions.append(1)
		else:
			predictions.append(0)
						
	return pandas.Series(predictions)
	
def predictions_6(data):
	
	# Accuracy = 82.27%
	predictions = []
	
	for _, passenger in data.iterrows():
		if passenger['Sex'] == 'female' and passenger['SibSp'] < 3 and passenger['Parch'] <4: 
			predictions.append(1)
		elif passenger['Sex'] == 'male' and passenger['Age'] <= 10 and passenger['SibSp'] < 3:
			predictions.append(1)
		else:
			predictions.append(0)
						
	return pandas.Series(predictions)
	
	
def predictions_7(data):
	
	# Accuracy = 82.27%
	predictions = []
	
	for _, passenger in data.iterrows():
		if passenger['SibSp'] < 3: 
			predictions.append(1)
		elif passenger['Sex'] == 'female' and passenger['Parch'] <4: 
			predictions.append(1)
		elif passenger['Sex'] == 'male' and passenger['Age'] <= 10:
			predictions.append(1)
		else:
			predictions.append(0)
						
	return pandas.Series(predictions)