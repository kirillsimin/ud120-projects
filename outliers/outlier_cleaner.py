#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here


    data = [(ages[i][0], net_worths[i][0], abs(net_worths[i][0] - predictions[i][0])) for i in range(0, len(ages))]
    
    data.sort(key=lambda tup: tup[2])
    
    cleaned_data = data[:-9]
    

    return cleaned_data

