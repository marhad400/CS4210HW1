#-------------------------------------------------------------------------
# AUTHOR: Mark Haddad
# FILENAME: decision_tree.py
# SPECIFICATION: Creates a decision tree based on the given dataset in a csv file
# FOR: CS 4210- Assignment #1
# TIME SPENT: ~ 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
feature_values_dict = {"Young": 1, "Prepresbyopic": 2, "Presbyopic": 3, "Myope": 1, "Hypermetrope": 2, "Yes": 1, "No": 2, "Normal": 1, "Reduced": 2}
num_rows = len(db)
num_cols = len(db[0])

X = [[0 for x in range(num_cols - 1)] for y in range(num_rows)]

for i in range(num_rows):
   for j in range(num_cols - 1): #excluding classification column
      key = db[i][j]
      if key in feature_values_dict:
         X[i][j] = feature_values_dict[key]
         
for row in X:
   print(row)


#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
class_dict = {"Yes": 1, "No": 2}

Y = [0 for y in range(num_rows)]
for i in range(num_rows):
   key = db[i][-1]
   if key in class_dict:
      Y[i] = class_dict[key]
      
for y in Y:
   print(y)
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()