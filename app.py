from flask import Flask, request, jsonify, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Premium AI</title>
<style>
body{
    margin:0;
    background:#0b0b12;
    color:#fff;
    font-family:Inter,system-ui;
}
h1{
    text-align:center;
    margin-top:120px;
    font-weight:600;
}
.plus{
    position:fixed;
    bottom:22px;
    left:18px;
    width:58px;
    height:58px;
    border-radius:50%;
    border:none;
    font-size:30px;
    color:#fff;
    cursor:pointer;
    background:linear-gradient(135deg,#7f5cff,#3aa9ff);
    box-shadow:0 0 25px rgba(127,92,255,.7);
}
.menu{
    position:fixed;
    bottom:95px;
    left:18px;
    background:#141422;
    border-radius:18px;
    padding:12px;
    width:200px;
    display:none;
    box-shadow:0 20px 40px rgba(0,0,0,.9);
}
.menu button{
    width:100%;
    background:none;
    border:none;
    color:#fff;
    padding:12px;
    text-align:left;
    border-radius:10px;
    cursor:pointer;
}
.menu button:hover{
    background:#1f1f33;
}
input[type=file]{display:none}
</style>
</head>
<body>

<h1>What can I help with?</h1>

<button class="plus" onclick="toggle()">+</button>

<div class="menu" id="menu">
    <button onclick="img()">🖼 Create Image</button>
    <button onclick="file()">📎 Upload File</button>
    <button onclick="search()">🌐 Web Search</button>
    <button onclick="study()">📘 Study & Learn</button>
    <button onclick="quiz()">🧠 Quiz</button>
    <button onclick="research()">🔍 Deep Research</button>
</div>

<input type="file" id="file">

<script>
function toggle(){
    let m=document.getElementById("menu");
    m.style.display=m.style.display=="block"?"none":"block";
}

function img(){ alert("Image generation connected"); }

function file(){
    document.getElementById("file").click();
}

document.getElementById("file").onchange=()=>{
    let f=new FormData();
    f.append("file",file.files[0]);
    fetch("/upload",{method:"POST",body:f})
    .then(r=>r.json()).then(d=>alert(d.msg));
}

function search(){
    fetch("/search",{method:"POST",json:true,
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({q:"AI"})})
    .then(r=>r.json()).then(d=>alert(d.result));
}

function study(){
    fetch("/study",{method:"POST",headers:{'Content-Type':'application/json'},
    body:JSON.stringify({topic:"Physics"})})
    .then(r=>r.json()).then(d=>alert(d.lesson));
}

function quiz(){
    fetch("/quiz",{method:"POST"})
    .then(r=>r.json()).then(d=>alert(d.q));
}

function research(){
    fetch("/research",{method:"POST",headers:{'Content-Type':'application/json'},
    body:JSON.stringify({topic:"AI"})})
    .then(r=>r.json()).then(d=>alert(d.report));
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return Response(HTML, mimetype="text/html")

@app.route("/upload", methods=["POST"])
def upload():
    return jsonify(msg="File uploaded successfully")

@app.route("/search", methods=["POST"])
def search():
    q=request.json.get("q")
    return jsonify(result=f"Live search result for {q}")

@app.route("/study", methods=["POST"])
def study():
    t=request.json.get("topic")
    return jsonify(lesson=f"Full explanation of {t}")

@app.route("/quiz", methods=["POST"])
def quiz():
    return jsonify(q="What is AI? → Machine Intelligence")

@app.route("/research", methods=["POST"])
def research():
    t=request.json.get("topic")
    return jsonify(report=f"Deep research report generated on {t}")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
