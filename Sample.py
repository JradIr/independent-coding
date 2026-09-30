def check_access_level(level):
    if level >= 3:
        print("Access Granted: Administrator privileges active.")
    else:
        print("Access Limited: Standard user privileges active.")
    return level

def select_environment():
    env = input("Target deployment environment (production, staging, or dev): ").strip().lower()
    
    match env:
        case "production":
            print("Connecting to Production Server (us-east-1)...")
        case "staging":
            print("Connecting to Staging Server (us-west-2)...")
        case "dev":
            print("Connecting to Local Development Cluster...")
        case _:
            print("Error: Unrecognized environment. Defaulting to safe-mode...")
            env = "safe-mode"
            
    return env

def main():
    sysadmin_name = input("Enter sysadmin username: ").strip()
    print(f"Authentication initiated for user: {sysadmin_name}")

    while True:
        try:
            clearance = int(input("Enter security clearance level (1-5): "))
            break
        except ValueError:
            print("Invalid input: Clearance level must be a numeric value.")
            
    active_level = check_access_level(clearance)
    target_env = select_environment()

    print(f"\n--- Deployment Summary ---")
    print(f"User: {sysadmin_name}")
    print(f"Clearance Level: {active_level}")
    print(f"Target Environment: {target_env}")
    print("--------------------------")

if __name__ == "__main__":
    main()
print("Session terminated.")
