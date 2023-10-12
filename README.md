

# Indian Legal Consultation Streamlit App

The Indian Legal Consultation Streamlit App is a simple tool that allows users to get legal advice for various issues by simulating a conversation with an Indian lawyer. This app uses a pre-trained language model from Hugging Face to provide information on relevant Indian acts and rights based on the user's input.

## Getting Started

### Prerequisites

Before running the app, make sure you have Python installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/manas95826/Falcon-7B-Legal
   ```

2. Navigate to the project directory:

   ```bash
   cd Falcon-7B-Legal
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

7. Open a web browser and navigate to [http://localhost:8501](http://localhost:8501) to use the app.

## How to Use

1. Once you've launched the app, you'll see a text area where you can describe your legal issue.

2. Input your legal issue in the text area.

3. Click the "Get Legal Advice" button.

4. The app will generate a response based on your input and provide information on relevant Indian acts and rights.

5. The legal advice will be displayed on the screen.

## Features

- Simulate a conversation with an Indian lawyer to get legal advice.
- Receive information on relevant Indian acts and rights for your specific legal issue.

## About the Model

The app uses a pre-trained language model from Hugging Face to generate legal advice. You can find more information about the model [here](https://huggingface.co/tiiuae/falcon-7b-instruct).

## Authors

- Manas Chopra

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to Hugging Face for providing the pre-trained language model.
- Inspired by real legal consultation scenarios.

