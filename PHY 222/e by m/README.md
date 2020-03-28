# e/m Ratio

## Important Files
- `e by m - Data.xlsx` - The spreadsheet file
    - The data in the first session did not give proper results, so the second session data is recorded in the sheets with S2 mark
- `e by m_SES.pdf` - The Lab Manual
- `Errors and Graphs.py` - The code for the error analysis and graphs
    - Utilizes two files: `Export Data Set 1.csv` and `Export Data Set 2.csv`. The filename set is to be mentioned in the `set_name` variable in the program
    - Displays graph of square of diameter vs accelerating voltage
    - Prints the following values with associated errors 
        - Diameter d (m)
        - d^2
        - e/m
            - Average e/m
            - Error from literature value
        - e/m from graph
            - Curve fit parameter - slope
            - R^2 of the plot
            - Error from literature value
- `Export Data Set 1.csv` and `Export Data Set 2.csv` - Export data files in CSV format
    - The "Set 1" and "Set 2" names are supposed to be mentioned in the `set_name` variable in the program code in `Errors and Graphs.py`


___

## Export Data Format

The files `Export Data Set 1.csv` and `Export Data Set 2.csv` are in the following format given in a table for example:

| Voltage (V) | Current (A) | Right (cm) | Left (cm) |
| ----------- | ----------- | ---------- | --------- |
| 200         | 1.5         | 13.2       | 6.1       |
| 180         | 1.5         | 12.9       | 6.7       |
| 160         | 1.5         | 13.0       | 7.0       |
| 140         | 1.5         | 12.6       | 7.2       |
| 120         | 1.5         | 12.4       | 7.3       |

The Set 1 file contains the data for Current = 1.5 A. The Set 2 file contains the data for Current = 1.1 A.

Any number of sets can be made for different values of current. 