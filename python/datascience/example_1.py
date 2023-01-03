import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas

#PRE-PROCESSING
archive = pandas.read_csv('dengue.csv')
years = archive[['ano']]
cases = archive[['casos']]

#DATA-MINING
linear_reg = LinearRegression()
linear_reg.fit(X = years, y = cases)
from_year = [[2048]]
from_cases = linear_reg.predict(from_year)

print(f"2018: cases prevision : {int(from_cases)}")

#POST-PROCESSING
plt.scatter(years, cases, color="gray")
plt.scatter(from_year, from_cases, color="green")
plt.plot(years, linear_reg.predict(years), color="red")
 
plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([2018])
plt.yticks([int(from_cases)])
 
plt.show()