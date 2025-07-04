users = []      
projects = []   

def register():
    print("=== Register ===")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")
    
    if password != confirm_password:
        print("Passwords do not match! Please try again.")
        return
    
    mobile = input("Enter Mobile Number (Egyptian): ")
    if not (mobile.startswith("01") and len(mobile) == 11 and mobile.isdigit()):
        print("Invalid Egyptian mobile number. Please try again.")
        return
    
    users.append({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "mobile": mobile
    })
    print(f"User {first_name} registered successfully!")

def login():
    print("=== Login ===")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome back, {user['first_name']}!")
            return user
    print("Invalid email or password. Please try again.")
    return None

def create_project(user):
    print("=== Create New Project ===")
    title = input("Enter Project Title: ")
    details = input("Enter Project Details: ")
    total_target = input("Enter Total Target (EGP): ")
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")
    
    project = {
        "owner_email": user["email"],
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date
    }
    
    projects.append(project)
    print(f"Project '{title}' created successfully!")

def view_projects(user):
    print(f"=== Projects of {user['first_name']} ===")
    user_projects = [p for p in projects if p["owner_email"] == user["email"]]
    if not user_projects:
        print("No projects found.")
        return
    
    for i, p in enumerate(user_projects, start=1):
        print(f"\nProject #{i}")
        print(f"Title: {p['title']}")
        print(f"Details: {p['details']}")
        print(f"Total Target: {p['total_target']} EGP")
        print(f"Start Date: {p['start_date']}")
        print(f"End Date: {p['end_date']}")

def edit_project(user):
    user_projects = [p for p in projects if p["owner_email"] == user["email"]]
    if not user_projects:
        print("No projects to edit.")
        return
    
    print("=== Edit Project ===")
    for i, p in enumerate(user_projects, start=1):
        print(f"{i}. {p['title']}")
    choice = input("Choose project number to edit: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(user_projects):
        print("Invalid choice.")
        return
    
    project = user_projects[int(choice) - 1]
    
    print("Leave blank if you don't want to change the field.")
    new_title = input(f"Enter new title ({project['title']}): ")
    new_details = input(f"Enter new details ({project['details']}): ")
    new_total_target = input(f"Enter new total target ({project['total_target']}): ")
    new_start_date = input(f"Enter new start date ({project['start_date']}): ")
    new_end_date = input(f"Enter new end date ({project['end_date']}): ")
    
    if new_title:
        project['title'] = new_title
    if new_details:
        project['details'] = new_details
    if new_total_target:
        project['total_target'] = new_total_target
    if new_start_date:
        project['start_date'] = new_start_date
    if new_end_date:
        project['end_date'] = new_end_date
    
    print("Project updated successfully!")

def delete_project(user):
    user_projects = [p for p in projects if p["owner_email"] == user["email"]]
    if not user_projects:
        print("No projects to delete.")
        return
    
    print("=== Delete Project ===")
    for i, p in enumerate(user_projects, start=1):
        print(f"{i}. {p['title']}")
    choice = input("Choose project number to delete: ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(user_projects):
        print("Invalid choice.")
        return
    
    project = user_projects[int(choice) - 1]
    projects.remove(project)
    print(f"Project '{project['title']}' deleted successfully!")

# ✅ دالة البحث عن المشاريع بالتاريخ
def search_projects_by_date():
    print("=== Search Projects by Date ===")
    search_date = input("Enter date to search (YYYY-MM-DD): ")
    
    found = False
    for project in projects:
        if project["start_date"] == search_date or project["end_date"] == search_date:
            found = True
            print(f"\nTitle: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Target: {project['total_target']} EGP")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print("-" * 30)
    
    if not found:
        print("No projects found for this date.")

def main():
    while True:
        print("\n--- Welcome to Crowdfunding App ---")
        print("1. Register")
        print("2. Login")
        print("3. Search Projects by Date")  
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Create Project")
                    print("2. View My Projects")
                    print("3. Edit Project")
                    print("4. Delete Project")
                    print("5. Logout")
                    user_choice = input("Choose an option: ")
                    if user_choice == "1":
                        create_project(user)
                    elif user_choice == "2":
                        view_projects(user)
                    elif user_choice == "3":
                        edit_project(user)
                    elif user_choice == "4":
                        delete_project(user)
                    elif user_choice == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option, try again.")
        elif choice == "3":
            search_projects_by_date()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
