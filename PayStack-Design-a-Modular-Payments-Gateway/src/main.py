from flask import Flask, request, jsonify
from payments.upi import UPIProcessor
from payments.card import CardProcessor
from webhooks.handler import handle_webhook
from logs.logger import Logger

app = Flask(__name__)
logger = Logger()

@app.route('/payment/upi', methods=['POST'])
def upi_payment():
    data = request.json
    try:
        processor = UPIProcessor()
        payment_response = processor.initiate_payment(data)
        return jsonify(payment_response), 200
    except Exception as e:
        logger.log_error(f"UPI Payment Error: {str(e)}")
        return jsonify({"error": "Payment initiation failed"}), 500

@app.route('/payment/card', methods=['POST'])
def card_payment():
    data = request.json
    try:
        processor = CardProcessor()
        payment_response = processor.initiate_payment(data)
        return jsonify(payment_response), 200
    except Exception as e:
        logger.log_error(f"Card Payment Error: {str(e)}")
        return jsonify({"error": "Payment initiation failed"}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        handle_webhook(data)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        logger.log_error(f"Webhook Handling Error: {str(e)}")
        return jsonify({"error": "Webhook processing failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)