from flask import Flask, render_template, send_file, request
from chess_opening_berserk import opening_times_played, extract_stats, collect_speed
import pandas as pd
import json
import plotly
import plotly.express as px
import berserk
from datetime import datetime
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__, template_folder='templates')

@app.route('/image/<filename>')
def image(filename):
    return send_file(f'static/{filename}')

@app.route('/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        username = request.form['username']
        df, games = extract_stats(username)
        total_games = len(games)

        fig1 = px.pie(df, values='Count', names='Result')
        graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

        dd = collect_speed(games, username)
        fig2 = px.bar(dd, x=["blitz", "rapid", "classical", "bullet"], y=['wins', 'draws', 'losses'],
                     title='Wins, Draws, and Losses for Each Category')
        graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

        qq = dd
        fig3 = go.Figure(data=[go.Pie(labels=['blitz', 'rapid', 'classical', 'bullet'],
                                     values=[qq['total']['blitz'], qq['total']['rapid'], qq['total']['classical'],
                                             qq['total']['bullet']])])
        graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('result.html', username=username, graph1JSON=graph1JSON, graph2JSON=graph2JSON,
                               graph3JSON=graph3JSON, total=total_games)

    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8003)
