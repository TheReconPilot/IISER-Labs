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