from bottle import request,route, run, template
import os

@route('/')
def index():
    html = """<html><head><title>Find Pages Relevant To Keyword(s)</title></head>
                <body>
                <div style='width:110%;height:100px;background:#333366;margin-left:-10px;margin-top:-10px;'>
                    <div style='color:#ffffff;font-weight:bold;font-size:20px;padding-top:20px;padding-left:20px;'>
                    Input a csv file with keywords. And you will get all relevant pages for each keyword.</div>
                </div>
                <div style='width:600px;margin-left:auto;margin-right:auto;margin-top:20px;'>
                <form action="/upload" method="post" enctype="multipart/form-data">
                Select a file: <input type="file" name="upload" />
                <input type="submit" value="Find Relevant Pages" /></form>
                </div>
                <div style='width:100%;height:200px;'>
                </div>
                </body></html>"""
    return template(html, name="Name")
                
@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.csv'):
        return 'File extension not allowed.'

    #upload.save('file.jpeg') # appends upload.filename automatically
    return 'OK'

run(host='localhost', port=8080)