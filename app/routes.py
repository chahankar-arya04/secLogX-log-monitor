from flask import render_template, request, redirect, url_for, flash, session
import os

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'txt', 'log'}

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload():
        if 'logged_in' not in session:
            # For now, allow access without login
            pass

        if 'logfile' not in request.files:
            flash('No file part')
            return redirect('/')
        
        file = request.files['logfile']
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Define keywords and severity levels
            keyword_severity = {
                'failed': 'Medium',
                'unauthorized': 'High',
                'error': 'Low',
                'root': 'Critical',
                'admin': 'High'
            }

            suspicious_lines = []

            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for line in lines:
                    matched = []
                    for keyword, severity in keyword_severity.items():
                        if keyword in line.lower():
                            matched.append({'line': line.strip(), 'severity': severity})
                    suspicious_lines.extend(matched)

            return render_template(
                'analysis.html',
                total_lines=len(lines),
                suspicious=suspicious_lines
            )

        else:
            flash('Invalid file type. Only .txt or .log allowed.')
            return redirect('/')
