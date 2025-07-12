from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import io
from weasyprint import HTML, CSS
from generate_resume import generate_resume_html

app = Flask(__name__)
CORS(app)

# In-memory payment store (for simulation)
payments = {}

def verify_payment(user_id, download_type):
    """
    Simulated payment verification for PayPal and M-PESA.
    In a real application, this would involve callbacks from the payment gateways.
    """
    # For simulation, we assume payment is made if the user attempts to download.
    # A real implementation would check a database that is updated by a webhook from PayPal/M-PESA.
    print(f"Verifying payment for {user_id}, type: {download_type}")

    # Simulate different requirements for different tiers
    if download_type == 'premium':
        # Let's say premium requires a specific flag or higher payment amount
        if payments.get(user_id) == 'premium':
            return True
    elif download_type == 'basic':
        if payments.get(user_id) in ['basic', 'premium']:
            return True

    # For this simulation, we'll be permissive. In production, default to False.
    # return False
    return True # Permissive for simulation

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    html_content = generate_resume_html(data)
    return jsonify({'html': html_content})

@app.route('/download', methods=['POST'])
def download_resume():
    data = request.get_json()
    download_type = request.args.get('type', 'basic')
    user_id = data['name']

    if not verify_payment(user_id, download_type):
        return jsonify({"error": "Payment not verified or insufficient for this level."}), 402

    html_string = generate_resume_html(data)

    # No watermark for paid downloads
    pdf = HTML(string=html_string).write_pdf()

    return send_file(
        io.BytesIO(pdf),
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'resume-{download_type}.pdf'
    )

@app.route('/payment/webhook', methods=['POST'])
def payment_webhook():
    """
    Placeholder for a payment webhook from PayPal or M-PESA.
    This endpoint would update the payment status of a user.
    """
    payment_data = request.get_json()
    user_id = payment_data.get('user_id')
    payment_status = payment_data.get('status') # e.g., 'completed'
    amount = payment_data.get('amount')

    if user_id and payment_status == 'completed':
        if amount >= 150:
             payments[user_id] = 'premium'
        elif amount >= 50:
             payments[user_id] = 'basic'
        print(f"Payment status updated for {user_id}: {payments[user_id]}")
        return jsonify({"status": "success"}), 200

    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(debug=True)
