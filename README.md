# Gemini AI Vision Quickstart

This PyQt5-based application allows users to upload an image, enter a prompt, and generate a response using Google's Gemini AI Vision model.

## Features

- Image upload and display
- Text prompt input
- AI-generated responses based on image and prompt
- User-friendly GUI

## Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- PyQt5
- Pillow (PIL)
- google-generativeai
- python-dotenv

## Installation

1. Clone this repository:
2. Install the required packages:
3. Obtain a Google API key for the Gemini AI model:
- Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
- Create or select a project
- Generate an API key

4. Create a `.env` file in the project root directory and add your API key: GOOGLE_API_KEY = <"your Google api key">
   
## Usage

1. Run the application
2. Use the "Select Image" button to upload an image.
3. Enter a prompt in the text box.
4. Click "Generate" to get an AI-generated response based on the image and prompt.

## Troubleshooting

If you encounter an error related to the API key:
1. Ensure you have created the `.env` file with the correct API key.
2. Check that the `.env` file is in the same directory as the `main.py` file.
3. Verify that you have installed the `python-dotenv` package.
