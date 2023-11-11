#!/usr/bin/env python3
import argparse
import os
import logging

try:
    import psutil        
except ModuleNotFoundError:
    print("ERROR: psutil package not found: pip install psutil")
    exit(1)


# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

LIMIT_TIME_CPU_DEFAULT = 600
LIMIT_TIME_REAL_DEFAULT = 1200


def calculate_odoo_config(cpus, ram, limit_time_cpu, limit_time_real, cron_worker=1):
    http_workers = cpus - 1
    memory_soft_limit_gb = (ram / 2) / (http_workers + cron_worker)
    memory_hard_limit_gb = memory_soft_limit_gb + 1
    
    memory_soft_limit_bytes = int(memory_soft_limit_gb * 1024**3)
    memory_hard_limit_bytes = int(memory_hard_limit_gb * 1024**3)
    
    odoo_conf = f'''
workers = {http_workers}
cron_workers = {cron_worker}

; Customize the Odoo timeouts
limit_time_cpu = {limit_time_cpu}
limit_time_real = {limit_time_real}

; Customize the Odoo memory limits
limit_memory_hard = {memory_hard_limit_bytes}
limit_memory_soft = {memory_soft_limit_bytes}

; Other configurations can be added below as needed
'''
    return odoo_conf.strip()

def get_args():
    parser = argparse.ArgumentParser(description="Calculate Odoo configuration.")
    parser.add_argument("--cpu", help="Number of CPUs", type=int)
    parser.add_argument("--ram", help="Amount of RAM in GB", type=float)
    parser.add_argument("--limit-time-cpu", help="Limit time CPU (default to 600)", type=int, default=LIMIT_TIME_CPU_DEFAULT)
    parser.add_argument("--limit-time-real", help="Limit time real (default to 1200)", type=int, default=LIMIT_TIME_REAL_DEFAULT)
    parser.add_argument("--output", help="Output file path to write the configuration")
    parser.add_argument("--self", action='store_true', help="Run quietly and use the current machine's resources")
    return parser.parse_args()

def prompt_for_value(prompt_message, default_value):
    try:
        return int(input(prompt_message) or default_value)
    except ValueError:
        logging.warning("Invalid input. Using default value.")
        return default_value

def confirm_overwrite(file_path):
    if os.path.exists(file_path):
        return input(f"The file {file_path} already exists. Do you want to overwrite it? [no/Yes]: ").lower() in ['yes', 'y']
    return True

def is_path_writable(file_path):
    if os.path.exists(file_path):
        return os.access(file_path, os.W_OK)
    else:
        parent_dir = os.path.dirname(file_path) or '.'
        return os.access(parent_dir, os.W_OK)

def get_system_resources():
    try:
        cpus = psutil.cpu_count(logical=False)
        ram_gb = round(psutil.virtual_memory().total / (1024**3))
        return cpus, ram_gb
    except NameError:
        print("Please install psutil: pip install psutil")
        exit(1)
        

def main():
    args = get_args()

    # Determine if we should run quietly and fetch system resources
    if args.self:
        cpus, ram = get_system_resources()
        limit_time_cpu = args.limit_time_cpu or LIMIT_TIME_CPU_DEFAULT
        limit_time_real = args.limit_time_real or LIMIT_TIME_REAL_DEFAULT
        logging.info(f"Running with current system's resources: {cpus} CPUs and {ram} GB RAM.")        
        valid_limits = True

    else:
        cpus = args.cpu if args.cpu else int(input("Enter the number of CPUs: "))
        ram = args.ram if args.ram else float(input("Enter the amount of RAM in GB: "))
        limit_time_cpu = args.limit_time_cpu
        limit_time_real = args.limit_time_real
        valid_limits = False

    while not valid_limits:
        # Only prompt for time limits if not provided via command line arguments
        if limit_time_cpu == LIMIT_TIME_CPU_DEFAULT and limit_time_real == LIMIT_TIME_REAL_DEFAULT:
            customize_limits = input(f"Do you want to customize the time limits? (current: cpu={limit_time_cpu}, real={limit_time_real}) [yes/No]: ").lower() in ['yes', 'y']
            if customize_limits:
                limit_time_cpu = prompt_for_value(f"Enter the value for limit_time_cpu (or press Enter to keep current value {limit_time_cpu}): ", limit_time_cpu)
                limit_time_real = prompt_for_value(f"Enter the value for limit_time_real (or press Enter to keep current value {limit_time_real}): ", limit_time_real)
        
        # Check if limit_time_cpu is smaller than limit_time_real
        if limit_time_cpu >= limit_time_real:
            print("The CPU time limit must be smaller than the real time limit. Please adjust the values.")
            # Reset to defaults to allow reprompting
            limit_time_cpu = LIMIT_TIME_CPU_DEFAULT
            limit_time_real = LIMIT_TIME_REAL_DEFAULT
        else:
            valid_limits = True

    odoo_config = calculate_odoo_config(cpus, ram, limit_time_cpu, limit_time_real)

    # Print the configuration to stdout
    print(odoo_config)

    # Handle the output file path if provided
    output_path = args.output
    if output_path:
        if not is_path_writable(output_path):
            logging.error(f"The path {output_path} is not writable. Please check the permissions or choose another path.")
            return
        
        if confirm_overwrite(output_path):
            with open(output_path, 'w') as file:
                file.write(odoo_config)
                if not args.self:
                    logging.info(f"Configuration written to {output_path}")
        else:
            if not args.self:
                logging.info("Operation cancelled by user. Configuration not written to file.")

if __name__ == "__main__":
    main()
