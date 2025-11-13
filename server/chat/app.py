from flask import Flask, request, jsonify, render_template
from threading import Thread
import time

app = Flask(__name__)

# 접속 유저와 밴 리스트
users = {}
banned_users = set()
messages = []

# ---------------------------
# 웹 페이지 제공
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html')  # templates/index.html 연결

# ---------------------------
# 메시지 전송
# ---------------------------
@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    user = data.get('user')
    msg = data.get('message')

    if user in banned_users:
        return jsonify({'status': 'error', 'msg': 'You are banned.'})

    messages.append({'user': user, 'message': msg})
    return jsonify({'status': 'success'})

# ---------------------------
# 메시지 수신
# ---------------------------
@app.route('/receive', methods=['GET'])
def receive_messages():
    return jsonify(messages)

# ---------------------------
# 사용자 접속 처리
# ---------------------------
@app.route('/join', methods=['POST'])
def join():
    data = request.get_json()
    user = data.get('user')

    if user in banned_users:
        return jsonify({'status': 'error', 'msg': 'You are banned.'})

    users[user] = time.time()
    return jsonify({'status': 'success'})

@app.route('/leave', methods=['POST'])
def leave():
    data = request.get_json()
    user = data.get('user')
    users.pop(user, None)
    return jsonify({'status': 'success'})

# ---------------------------
# 서버 실행
# ---------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
