import json
from joblib import PrintTime
from app import app
from flask import render_template,request, Response
import language_tool_python  
from urllib.parse import unquote
import json
@app.route("/api/corrections")
def getCorrections():
    my_tool = language_tool_python.LanguageTool('en-US')  
    # given text  
    my_text = request.args.get("text")
    my_text = unquote(my_text)
    correctedText = my_tool.check(my_text)
    response = []
    for match in correctedText:
        response.append(str(match))
    resp = Response(json.dumps({"correction":response}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-type'] = 'application/json'
    return resp
