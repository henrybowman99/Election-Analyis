# Election Analysis

## Overview of Project

Utilizing daily data on 12 stocks in the alternative energy industry from the years 2017 and 2018, I sought to create a table displaying each stocks total volume for the respective year as well as each stocks annual return. With this information, I am able to draw conclusions on the past performance of each individual stock while also gathering a synopsis of the overall performance of the entire alternative energy sector.

##Results

As you can see from the All Stocks (2018) and All Stocks (2017) workbooks below, the group of stocks collectively faired far better in 2017 compared to 2018. This conclusion is most evident by seeing that 11 of the 12 stocks experienced positive returns in 2017 while just 2 of the 12 stocks increased in value during the year 2018. 

![All Stocks (2017)](https://user-images.githubusercontent.com/95651156/149394512-24bf583b-0dbb-4edf-9618-6a6eaae09545.png)

![All Stocks (2018)](https://user-images.githubusercontent.com/95651156/149398798-c59a28f6-dbb4-4f93-ae22-0b83e147309b.png)


The only stock to experience a negative return in 2017 wast TerraForm Power Operating (TERP), and while this stock dropped in value, the 7.2% decline is relatively minor compared to some of the substantial drops seen in the 2018 table. That being said, however, the fact that TERP was unable to capitalize on an apparent 2017 boom in the alternative energy sector suggests that it might not be the safest or smartest company to invest in going forward.

On the other end of the spectrum, the only two companies to reach a positive return in 2018 were Enphase Energy (81.9%) and Sunrun (84%) . These companies increasing their stock price while other firms in their sector experienced declines as high as 62.6% suggests that they may be capable of resisting negative shocks to the alternative energy sector in the future. 

There isn't an obvious conclusion to be reached when obsergving the total daily volume of the 12 stocks in 2017 and 2018. 7 of the stocks saw higher total volume in 2018 compared to 2017 while 5 of the stocks were traded less frequently. Given that the total volume of the overall sector remained relatively steady, I can conclude that the sector didn't change very much from a volatility standpoint from year to year.

In attempt to inmprove the run time of the stock analysis, I refactored my original code. Before refactoring the code, the algorithm was such that for every new ticker, the subroutine scanned every single row of the stocks data (either the 2017 or 2018 sheet). After refactoring, the subroutine was made more efficient in that it required just one total scan through the data. Instead of going back to the first row of data when moving to the next ticker, the refactored subroutine holds the current row and updates the ticker index to the next integer. More specifically, within the original code, the ticker is updated and then a for loop is executed to check every row starting from the first row of data. The below image shows this process.![Original Code screenshot](https://user-images.githubusercontent.com/95651156/149425346-e53f72ba-86db-405e-aa3a-6c9e645ff9d0.png). 

In the refactored code, the ticker index is instead updated within the for loop that runs through each row of the data. This process is showed in the below code.
![Refactored Code Screenshot](https://user-images.githubusercontent.com/95651156/149425823-ea831ab7-a7f4-491f-a3b8-863f3d7ab226.png).

This change, while subtle, lowered the run time of the subroutine substantially:

Run Times with Original Code

![Slow_2017](https://user-images.githubusercontent.com/95651156/149425958-9d1cc09b-c081-41ef-be83-024f53e09574.png)
![slow 2018](https://user-images.githubusercontent.com/95651156/149425968-bca91c0a-1b26-475c-b4df-efc6e1f9eb5d.png)


Run Times With Refactored Code

![VBA_Challenge_2017](https://user-images.githubusercontent.com/95651156/149425996-193f77af-16a5-4464-b98d-eb16dce67785.png)
![VBA_Challenge_2018](https://user-images.githubusercontent.com/95651156/149426011-d56e38e1-084d-45cf-9f19-d165e12fef24.png)

The above images show that the refactored code ran in approximately 1/5 the amount of time as the original code.

##Summary

There are both advantages and disadvantages to refactoring code. The obvious advantage, as discussed in the previous section, is that refactoring code can lower the run time of the subroutine. This is especially important when the subroutine has a significant run time to begin with. If the runtime was origally multiple minutes, for example, refactoring the code could lead to saving minutes, if not hours, when running the subroutine in the long run. However, this advantage is far less meaningful when talking about subroutines such as my stock analysis that already ran in less than one sec. The time that refactoring the code saved is extremely marginal considering that less than one second is saved every time the subroutine is ran.

The main disadvantage of refactoring code is that it requires the coder to put more time and energy into creating the subroutine without changing the algorithm's overall output. If refactoring the code is unlikely to save much time when the subroutine is ran later, the coder should consider if it's worth it to take the time to refactor. In my case, refactoring the code for the 12-stock analysis required far more time than it saved me. However, if I was trying to run the subroutine on a data set that held signifigantly more stocks, the refactoring I executed would likely be worthwile because of the substantial lowering of the run time.
