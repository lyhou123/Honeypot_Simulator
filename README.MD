# Honeypot Simulator

This project is a simple **Honeypot Simulator** built with **Python**, **Flask**, **SQLite**, and **requests**. The goal is to create a fake login page that records malicious activity such as failed login attempts or unauthorized access. This simulator helps in detecting and logging potential attackers trying to interact with the web server.

## Features

- Fake login page (`/login`) to capture login attempts.
- Restricted access page (`/admin`) to simulate unauthorized access.
- All activities are logged to an SQLite database (`honeypot.db`), including:
  - IP address
  - Endpoint visited
  - User-Agent
  - Form data (e.g., submitted username, password)
  - Timestamp of the activity

## Admin page (`/admin`) and (`/login`) to view logs of all recorded activities.
- Basic authentication for the admin page to restrict access to authorized users only.
- Simple HTML interface for the login page and admin page.
- Logging of all requests to the SQLite database for analysis.
- running this command to see all who route to the admin page and their ip address.

```bash
localhost:5000/logs
```


## Technologies Used

- **Python**: The main programming language.
- **Flask**: A lightweight Python web framework.
- **SQLite**: A built-in database to store logs.
- **requests**: Python library for making HTTP requests (added to dependencies).
- **HTML**: For the login page interface.

## Getting Started

### Prerequisites

Make sure you have **Python 3** installed on your machine.

### Install Dependencies

1. Clone the repository:

```bash
git clone https://github.com/lyhou123/Honeypot_Simulator.git
cd Honeypot_Simulator
pip install -r requirements.txt

