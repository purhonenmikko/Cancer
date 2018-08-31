
from sklearn import tree
import numpy

data = numpy.genfromtxt('breast-cancer-wisconsin.txt', dtype = numpy.int32 , skip_header=0, delimiter = ',')
features = []
labels = []
for j in range(len(data)):
	labels.append(data[j][10])
	row = [0]*10
	for i in range (1,11):
		row[i-1] = data[j][i]
	features.append(row)
		
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print("\nThis program estimates whether a tumor is benign or malignant\n")
print("\nAttribute Information:\n")
print("1. Sample code number: id number\n")
print("2. Clump Thickness: 1 - 10 \n")
print("3. Uniformity of Cell Size: 1 - 10 \n")
print("4. Uniformity of Cell Shape: 1 - 10 \n")
print("5. Marginal Adhesion: 1 - 10 \n")
print("6. Single Epithelial Cell Size: 1 - 10 \n") 
print("7. Bare Nuclei: 1 - 10 \n")
print("8. Bland Chromatin: 1 - 10 \n")
print("9. Normal Nucleoli: 1 - 10 \n")
print("10. Mitoses: 1 - 10 \n")
print("11. Class: (2 for benign, 4 for malignant)\n")
print("------------------------------------------\n")

print("\nInput data\n")
ID = int(input("1. Sample code number: "))
CT = int(input("2. Clump Thickness: "))
UCSize = int(input("3. Uniformity of Cell Size: "))
UCShape = int(input("4. Uniformity of Cell Shape: "))
MA = int(input("5. Marginal Adhesion: "))
SECSize = int(input("6. Single Epithelial Cell Size: "))
BN = int(input("7. Bare Nuclei: "))
BC = int(input("8. Bland Chromatin: "))
NC = int(input("9. Normal Nucleoli: "))
M = int(input("10. Mitoses: "))
print("------------------------------------------\n")

diagnosis = clf.predict([[ID, CT, UCSize, UCShape, MA, SECSize, BN, BC, NC, M]])

if (diagnosis == 4):
	print("Result: Tumor is malignant.\n")
elif (diagnosis == 2):
	print("Result: Tumos is benign.\n")




