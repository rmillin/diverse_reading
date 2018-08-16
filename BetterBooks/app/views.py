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
        
    return render_template("output.html", book_recs=book_table, 
                               user_book=book_title)

@app.route('/validation')
def books_input_val():
    return render_template("input_val.html")


@app.route('/output_val')
def books_output_val():
    book_title = request.args.get('book_title')
    book_table = return_match(book_title)

    return render_template("output_val.html", book_recs=book_table,
                           user_book=book_title)


@app.route('/about')
def about():
    return render_template("about.html")
