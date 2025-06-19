# Simple Calculator

A web-based calculator built with Python and Flask. It performs basic arithmetic operations (addition, subtraction, multiplication, division) and is responsive for both desktop and mobile devices.

<img height="100px" width="100%" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHh4aDhsMHF6dmI4b3pybWR2bWlhdDJ2dXI0bzBjanAxaDdtZzdzZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/TIj8cbzWYKnE9ul3ab/giphy.gif"  />

## Features

* Supports basic arithmetic: `+`, `-`, `×`, `÷`.
* Responsive design for desktop and mobile browsers.
* Error handling for invalid inputs and division by zero.

<img height="100px" width="100%" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHh4aDhsMHF6dmI4b3pybWR2bWlhdDJ2dXI0bzBjanAxaDdtZzdzZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/TIj8cbzWYKnE9ul3ab/giphy.gif"  />

## Prerequisites

Before you begin, ensure you have:

* **Python 3.6** or later
* **Flask**: Install via pip (`pip install flask`)

---

## How to Run Locally

Follow these steps to get the calculator running on your local machine:

1.  **Clone this repository**:
    ```bash
    git clone [https://github.com/your-username/simple-calculator.git](https://github.com/your-username/simple-calculator.git)
    cd simple-calculator
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the app**:
    ```bash
    python app.py
    ```
4.  **Open in browser**: Visit `http://127.0.0.1:5000` in your web browser.

    For mobile access, find your PC's IP address (e.g., `192.168.x.x`) using `ipconfig` (Windows) or `ifconfig` (Linux/Mac). Then, visit `http://<PC-IP>:5000` from your phone, ensuring both devices are on the same Wi-Fi network.

---

## Deployment

This Flask application requires a server to run dynamically. GitHub Pages only supports static content, so consider platforms like Render, Railway, or Heroku for deployment.

### Deploying on Render

1.  **Create a free account** at [Render](https://render.com/).
2.  **Create a new Web Service** and connect this GitHub repository.
3.  **Configure settings**:
    * **Runtime**: `Python`
    * **Build Command**: `pip install -r requirements.txt`
    * **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
4.  **Deploy** and access the public URL (e.g., `https://your-app.onrender.com`).

---

## Live Demo

*Replace this with your Render URL after deployment*

---

## Project Structure

simple-calculator/
├── app.py              # Flask app with calculator logic
├── templates/
│   └── index.html      # HTML template for the web interface
├── static/
│   └── styles.css      # CSS for responsive design
├── requirements.txt     # Python dependencies
└── README.md           # This file


---

## Technologies

* Python
* Flask
* HTML/CSS

---

## Screenshots

*Include your screenshots here, perhaps by linking to them or embedding if the platform supports it.*

---

## Contributing

Feel free to fork this repository, submit pull requests, or open issues for improvements!

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
