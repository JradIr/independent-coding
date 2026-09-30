# IMPORTING LIBRARIES NEEDED FOR THIS SCRIPT
import time # for time.sleep()
import random # for random numbers
from datetime import datetime # for getting the current date and time
import sys # sys module for exiting
import os # might need this later for os.system commands
import math # imported just in case we need math later

# GLOBAL VARIABLES
global_deployment_status = "NOT_STARTED"
admin_users_list = ["admin", "root", "sysadmin", "superuser"] # list of valid admins

# I learned Object Oriented Programming in my last semester so I made a class for the User!
class SystemAdministratorUserObject:
    def __init__(self, username, clearance_level=1):
        # constructor method
        self.username = username
        self.clearance_level = clearance_level
        self.is_authenticated = False

    # GETTERS AND SETTERS - best practice!
    def get_username(self):
        return self.username
        
    def set_username(self, new_name):
        self.username = new_name
        
    def get_clearance_level(self):
        return self.clearance_level
        
    def set_clearance_level(self, new_level):
        self.clearance_level = new_level

    def get_is_authenticated(self):
        return self.is_authenticated
        
    def set_is_authenticated(self, status):
        self.is_authenticated = status


def cool_loading_animation():
    # StackOverflow showed me how to do this progress bar
    print("Initializing Enterprise Framework...")
    for i in range(1, 101):
        if i % 20 == 0: # only print every 20 percent so it doesn't spam
            print(f"Loading modules... {i}%")
            time.sleep(0.5)
    # print("DEBUG: done loading")
    print("System Ready!\n")

def simulate_mfa():
    # function to simulate multi factor authentication
    print("\n--- Multi-Factor Authentication ---")
    
    # Generate a random 6-digit code
    correct_code = str(random.randint(100000, 999999))
    print(f"[SYSTEM MESSAGE: Your MFA code is {correct_code}]")
    
    attempts_variable = 3
    
    while attempts_variable > 0:
        user_code = input("Enter the 6-digit MFA code sent to your device: ")
        
        # trim whitespace just in case
        user_code = user_code.strip()
        
        if user_code == correct_code:
            print("MFA Verified. Access granted.")
            return True
        else:
            attempts_variable = attempts_variable - 1
            if attempts_variable > 0:
                print("Invalid code. Attempts remaining: " + str(attempts_variable))
            else:
                print("Invalid code. You have 0 attempts left.")
                
    print("MFA Failed. Security protocol engaged.")
    return False

def check_access_level(level):
    # checks if they are admin or superuser
    print("\n--- Privilege Check ---")
    
    if level == 5 or level > 5:
        print("Access Granted: Superuser (Root) privileges active.")
        return level
    elif level == 3 or level == 4:
        print("Access Granted: Administrator privileges active.")
        return level
    elif level == 1 or level == 2:
        print("Access Limited: Standard user privileges active.")
        return level
    else:
        # fallback
        return 1

def select_environment():
    # match/case is confusing so I used if/elif/else instead
    print("\n--- Environment Selection ---")
    env = input("Target deployment environment (production, staging, or dev): ")
    env = env.strip()
    env = env.lower()
    
    if env == "production":
        print("Connecting to Production Server (us-east-1)...")
        ip_address = "192.168.1.100"
    elif env == "staging":
        print("Connecting to Staging Server (us-west-2)...")
        ip_address = "192.168.2.50"
    elif env == "dev":
        print("Connecting to Local Development Cluster...")
        ip_address = "127.0.0.1"
    else:
        print("Error: Unrecognized environment. Defaulting to safe-mode...")
        env = "safe-mode"
        ip_address = "0.0.0.0"
            
    # returning a tuple
    return env, ip_address

def run_pre_deployment_checks(env, ip_address):
    # checks cpu and ram
    print("\n--- Running System Checks on " + env.upper() + " (" + ip_address + ") ---")
    time.sleep(1) # fake delay
    
    cpu_usage = random.randint(10, 85)
    memory_usage = random.randint(20, 90)
    
    print("CPU Usage: " + str(cpu_usage) + "%")
    print("Memory Usage: " + str(memory_usage) + "%")
    
    if cpu_usage > 80:
        print("WARNING: High CPU resource usage detected.")
        return False
    
    if memory_usage > 85:
        print("WARNING: High Memory resource usage detected.")
        return False
        
    print("System checks passed. Environment is stable.")
    return True

