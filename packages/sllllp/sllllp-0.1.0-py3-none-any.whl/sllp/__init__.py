def slp():

	s= """
	import pandas as pd
	import numpy as np
	import seaborn as sns
	import statistics as stat
	import matplotlib.pyplot as plt
	from sklearn.preprocessing import LabelEncoder

	df = pd.read_csv("Stores.csv")
	for i in df.columns:
		df[i].fillna(df[i].mean(), inplace = True)
		df.isnull().sum()
		
	input_Dimension = 9
	Weights = np.random.rand(input_Dimension)
	co =0
	er =[]
	w = []
	l = [0,0.1,0.2]

	for i in l:
		learning_rate = i
		e =[]
		Training_Data = df.copy(deep=True)
		Expected_Output = Training_Data.Price
		Training_Data = Training_Data.drop(['Price'],axis = 1)
		Training_Data = np.asarray(Training_Data)
		Training_count = len(Training_Data[:, 0])
		
		for epoch in range(0,5):
			for datum in range(0, Training_count):
				Output_Sum = np.sum(np.multiply(Training_Data[datum, :], Weights))
				if Output_Sum < 0:
					Output_Value = 0;
				else:
					Output_Value = 1;
				error = Expected_Output[datum] - Output_Value
				e.append(error)
				for n in range(0, input_Dimension):
					Weights[n] = Weights[n] + learning_rate * error * Training_Data[datum,n]
	er.append(e)
	w.append(Weights)

	min_er = []
	for i in er:
		c = 0;
		for j in i:
			c += abs(j)
		min_er.append(c)

	for i in range(len(min_er)):
		if min_er[i] == min(min_er):
			print(l[i])
			print(w[i])

	plt.plot(er[0])
	plt.show()"""
	
	print(s)