

def returns(file1, file2, col_name1, col_name2, col_name3, col_name4):
    """Will divide Col2 by Col1."""
    # Merge two files
    file1 = file1.merge(file2, left_index=True, right_index=True)
    # Add Column with the subtraction of column2 from column1
    file1[col_name3] = (file1[col_name2] - file1[col_name1])
    # Save as Integer
    file1[col_name3] = (file1[col_name3].astype('int'))
    # Add Column with the ratio of column2 from column1
    file1[col_name4] = ((file1[col_name2] / file1[col_name1])-1)
    # Drop individual columns
    file1.drop([col_name1, col_name2], axis=1, inplace=True)
    # Return dataframe
    return file1