def confirm_deployment():
    # asks if user wants to continue
    print("\n--- Deployment Confirmation ---")
    choice = input("Proceed with deployment? (yes/no): ")
    
    if choice == "yes":
        return True
    elif choice == "y":
        return True
    elif choice == "no":
        return False
    elif choice == "n":
        return False
    else:
        print("You didn't type yes or no so I am cancelling just to be safe.")
        return False

def log_deployment(sysadmin_name, level, env, status):
    # logs the output
    time_now = datetime.now()
    timestamp_string = str(time_now.year) + "-" + str(time_now.month) + "-" + str(time_now.day) + " " + str(time_now.hour) + ":" + str(time_now.minute)
    
    log_entry = "[" + timestamp_string + "] User: " + sysadmin_name + " | Clearance: " + str(level) + " | Env: " + env + " | Status: " + status + "\n"
    
    try:
        log_file = open("deployment_log.txt", "a")
        log_file.write(log_entry)
        log_file.close() # don't forget to close!
        print("Deployment successfully logged to 'deployment_log.txt'.")
    except Exception as e: # catch all exceptions
        print("Failed to write to log file.")

def log_deployment_backup(sysadmin_name, level, env, status):
    # TODO: Refactor this later. I made a backup log just in case the first file gets deleted
    # My professor said backups are important.
    time_now = datetime.now()
    log_entry = str(time_now) + " - " + sysadmin_name + " - " + str(level) + " - " + env + " - " + status + "\n"
    
    try:
        backup_file = open("backup_deployment_log_v2.txt", "a")
        backup_file.write(log_entry)
        backup_file.close()
    except Exception as e:
        pass # ignore errors for the backup

# MAIN FUNCTION
def main():
    print("*******************************************")
    print("*                                         *")
    print("*      ENTERPRISE DEPLOYMENT TERMINAL     *")
    print("*             Version 1.0                 *")
    print("*                                         *")
    print("*******************************************\n")
    
    cool_loading_animation()
    
    # get user input
    user_input_name = input("Enter sysadmin username: ")
    
    # create the OOP object
    current_user = SystemAdministratorUserObject(user_input_name)
    
    print("Authentication initiated for user: " + current_user.get_username())

    mfa_result = simulate_mfa()
    if mfa_result == False:
        print("Session terminated due to security failure.")
        sys.exit() # force exit the program

    # loop until they type a valid number
    is_valid_number = False
    while is_valid_number == False:
        try:
            clearance_string = input("\nEnter security clearance level (1-5): ")
            clearance_int = int(clearance_string) # cast to integer
            
            if clearance_int >= 1 and clearance_int <= 5:
                current_user.set_clearance_level(clearance_int)
                is_valid_number = True
            else:
                print("Clearance must be between 1 and 5.")
        except Exception:
            # this catches if they type a word instead of a number
            print("Invalid input: Clearance level must be a numeric value.")
            
    active_level = check_access_level(current_user.get_clearance_level())
    
    # unpacking tuple
    target_env, ip_address = select_environment()
    
    checks_passed = run_pre_deployment_checks(target_env, ip_address)
    
    if checks_passed == False:
        print("\nDeployment aborted due to failed pre-deployment checks.")
        log_deployment(current_user.get_username(), active_level, target_env, "FAILED_PRE_CHECK")
        log_deployment_backup(current_user.get_username(), active_level, target_env, "FAILED_PRE_CHECK")
        sys.exit()
        
    confirmation = confirm_deployment()
    
    if confirmation == True:
        print("\nDeploying payload...")
        time.sleep(2)
        print("Deployment successful!")
        global_deployment_status = "SUCCESS"
    else:
        print("\nDeployment cancelled by user.")
        global_deployment_status = "CANCELLED"

    # print final output screen
    print("\n--- Deployment Summary ---")
    print("Timestamp: " + str(datetime.now()))
    print("User: " + current_user.get_username())
    print("Clearance Level: " + str(active_level))
    print("Target Environment: " + target_env + " (" + ip_address + ")")
    print("Final Status: " + global_deployment_status)
    print("--------------------------")
    
    log_deployment(current_user.get_username(), active_level, target_env, global_deployment_status)
    log_deployment_backup(current_user.get_username(), active_level, target_env, global_deployment_status)

# this makes sure it only runs if it's the main file
if __name__ == "__main__":
    main()
    print("\nSession terminated.")
