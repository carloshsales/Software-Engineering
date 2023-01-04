from sklearn.datasets import load_iris, fetch_kddcup99
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.svm import SVC

#-------------------------------------------PRÉ-PROCESSING
#------Collect and integration
iris = load_iris()

characteristics = iris.data
labels = iris.target

print(f"CHARACTERISTICS:\n {characteristics[:2]}\n")
print(f"LABELS:\n {labels[:2]}\n")

print("################################################\n")

#------DATA PARTITION
characteristics_fit, characteristics_test, label_fit, label_test = train_test_split(characteristics, labels)


#-------------------------------------------------MINING
tree = DecisionTreeClassifier(max_depth=2)
tree.fit(X= characteristics_fit, y= label_fit)

label_p = tree.predict(characteristics_test)
accuracy_tree = accuracy_score(label_test, label_p)

#----------------------------------------Support Vector Machine
clf = SVC()
clf.fit(X=characteristics_fit, y=label_fit)

label_p_smv = clf.predict(characteristics_test)
accuracy_smv =accuracy_score(label_test, label_p_smv)

print("################################################\n")

result = export_text(tree, feature_names=iris['feature_names'])
print("Structure Tree")
print(result)#FINAL



