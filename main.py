# -*- codeing = utf-8 -*-
# @Time : 2021/7/15 11:07
# @Author : songdk
# @File : main.py
# @Software: PyCharm

from flask import Flask, send_file
import css

app = Flask(__name__)


@app.route("/css")
def gen_docx():
    template = '1.docx'
    signature = 'signature.png'
    document = css.from_template(template, signature)
    document.seek(0)

    return send_file(
        document, mimetype='application/vnd.openxmlformats-'
                           'officedocument.wordprocessingml.document', as_attachment=True,
        attachment_filename='2.docx')


if __name__ == "__main__":
    app.run(debug=True)
