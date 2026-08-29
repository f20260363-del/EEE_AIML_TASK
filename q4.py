import numpy as np
hours = np.array([6, 7, 8, 2, 5])
attend = np.array([70, 82, 63, 49, 29])
prev_sc = np.array([91, 92, 61, 48, 89])
final_sc = np.array([92, 92, 61, 50, 89])

print("Hours shape: ", hours.shape)
print("Attendance shape: ", attend.shape)
print("Previous Score shape: ", prev_sc.shape)
print("Final Score shape: ", final_sc.shape)
print("Hours datatype: ", hours.dtype)
print("Attendance datatype: ", attend.dtype)
print("Previous Score datatype: ", prev_sc.dtype)
print("Final Score datatype: ", final_sc.dtype)

print("Mean Final Score: ", np.mean(final_sc))
print("Maximum Final Score: ", np.max(final_sc))
print("Minimum Final Score: ", np.min(final_sc))
print("Standard Deviation of Final Scores: ", np.std(final_sc))

final_sc+=5

final_bl = final_sc[final_sc>=75]
print("Scores more than 75: ", final_sc[final_sc>=75])