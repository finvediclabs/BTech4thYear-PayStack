def handle_webhook(event):
    """
    Handle incoming webhook events from the payment gateway.
    
    Args:
        event (dict): The webhook event data.
    
    Returns:
        str: A response message indicating the result of the processing.
    """
    event_type = event.get('type')

    if event_type == 'payment.success':
        # Process successful payment
        # Add your logic here
        return "Payment processed successfully."
    
    elif event_type == 'payment.failed':
        # Process failed payment
        # Add your logic here
        return "Payment failed. Please try again."
    
    elif event_type == 'refund.processed':
        # Process refund
        # Add your logic here
        return "Refund processed successfully."
    
    else:
        return "Unknown event type."