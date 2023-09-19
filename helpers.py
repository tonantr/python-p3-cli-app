import datetime

def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_cost(cost_string):
    if cost_string.isdigit():
        return True
    else:
        return False
    
def is_valid_id(id_string):
    if id_string.isdigit():
        return True
    else:
        return False

    



    
