
# import
import pickle


























## To Save the data into pickle format
# df - variable name which we want to save
# filename - Out filename 
pickle.save(df, open(filename, 'wb')


## To Read the data from pickle format
# df - variable name 
# filename - Out filename 
df = pickle.load(open(filename, 'rb')