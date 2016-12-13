import pandas

def predictions_3(data):
    
    import pandas
    """ Model with two features: 
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        if passenger['Sex'] == 'female' or passenger['Age'] <= 10:
            predictions.append(1)
            
        else: 
            predictions.append(0)
        pass
    
    # Return our predictions
    return pandas.Series(predictions)