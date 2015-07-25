from sklearn import linear_model

clf = linear_model.LinearRegression()

entries = [x for x in range(100)]

times = [x * 7 for x in range(100)]

z = zip(entries, times)
print z

clf.fit(z, times)

print clf.coef_

print clf.predict(101)
