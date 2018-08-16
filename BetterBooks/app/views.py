from flask import render_template, request
from app import app
#from KaraokeCompass.Song_filter import filter_songs, song_listing
from return_match import return_match
from return_random_match import return_random_match

from pathlib import Path
import datetime as dt

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
        print('user selected on table 1: the recommended results')
        record_validation_answer(True)
    else:
        print('user selected on table 2: the random results')
        record_validation_answer(False)
    return('Thanks!')

#Button Pressed = 0        
@app.route('/validation_button_2')
def button2():
    print(request.args['t2_choice'].split(','))
    if request.args['t2_choice'].split(',')[0][1:] == '2':
        print('user selected on table 2: the recommended results')
        record_validation_answer(True)
    else:
        print('user selected on table 1: the random results')
        record_validation_answer(False)
    return('Thanks!')

    #if request.method == "GET":
    #    return render_template("button.html", ButtonPressed = ButtonPressed)
    #return redirect(url_for('button'))

# Input: df (pd.DataFrame)
# Returns: that DataFrame with any columns containing 'Unnamed' removed.
def remove_unnamed_cols(df):
    unnamed_cols = [col for col in df.columns if col.find('Unnamed') != -1]
    return df.drop(unnamed_cols, 1)

# Function that stores validation choices in a CSV file
def record_validation_answer(correct, book_title='', validation_log='validation_log.csv'):
    if not Path(validation_log).exists():
        new_row_df = pd.DataFrame({'time': [dt.datetime.now()], 'correct': [correct], 'title': [book_title]})
        new_row_df.to_csv(validation_log)
    else:
        log_df = remove_unnamed_cols(pd.read_csv(validation_log))
        log_df.loc[len(log_df)] = [dt.datetime.now(), correct, book_title]
        log_df.to_csv(validation_log)

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
