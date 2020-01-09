# steam-game-sales-data
EDA.ipynb
FreeGames.ipynb
FreeIndieGames.ipynb
PaidGames.ipynb
PaidIndieGames.ipynb contain the visualization for the data

PaidByPrice and PaidByPriceIndie contain visualization for earnings

hypothesis*** files contain the testing whether certain genres are more popular

graphs contains all the png files of plots

steamspyScrape.ipynb contains the scraping code

helpers.py contains helper functions

clean.json is the clean data in a json folder

toDo.txt is just for brainstorming ideas.

# Data Info

Original Cleaned Data:  
![Cleaned Data](/graphs/Cleaned.png)

Further Cleaned Data:  
![Further Cleaned Data](/graphs/FurtherCleaned.png)

# How the Data is Organized

Each graph file contains graphs for different categories  
**Example (Free Indie Games):** 
![a](/graphs/FreeIndieGames/OwnersByGenre.png)  
Can see many action owners  
  
![a](/graphs/FreeIndieGames/GamesByGenre.png)  
Can see many action games, so maybe that's why there are so many owners  

![a](/graphs/FreeIndieGames/AvgOwnersByGenre.png)  
MMO seems to have a very high average owners for the amount of total owners, worth looking into  

![a](/graphs/FreeIndieGames/NewOwnersByGenre.png)  
We can see sports are not a very good indie type game 

![a](/graphs/FreeIndieGames/AvgNewOwnersByGenre.png)  
MMOs still dominate the average new owners, due to the large outliers

Before we look into and compare the interesting genres, we remove all games that have 0 owners.  
![a](/graphs/FreeIndieGames/freeIndie0count.png)
We see that adventure and action have a lot of games that do not get played.  

Now we compare the top 3 categories, action, strategy, and adventure, ignoring MMO because it seems like only the super popular ones get played.  
![a](/graphs/FreeIndieGames/action_adventure_strategy.png)  
We can see in all the graphs action tends to get more owners, and adventure does a little better than strategy.

**We now hypothesis test whether action/adventure/mmo are better than the other genres:**  
All tests are Mann Whitney U Tests ran with games having 0 owners being removed  

*H0*: Action has the same amount of owners as other Genres  
*H1*: Action have a greater amount of owners than other Genres  

p-value: 0.0029052114451273664  
power: 0.9999999533757833  
*Conclusion*: Reject H0 and determine that Action games tend to have a greater amount of owners than games from other genres  

*H0*: Adventure has the same amount of owners as other Genres  
*H1*: Adventure have a greater amount of owners than other Genres  

p-value: 0.2862187839884423
power: 0.5729919570177814 
*Conclusion*: Fail to Reject H0 and determine that Adventure games could have on average the same amount of owners as games from other genres  

*H0*: MMO has the same amount of owners as other Genres  
*H1*: MMO have a greater amount of owners than other Genres  

p-value: 1.0107732291236831e-07
power: 0.9994968474730219
*Conclusion*: Reject H0 and determine that Action games tend to have a greater amount of owners than games from other genres  

*H0*: MMOs has the same amount of owners as Action Games 
*H1*: MMOs have a greater amount of owners than Action Games  

p-value: 0.0018082954517863268
power: 0.084115420632348
*Conclusion*: Reject H0 and determine that MMO games tend to have a greater amount of owners than Action games, but this could easily be false due to the very lower power level  

**Looking at Tags**  
![a](/graphs/FreeIndieGames/OwnersByTag.png)  
![a](/graphs/FreeIndieGames/GameByTag.png)  
![a](/graphs/FreeIndieGames/AvgOwnersByTag.png)  
![a](/graphs/FreeIndieGames/NewOwnersByGenre.png)  
![a](/graphs/FreeIndieGames/AvgNewOwnersByGenre.png)  

Tags are harder to analyze due to the nature of games having the same tags over and over and being able to have many different types of tags, such as most open world games being sandbox, fps being first-person, etc.

We can see that PvE games do very well but seem to be hard to create because there are not many of them. We also see that co-op and open world games also tend to do very well, but these games are also overlap a lot.  

This type of analysis is done on all 4 different types of games, Free Indie, Free non-Indie, Paid Indie, and Paid non-Indie, with all the graphs being provided in the graphs folder and hypothesis testing provided in the corresponding notebook.


