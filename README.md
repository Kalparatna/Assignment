Certainly! Below is a sample README file for your Flask application that you can include in your GitHub repository. Customize it according to your project's specifics.

```markdown
# PDF Summarizer Web App

This web application extracts text from PDF files, performs extractive summarization, and displays a summary along with keywords. It is built using Flask, fitz (PyMuPDF), spacy, and bert-extractive-summarizer.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pdf-summarizer-web-app.git
   ```

2. Change into the project directory:

   ```bash
   cd pdf-summarizer-web-app
   ```


## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

   The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

2. Upload a PDF file using the provided form, and the application will provide a summary and keywords.

## Customization

- Adjust the `max_summary_length` or `ratio` parameter in `app.py` to control the length of the summary.
- Customize the HTML template (`templates/index.html`) for the frontend as needed.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature` or `git checkout -b bugfix/fix-issue`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push your changes to your fork: `git push origin feature/new-feature`.
5. Create a pull request on the main repository.

