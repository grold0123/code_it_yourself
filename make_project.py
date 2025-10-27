import subprocess,sys,pathlib,time

base_dir = 'C:\projects\code_it_yourself\project'
src_dir = base_dir + '\src'
build_dir = base_dir + r'\build'

project_name = sys.argv[1]


if project_name:

    project_path = pathlib.Path(base_dir)/project_name
    src_path = project_path/'src'
    build_path = project_path/'build'
    main_cpp = src_path/'main.cpp'

    time.sleep(2)
    print("\n\n\t\t--Creating project directory--\n")
    project_path.mkdir(exist_ok=True)
    time.sleep(2)
    print("\n\n\t\t--Creating project source directory--\n")
    src_path.mkdir(exist_ok=True)
    time.sleep(2)
    print("\n\n\t\t--Creating project build directory--\n")
    build_path.mkdir(exist_ok=True)
    time.sleep(2)
    print('\n\n\t\t--Creating main.cpp file--')
    main_cpp.touch(exist_ok=True)
    
    if main_cpp.exists():
        subprocess.run([
            'code',
            main_cpp
        ])
        