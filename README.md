# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes case.
2. Get a complete list of candidates who receieved votes.
3. Calculate the total number of votes each candidate receieved. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary 
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham receieved 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette receieved 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane receieved 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Overview of Election Audit
This challenge utilized Python to analyze a large election data set and assess: vote counts, winning candidates and county totals. This data was then written into a text file for ease of readability. This analysis is intended to clearly and concisely share the results of the local election and allow for insight into how different counties and therefore districts fared. This insight into voting patterns allows all readers to easily understand what voter turnout looks like based on county as well as understand where future campaigns should be focused.

## Election Audit Results
- How many votes were cast in this congressional election?
  - There were a total of 369,711 votes cast in this election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
![county votes](https://user-images.githubusercontent.com/102930649/166179580-815ea3a7-f92a-498b-ae16-052a3d34d9a5.png)
- Which county had the largest number of votes?
  - Denver County had the largest number of votes.
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
![total counts](https://user-images.githubusercontent.com/102930649/166179591-782a56f0-c722-44e4-8c20-bc7bde8071ed.png)
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana DeGette won the election with 272,892 votes which was 73.8% of the total votes. 

Deliverable One:
![Deliverable 1](https://user-images.githubusercontent.com/102930649/166180174-a7ba729a-826d-4c89-9b62-2053ef3664d0.png)
Deliverable Two:
![Deliverable 2](https://user-images.githubusercontent.com/102930649/166180347-5314213d-da85-43b3-8758-1f29f6e962cb.png)

## Election Audit Summary
In short, as a result of this audit it is clear that Diana DeGette won the election by a landslide. The script created for this audit can be easily repurposed for future elections as long as voter ID, county and candidate names are available. Some potential ideas for how this script could be reused include: school board elections as it would allow you to see where the highest and lowest concentration of turnouts are to help guide future campaigning as well as for local mayoral races. Being that campaign spend can be such a crucial part of campaigning, having insight from a script like this can save candidates large sums of money. If one were to reuse this script for a school board election, it is recommended that one were to filter by local school instead of county. If one were to reuse this script for a local mayoral election, it is recommended that instead of looking by county, to instead filter by district. This insight would prove more helpful as a mayor would only be looking within one county. 
