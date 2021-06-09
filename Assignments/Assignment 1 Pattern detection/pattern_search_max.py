#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
    Author
    ------
        Roman Takhovskiy (zID: 5364695)

    Purpose
    -------
        To find the maximum similarity value of data which is greater or equal 
        to the theshold and to return the index of the maximum similarity value.

    Description
    -----------
        The function searches maximum similarity value of data which is greater 
        or equal to the theshold and to return the index of the maximum similarity 
        value. Firstly, function checks if data is greater or equal than pattern, 
        if not then returns an error, "Insufficient data". Then it calcuates
        the similarity measure for the data using calculate_similarity_list
        function and store it in a variable, similarity. If similarity value
        is greater than threshold, then take the maximum value and return it's
        index.

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

    threshold : [float]
        A float value. Selected similarity measure needs to be greater than or
        equal to the given threshold value.

    Returns
    -------
    "Insufficient data" : [String]
        If the given data_series is shorter than the given pattern.

    "Not detected" : [String]
        If all the similarity measures are (strictly) less than the given
        threshold value.

    integer
        Index of the highest similarity measure that is also greater than
        or equal to the given threshold value.
    """

# Importing calculate_similairty_list funciton as csl
from calculate_similarity_list import calculate_similarity_list as csl

def pattern_search_max(data_series, pattern, threshold):
    # Statement to check if length of data is greater or equal to length of pattern
    if len(data_series) >= len(pattern):
        # Calculating similairty list and storing it
        similarity = csl(data_series, pattern)
        # Loop for lenght of similairty
        for i in range(len(similarity)):
            # Checking if similarity value is greater than threshold
            if similarity[i] > threshold:
                # Finding the hihest similarity and assigning it to a variable
                search_max = similarity.index(max(similarity))
            # If all the similairty is less than threshold then return "Not detected"
            else:
                search_max = "Not detected"
    # If length of data is smaller than length of pattern then return an "Insufficient data"
    else:
        search_max = "Insufficient data"
    
    return search_max

