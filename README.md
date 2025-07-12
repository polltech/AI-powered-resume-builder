# AI-Powered Resume Builder

This is a full-stack web application that allows users to generate professional resumes using AI. It features a monetization model with options for free, watermarked previews and paid, clean PDF downloads at basic and premium tiers.

## Features

- **AI-Powered Content:** Generates resume content based on user input.
- **Watermarked Previews:** Free users can see a preview of their resume with a watermark.
- **Tiered PDF Downloads:**
  - **Basic (KSh 50):** Download a clean PDF of your resume.
  - **Premium (KSh 150):** Download a clean PDF with access to more templates and a cover letter (feature stubbed).
- **Multiple Payment Options:** Supports PayPal and includes instructions for M-PESA.
- **Separate Frontend & Backend:** The frontend is a static site, and the backend is a Python Flask API.

## Local Development

### Prerequisites

- Python 3.7+
- `pip` for package installation

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The backend will be running at `http://127.0.0.1:5000`.

### Frontend Setup

1.  **Open `index.html` in your browser:**
    Simply open the `index.html` file directly in a web browser to view the frontend.

2.  **Connect to the backend:**
    Ensure the `fetch` URLs in `static/script.js` point to your running Flask server address (`http://127.0.0.1:5000`).

## Deployment

### Backend on Render.com (Free Tier)

1.  **Sign up for Render:** Create an account at [render.com](https://render.com).

2.  **Create a new Web Service:**
    - Click "New +" and select "Web Service".
    - Connect your GitHub repository where this code is hosted.
    - On the settings page:
      - **Name:** Choose a unique name (e.g., `ai-resume-backend`).
      - **Region:** Choose a region.
      - **Branch:** Select your main branch.
      - **Build Command:** `pip install -r requirements.txt`
      - **Start Command:** `gunicorn app:app` (You'll need to add `gunicorn` to `requirements.txt`)
      - **Instance Type:** `Free`

3.  **Deploy:** Click "Create Web Service". Render will build and deploy your app. You'll get a public URL (e.g., `https://ai-resume-backend.onrender.com`).

4.  **Update Frontend API URLs:** In `static/script.js`, change all `http://127.0.0.1:5000` URLs to your new Render URL.

### Frontend on GitHub Pages

1.  **Go to your repository settings:** On GitHub, navigate to your repository and click "Settings".

2.  **Pages:** In the left sidebar, click "Pages".

3.  **Source:** Under "Build and deployment", select "Deploy from a branch".
    - **Branch:** Choose your main branch and `/ (root)` folder.

4.  **Save:** Click "Save". GitHub will deploy your `index.html`, `static/style.css`, and `static/script.js` files.

5.  **Access your site:** You'll be given a public URL (e.g., `https://<your-username>.github.io/<your-repo-name>/`).

## Monetization

- **PayPal:** The app includes a direct link to a PayPal.me page. For a full integration, you would use PayPal's Developer APIs to create buttons and verify transactions via webhooks.
- **M-PESA:** Instructions are provided for manual payment. A full integration would require using Safaricom's Daraja API to implement STK Push and a webhook to confirm payments. The current implementation simulates this verification.
- **Payment Verification:** The backend has a placeholder `/payment/webhook` endpoint. In a production environment, you would secure this endpoint and have it update a database of paid users. The `/download` endpoint would then check this database before serving a clean PDF.
