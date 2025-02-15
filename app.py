from flask import Flask, render_template_string

app = Flask(__name__)

# Minified and embedded HTML (hides source)
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Editor</title>
    <link rel="icon" href="https://i.ibb.co/JFj2FQfG/logo-editorush-removebg-preview.png" type="image/png">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">
    <style>body {font-family: 'Open Sans', sans-serif; background-color: #121212; color: #eee; text-align: center;}</style>
</head>
<body>
    <h1>Resume Editor</h1>
    <div contenteditable="true" id="textInput" style="border:1px solid #ddd;padding:20px;width:80%;margin:auto;"></div>
    <button onclick="downloadPdf()">Download PDF</button>
    <script>
        function downloadPdf() {
            const text = document.getElementById('textInput').innerText.trim();
            if (!text) { alert("Enter text first!"); return; }
            const { jsPDF } = window.jspdf; const doc = new jsPDF();
            doc.text(text, 10, 10); doc.save("resume.pdf");
        }
    </script>
</body>
</html>"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
