#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Author
    ------
        Roman Takhovskiy (zID: 5364695)

    Purpose
    -------
        To calculate the similairty betwee data segment and the pattern.

    Description
    -----------
        This function calculates the similairity value based on the given 
        data segment and pattern. Initially it checks if length of data
        segment is the same as length of pattern, if not then it returns
        an error. Then value of data segment is multipled with value of 
        pattern and added to the sum of similairty variable.

    Data Dictionary
    ---------------
        similarity : [float]
            Variable to store the simialrity value

    Parameters
    ----------
        data_segment : [float]
            A list of float values to compare against the pattern.

        pattern : [float]
            A list of float values representing the pattern.

    Returns
    -------
        float
            The similarity score/value.

        "Error"
            If data segment and pattern are not the same length.
"""


def calculate_similarity(data_segment, pattern):

    # variable for similarity calculation and was set to 0
    similarity = 0

    # statement to check if length of data segment is equal to length of pattern
    if len(data_segment) == len(pattern):
        # For loop with range of length of data segment
        for i in range(len(data_segment)):
            # calculating similarity and adding it the similarirt variable
            similarity += data_segment[i]*pattern[i]

    # if length of data segment is not equal to length of pattern then return an error
    else:
        similarity = "Error"

    return similarity