#!/bin/bash

# Runs the scraper for Goodreads lists that will likely be useful for creating diverse reading lists.

cd GoodreadsScraper

diverse_lists=('12716.Speculative_Fiction_by_Authors_of_Color' '116887.2018_Books_by_Authors_of_Color_Native_Authors' '113712.Book_Riot_s_100_Must_Read_Classics_by_People_of_Color' '96119._ReadPOC_List_of_Books_by_Authors_of_Color' '83339.Women_s_Fiction_by_Strong_Women' '22135.Around_the_World_One_Book_from_Each_Country' '4283.Around_the_World_in_100_Books' '5534.Non_American_books_that_every_American_should_read' '71912.Africa_s_100_Best_Books_of_the_20th_Century' '90194.Women_in_Translation' '73176.African_Writers_Series' '95678.Multicultural_Female_Authors' '31853.Iranian_Fiction')

diverse_ya_lists=('104750.Young_Adult_books_with_chronically_ill_physically_or_mentally_disabled_protagonists' '84609.South_Asians_in_Contemporary_YA' '100873.Anticipated_Diverse_2016_2017_YA_Books' '94201.MG_YA_Speculative_Fiction_by_Authors_of_Color' '97984.South_Africa_in_YA_Middle_Grade_Fiction' '92685.International_YA_Books' '104480.Internationally_Minded_YA_Books')

western_classics_lists=('3751.A_Journey_Through_Literary_America' '1126.John_Steinbeck' '9370.Best_of_Hemingway_' '5465.Best_of_Mark_Twain' '21652.Best_of_William_Faulkner' '74999.Historical_Novels_of_Early_America' '36785.WWII_Historic_Fiction' '68.Best_European_Literature' '10785.The_French_Revolution' '3990.Greatest_Eastern_European_Classics' '1339.Best_British_and_Irish_Literature' '1077.Modern_British_Novels' '2457.Best_Books_Of_The_Decade_1880s' '4509.Oh_Canada_' '2458.Best_Books_Of_The_Decade_1860s' '5464.Best_of_Charles_Dickens')

western_ya_lists=('18678.Best_UKYA_Books' '7170.Young_Adult_fiction_by_UK_authors')

for((i=0;i<${#diverse_lists[@]};i++))
do
    cmd=$(printf './run_scraper.sh %s 1 25 diverse_%s' ${diverse_lists[$i]} "$i")
    echo $cmd
    eval $cmd
done

for((i=0;i<${#diverse_ya_lists[@]};i++))
do
    cmd=$(printf './run_scraper.sh %s 1 25 diverse_ya_%s' ${diverse_ya_lists[$i]} "$i")
    echo $cmd
    eval $cmd
done

for((i=0;i<${#western_classics_lists[@]};i++))
do
    cmd=$(printf './run_scraper.sh %s 1 25 western_%s' ${western_classics_lists[$i]} "$i")
    echo $cmd
    eval $cmd
done

for((i=0;i<${#western_ya_lists[@]};i++))
do
    cmd=$(printf './run_scraper.sh %s 1 25 western_ya_%s' ${western_ya_lists[$i]} "$i")
    echo $cmd
    eval $cmd
done

cd ..