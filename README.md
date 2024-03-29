# Modernizing Old Code to New Code - Family Slot Machine

[![Lyons Slots Demo](http://img.youtube.com/vi/bGcdEW6fYlA/0.jpg)](http://www.youtube.com/watch?v=bGcdEW6fYlA)


## Modernizer

The Modernizer is a Python script that uses OpenAI's GPT-3 to analyze, convert to pseudocode, and generate modern code from legacy code. It's located in the [modernizer](modernizer/) directory.

### Usage

To use the Modernizer, you need to provide the GitHub repository, path to the file in the repository, and the branch name. The script will fetch the code, analyze it, convert it to pseudocode, and generate modern code in Python using Flask.

```sh
python app.py
```

Backend
The backend of the new app is a Flask application generated by the Modernizer. It's located in the new-app directory.

Usage
To run the backend, you need to install the required packages and then run the Flask application.

```sh
pip install -r requirements.txt
python app.py
```

Frontend
The frontend of the new app is a React application. It's located in the frontend directory.

Usage
To run the frontend, you need to install the required packages and then start the React application.


```sh
npm install
npm start
```

Open http://localhost:3000 to view it in your browser.

Building for Production
To build the app for production, run the following command:

```sh
npm run build
```

This will create a build folder with the production-ready app.

