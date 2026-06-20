def send_critical_alert(error_code, message):
    """Triggers an external notification (SMS/Email)."""
    print(f"CRITICAL ALERT [{error_code}]: {message}")
    # Integration with Twilio or SendGrid would go here
  
