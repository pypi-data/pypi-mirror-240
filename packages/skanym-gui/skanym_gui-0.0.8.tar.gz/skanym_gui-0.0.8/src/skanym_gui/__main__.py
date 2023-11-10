import os
import sys

def install():
    # Get cwd
    cwd = os.getcwd()
    print(f"cwd: {cwd}")
    
    # Check if the GeeXLab executable is in the current directory
    geexlab_exe_path = os.path.join(cwd, "geexlab.exe")
    if not os.path.exists(geexlab_exe_path):
        raise FileNotFoundError(f"geexlab.exe not found in current working directory : {cwd}.")
    
    # Get python site-packages folder from python path
    python_site_packages_path = ""
    for path in sys.path:
        if "site-packages" in path:
            python_site_packages_path = path
            break

    print(f"python_site_packages_path: {python_site_packages_path}")

    # Get skanym-gui folder path
    skanym_gui_path = os.path.join(python_site_packages_path, "skanym_gui")

    if not os.path.exists(skanym_gui_path):
        raise FileNotFoundError(f"skanym_gui package not found in {python_site_packages_path}")
    
    # copy skanym-gui folder to cwd
    skanym_gui_copy_path = os.path.join(cwd, "skanym_gui")
    os.system(f"xcopy {skanym_gui_path} {skanym_gui_copy_path} /E /I /Y")
    # the /E flag copies all subfolders and files
    # the /I flag creates a directory if it doesn't exist
    # the /Y flag automatically overwrites files

    # Remove unnecessary files from the skanym-gui folder
    try:
        os.remove(os.path.join(skanym_gui_copy_path, "__init__.py"))
        os.remove(os.path.join(skanym_gui_copy_path, "__main__.py"))
        os.remove(os.path.join(skanym_gui_copy_path, "geexlab_exe_path.cfg"))
        pycache_path = os.path.join(skanym_gui_copy_path, "__pycache__")
        if os.path.exists(pycache_path):
            for file in os.listdir(pycache_path):
                os.remove(os.path.join(pycache_path, file))
            os.rmdir(pycache_path)
    except:
        # If the file doesn't exist, it is not removed.
        pass
         

    # Save GeeXLab executable path to file
    geexlab_exe_path_file = os.path.join(skanym_gui_path, "geexlab_exe_path.cfg")
    with open(geexlab_exe_path_file, "w") as f:
        f.write(geexlab_exe_path)

    # Get path to the python home directory
    python_home_dir = os.path.dirname(sys.executable)

    # Configure the init0.xml file

    # Read xml file
    xml_file_path = os.path.join(cwd, "init0.xml")
    with open(xml_file_path, "r") as xml_file:
        xml_file_content = xml_file.read()
    xml_file = open(xml_file_path, "r")
    xml_file_content = xml_file.read()
    xml_file.close()

    # Configure default_scene
    xml_file_content = xml_file_content.replace('default_scene="./startup-demo/main.xml"', f'default_scene="{skanym_gui_copy_path}/main.xml"')

    # Configure python_home
    xml_file_content = xml_file_content.replace('python3_10_home=""', f'python3_10_home="{python_home_dir}"')

    # Write xml file
    xml_file = open(xml_file_path, "w")
    xml_file.write(xml_file_content)
    xml_file.close()

def run():
    # Read GeexLab executable path from file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    geexlab_exe_path_file = os.path.join(current_dir, "geexlab_exe_path.cfg")
    with open(geexlab_exe_path_file, "r") as f:
        geexlab_exe_path = f.read()
    
    # Run GeexLab
    os.system(geexlab_exe_path)
