from flask import render_template, request
from app import app
#from KaraokeCompass.Song_filter import filter_songs, song_listing
from return_match import return_match

@app.route('/')
@app.route('/input')
def books_input():
    return render_template("input.html")


@app.route('/output')
def books_output():
 
    book_title = request.args.get('book_title')
    book_table = return_match(book_title)

    # if isinstance(results, int):
    #     if results == 1:
    #         return render_template("error.html")
    #     elif results == 2:
    #         return render_template("redo.html")
    #book_title = book_table
        # User's song information
        # url = string + original_song['uri'].values[0] + "&theme=white"
        # user_song = dict(Song=original_song['Song_x'].values[0], 
        #              Artist=original_song['Artist'].values[0], 
        #              Suggested_key='Original Key', 
        #              Low_note=original_song['New_Low_Note'].values[0], 
        #              High_note=original_song['New_High_Note'].values[0], 
        #              uri=url)
        
        # Results song information
        # for i in range(len(results)):
        #     url = string + results.iloc[i]['uri'] + "&theme=white"
        #     songs.append(dict(Song=results.iloc[i]['Song_x'], 
        #                       Artist=results.iloc[i]['Artist'], 
        #                       Suggested_key = results.iloc[i]['Suggested_key'], 
        #                       Low_note=results.iloc[i]['New_Low_Note'], 
        #                       High_note=results.iloc[i]['New_High_Note'], 
        #                       uri=url))
        
    return render_template("output.html", book_recs=book_table, 
                               user_book=book_title)
        
@app.route('/about')
def about():
    return render_template("about.html")
