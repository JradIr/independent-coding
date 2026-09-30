import time
import random
from datetime import datetime

def simulate_mfa():
    """Simulates a Multi-Factor Authentication process."""
    print("\n--- Multi-Factor Authentication ---")
    # Generate a random 6-digit code to simulate an SMS or token
    correct_code = str(random.randint(100000, 999999))
    print(f"[SYSTEM MESSAGE: Your MFA code is {correct_code}]")
    
    attempts = 3
    while attempts > 0:
        user_code = input("Enter the 6-digit MFA code sent to your device: ").strip()
        if user_code == correct_code:
            print("MFA Verified. Access granted.")
            return True
        else:
            attempts -= 1
            print(f"Invalid code. Attempts remaining: {attempts}")
    
    print("MFA Failed. Security protocol engaged.")
    return False

def check_access_level(level):
    """Verifies user privileges based on clearance level."""
    print("\n--- Privilege Check ---")
    if level >= 5:
        print("Access Granted: Superuser (Root) privileges active.")
    elif level >= 3:
        print("Access Granted: Administrator privileges active.")
    else:
        print("Access Limited: Standard user privileges active.")
    return level

def select_environment():
    """Prompts user to select a deployment environment."""
    print("\n--- Environment Selection ---")
    env = input("Target deployment environment (production, staging, or dev): ").strip().lower()
    
    match env:
        case "production":
            print("Connecting to Production Server (us-east-1)...")
            ip_address = "192.168.1.100"
        case "staging":
            print("Connecting to Staging Server (us-west-2)...")
            ip_address = "192.168.2.50"
        case "dev":
            print("Connecting to Local Development Cluster...")
            ip_address = "127.0.0.1"
        case _:
            print("Error: Unrecognized environment. Defaulting to safe-mode...")
            env = "safe-mode"
            ip_address = "0.0.0.0"
            
    return env, ip_address

def run_pre_deployment_checks(env, ip_address):
    """Simulates checking system health before deployment."""
    print(f"\n--- Running System Checks on {env.upper()} ({ip_address}) ---")
    time.sleep(1) # Simulates a delay while the system checks network/servers
    
    cpu_usage = random.randint(10, 85)
    memory_usage = random.randint(20, 90)
    
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    
    if cpu_usage > 80 or memory_usage > 85:
        print("WARNING: High resource usage detected. Deployment unsafe.")
        return False
        
    print("System checks passed. Environment is stable.")
    return True

def confirm_deployment():
    """Asks for final user confirmation before executing."""
    print("\n--- Deployment Confirmation ---")
    while True:
        choice = input("Proceed with deployment? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please answer 'yes' or 'no'.")

def log_deployment(sysadmin_name, level, env, status):
    """Writes the deployment record to a persistent log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] User: {sysadmin_name} | Clearance: {level} | Env: {env} | Status: {status}\n"
    
    try:
        # 'a' opens the file in append mode so we don't overwrite old logs
        with open("deployment_log.txt", "a") as log_file:
            log_file.write(log_entry)
        print("Deployment successfully logged to 'deployment_log.txt'.")
    except IOError as e:
        print(f"Failed to write to log file: {e}")

def main():
    print("===========================================")
    print("      ENTERPRISE DEPLOYMENT TERMINAL       ")
    print("===========================================\n")
    
    sysadmin_name = input("Enter sysadmin username: ").strip()
    print(f"Authentication initiated for user: {sysadmin_name}")

    if not simulate_mfa():
        print("Session terminated due to security failure.")
        return

    while True:
        try:
            clearance = int(input("\nEnter security clearance level (1-5): "))
            if 1 <= clearance <= 5:
                break
            else:
                print("Clearance must be between 1 and 5.")
        except ValueError:
            print("Invalid input: Clearance level must be a numeric value.")
            
    active_level = check_access_level(clearance)
    
    target_env, ip_address = select_environment()
    
    checks_passed = run_pre_deployment_checks(target_env, ip_address)
    
    if not checks_passed:
        print("\nDeployment aborted due to failed pre-deployment checks.")
        log_deployment(sysadmin_name, active_level, target_env, "FAILED_PRE_CHECK")
        return
        
    if confirm_deployment():
        print("\nDeploying payload...")
        time.sleep(2)
        print("Deployment successful!")
        final_status = "SUCCESS"
    else:
        print("\nDeployment cancelled by user.")
        final_status = "CANCELLED"

    print(f"\n--- Deployment Summary ---")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"User: {sysadmin_name}")
    print(f"Clearance Level: {active_level}")
    print(f"Target Environment: {target_env} ({ip_address})")
    print(f"Final Status: {final_status}")
    print("--------------------------")
    
    log_deployment(sysadmin_name, active_level, target_env, final_status)

if __name__ == "__main__":
    main()
    print("\nSession terminated.")
