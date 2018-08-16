#!/bin/bash

# Runs the scraper for Goodreads lists that will likely be useful for creating diverse reading lists.

cd GoodreadsScraper

diverse_lists=('11395.Non_Caucasian_Protagonists_in_Science_Fiction_Fantasy_Horror_and_Paranormal_Romance' '203.Native_American_Fiction' '7107.Best_Native_American_Romance' '12763.Best_Native_American_First_Nations_Fiction' '8036.Native_American_Authors' '2508.Favorite_Poets_of_Color' '3739.Teen_Books_With_Native_American_Characters_and_Stories' '338.Immigrant_Experience_Literature' '193.Best_African_American_Books' '27758.Anticipated_Literary_Reads_for_Readers_of_Color_2013' '73078.Diversity_in_Fantasy_and_Science_Fiction' '12800.Best_Black_African_American_Chicklit' '22314.Best_Multicultural_General_Fiction' '3446.African_American_Books_for_Teens' '823.Africa_fiction_and_nonfiction_' '12753.African_Fiction' '48067.Women_Around_the_World' '10961.Fictitious_Africa' '8943.Books_Set_in_Zimbabwe' '12213.Black_Speculative_Fiction' '24317.Plight_of_a_Nation' '71912.Africa_s_100_Best_Books_of_the_20th_Century' '113712.Book_Riot_s_100_Must_Read_Classics_by_People_of_Color' '16436.Arab_Americans_in_Fiction' '338.Immigrant_Experience_Literature' '1336.Best_Middle_East_Fiction' '1337.Best_Middle_East_Nonfiction' '18463.Asian_Fantasy_Science_Fiction' '4323.Iran_and_Iraq_Ancient_and_Modern' '89207.Books_by_LGBTQ_People_of_Color' '76798.Diverse_Horror' '2847.Best_Fiction_With_Disfigured_Disabled_Leads' '8282.Books_with_Disabled_Heros' '10404.Blind_Deaf_Mute' '38493.Characters_with_mental_illnesses_or_learning_disabilites' '756.Best_Books_by_Muslim_Women' '1348.Notable_Books_by_Pakistani_Authors' '18714.1001_Islamic_Books_to_Read_Before_You_Die' '7760.A_Kindle_Muslim_Reading_List' '11481.Islamic_Fiction' '73637.YA_LGBT_Books_Not_Coming_Out_' '91823.Trans_Books_by_Trans_Authors' '653.Best_YA_Fiction_with_GLBTQQI_themes_character' '16026.Diversity_in_Young_Adult_and_Middle_Grade' '3883.Best_Gay_Mystery' '12513.Best_LGBT_Humor' '14155.Latinx_Characters_and_Themes_in_YA' '117159.Latinx_MG_YA_Speculative_Fiction' '118840.2018_books_published_by_for_about_Latinos_Latinas_Latinx' '186.Latino_Latina_Fiction' '2508.Favorite_Poets_of_Color' '14155.Latinx_Characters_and_Themes_in_YA' '23145.Fiction_about_lesbian_bisexual_and_queer_women_of_color' '1341.Best_Asian_American_Teen_Fiction' '42675.Multicultural_New_Adult_Fiction' '46.Best_Feminist_Fiction' '38997.Female_Psychological_Thrillers_Suspense_Written_by_Women' '5401.Strong_Female_Characters_Written_by_Female_Authors' '6934.Science_Fiction_Books_by_Female_Authors')

for((i=0;i<${#diverse_lists[@]};i++))
do
    cmd=$(printf './run_scraper.sh %s 1 1 diverse_%s' ${diverse_lists[$i]} "$i")
    echo $cmd
    eval $cmd
done

cd ..