'''
 !/usr/bin/env python3
 Path: make.pyc / make.py
 Description: This program will create a good starting point for a python program.
 Author: @Ze7111
 License: MIT
'''
try: # try
    from rich import console; import os, logging, sys, time; import shutil; print = console.Console().print; import random;  # import modules
except: # if error
    import os # import os
    os.system('pip install rich') # install rich
    os.system('pip install shutil') # install shutil
    os.system('pip install random') # install random
    os.system('pip install logging') # install logging
    os.system('pip install sys') # install sys
    os.system('cls' if os.name == 'nt' else 'clear') # clear screen
    os.system('color a' if os.name == 'nt' else 'printf "\033[32m"') # set color to green
    print('Please run the program again.') # print error if file is imported
    exit() # exit program

print('Enter path to projects root dir (leave blank if already in the dir): ', style='bold red', end=''); path = input(); logging_file = f'make.py.log' # set logging file
if path == '':
    path = os.getcwd()
logging.basicConfig(level=logging.NOTSET,filename=logging_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y  %H:%M:%S') # Logging setup
logging.warning('Starting script...'); logging.info(f'Path: {path}')
admin_module_data = r"""'''
 !/usr/bin/env python3
 Path: backend/modules/admin.py
 Description: This file is used to run the program with admin rights.
 Author: @Ze7111
'''

import ctypes, sys # import ctypes and sys
def main(): # main function
    def is_admin(): # check if user is admin
        try: # try
            return ctypes.windll.shell32.IsUserAnAdmin() # check if user is admin
        except: # if the user is not on windows
            return False # if not windows
    if is_admin(): # check if user is admin
        pass # pass
    else: # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) # re-run the program with admin rights"""
basic_handling_data = (r"""'''
 !/usr/bin/env python3
 Path: backend/core/basic_handling.py
 Description: This file is used to innitiate the innit.py file and the logs folder. It also deletes old log files. and makes backups
 Author: @Ze7111
'''

# ====================================================================================== Default imports ======================================================================================
import sys, os, time, logging, shutil, tarfile; from rich import console; print = console.Console().print # import basic modules and rich                                                     |
log_datetimefmt = time.strftime('%d-%m-%Y %H-%M-%S',time.localtime(time.time())) # set log datetime format                                                                                    |
logging_file = f'logs/{log_datetimefmt}.log' # set logging file                                                                                                                               |
# =============================================================================================================================================================================================

# ====================== Global Variables ======================
rundone = False # set rundone to false                         |
rundone2 = False # set rundone2 to false                       |
#                                                              |
logging_maxFiles = 5 # set max number of log files             |
max_backups = 4 # set max backups to 10                        |
#                                                              |
this_file = os.path.basename(__file__) # get name of this file |
log_folder_name = f'{os.getcwd()}/logs/' # set log folder name |
# ==============================================================

# ================================================================================ Logging Setup ================================================================================
logging.basicConfig(level=logging.NOTSET,filename=logging_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%y  %H:%M:%S') # Logging setup |
# ===============================================================================================================================================================================


class file_actions():  # log_file_actions class
    def count_log_files(directory): # count log files function
        global rundone # set rundone to global
        if rundone is not True: # if rundone is not true
            logging.info(f'count_log_files function is starting in file {__file__}') # log that count_log_files function is starting
        try: # try
            list_of_files = os.listdir(directory) # get list of files in directory
            log_files_path = ['logs/{0}'.format(x) for x in list_of_files] # get path of log files
        except Exception as e: # if error
            logging.error(f'count_log_files function FAILED in file {__file__} with error: {e}') # log that count_log_files function failed
            return None # return none
        if rundone is not True: # if rundone is not true
            logging.info(f'count_log_files function is finsihed in file {__file__}') # log that count_log_files function is finsihed
            rundone = True # set rundone to true
        return log_files_path # return log files path

    def count_backup_files(directory): # count log files function
        global rundone2 # set rundone to global
        if rundone2 is not True: # if rundone is not true
            logging.info(f'count_backup_files function is starting in file {__file__}') # log that count_log_files function is starting
        try: # try
            list_of_files = os.listdir(directory) # get list of files in directory
            log_files_path = ['backups/{0}'.format(x) for x in list_of_files] # get path of log files
        except Exception as e: # if error
            logging.error(f'count_backup_files function FAILED in file {__file__} with error: {e}') # log that count_log_files function failed
            return None # return none
        if rundone2 is not True: # if rundone is not true
            rundone2 = True # set rundone to true
        return log_files_path # return log files path
    
    def delete_logs(): # delete logs function
        global logging_maxFiles, log_folder_name # set logging_maxFiles and log_folder_name to global
        if len(file_actions.count_log_files(log_folder_name)) >= logging_maxFiles: # if number of files in ./logs is greater than 10 
            logging.info(f'Number of log files in ./logs is {len(file_actions.count_log_files(log_folder_name))} before deletion') # log number of files ./logs
            while len(file_actions.count_log_files(log_folder_name)) > logging_maxFiles: # while number of files in ./logs is greater than 10
                oldest_file = min(file_actions.count_log_files(log_folder_name), key=os.path.getctime) # get oldest file in ./logs
                os.remove(oldest_file) # remove oldest file in ./logs
                logging.info(f'Removed log file {oldest_file} in ./logs') # log number of files ./logs
            logging.info(f'Number of log files in ./logs is {len(file_actions.count_log_files(log_folder_name))} after deletion') # log number of files ./logs
            
    def create_zip_backup():
        logging.info(f'create_zip_backup function is starting in file {__file__}') # log that create_zip_backup function is starting
        global max_backups # set max_backups to global
        backup_path = f'{os.getcwd()}\\backups\\' # set backup path
        project_name = os.path.basename(os.getcwd()) # get project name
        temp_dir = os.path.join('C:\\Temp', project_name) # set temp_dir to C:\Temp\project_name
        folder_time = time.strftime('%d-%m-%Y %H-%M-%S',time.localtime(time.time())) # set log datetime format
        logging.info(f'Folder time set to {folder_time}') # log folder time
        try: # try
            logging.info(f'Creating backup of {project_name} in {temp_dir}') # log that backup is being created
            shutil.copytree(os.getcwd(), temp_dir + folder_time) # copy all files in current directory to temp directory
            shutil.rmtree(temp_dir + folder_time + '\\backups') # remove backups folder
            logging.info(f'Backup of {project_name} created in {temp_dir}') # log that backup is created
            shutil.make_archive(backup_path + folder_time, 'zip', temp_dir + folder_time) # create zip file
            logging.info(f'Zip file of {project_name} created in {backup_path}') # log that zip file is created
            time.sleep(0.5) # sleep for 0.5 seconds
            shutil.rmtree(temp_dir + folder_time, ignore_errors=True) # delete temp directory
            logging.info(f'Temp directory {temp_dir + folder_time} deleted') # log that temp directory is deleted
            shutil.rmtree(temp_dir, ignore_errors=True) # delete temp directory
            logging.info(f'Temp directory {temp_dir} deleted') # log that temp directory is deleted
        except Exception as e: # if error
            logging.error(f'Backup of {project_name} FAILED with error: {e}') # log that backup failed
            return 'failed' # return failed
        #delete old backups
        try: # try
            if len(file_actions.count_backup_files(backup_path)) >= max_backups: # if number of files in ./logs is greater than 10 
                while len(file_actions.count_backup_files(backup_path)) > max_backups: # while number of files in ./logs is greater than 10
                    oldest_file = min(file_actions.count_backup_files(backup_path), key=os.path.getctime) # get oldest file in ./logs
                    logging.info(f'Removed backup file {oldest_file} in ./backups') # log number of files ./logs
                    os.remove(oldest_file) # remove oldest file in ./logs
        except FileNotFoundError as e: # if error
            logging.error(f'create_zip_backup function FAILED in file {__file__} with error: {e}') # log that create_zip_backup function failed

        logging.info(f'create_zip_backup function is finsihed in file {__file__}') # log that create_zip_backup function is finsihed
        return 'success' # return success
        """)
innit_data = (r"""'''
 !/usr/bin/env python3
 Path: innit.py
 Description: This file is used to innitiate the project. It is run when the project is started and it creates the innit.py file and the logs folder. It also deletes old log files.
 Author: @Ze7111
'''

# ====================================================================================== Default imports =======================================================================================================
import sys, os, time, logging, shutil; from rich import console; print = console.Console().print; from backend.core.basic_handler import file_actions; from backend.modules.admin import main as admin #       |
# ==============================================================================================================================================================================================================

# ================================ Global Variables ================================
runadmin = False # set runadmin to false                                           |
backup = file_actions.create_zip_backup # set backup to create_zip_backup function |
clearLogs = file_actions.delete_logs # set clearLogs to delete_logs function       |
# ==================================================================================

class innit(): # innit class
    def __init__(): # innit function
        backup() # create zip backup
        clearLogs() # delete logs
        pass # pass
    
    
    def main(): # main function
        pass # pass
        
if __name__ == '__main__': # check if file is being run directly
    if runadmin is True: # if runadmin is true
        admin() # run admin module ---------------------------------------- use this only if you want to run the admin module ----------------------------------------
    innit.__init__() # run innit function
else: # if file is not being run directly
    print('This file is not meant to be imported.', style='bold red') # print error if file is imported""")

def exit_seq(): # exit sequence
    global path # set path to global
    logging.info('Exiting Program...') # log that program is exiting
    try: # try
        with open(f'{path}/make.py.log', 'r') as f: # open make.py.log
            data = f.readlines() # read lines
            for line in data: # for line in data
                line = line.replace('\n', '') # remove \n
                print(line, style='bold red') # print error if file is imported
                time.sleep(random.uniform(0.0, 0.2)) # sleep for 0.0 to 0.2 seconds
            f.close() # close file
    except Exception as e: # if error
        logging.error(f'Error reading log file: {e}') # log error
    finally: # finally
        logging.warning('Finished :)') # log that program is exiting
        logging.shutdown() # shutdown logging
        sys.exit() # exit program

class files(): # files class
    def innit_file(): # innit file
        logging.warning('Creating innit file...') # log that innit file is being created
        global path, innit_data # set innit_data to global
        path2 = f"{path}/innit.py" # set path2 to innit.py
        logging.info(f'Innit.py File Path: {path2}') # log innit.py file path
        with open(path2, 'w') as f: # open innit.py
            logging.info('Writing innit file...') # log that innit file is being written
            f.write(innit_data) # write innit_data to innit.py
            logging.info(f'Data being written to innit file :\n{innit_data}\n') # log innit_data
            logging.warning('Innit file created.') # log that innit file is created
            f.close # close innit.py
    def basic_handeler(): # basic handeler file
        logging.warning('Creating basic_handeler file...') # log that basic_handeler file is being created
        global path, basic_handling_data # set basic_handling_data to global
        path2 = f"{path}/backend/core/basic_handler.py" # set path2 to backend/core/basic_handler.py
        logging.info(f'basic_handling.py File Path: {path2}') # log basic_handling.py file path
        with open(path2, 'w') as f: # open basic_handling.py
            logging.info('Writing basic_handeler file...') # log that basic_handeler file is being written
            f.write(basic_handling_data) # write basic_handling_data to basic_handling.py
            logging.info(f'Data being written to basic_handler file :\n{basic_handling_data}\n') # log basic_handling_data
            logging.warning('basic_handeler file created.') # log that basic_handeler file is created
            f.close # close basic_handling.py     
    def admin_module(): # admin module file
        logging.warning('Creating admin_module file...') # log that admin_module file is being created
        global path, admin_module_data # set admin_module_data to global
        path2 = f"{path}/backend/modules/admin.py" # set path2 to backend/modules/admin.py
        logging.info(f'admin.py File Path: {path2}') # log admin.py file path
        with open(path2, 'w') as f: # open admin.py
            logging.info('Writing admin_module file...') # log that admin_module file is being written
            f.write(admin_module_data) # write admin_module_data to admin.py
            logging.info(f'Data being written to admin_module file :\n{admin_module_data}\n') # log admin_module_data
            logging.warning('admin_module file created.') # log that admin_module file is created
            f.close # close admin.py         
class folders(): # folders class
    def innit_folder_structure(): # innit folder structure function
        try: # try
            logging.warning('Creating innit folder structure...') # log that innit folder structure is being created
            global path # set path to global
            
            os.mkdir(f'{path}/logs') # create logs folder
            logging.warning('Created logs folder.') # log that logs folder is created

            os.mkdir(f'{path}/database') # create database folder
            logging.warning('Created database folder.') # log that database folder is created

            os.mkdir(f'{path}/config') # create config folder
            logging.warning('Created config folder.') # log that config folder is created

            os.mkdir(f'{path}/backups') # create backups folder
            logging.warning('Created backups folder.') # log that backups folder is created

            os.mkdir(f'{path}/build') # create build folder
            logging.warning('Created build folder.') # log that build folder is created

            os.mkdir(f'{path}/backend') # create backend folder
            logging.warning('Created backend folder.') # log that backend folder is created

            os.mkdir(f'{path}/backend/classes') # create backend/classes folder
            logging.warning('Created backend/classes folder.') # log that backend/classes folder is created

            os.mkdir(f'{path}/backend/functions') # create backend/functions folder
            logging.warning('Created backend/functions folder.') # log that backend/functions folder is created

            os.mkdir(f'{path}/backend/core') # create backend/core folder
            logging.warning('Created backend/core folder.') # log that backend/core folder is created

            os.mkdir(f'{path}/backend/data') # create backend/data folder
            logging.warning('Created backend/data folder.') # log that backend/data folder is created

            os.mkdir(f'{path}/backend/modules') # create backend/modules folder
            logging.warning('Created backend/modules folder.') # log that backend/modules folder is created

            os.mkdir(f'{path}/frontend') # create frontend folder
            logging.warning('Created frontend folder.') # log that frontend folder is created

            os.mkdir(f'{path}/frontend/client') # create frontend/client folder
            logging.warning('Created frontend/client folder.') # log that frontend/client folder is created

            os.mkdir(f'{path}/frontend/server') # create frontend/server folder
            logging.warning('Created frontend/server folder.') # log that frontend/server folder is created

            os.mkdir(f'{path}/frontend/assets') # create frontend/assets folder
            logging.warning('Created frontend/assets folder.') # log that frontend/assets folder is created

            os.mkdir(f'{path}/frontend/data') # create frontend/data folder
            logging.warning('Created frontend/data folder.') # log that frontend/data folder is created

            os.mkdir(f'{path}/frontend/core') # create frontend/core folder
            logging.warning('Created frontend/core folder.') # log that frontend/core folder is created
 
            os.mkdir(f'{path}/frontend/functions') # create frontend/functions folder
            logging.warning('Created frontend/functions folder.') # log that frontend/functions folder is created

            os.mkdir(f'{path}/frontend/classes') # create frontend/classes folder
            logging.warning('Created frontend/classes folder.') # log that frontend/classes folder is created

            os.mkdir(f'{path}/src') # create src folder
            logging.warning('Created src folder.') # log that src folder is created

            os.mkdir(f'{path}/src/client') # create src/client folder
            logging.warning('Created src/client folder.') # log that src/client folder is created

            os.mkdir(f'{path}/src/server') # create src/server folder
            logging.warning('Created src/server folder.') # log that src/server folder is created

            os.mkdir(f'{path}/src/assets') # create src/assets folder
            logging.warning('Created src/assets folder.') # log that src/assets folder is created

            os.mkdir(f'{path}/src/data') # create src/data folder
            logging.warning('Created src/data folder.') # log that src/data folder is created

            os.mkdir(f'{path}/src/core') # create src/core folder
            logging.warning('Created src/core folder.') # log that src/core folder is created

            os.mkdir(f'{path}/src/functions') # create src/functions folder
            logging.warning('Created src/functions folder.') # log that src/functions folder is created

            os.mkdir(f'{path}/src/classes') # create src/classes folder
            logging.warning('Created src/classes folder.') # log that src/classes folder is created

            os.mkdir(f'{path}/src/dependencies') # create src/dependencies folder
            logging.warning('Created dependencies folder.') # log that dependencies folder is created
            
            logging.warning('Innit folder structure created.') # log that innit folder structure is created
            
        except FileExistsError: # if folder already exists
            logging.warning('Innit folder structure already exists.') # log that innit folder structure already exists
            
        except Exception as e: # if error
            logging.error(f'Error creating innit folder structure: {e}') # log error creating innit folder structure
            
        return True # return True
           
if __name__ == '__main__': # if __name__ == __main__
    try: # try
        files.innit_file() # innit file
        folders.innit_folder_structure() # innit folder structure
        files.basic_handeler() # run basic_handeler function
        files.admin_module() # run admin_module function
        exit_seq() # exit sequence
    except KeyboardInterrupt: # if keyboard interrupt
        print('Keyboard Interrupt Detected. Exiting...', style='red') # print keyboard interrupt detected
        exit_seq() # exit sequence
    except Exception as e: # if error
        print(f'Error: {e}', style='red') # print error
    finally: # finally
        exit() # exit