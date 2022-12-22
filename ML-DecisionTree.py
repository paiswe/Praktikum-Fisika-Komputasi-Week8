from sklearn import tree
 
#database : gerbang logika AND
# x = data, Y = Target

x = [[0 , 0,  0,  0,  0],
     [0 , 5,  0,  5,  0],
     [0 , 0,  5,  5,  5],
     [0 , 5,  5,  10, 0],
     [5 , 5,  0,  10, 5],
     [5 , 0,  5,  10, 15],
     [5 , 5,  5,  15, 15],
     [10, 5,  5,  15, 20],
     [5 , 10, 5,  20, 20],
     [10, 10, 10, 20, 20]
     ]
y = [0,0,0,10,10,15,10,20,15,20]

# Training and Classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#prediksi
print ("logika AND Metode Decision Tree")
print ("Logika = Prediksi")
print ("10 10  5  15  20  = ", clf.predict([[10 ,10  ,5 , 15, 20] ] ) )
print ("5  10  5  20  5   = ", clf.predict([[5  ,10  ,5 , 20, 5 ] ] ) )
print ("2  0   10 15  15  = ", clf.predict([[2  ,0   ,10, 15, 15] ] ) )
print ("5  0   0  20  10  = ", clf.predict([[5  ,0   ,0 , 20, 10] ] ) )
print ("0  0   2  20  20  = ", clf.predict([[0  ,0   ,10, 20, 20] ] ) )
print ("0  10  10 20  20  = ", clf.predict([[0  ,10  ,10, 20, 20] ] ) )
print ("10 12  5  15  15  = ", clf.predict([[10 ,12  ,5 , 15, 15] ] ) )
print ("0  5   0  20  20  = ", clf.predict([[0  ,5   ,0 , 20, 20] ] ) )
print ("10 5   20 20  20  = ", clf.predict([[10 ,5   ,20, 20, 20] ] ) )
