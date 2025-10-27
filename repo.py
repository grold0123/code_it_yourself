import subprocess 

base_dir = "C:/projects/code_it_yourself"

args = [
    ('\n\ngit add:',[
        'git','add',"C:/projects/code_it_yourself"
    ]),#git add
    ('\n\ngit commit:\n\n',[
        'git','commit','-m',"update"
    ]),#git commit
    ('git push:\n\n',[
        'git','push'
    ]),#git push
]


for prompt,arg in args:
    print(prompt)
    subprocess.run(arg)
    print("\n\nsuccessful\n\n")

print("\n\nRepository updated\n\n")