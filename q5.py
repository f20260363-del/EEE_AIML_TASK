import pandas as pd #importing pandas library

#loading csv into dataframe
df = pd.read_csv("/Users/anirudhjs/Documents/aiml/ieee/student_performance.csv")

#print first 5 rows
print(df[0:5])

#print number of rows and columns
print("Rows: ", df.shape[0])
print("Columns: ", df.shape[1])

#dislay column names
print("Column Names: ", df.columns)

#checking of missing values
print("Missing Values Present: ", df.isnull().values.any())

#average final score
print("Average Final Score: ", df['Final_Score'].mean())

#High Scoring Student
high_ind = df['Final_Score'].idxmax()
print("Highest Scorer: ", df['Student'].loc[high_ind])

#Improvement Column
df['Improvement'] = df['Final_Score'] - df['Previous_Score']
print(df)

#Students with attendance >=80
print(df[df['Attendance']>=80]['Student'])

#Dataframe in descending order
df = df.sort_values(by = 'Final_Score', ascending=False)
print(df)

#final processed dataframe
df.to_csv('processed_student_performance.csv')