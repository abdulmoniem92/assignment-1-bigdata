import pandas as pd

#1
insight_1 = "The dataset contains missing values in the 'age' column."
insight_1_filename = "eda-in-1.txt"
with open(insight_1_filename, "w") as file:
    file.write(insight_1)

#2
insight_2 = "There is a high correlation between variables X and Y in the dataset."
insight_2_filename = "eda-in-2.txt"
with open(insight_2_filename, "w") as file:
    file.write(insight_2)

#3
insight_3 = "The dataset exhibits a significant class imbalance in the target variable."
insight_3_filename = "eda-in-3.txt"
with open(insight_3_filename, "w") as file:
    file.write(insight_3)