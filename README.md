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
| Stretch/Untouched | ProbDistribution | Accuracy |
| --- | --- | --- |
| Stretched | Gaussian | .843 |

Original Cleaned Data:  

RangeIndex: 33099 entries, 0 to 33098  
Data columns (total 18 columns):  
| Category | Count | Type |
| --- | --- | --- |
| Genres | 33099 | non-null object |

Tags|33099|non-null object  
appid|33099|non-null int64  
average_2weeks|33099|non-null int64  
average_forever|33099|non-null int64  
developer|33099|non-null object  
initialprice|33077|non-null object  
llOwners|33099|non-null float64  
median_2weeks|33099|non-null int64  
median_forever|33099|non-null int64  
name|33099|non-null object  
negative|33099|non-null int64  
positive|33099|non-null int64  
price|33070|non-null object  
publisher|33099|non-null object  
score_rank|33099|non-null object  
ulOwners|33099|non-null float64  
userscore|33099|non-null int64  
dtypes: float64(2), int64(8), object(8)  
memory usage: 4.5+ MB  

Further Cleaned Data:  

RangeIndex: 33099 entries, 0 to 33098  
Data columns (total 8 columns):  
Category|Count|Type  
------------|------------|------------  
name|33099|non-null object  
Genres|33099|non-null object  
Tags|33099|non-null object  
average_forever|33099|non-null int64  
price|33099|non-null int64  
llOwners|33099|non-null float64  
ulOwners|33099|non-null float64  
Like/Dislike Ratio|32623|non-null float64  
dtypes: float64(3), int64(2), object(3)  
memory usage: 2.0+ MB  
