#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
    Author
    ------
        Roman Takhovskiy (zID: 5364695)

    Purpose
    -------
        To calculate the peaks of similairty of the given data based on threshold 
        and pattern width parameters.

    Description
    -----------
        The function checks if lengt of data values is greater or equal to pattern
        width. If not then return an error, "insufficient data". The data is sliced
        to the pattern width and overlapping indices are removed, repeated for an
        entire data. Then, sliced data segment is check for highest value and if it
        is above the threshold value, if yes then it is stored in the list and returns
        this list. If nothing meetings the criteria then, it returns an error,
        "Not detected".

    Data Dictionary
    ---------------
    data_sliced: [list]
        A list to store sliced data
        
    similarity_list: [list]
        A list to store calculated similairty
    
    Parameters
    ----------
    data_values : [float]
        A list of float values representing similarity measures. You are looking
        for instances of the pattern inside this data_values.

    pattern_width : [float]
        A float value. The length/width of the pattern.

    threshold : [float]
        A float value. Selected similarity measure needs to be greater than or
        equal to the given threshold value.

    Returns
    -------
        - "Insufficient data"
        - "Not detected"
        -  A list of peaks

    """

import matplotlib.pyplot as plt
def pattern_search_multiple(data_values, pattern_width, threshold):
    # Checking if length of data values lis is greater or equal to pattern width
    if len(data_values) >= pattern_width:
        # List to store values above threshold
        separation_list=[]
        # List to store peaks
        multiple_list=[]

        # A loop for range of length of data values to remove overlapping indices
        for i in range(pattern_width, len(data_values)-pattern_width):
            # Removing overlapping
            separation_list = (data_values[slice(i-(pattern_width-1),i + pattern_width)])

            # Checking if maximum value in separation list is equal to data value 
            # And data value is above the threshold
            if max(separation_list) == data_values[i] & data_values[i] >= threshold:
                # If it meetings the requirement then store it in the list
                multiple_list.append(i)

        # Storing the multiple_list in a variable to return it
        search_multiple = multiple_list

        # If multiple_list is empty then return "not detected"
        if multiple_list == []:
                search_multiple = ("Not detected")

    # If length of data is smaller than length of pattern then return an "Insufficient data"
    else:
        search_multiple = "Insufficient data"
        
    # Return the search multiple or errors
    return search_multiple