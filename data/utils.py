from register.utils import create_background_color


def create_task_dic(request_data):
        task_dic = {
            "title": request_data["title"],
            "description": request_data["description"],
            "category": request_data["category"],
            "subtask": request_data["subtask"],
            "due_date": request_data["dueDate"],
            "prio": request_data["prio"],
            "assigned_to": request_data["assignTo"],
            "processing_status": request_data["processingStatus"],
        }
        return task_dic
    
def create_contact_dic(request_data):
    contact_dic = {
        "username": request_data["username"],
        "email": request_data["email"],
        "firstname": request_data["firstname"],
        "lastname": request_data["lastname"],
        "name_abbreviation": request_data["nameAbbreviation"],
        "background_color": create_background_color(request_data["firstname"][0], request_data["lastname"][0]),
        "checked": request_data["checked"],
        "phone": request_data["phone"],
        "has_account": request_data["hasAccount"],
    }
    return contact_dic
    