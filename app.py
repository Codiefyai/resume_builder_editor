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
    <style>
        body { font-family: 'Open Sans', sans-serif; background: #121212; color: #eee; text-align: center; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: flex-start; min-height: 100vh; }
        .container { max-width: 800px; width: 100%; background: #222; padding: 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
        h1 { color: #00a2ff; text-transform: uppercase; font-size: 24px; }
        #textInput { width: 100%; min-height: 300px; padding: 12px; border: 1px solid #555; border-radius: 6px; font-size: 16px; background: #fff; color: #333; resize: both; overflow: auto; }
        button { padding: 10px 20px; background: #00a2ff; color: white; border: none; font-weight: bold; border-radius: 6px; cursor: pointer; margin-top: 10px; }
        button:hover { background: #007acc; }
        .floating-icon { position: absolute; top: 120px; right: 40px; background: #00a2ff; color: white; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 20px; transition: background 0.3s; }
        .floating-icon:hover { background: #007acc; }
    </style>
</head>
<body oncontextmenu="return false">
    <div class="container">
        <h1>Resume Editor</h1>
        <div id="textInput" contenteditable="true"></div>
        <button onclick="downloadPdf()">Download as PDF</button>
    </div>

    <button class="floating-icon" onclick="pasteResume()"><i class="fas fa-paste"></i></button>

    <script>
        (function() {
            function disableInspect() {
                document.addEventListener("contextmenu", e => e.preventDefault());
                document.addEventListener("keydown", e => {
                    if (e.key === "F12" || (e.ctrlKey && e.shiftKey && (e.key === "I" || e.key === "J")) || (e.ctrlKey && e.key === "U")) {
                        e.preventDefault();
                    }
                });
            }

            function pasteResume() {
                navigator.clipboard.readText().then(text => {
                    document.getElementById('textInput').innerText = text.replace(/[^\w\s.,!?\-]/g, '');
                }).catch(console.error);
            }

            function downloadPdf() {
                let text = document.getElementById('textInput').innerText.trim();
                if (!text) { alert("Enter some text before downloading."); return; }
                let doc = new jsPDF();
                doc.text(text, 10, 10);
                doc.save("resume.pdf");
            }

            disableInspect();
            window.downloadPdf = downloadPdf;
            window.pasteResume = pasteResume;
        })();
    </script>
</body>
</html>"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
