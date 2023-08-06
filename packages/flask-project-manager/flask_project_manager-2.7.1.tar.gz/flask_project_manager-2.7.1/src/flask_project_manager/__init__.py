import requests, zipfile,sys,os,tarfile
zip_file_url = "https://www.s79.ir/tmp/blankProject.tar.gz"


print("""
███████╗██╗░░░░░░█████╗░░██████╗██╗░░██╗
██╔════╝██║░░░░░██╔══██╗██╔════╝██║░██╔╝
█████╗░░██║░░░░░███████║╚█████╗░█████═╝░
██╔══╝░░██║░░░░░██╔══██║░╚═══██╗██╔═██╗░
██║░░░░░███████╗██║░░██║██████╔╝██║░╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
""")
print("Flask project manager, version 2.7")
print("Initializing new flask project....")
print("Downloading requirements ....")

def main():
    r = requests.get(zip_file_url, stream=True)
    with open('tmp.tgz', 'wb') as file:
        file.write(r.raw.read())
    tar = tarfile.open("tmp.tgz")
    tar.extractall(path=os.getcwd())
    tar.close()
    print("Operation done!")
    print("Project path: " + os.getcwd())
    os.remove('tmp.tgz')


if __name__ == '__main__':
    main()

if __name__ == 'flask_project_manager.__main__':
    main()
