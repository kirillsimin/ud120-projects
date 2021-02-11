#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
pp = pprint.PrettyPrinter(indent=2)

poi_count = 0
payments = 0
payments_count = 0
no_payment_count = 0
poi_no_payment_count = 0
total = 0


for name, data in enron_data.iteritems():
    if(data['poi']) :
        poi_count += 1
        if data['total_payments'] == 'NaN':
            poi_no_payment_count += 1

    if data['total_payments'] != 'NaN':
        payments_count += 1
        payments += data['total_payments']
    else :
        no_payment_count += 1

    total += 1

print 'poi count : ' + str(poi_count)
print 'payments : ' + str(payments)
print 'payment count : ' + str(payments_count)
print 'no payment : ' + str(no_payment_count)
print 'poi no payment count : ' + str(poi_no_payment_count)
print 'percent with payments : ' + str(float(payments_count) / float(total))
print 'total : ' + str(total)
