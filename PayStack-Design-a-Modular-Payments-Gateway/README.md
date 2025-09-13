# PayStack: Design a Modular Payments Gateway

## Overview
This project implements a modular payments gateway that supports UPI and card payment flows. It is built using Flask and includes webhook handling and logging functionalities.

## Project Structure
```
PayStack-Design-a-Modular-Payments-Gateway
├── src
│   ├── main.py
│   ├── payments
│   │   ├── upi.py
│   │   ├── card.py
│   │   └── __init__.py
│   ├── webhooks
│   │   └── handler.py
│   ├── logs
│   │   └── logger.py
│   └── utils
│       └── helpers.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd PayStack-Design-a-Modular-Payments-Gateway
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Flask application by executing:
   ```
   python src/main.py
   ```

4. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:5000` to access the payment gateway.

## Payment Flows
- **UPI Payment Flow:** Implemented in `src/payments/upi.py` with methods to initiate and verify payments.
- **Card Payment Flow:** Implemented in `src/payments/card.py` with similar methods for card transactions.

## Webhooks
Webhook events are handled in `src/webhooks/handler.py`. Ensure your server is accessible to receive webhook notifications from payment providers.

## Logging
Logging is set up in `src/logs/logger.py`. Use the `Logger` class to log information and errors throughout the application.

## Common Bugs and Resolutions
- **Issue: Application not starting**
  - Ensure all dependencies are installed correctly. Check for any missing packages in `requirements.txt`.

- **Issue: Payment verification fails**
  - Verify that the payment data is correctly formatted. Use the `validate_payment_data` function from `src/utils/helpers.py` to assist with this.

- **Issue: Webhook not received**
  - Check your server's accessibility and ensure that the webhook URL is correctly configured with the payment provider.

- **Issue: Logs not being generated**
  - Ensure that the logging configuration in `src/logs/logger.py` is set up correctly and that the application has permission to write logs.

## Contributing
Feel free to submit issues or pull requests to improve the project. Your contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.