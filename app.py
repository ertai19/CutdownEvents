from flask import Flask, render_template, jsonify
from datetime import datetime
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
        delta = date - now
        time_until_events[event] = {
            "months": delta.days // 30,
            "days": delta.days % 30,
            "hours": delta.seconds // 3600,
            "minutes": (delta.seconds % 3600) // 60,
            "seconds": delta.seconds % 60
        }
    return render_template('index.html', events=time_until_events)

@app.route('/events')
def get_events():
    now = datetime.now()
    # Ordena los eventos por la fecha de manera ascendente
    sorted_events = sorted(events.items(), key=lambda x: x[1])
    
    time_until_events = {}
    for event, date in sorted_events:
        delta = date - now
        time_until_events[event] = {
            "months": delta.days // 30,
            "days": delta.days % 30,
            "hours": delta.seconds // 3600,
            "minutes": (delta.seconds % 3600) // 60,
            "seconds": delta.seconds % 60
        }
    
    return jsonify(time_until_events)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
