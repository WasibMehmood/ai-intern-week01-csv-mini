import pandas as pd

# Function to Calculate Average Marks


def compute_average(data=None):
    if data is None:

        data = pd.read_csv("students.csv")

    data['Average'] = data[['Math', 'Science', 'English']].mean(
        axis=1).round(2)

    print(data)
# Converting Result to Summary CSV File
    data.to_csv('summary.csv', index=False)
    return data


compute_average()
