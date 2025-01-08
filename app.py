from flask import Flask, render_template, jsonify
from datetime import datetime
from dateutil.relativedelta import relativedelta  # Importa esta librería para cálculos precisos
import os

app = Flask(__name__)

# Define key events and their dates
events = {
    "Rebajas Verano": datetime(2025, 6, 25),
    "Black Friday": datetime(2025, 11, 28),
    "Rebajas Invierno": datetime(2025, 12, 25),
    # Add more events here
}

@app.route('/')
def index():
    now = datetime.now()
    time_until_events = {}
    for event, date in events.items():
        delta = relativedelta(date, now)  # Usa relativedelta para calcular las diferencias exactas
        time_until_events[event] = {
            "months": delta.months,
            "days": delta.days,
            "hours": delta.hours,
            "minutes": delta.minutes,
            "seconds": delta.seconds
        }
    return render_template('index.html', events=time_until_events)

@app.route('/events')
def get_events():
    now = datetime.now()
    # Ordena los eventos por la fecha de manera ascendente
    sorted_events = sorted(events.items(), key=lambda x: x[1])
    
    time_until_events = {}
    for event, date in sorted_events:
        delta = relativedelta(date, now)  # Usa relativedelta para cálculos precisos
        time_until_events[event] = {
            "months": delta.months,
            "days": delta.days,
            "hours": delta.hours,
            "minutes": delta.minutes,
            "seconds": delta.seconds
        }
    
    return jsonify(time_until_events)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
