from flask import render_template, request
from app import app
#from KaraokeCompass.Song_filter import filter_songs, song_listing
from return_match import return_match
from return_random_match import return_random_match

import pandas as pd

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

#Button Pressed = 0        
@app.route('/validation_button_1')
def button1():
    print(request.args['t1_choice'].split(','))
    if request.args['t1_choice'].split(',')[0][1:] == '1':
        print('user selected on table 1: the recomended results')
    else:
        print('user selected on table 1: the random results')
    return('Thanks!')

#Button Pressed = 0        
@app.route('/validation_button_2')
def button2():
    print(request.args['t2_choice'].split(','))
    if request.args['t2_choice'].split(',')[0][1:] == '2':
        print('user selected on table 2: the recomended results')
    else:
        print('user selected on table 2: the random results')
    return('Thanks!')

    #if request.method == "GET":
    #    return render_template("button.html", ButtonPressed = ButtonPressed)
    #return redirect(url_for('button'))

@app.route('/output_val')
def books_output_val():
    import random
    book_title = request.args.get('book_title')
    book_table = return_match(book_title)

    book_table = return_match(book_title)
    random_book_table = return_random_match()

    true_table = random.choice([1,2])
    if true_table == 1:
        table_1 = book_table
        table_2 = random_book_table
    else:
        table_1 = random_book_table
        table_2 = book_table

    return render_template("output_val_two_tables.html", 
                            table_1=table_1,
                            user_book=book_title,
                            table_2=table_2,
                            true_table = true_table)

@app.route('/about')
def about():
    return render_template("about.html")
