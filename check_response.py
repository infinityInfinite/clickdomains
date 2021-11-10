def check_response(domain,excepted_res=200):
    req = requests.get(domain)
    if req.status_code == 200:
        return f"{req.status_code} SUCESSFUL"
    elif req.status_code == 404:
        return f"{req.status_code} FORBIDDEN"
    elif req.status_code == 101:
        return f"{req.status_code} SWITCHING PROTOCOL"
    elif req.status_code == 103:
        return f"{req.status_code} EARLY HINTS"
    elif req.status_code == 201:
        return f"{req.status_code} CREATED"
    elif req.status_code == 202:
        return f"{req.status_code} ACCEPTED"
    elif req.status_code == 204:
        return f"{req.status_code} NO CONTENT"
    elif req.status_code == 301:
        return f"{req.status_code} MOVED PREMANENTLY"
    elif req.status_code == 302:
        return f"{req.status_code} FOUND"
    elif req.status_code == 400:
        return f"{req.status_code} BAD REQUEST"
    elif req.status_code == 401:
        return f"{req.status_code} Unauthorized"
    elif req.status_code == 402:
        return f"{req.status_code} PAYMENT REQUIRED"
    elif req.status_code == 404:
        return f"{req.status_code} NOT FOUND"
    else:
        return req.status_code

    
def check_statuscode(domain,ignored):        
    if domain[:4] == "http":                 
        res = requests.get(domain)           
    else:                                    
        res = requests.get("https://"+domain)
                                             
    if res.status_code in ignored:           
        return False                         
    elif res.status_code == 404:             
        return False                         
    else:                                    
        return True                          
