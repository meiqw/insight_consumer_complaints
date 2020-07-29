# Consumer Complaints

## Table of Contents
1. [Problem](README.md#problem)
1. [Approach](README.md#approach)
1. [Running_Instructions](README.md#running_instructions)

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies. 

**For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

## Approach
The complaints_analysis.py under src directory does the analysis of the input csv file under input directory.

The file is mainly consists of two functions, the read_csv function reads into the input csv file and the write_csv function does the data analysis and writes the output into the output file under output directory.

Under insight_testsuite directory, I added two more tests test_2 and test_3 with some sample data from the complaints.csv posted on the GitHub.

## Running Instructions
The 'run.sh' shell script executes my code and outputs the results to an output file report.csv under output directory.

