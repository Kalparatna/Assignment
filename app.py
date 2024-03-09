from flask import Flask, render_template, request
import fitz  
import spacy

app = Flask(__name__)

nlp = spacy.load('xx_ent_wiki_sm')
nlp.add_pipe('sentencizer')  

def process_pdf(file_path, max_summary_length=500):
    doc = fitz.open(file_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    doc = nlp(text)
    sentences = list(doc.sents)

    total_chars = 0
    summary_sentences = []

    for sent in sentences:
        total_chars += len(sent.text)
        if total_chars <= max_summary_length:
            summary_sentences.append(sent)
        else:
            break

    summary = " ".join(sent.text for sent in summary_sentences)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop][:5]

    return summary, keywords

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    keywords = None

    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.pdf'):
            file_path = f"uploads/{file.filename}"
            file.save(file_path)
            summary, keywords = process_pdf(file_path)

    return render_template('index.html', summary=summary, keywords=keywords)

if __name__ == '__main__':
    app.run(debug=True)
