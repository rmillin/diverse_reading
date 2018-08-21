# diverse_reading
In progress development of an application to suggest books by international and diverse authors with similar themes to classic reading list books.

### progress
1. Scraping book lists from Goodreads:
- scrape_goodreads_lists.sh is a  bash script that calls a package to download book data from Goodreads based on Listopia lists (https://github.com/havanagrawal/GoodreadsScraper.git).  The following lists are used:

<b>minority and international lists:</b>
<li>12716.Speculative_Fiction_by_Authors_of_Color</li>
<li>116887.2018_Books_by_Authors_of_Color_Native_Authors</li>
<li>113712.Book_Riot_s_100_Must_Read_Classics_by_People_of_Color</li>
<li>96119._ReadPOC_List_of_Books_by_Authors_of_Color</li>
<li>83339.Women_s_Fiction_by_Strong_Women</li>
<li>22135.Around_the_World_One_Book_from_Each_Country</li>
<li>4283.Around_the_World_in_100_Books</li>
<li>5534.Non_American_books_that_every_American_should_read</li>
<li>90194.Women_in_Translation</li>
<li>71912.Africa_s_100_Best_Books_of_the_20th_Century</li>
<li>73176.African_Writers_Series</li>
<li>95678.Multicultural_Female_Authors</li>
<li>31853.Iranian_Fiction</li>
These are saved in files with names diverse_N_01_25.json where N = 0:12, respectively
<p> </p>

<b>young adult minority and international:</b>
<li>104750.Young_Adult_books_with_chronically_ill_physically_or_mentally_disabled_protagonists</li>
<li>84609.South_Asians_in_Contemporary_YA</li>
<li>100873.Anticipated_Diverse_2016_2017_YA_Books</li>
<li>94201.MG_YA_Speculative_Fiction_by_Authors_of_Color</li>
<li>97984.South_Africa_in_YA_Middle_Grade_Fiction</li>
<li>92685.International_YA_Books</li>
<li>104480.Internationally_Minded_YA_Books</li>
These are saved in files with names diverse_ya_N_01_25.json where N = 0:6
<p> </p>

<b>likely assigned books lists:</b>
<li>3751.A_Journey_Through_Literary_America</li>
<li>1126.John_Steinbeck</li>
<li>9370.Best_of_Hemingway_</li>
<li>5465.Best_of_Mark_Twain</li>
<li>21652.Best_of_William_Faulkner</li>
<li>74999.Historical_Novels_of_Early_America</li>
<li>36785.WWII_Historic_Fiction</li>
<li>68.Best_European_Literature</li>
<li>10785.The_French_Revolution</li>
<li>3990.Greatest_Eastern_European_Classics</li>
<li>1339.Best_British_and_Irish_Literature</li>
<li>1077.Modern_British_Novels</li>
<li>2457.Best_Books_Of_The_Decade_1880s</li>
<li>4509.Oh_Canada_</li>
<li>2458.Best_Books_Of_The_Decade_1860s</li>
<li>5464.Best_of_Charles_Dickens</li>
These are saved in files with names western_N_01_25.json where N = 0:15
<p> </p>

<b>likely assigned young adult:</b>
<li>18678.Best_UKYA_Books</li>
<li>7170.Young_Adult_fiction_by_UK_authors</li>
These are saved in files with names western_ya_N_01_25.json where N = 0:1
<p> </p>

2. Data processing
- process_data.ipynb contains a first look at the data from one of the lists.  The descriptions have a problem where some lines are duplicated.  I'm not sure if it makes sense to try to chop these off or just use unique words, or...?

