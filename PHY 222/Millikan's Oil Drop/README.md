# Millikan's Oil Drop Experiment

There are the main files in this folder:

- `Calculations - Balancing Method.py`
- `Calculations - Dynamic Method.py`
- `Data - Balancing Method.csv`
- `Data - Dynamic Method.csv`
- `Data - Millikan's Oil Drop Experiment.ods`
- `Millikan's_SES.pdf`

---
The `Millikan's_SES` PDF file describes the method in fair detail. 

The LibreOffice Calc *Data* file has all the data in its raw form. 

The two CSVs are exported data from the Calc spreadsheet.

The two Python programs calculate the errors in all the values.

___

## Dependencies

The code uses the following packages:
- numpy
- scipy
- uncertainties

Use `pip install <package-name>` to install the relevant packages if needed.

___

## Data File Format

Export the data in CSV Format. There must be no empty spaces, or the `numpy.loadtxt()` method will crash.

Refer to the actual data files in this folder for a better idea.

### Dynamic Method Data

Save the Data file as `Data - Dynamic Method.csv`

Put the data in the following format:

```Droplet No., Fall Time (s), Rise Time (s), Voltage (V)```

The first line is the heading, and the successive lines contain the numerical data values in SI units in the format of the heading line.

Each droplet must have the corresponding number and voltage written.
For the Dynamic Method, this means that the droplet number and voltage is going to be repeated.

Example [Table to be exported as CSV]

| Droplet No. | Fall Time (s) | Rise Time (s) | Voltage (V) |
| ----------- | ------------- | ------------- | ----------- |
| 1 | 6.6 | 5.2 | 142 |
| 1 | 5.9 | 5.5 | 142 |
| 1 | 6.3 | 5.7 | 142 |
| 2 | 4.8 | 5.0 | 185 |
| 2 | 4.8 | 5.2 | 185 |
| 3 | 6.0 | 4.3 | 559 |
| 3 | 6.1 | 4.8 | 559 |
| 4 | 5.3 | 5.8 | 359 |
| 4 | 5.3 | 5.9 | 359 |

### Balancing Method Data

Save the Data file as `Data - Balancing Method.csv`

The first line is the heading, and the following lines in the following format:

`Droplet No., Fall Time (s), Balancing Voltage (V)`

If there are more fall time readings for which the corresponding balancing voltage is not available, then the voltage column must be filled with a 0.

Example Table:

| Droplet No. | Fall Time (s) | Balancing Voltage (V) |
| ----------- | ------------- | --------------------- |
| 1 | 3.5 | 549 |
| 1 | 3.3 | 550 |
| 1 | 3.5 | 552 |
| 1 | 3.4 | 0 |
| 1 | 3.4 | 0 |
| 2 | 2.2 | 591 |
| 2 | 2.2 | 590 |
| 2 | 2.5 | 593 |
| 2 | 2.3 | 0 |
| 2 | 2.4 | 0 |


## Cautionary Note in Calculations

The Python Programs involve a method of computing approximate GCD, as mentioned in the PDF Lab Manual.

The other method involved is the method of linear regression after approximate GCD is obtained. [Read on it here](https://stackoverflow.com/questions/445113/approximate-greatest-common-divisor).

The general algorithm is:

- Take the list of `ne`
- Divide them by the lowest value
- Round these to the nearest multiple of 0.5
- Reject the cases where we don't have a perfect integer

After rejecting these cases, if we have only one value left in the arrays, then regression won't work. 

To troubleshoot, look at the output. All the required values are printed at the end with their corresponding errors. 

---

For questions, comments, or anything, please reach out to me (Purva Parmar) on my IISER Email ID.