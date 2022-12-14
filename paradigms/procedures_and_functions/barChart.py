import matplotlib.pyplot as plot

x = ["A", "B", "C", "D"]
y = [3, 8 , 1, 10]

barChart = plot.bar(x, y)
plot.ylabel("SALES")
plot.title("Product sales")
plot.show()
