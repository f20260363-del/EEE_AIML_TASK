import matplotlib.pyplot as plt
import pandas as pd

#importing csv file
df = pd.read_csv('/Users/anirudhjs/Documents/code/processed_student_performance.csv')

#bar chart
x = df['Student']
y = df['Final_Score']
plt.figure()
plt.bar(x,y)
plt.title('Bar Chart')
plt.xlabel('Student Names')
plt.ylabel('Final Scores')
plt.savefig('final_scores.png')

#scatter plot
x = df['Hours_Studied']
y = df['Final_Score']
plt.figure()
plt.scatter(x,y)
plt.title('Scatter Plot')
plt.xlabel('Hours Studied')
plt.ylabel('Final Score')
plt.savefig('study_vs_score.png')

#histogram
plt.figure()
plt.hist(df['Final_Score'], bins = 5)
plt.xlabel('Final Score')
plt.ylabel('No of students')
plt.title('Distribution of Final Scores')
plt.savefig('score_distribution.png')

#custom plot
plt.figure()
x = df['Attendance']
y = df['Final_Score']
plt.plot(y,x)
plt.title('Attendance vs Final Score')
plt.xlabel('Final Score')
plt.ylabel('Attendance')
plt.savefig('custom_plot.png')

plt.show()