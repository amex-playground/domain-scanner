import re
import os
import sys

file_path = os.getcwd()

print(file_path)
with open(f'{sys.argv[1]}.csv', 'w', newline='') as system_audit_log:
    system_audit_log.write("File Path, Line Number, Domain Found\n")
    target_dir = file_path
    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        for root, dirs, files in os.walk(target_dir):
            print(f"Current directory: {root}")
            for file in files:
                print(os.path.join(root, file))
                file_path = os.path.join(root, file)
                if '.git' in file_path:
                    continue
                if file_path.endswith(('.zip', '.rar', '.tar', '.gz', '.7z', '.jpg', '.png', '.exe', '.json', '.bin')):
                    continue
                with open(file_path, 'r', encoding='utf-8') as file:
                    line_num = 0
                    try:
                        for line in file:
                            line_num+=1
                            line = line.strip()
                            m = re.search('https?://([A-Za-z_0-9.-]+).*', line)
                            if m:
                                clean_path = file_path.split("repository_for_scan")[1]
                                print(clean_path)
                                system_audit_log.write(f"{clean_path},  {line_num}, {m.group(1)}\n")
                    except Exception as ex:
                        print(f"Could not parse file {file_path}")
                        print(ex)
                        print("Skipping")
                        continue
            print("- - - - - - - - - - - - - - - - - - ")
    else:
        print("Does not exist")
