global valid
valid = False
repeat = True
def validation(email):
    feedback = []
    if " " in email:
        feedback.append("No spaces in the email.")
    if "@" not in email:
        feedback.append("Email must contain '@'")
    if "." not in email:
        feedback.append("Email must contain '.'")
    if not email.strip():
        feedback.append("Email cannot be blank.")
        print(feedback,
              email[-1])
    return feedback if feedback else "valid"


def file_validation(filename):
    result = []
    file = open(filename, "r")
    for lineNumber, email in enumerate(file, start=1):
        email = email.strip()
        feedback = validation(email)
        result.append((lineNumber, email, feedback))
    return result

while repeat == True:
    print(
        " Email Validator:\n",
        "Options:\n",
        "1. Validate singular email\n",
        "2. Validate list of emails from a file\n",
        "3. Exit\n"
        )
    choice = input("Chose option:\t").strip()
    if choice == "1":
        email = input("Enter email: ").strip()
        feedback = validation(email)
        if "valid" in feedback:
            print(f"Valid email: {email}")
        else:
            print(f"Invalid Email: {email} fix {feedback}")
    elif choice == "2":
        filename = input("Enter Filename: ").strip()
        results = file_validation(filename)
        if results:
            for lineNumber, email, feedback in results:
                print(f"Line {lineNumber}: {email}")
                if feedback != "valid":
                    for msg in feedback:
                        print(f"   - {msg}")
                else:
                    print(f"  - Valid")
    elif choice == "3":
        repeat = False
        print("Exiting program...")
    else:
        print("Invalid Choice.")