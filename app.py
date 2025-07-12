from flask import Flask, render_template, request, jsonify, send_file
from generate_resume import generate_resume_data
from weasyprint import HTML
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

import csv

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    with open('emails.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['email']])
    resume_data = generate_resume_data(data)
    return jsonify(resume_data)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    template = data.get('template', 'classic')
    template_name = f'resume_template_{template}.html'
    try:
        rendered_template = render_template(template_name, data=data)
    except:
        rendered_template = render_template('resume_template.html', data=data)

    pdf = HTML(string=rendered_template).write_pdf()
    return send_file(
        io.BytesIO(pdf),
        mimetype='application/pdf',
        as_attachment=True,
        download_name='resume.pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
