import pandas as pd
from summary import compute_average

# Test Function to Check if Code compute correct averagee


def test_avegrage():
    data = {
        "Name": ['Hassan', 'Awais'],
        "Math": [90, 80],
        "English": [85, 75],
        "Science": [95, 70]
    }
    df = pd.DataFrame(data)
    result = compute_average(df)
    expected_average = [90.0, 75.0]
    assert result["Average"].tolist() == expected_average
