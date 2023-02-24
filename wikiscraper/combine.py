
#for each element on the page:

# # create a new object to hold both the character string and it's associated home URL.
# This will be sufficient for radicals and character links; for the character page itself, an "endpoint page", there will have to be separate functionality. So the URL grabber shouldn't go more than 2 levels deep. 

# how can we define an endpoint page? are the URLS unique? UTF-8 encoding

#running radLinks returns URLS for top level pages; running charGrab CAN find urls for 2nd tier pages with some modification. Once modified!charGrab is run, the data i need for a given char is available, and no more url grabbing needs to be done.

# level1 : radLinks
# level2: modified!chargrab
# level3: functionality for individual char page