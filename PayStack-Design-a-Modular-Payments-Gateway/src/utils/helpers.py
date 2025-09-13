def generate_unique_id():
    import uuid
    return str(uuid.uuid4())

def validate_payment_data(data):
    required_fields = ['amount', 'currency', 'payment_method']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, "Validation successful"