from register.utils import create_background_color
from .models import AddTaskItem

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


def filter_assigned_to_logged_user(user_id):
    found_tasks = []
    allTasks = AddTaskItem.objects.all()
    for task in allTasks:
        assigned_to = task.assigned_to
        if not assigned_to or any(assignment['id_user'] == user_id for assignment in assigned_to):
            found_tasks.append(task)
    return found_tasks
