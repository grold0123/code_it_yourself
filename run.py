import subprocess,os,sys,time


project_name = sys.argv[1] 
base_dir = 'C:/projects/code_it_yourself/project'

src_files = f'{base_dir}/{project_name}/src/*.cpp'
project_file = f'{base_dir}/{project_name}/build/{project_name}.exe'
# a =                     base_dir + '\' + p 

if project_name:
    args = [
        'g++',
        src_files,
        '-o',
        project_file

    ]
    print("\n\n\t\t---Building project---\n\n")
    result = subprocess.run(args)
    if result.returncode == 0:
        print("\n\n\t\t---Build successful---\n\n")
        print(f"\n\n\t\t---Opening: {project_name}.exe ---\n\n")        
        time.sleep(2)
        os.system("cls")
        subprocess.run(project_file)
    else:
        print("\n\n\t\t---Build unsuccesful---\n\n")

else:
    os.system("\n\n\t\t---No project name---\n\n")







