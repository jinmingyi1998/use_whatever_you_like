from flask import *
import xlrd
import xlwt
import math
import time
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/go', methods=['POST', 'GET'])
def go():
    if request.method == 'POST':
        upload_file = request.files['file']
        filename = str(int(time.time())) + '.xls'
        basepath = 'static/upload/' + filename
        upload_file.save(basepath)
        solve(filename)
        #  return send_from_directory('static/res', filename, as_attachment=True)
        send_from_directory('static/res', filename, as_attachment=True)
        return '<img src=\"static/res/png/' + filename + '.png\"/>' \
                                                         '<a href=\"static/res/' + filename + '\">download</a>'
    else:
        abort(404)


@app.route('/')
def index():
    return render_template('upload.html')


def solve(filename=None):
    print(filename)
    workbook = xlrd.open_workbook('static/upload/' + filename)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])
    writebook = xlwt.Workbook(encoding='ascii')
    writesheet = writebook.add_sheet("Sheet1")
    writesheet.write(0, 0, 'gene_id')
    writesheet.write(0, 1, 'control_sample')
    writesheet.write(0, 2, 'treat_sample')
    writesheet.write(0, 3, 'log_2[FC]')
    x = []
    y = []
    for i in range(sheet.nrows):
        if i == 0:
            continue
        row = sheet.row_values(i)
        control_number = float(row[1])
        treat_sample = float(row[2])
        if control_number == 0:
            result = 0
        else:
            result = round(math.log(treat_sample / control_number, 2), 2)
        writesheet.write(i, 0, row[0])
        writesheet.write(i, 1, control_number)
        x.append(control_number)
        writesheet.write(i, 2, treat_sample)
        y.append(treat_sample)
        writesheet.write(i, 3, result)
    writebook.save('static/res/' + filename)

    def draw(x, y):
        ax = plt.subplot(111)
        plt.scatter(x, y)
        plt.savefig('static/res/png/' + filename + '.png')

    draw(x, y)

    # return 'static/res/' + filename
    return filename


if __name__ == '__main__':
    app.run(host='0.0.0.0')
