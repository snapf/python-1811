#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
    Author
    ------
        Roman Takhovskiy (zID: 5364695)
    Date
    ----
        4/1/2021

    Purpose
    -------
        To calculate the similarity value of data segment

    Description
    -----------
        This function uses calculate_similarity function to calculate similarity
        value of the data segment against the patten. The function initially 
        slices the data into segments with same length as pattern. Using 
        calculate_similarity function to calculate the similarity of data segments. 
        Then function returns the list of calculated similarity for each data segment.

    Data Dictionary
    ---------------
    data_sliced: [list]
        A list to store sliced data
        
    similarity_list: [list]
        A list to store calculated similairty
    
    Parameters
    ----------
    data_series : [float]
        A list of float values representing a data series.

    pattern : [float]
        A list of float values representing the pattern.

    Returns
    -------
        List of floats
            The list of calculated similarity values.

    """
# Importing function calculate_similarity and equating it to name cs
from calculate_similarity import calculate_similarity as cs

def calculate_similarity_list(data_series, pattern):
    # Empty list for sliced data
    data_sliced = []
    # Loop for range of length of data series
    for i in range(len(data_series)):
        # Slicing data series into segments of pattern width
        data_sliced.append(data_series[slice(i, i + len(pattern))])

    # Empty list for similarity list
    similarity_list = []
    # Loop to check if sliced data is the same length as pattern
    for j in range(len(data_sliced)):
        if len(data_sliced[j]) == len(pattern):
            # If it is meets the criteria in if statement, then it 
            # Calculates the similairity and stores it in a list
            similarity_list.append(cs(data_sliced[j], pattern))

    return similarity_list

