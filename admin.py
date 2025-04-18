ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin321"

pending_payments = {}

def check_credentials(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def add_pending_payment(user_id, plan):
    pending_payments[user_id] = plan

def get_pending_payments():
    return pending_payments

def approve_payment(user_id, users_data):
    if user_id in pending_payments:
        plan = pending_payments.pop(user_id)
        users_data[user_id] = {
            "plan": plan,
            "used_free": True
        }
        return True
    return False

def reject_payment(user_id):
    return pending_payments.pop(user_id, None) is not None
