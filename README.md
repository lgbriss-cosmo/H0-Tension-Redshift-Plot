# H0-Tension-Redshift-Plot
Intended as a companion plot to the publicly available whisker plot code of Di Valentino et al, showing the trend of H_0 measurements with redshift.

- The .py source file plots from the exaggerated .csv data file. Note that the smaller redshift ranges for CMB and GW measurements are exaggerated for visibility - I include the original .csv purely for comparison.
- You can add or remove data and categories from the .csv file. Note that if you add categories of measurement you will have to make new empty variables for the arraylist and data processing in the .py (but nothing after that).
- You can introduce a cut-off of data by precision, date, or number of measurements per category in the .py source file, without altering the .csv file. If you don't want a cutoff set these to None.
- Within a category, the .py file plots from least to most precise i.e. most precise on top.
- You can sort the order of plotting manually by category or automatically plot the categories that contain the lowest error bars on top by setting the sort to 'manual' or 'automatic'.
- Sample plots with and without cutoff are included for reference.
- List of colours is sorted according to the original order of the data categories (so that you can make a consistent colour scheme for Indirect vs Direct measurements).
- List of transparencies is sorted according to the final order of the data categories (so that more uncertain measurements can be more transparent).
- If you use this code please reference my paper!
