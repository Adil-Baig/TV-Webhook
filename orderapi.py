import os, config

def global_var(payload):
    global account
    global api
    global api_key
    global api_secret

    account_id = payload["account"]
    if account_id=='GE3646':
        api_key = os.environ.get('API_KEY_GE3646', config.API_KEY_GE3646)
        api_secret = os.environ.get('API_SECRET_GE3646', config.API_SECRET_GE3646)
    
    else:
        return {
            "success": False,
            "error": f"Account {account_id} not found"
        }
    
    return {
        "success": True
    }

# ================== MAIN ==================


def order(payload: dict):
    #   DEFINE GLOBAL VARIABLE
    glob = global_var(payload)
    
    if not glob['success']:
        return glob
    
    
