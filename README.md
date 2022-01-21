# Election Analysis 

## Overview of Election Audit
I sought to run an analysis on a csv file holding data from a Colorado congressional race. The first part of the analysis focuses on outputting the counties included in the election, the voter turnout in each county, and which county had the highest voter turnout. The second portion of the analysis sought to identify the candidates up for election, the number of votes each candidate received, the percentage of the total vote received by each candidate, and the overall winner of the election. I used Python 3.7.6 along with Visual Studio Code to perform my election analysis.

## Election Audit Results
The following image displays the output of my election audit code:


![Screen Shot 2022-01-20 at 3 52 57 PM](https://user-images.githubusercontent.com/95651156/150440600-923be978-4b07-4f4b-a3e4-d03fe508c63f.png)

Summary of Election Results:
* There were 369,711 total votes cast in this congressional election
* There were three counties included in the election: Jefferson, Denver, Arapahoe
*	Jefferson accounted for 10.5% of the total vote with 38,855 votes cast, Denver accounted for 82.8% of the total vote with 306,055 votes cast, and Arapahoe accounted for 6.7% of the total vote with 24,801 votes cast.
* With 306,055 votes cast, Denver County cast the largest number of votes out of the three counties included in the election
* There were three candidates who received votes: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane
* Charles Casper Stockham received 23.0% of the votes with 85,213 votes received, Diana DeGette received 73.8% of the vote with 272,892 votes received, and Raymon Anthony Doane received 3.1% of the votes with 11,606 votes received
* Diana DeGette won the election with 272,892 votes, receiving 73.8% of the total vote


## Election Audit Summary
It's important to note that the code I developed for this election analysis can be modified slightly and be applied to essentially any kind of election. Suppose for example that I had a data set that included every vote cast in some state for a United States presidential election. In this scenario, I would first be able to modify the code ever so slightly to key in on each voting district rather than each county. This can be done by changing the counties list and county_votes dictionary in the below code to a voting_district list and district_votes dictionary.


![Screen Shot 2022-01-20 at 4 26 53 PM](https://user-images.githubusercontent.com/95651156/150443723-07db64c6-252d-4cf1-9764-4bee369e167e.png)

Then it is important to modify the code to make sure the for loop is referencing the correct columns when extracting the name of the districts. Since the csv file I used for the Colorado congressional election listed county names in the second column, I used county = row[2] in the for loop as seen below. With the hypothetical presidential dataset, this command would be modified to district = row[#] where # represents the column number in which the district names are listed.


![Screen Shot 2022-01-20 at 4 29 22 PM](https://user-images.githubusercontent.com/95651156/150443798-934ec09b-4221-4514-8230-ce5688d4c926.png)

There are several other analogous adjustments that would need to be made in order to transition from counties to districts, but for the sake of time and simplicity, I will not list all of them here.

One other possible modification I would like to quickly discuss addresses the scenario in which we are provided a dataset of every single vote cast for all 50 states in a presidential election. I could use my current code (along with some simple modifications such as the ones discussed in the previous two paragraphs) and one more for loop to determine the winner of each state. The for loop would run the code for each of the 50 states and then output the winner of each state. Then, to determine the overall winner of the election, I could add code that totals each candidates’ electoral votes based on the number of states he/she won. This could also be easily done with a for loop and nested if statements that iterate through each of the candidates and adds electoral votes to their tally by checking if he/she won a given state.
