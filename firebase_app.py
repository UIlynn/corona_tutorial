import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, render_template, jsonify, request

# 플라스크 앱 생성
app = Flask(__name__)

# 인증
cred = credentials.Certificate("firebase_key.json")
default_app = firebase_admin.initialize_app(cred)

# db 연결 - 커서 생성
db = firestore.client()
todo_ref = db.collection('todos') # 커서

# 생성 테스트
# data = {'id': '1', 'title':'Test Content'}
# todo_ref.document('1').set(data)

# 추가
@app.route('/add', methods=['POST'])
def create():
    try:
        # id = data['id']
        print(request.form)
        id = request.form.get('id')
        todo_ref.document(id).set(request.form)
        return {"success": True}, 200
    except Exception as e:
        return f"An Error Occured: {e}"

# 목록 확인
@app.route('/list', methods=['GET'])
def read():
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')    
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"

# 갱신(업데이트 - 기존 값을 수정)
@app.route('/update', methods=['POST', 'PUT'])
def update():
    try:
        id = request.json['id']
        todo_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

# 삭제
@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        todo_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

# port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(threaded=True, host='0.0.0.0', port=port)