from flask import Flask, render_template_string, jsonify
import random, time

app = Flask(__name__)
start_time = time.time()

HTML = '''<!DOCTYPE html>
<html>
<head>
<title>Game Server Dashboard</title>
<style>
body{font-family:Arial;background:#0b1020;color:white;margin:0;padding:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.card{background:#151b34;padding:20px;border-radius:18px;box-shadow:0 8px 24px rgba(0,0,0,.35)}
.value{font-size:32px;font-weight:bold;margin-top:8px}
small{color:#9fb0ff}
h1{margin-bottom:20px}
#logs{height:220px;overflow:auto;white-space:pre-line}
</style>
</head>
<body>
<h1>🎮 Game Server Dashboard</h1>
<div class='grid'>
<div class='card'><small>Status</small><div class='value' id='status'>Online</div></div>
<div class='card'><small>Ping</small><div class='value' id='ping'>0 ms</div></div>
<div class='card'><small>CPU</small><div class='value' id='cpu'>0%</div></div>
<div class='card'><small>RAM</small><div class='value' id='ram'>0%</div></div>
<div class='card'><small>Players</small><div class='value' id='players'>0</div></div>
<div class='card'><small>Uptime</small><div class='value' id='uptime'>0h</div></div>
<div class='card' style='grid-column:1/-1'><small>Live Logs</small><div id='logs'></div></div>
</div>
<script>
async function load(){
 const r = await fetch('/stats');
 const d = await r.json();
 for (const k of ['status','ping','cpu','ram','players','uptime']) document.getElementById(k).innerText=d[k];
 document.getElementById('logs').innerText=d.logs.join('\n');
}
setInterval(load,2000); load();
</script>
</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/stats')
def stats():
    uptime_sec = int(time.time()-start_time)
    h = uptime_sec//3600
    m = (uptime_sec%3600)//60
    logs = [
        'Player connected: user_'+str(random.randint(100,999)),
        'Match started in Arena-'+str(random.randint(1,5)),
        'Latency stable',
        'Autosave completed',
        'Voice chat synced'
    ]
    return jsonify({
        'status':'Online',
        'ping':f"{random.randint(18,55)} ms",
        'cpu':f"{random.randint(25,78)}%",
        'ram':f"{random.randint(40,88)}%",
        'players':random.randint(80,240),
        'uptime':f"{h}h {m}m",
        'logs':logs
    })

if __name__ == '__main__':
    app.run(debug=True)
