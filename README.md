# YouTube Web Downloader

A lightweight web application that allows users to download YouTube videos directly from a browser interface.
It provides a simple UI where users can paste multiple video URLs and download them using the powerful **yt-dlp engine**.

This project demonstrates a **Python Flask backend + WebSocket progress updates + modern browser UI**.

---

## Features

* Download **multiple YouTube videos**
* Real-time **download progress**
* **Speed and ETA display**
* **Completed downloads list**
* Simple and responsive **dark UI**
* Built with **Flask + SocketIO + yt-dlp**

---

## Tech Stack

* Python
* Flask
* Flask-SocketIO
* yt-dlp
* HTML / CSS / JavaScript

---

## Project Structure

youtube_web_downloader/

app.py – Flask server
downloader.py – yt-dlp download engine
templates/index.html – web interface
downloads/ – downloaded videos
requirements.txt – dependencies

---

## Installation

Clone the repository.

```bash
git clone https://github.com/ganeshgummalla/youtube-web-downloader.git
cd youtube-web-downloader
```

Create a virtual environment (recommended).

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the server.

```bash
python3 app.py
```

Open the browser.

```
http://127.0.0.1:5000
```

Paste YouTube links and click **Download**.

Downloaded videos will be saved inside the **downloads/** folder.

---

## Screenshots

### Downloader Interface

Paste one or more YouTube links.
<img width="1399" height="629" alt="Screenshot 2026-03-07 at 12 45 17" src="https://github.com/user-attachments/assets/18d812e6-935b-4b62-9e8a-e35e39a548cf" />



### Live Download Progress

The UI shows:

* download percentage
* download speed
* ETA

### Completed Downloads

Downloaded files appear in a list once finished.

---

## Disclaimer

This tool is intended for **educational and personal use only**.
Users are responsible for complying with YouTube's terms of service and copyright laws.

---

## Author

Ganesh Gummalla
