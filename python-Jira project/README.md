
---
# Jira API Integration with Python, Flask & GitHub Webhooks

This project demonstrates how to integrate **Python** with the **Jira Cloud REST API**, expose functionality using **Flask**, and connect it with **GitHub Webhooks** for automation.
It contains two scripts:

1. **Flask API for Creating Jira Issues** (`create-jira.py`)
2. **Standalone Script for Listing Jira Projects** (`list-projects.py`)

---

## 📂 Python file structure

```
.
├── create-jira.py   # Flask app to create Jira issues (GitHub webhook target)
├── list-projects.py   # Script to fetch & display Jira projects
└── README.md
```

---

## 🚀 Features

### `create-jira.py` → Flask Jira Issue Creator (Webhook Receiver)

* Runs a Flask server on `0.0.0.0:5000`.
* Exposes `/createJira` endpoint (`POST`).
* Can receive **GitHub Webhook events** (e.g., `push`, `ping`) and trigger Jira issue creation.
* Sends a REST API call to Jira to create a new issue.
* Returns the Jira API response in JSON format.

### `list-projects.py` → Jira Project Fetcher

* Makes a GET request to Jira Cloud API.
* Authenticates using `requests` and `HTTPBasicAuth`.
* Fetches all Jira projects in your workspace.
* Prints project names in the terminal.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create & activate virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install dependencies

```bash
pip install requests flask
```

### 4. Configure API Token

* Generate a Jira API token from [Atlassian API Tokens](https://id.atlassian.com/manage/api-tokens).
* Replace the `API_TOKEN` variable in both files with your token.
* Update the Jira email ID (" ") if required.

---

## ▶️ Running the Scripts

### Run Flask app (`create-jira.py`)

```bash
python create-jira.py
```

* Server will start at: `http://0.0.0.0:5000/`

#### GitHub Webhook Integration

1. Deploy `create-jira.py` Flask app on your EC2 instance.
2. Expose port `5000` (security group rules).
3. In your **GitHub repository settings → Webhooks**, add:

   * **Payload URL**: `http://<your-ec2-public-ip>:5000/createJira`
   * **Content type**: `application/json`
   * Choose events (`push`, `issues`, etc.).
4. On a push event, GitHub will `POST` to your Flask API, and a Jira ticket will be created.

### Run project fetcher (`list-projects.py`)

```bash
python list-projects.py
```

* Prints all available Jira project names.

---

## 🛠 Tools & Libraries Used

* **Python 3.x** 🐍
* **Flask** → API endpoint
* **Requests** → REST API communication
* **HTTPBasicAuth** → Authentication with Jira Cloud API
* **Jira Cloud API** → Issue creation & project listing
* **GitHub Webhooks** → Event-driven Jira automation
* **AWS EC2** → Hosting Flask app for external webhook access

---

## 📌 Notes

* Ensure your Jira site URL (`https://<your-domain>.atlassian.net`) is correct.
* Replace project key (`SCRUM`) and issue type ID (`10003`) in `create-jira.py` as per your Jira project configuration.
* Configure your EC2 instance security group to allow **port 5000** inbound traffic.
* Keep your API token secure — do not commit it to public repositories.

---


