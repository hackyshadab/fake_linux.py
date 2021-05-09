from __future__ import print_function

import time


print(r"""
 _______
|         | |                    | |      | |
|         | |                    | |      | | 
\_______  | |__,___    ____   ___| | ____ | |__,___
        \ | |_____  \ /   ' \/     |/   ' \ |      \
        | | |     \  |   _  |   _  |   _  | |   _  |    
        | | |     |  |  (_| |  (_| |  (_| | |  (_| |    
___,,,__| | |     |  |\__,__|\__,__|\__,__| |___,__|"""

                                  print("A FAKE LINUX ONLY FOR FUN BUT MANY TOOL WORK PROPERLY IN THIS SCRIPT")

time.sleep(3.0)
print("\n****************************************************************")
print("\n* Copyright of Shadab Mazhar, 2021                             *")
print("\n* https://www.Github/Hacky_Shadab.com                          *")
print("\n* https://www.instagram/iam__s__king.com                       *")
print("\n****************************************************************")

shadab = print("HERE I PRESENT YOU A LINUX SYSTEM")
time.sleep(1.0)

print("1.Information gathering")
print("2.Vulnerability assessment")
print("3.Web applications")
print("4.Database assessment")
print("5.Password attacks")
print("6.Wireless attacks")
print("7.Exploitation tools")
print("8.Sniffing and spoofing")
print("9.Post exploitation")
print("10.Reporting tools")
print("11.Social engineering tools")

a = input("enter a number----------- ")
if a == "1":
    print("1.Nmap Tool")
    print("2.ZenMAP")
    print("3.whois lookup")
    print("4.SPARTA")
    print("5.nslookup")

b=input("enter a number")

if b == "1":
    import nmap
    nmScan = nmap.PortScanner()

    nmScan.scan(input(''))
    nmScan.command_line()

elif b == "2":
    import nmap

    nmScan = nmap.PortScanner()

    nmScan.scan(input(''))
    nmScan.command_line()


elif b == "3":
    import whois
    w = whois.whois(input(''))
    w.expiration_date  # dates converted to datetime object

    w.text
    print(w)

elif b == "4":
    import webbrowser

    webbrowser.open('https://images.app.goo.gl/KopEBCVfUKShXsBL8')
    time.sleep(5.0)
    webbrowser.open('https://www.google.com/imgres?imgurl=https%3A%2F%2Fmiro.medium.com%2Fmax%2F2032%2F0*9ck3jwmY9ZqFu_ba.png&imgrefurl=https%3A%2F%2Fmedium.com%2F%40briskinfosec%2Fsparta-aa513b4ca224&tbnid=95TqFefhCTXyVM&vet=1&docid=8E-MUETlgNa5LM&w=1016&h=676&source=sh%2Fx%2Fim')

if b == "5":
    from nslookup import Nslookup

    domain = input("Enter a website URL----")

    # set optional Cloudflare public DNS server
    dns_query = Nslookup(dns_servers=input("enter DNS_server address----"))

    ips_record = dns_query.dns_lookup(domain)
    print(ips_record.response_full, ips_record.answer)

    soa_record = dns_query.soa_lookup(domain)
    print(soa_record.response_full, soa_record.answer)


elif a == "2":
    print("1.Nikto")
    print("2.Burp Suite")
    print("3.SQLMap")
    print("4.ZenMAP")
    print("5.Nmap")


c = input("enter a number-------")

if c == "1":
    import webbrowser
    webbrowser.open('https://images.app.goo.gl/utoRj4tDN25KbgDC6')

if c == "2":
    import burpsuite
    import os

    # This example uses the DVWA web application running on localhost as the target app to scan.
    # https://hub.docker.com/r/vulnerables/web-dvwa/

    # It's recommended to use an API key when working with the Burp Suite API. It can be set in the 'User Options' menu

    SERVER_URL = os.getenv("BURP_SERVER_URL", None)
    API_KEY = os.getenv("BURP_API_KEY", None)

    burp_api_client = burpsuite.BurpSuiteApi(server_url=SERVER_URL, api_key=API_KEY)

    # Each scan request requires a scan options object. You can learn more about these options via the Burp Suite REST API
    # documentation along with the values required
    options = {
        "urls": input(["enter your terget URLs---"]),
        "application_logins": [{"username": input("username--"), "password": input("password--")}],
        "scan_callback": {"url": input("scan_callback---")}
    }

    # Initiate a scan
    task_id = burp_api_client.initiate_scan(options=options)
    print("Burp Suite scan initiated! task_id: {}".format(task_id))

    # Get the scan progress of a task
    progress = burp_api_client.get_scan(task_id=task_id)
    print(progress)

if c == "3":
    import webbrowser
    webbrowser.open("https://images.app.goo.gl/SSDHkXzJXhCvAxZS9")

if c == "4":
    import webbrowser
    webbrowser.open('https://images.app.goo.gl/8LhNV7j23eH8RWes8')

if c == "5":
    import nmap

    nmScan = nmap.PortScanner()

    nmScan.scan(input(''))
    nmScan.command_line()

if a == "3":
    print("1. Burp Suite")
    print("2. Nikto")
    print("3. Maltego")
    print("4. SQLMap")

d = input("enter a number---")

if d == "1":
    import burpsuite
    import os

    # This example uses the DVWA web application running on localhost as the target app to scan.
    # https://hub.docker.com/r/vulnerables/web-dvwa/

    # It's recommended to use an API key when working with the Burp Suite API. It can be set in the 'User Options' menu

    SERVER_URL = os.getenv("BURP_SERVER_URL", None)
    API_KEY = os.getenv("BURP_API_KEY", None)

    burp_api_client = burpsuite.BurpSuiteApi(server_url=SERVER_URL, api_key=API_KEY)

    # Each scan request requires a scan options object. You can learn more about these options via the Burp Suite REST API
    # documentation along with the values required
    options = {
        "urls": input(["enter your terget URLs---"]),
        "application_logins": [{"username": input("username--"), "password": input("password--")}],
        "scan_callback": {"url": input("scan_callback---")}
    }

    # Initiate a scan
    task_id = burp_api_client.initiate_scan(options=options)
    print("Burp Suite scan initiated! task_id: {}".format(task_id))

    # Get the scan progress of a task
    progress = burp_api_client.get_scan(task_id=task_id)
    print(progress)

if d == "2":
    import webbrowser

    webbrowser.open('https://images.app.goo.gl/utoRj4tDN25KbgDC6')

if d == "3":
    import magento

    url = input("url---")
    apiuser = input("username--")
    apipass = input("password---")

    # Create an instance of API
    client = magento.API(url, apiuser, apipass)

    # A filter expression as dictionary.
    order_filter = {'created_at': {'from': '2011-09-15 00:00:00'}}
    products = client.product.list(order_filter)

    # Get a list of product types
    product_types = client.product_types.list()

    # Get a specific product
    sku = 'prod1'
    product = client.product.info(sku)

    # Add comment to an order
    order_increment_id = '100000001 '
    status = 'canceled'
    client.order.addcomment(order_increment_id, status)

if d == "4":
    import webbrowser

    webbrowser.open("https://images.app.goo.gl/SSDHkXzJXhCvAxZS9")

if a == "4":
    import webbrowser

    webbrowser.open("https://images.app.goo.gl/GMvJe3sGS43cNxNb6")

if a == "5":
    print("Crunch tool")
    print("Hashcat tool")
    print("John the ripper toolkit")
    print("Hydra")

if a=="5":
    print("e")
    e=input("enter a number-------")

if e == "1":
    import os
    import io
    import re
    from setuptools import setup, find_packages

    thisdir = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(thisdir, 'src', 'pycrunch', 'version.py')) as v_file:
        VERSION = re.compile(
            r".*__version__ = '(.*?)'",
            re.S).match(v_file.read()).group(1)


    def get_long_desc():
        readme_fn = os.path.join(thisdir, 'README.md')
        with io.open(readme_fn, encoding='utf-8') as stream:
            return stream.read()


    requires = [
        'requests>=2.14.0',
        'six',
    ]

    tests_requires = [
        'mock',
        'pytest',
        'pytest-cov',
    ]

    setup_params = dict(
        name='pycrunch',
        python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
        version=VERSION,
        description="Crunch.io Client Library",
        long_description=get_long_desc(),
        url='https://github.com/Crunch-io/pycrunch',
        classifiers=[
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        author=u'Crunch.io',
        author_email='dev@crunch.io',
        license='LGPL',
        install_requires=requires,
        tests_require=tests_requires,
        packages=find_packages('src', exclude=['tests']),
        package_dir={'': 'src'},
        include_package_data=True,
        extras_require={
            'pandas:python_version=="3.4"': ['pandas~=0.19.0'],
            'pandas:python_version=="2.7" or python_version>="3.5"': ['pandas'],
            'testing:python_version=="3.4"': ['pandas~=0.19.0'],
            'testing:python_version=="2.7" or python_version>="3.5"': ['pandas'],
            'testing': tests_requires,
        },
        zip_safe=True,
        entry_points={},
    )

    if __name__ == '__main__':
        setup(**setup_params)

if e == "2":
    import webbrowser

    webbrowser.open("https://images.app.goo.gl/c7x7Zhcs4LpJo16u8")

if e == "3":
    import webbrowser
    webbrowser.open("https://images.app.goo.gl/qtxiyExbJE7MUQ1R8")

if e == "4":
    import pathlib

    import pkg_resources
    from setuptools import find_packages, setup

    from build_helpers.build_helpers import (
        ANTLRCommand,
        BuildPyCommand,
        CleanCommand,
        Develop,
        SDistCommand,
        find_version,
    )

    with pathlib.Path("requirements/requirements.txt").open() as requirements_txt:
        install_requires = [
            str(requirement)
            for requirement in pkg_resources.parse_requirements(requirements_txt)
        ]

    with open("README.md", "r") as fh:
        LONG_DESC = fh.read()
        setup(
            cmdclass={
                "antlr": ANTLRCommand,
                "clean": CleanCommand,
                "sdist": SDistCommand,
                "build_py": BuildPyCommand,
                "develop": Develop,
            },
            name="hydra-core",
            version=find_version("hydra", "__init__.py"),
            author="Omry Yadan",
            author_email="omry@fb.com",
            description="A framework for elegantly configuring complex applications",
            license="MIT",
            long_description=LONG_DESC,
            long_description_content_type="text/markdown",
            url="https://github.com/facebookresearch/hydra",
            keywords="command-line configuration yaml tab-completion",
            packages=find_packages(include=["hydra"]),
            include_package_data=True,
            classifiers=[
                "License :: OSI Approved :: MIT License",
                "Development Status :: 4 - Beta",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Operating System :: POSIX :: Linux",
                "Operating System :: MacOS",
                "Operating System :: Microsoft :: Windows",
            ],
            install_requires=install_requires,
            entry_points={"pytest11": ["hydra_pytest = hydra.extra.pytest_plugin"]},
            # Install development dependencies with
            # pip install -r requirements/dev.txt -e .
        )

if a=="5":
    print("")
    f=input("enter a number-------")

if a == 5:
    print("1.Aircrack-ng")
    print("2.Wireshark")

if f== "1":
    import os
    import subprocess
    import time
    import sys
    import traceback
    import csv
    import sys
    import atexit
    # Import custom modules
    import modules
    import attacks

    # Add some aliases for commonly used functions
    ioStream = modules.ioStream
    bashRun = modules.bashRun
    bashReturnValue = modules.bashReturnValue
    clearTerm = modules.clearTerm
    col = modules.col
    # Script Version number
    scriptVersion = "1.9_build_date_08/12/2018"
    # Some variables which will find out some basic system info
    cpuModel = ioStream(
        "cat /proc/cpuinfo | grep -i \"Model name\" | sort | uniq | awk -F ' ' {'print $4,$5,$6,$7,$8,$9,$10'}")
    userName = ioStream("uname -n")
    userDistro = ioStream("lsb_release -d | awk -F ':' {'print $2'} | tr -d \"\t\" ")
    userKernel = ioStream("uname -r")
    userArch = ioStream("uname -m")
    userArchDpkg = ioStream("dpkg --print-architecture 2>/dev/null").upper()
    invocationType = sys.argv[0]
    # Determines a few values, useful when the -v argument is used
    if invocationType.lower().startswith('./'):
        scriptInvocation = ('%s' % (sys.argv[0]))
    else:
        scriptInvocation = ('python3 %s' % (sys.argv[0]))


    # A quick check to determine if dependencies are installed
    def dependenciesInstalled():
        if modules.quickCheckDepsInstalled():
            return '{}Installed{}'.format(col.green, col.endl)
        else:
            return '{}Not installed{}'.format(col.red, col.endl)


    # The GPLv3+ exclusion of warranty. Just in case.
    def displayWarranty():
        print("    %sAirscript-ng Copyright (C) 2017-2018 Sh3llcod3%s" % (col.red, col.endl))
        print("    %sThis program comes with ABSOLUTELY NO WARRANTY; for details visit: https://goo.gl/W1jcr5.%s" % (
        col.red, col.endl))
        print("    %sThis is free software, and you are welcome to redistribute it%s" % (col.red, col.endl))
        print("    %sunder certain conditions; visit: https://goo.gl/FSy6nc for details.%s" % (col.red, col.endl))
        print("    %sPlease follow all instructions that appear. Thanks for using this program.%s\n" % (
        col.red, col.endl))


    # Create the functions class, where all the re-usable code for the main functions will reside
    class functions:
        # Exit the program after a functions has finshed running.
        def silentExit():
            clearTerm()
            if modules.startNetworkManager():
                bashRun("rm ./HANDSHAKES/TEMP_DUMP_* 2>/dev/null")
                print("\n[{}+{}] Detected network-manager as inactive,"
                      " restarted it.".format(
                    col.green,
                    col.endl))
                print("[{}+{}] Internet connection may take up"
                      " to 10 seconds to come back.\n".format(
                    col.green,
                    col.endl))
            modules.normalQuit(0)

        # Give the user the option to quit or head to menu.
        def menuOrExit():
            while True:
                modules.createNewLine()
                getUserChoice = input("[{0}+{2}] Head to [{1}m{2}]enu"
                                      " or [{1}q{2}]uit? m/q >> ".format(
                    col.green,
                    col.red,
                    col.endl)).lower()
                if getUserChoice.startswith('m'):
                    mainMenu()
                elif getUserChoice.startswith('q'):
                    functions.silentExit()

        # Check for missing dependencies and if there are any, fetch them.
        def getDependencies():
            print("{}[-] {}Checking for dependancies".format(
                col.yellow_deep,
                col.endl))
            modules.checkDependencies()
            modules.gitDeps()
            print("{}[-] {}All dependancies are met."
                  " Make sure you have correct drivers! {}".format(
                col.yellow_deep,
                col.pink,
                col.endl))
            clearTerm()

        # Downloads and builds hashcat and hashcat-utils, which are needed for GPU based cracking.
        # Note: this doesn't install the Opencl-drivers, which still needs to be installed by hand.
        def hashcatDownloadFunction():
            try:
                if not modules.connActive():
                    raise ConnectionError
                hashcatDownloader = attacks.capObj(col)
                hashcatDownloader.downloadHashcat()
            except(ConnectionError):
                clearTerm()
                modules.createNewLine()
                modules.printRed(col, "Internet connection not found!")
            finally:
                functions.menuOrExit()

        # This function used to add the Kali-Rolling repository to the apt lists, however it was too dangerous, so its has been deprecated and removed.
        # Why was it dangerous? Because it replaces Ubuntu's Coreutils with Kali's Coreutils,Display manager, and breaks GPU (OpenCL) drivers.
        # Your system will refuse to boot properly if kali tools aren't installed correctly. Use Katoolin if your're on Ubuntu >> https://goo.gl/rykBwg
        # This function switches the colors on/off in realtime, without changing programs or restarting.
        def switchColors():
            clearTerm()
            global col
            if col == modules.col:
                col = modules.blank_col
            else:
                col = modules.col

        # This function simply performs a full-upgrade of all system packages from apt, a nice to have add-on.
        # It also pulls the latest version from GitHub as an added bonus.
        def updateAptPackagesFull():
            functions.getDependencies()
            modules.createNewLine()
            if modules.yesNo("Run apt update and full-upgrade?", col):
                bashRun("apt update && apt full-upgrade -y"
                        " && apt autoremove -y && apt autoclean")
            modules.createNewLine()
            modules.stashAndPullUpdate(col)

        # This will restore the /etc/apt/source.list file. It won't be needed as the option to append the kali sources has been removed.
        # This mainly concerns users who used a very early build of this program. This is here for compatibility reasons.
        def revertKaliSources():
            clearTerm()
            if bashReturnValue("ls backup-repos") == '0':
                if not modules.pickYesOrNo("Restore sources.list",
                                           "Restore repository sources list?"):
                    return None
                bashRun("cp backup-repos/sources.list /etc/apt/sources.list")
                modules.printSuccess(col, "Successfully reverted sources file back!")
                bashRun("apt update")
                printInfo(col, "If you don't see errors above then sources.list file is OK.")
                functions.menuOrExit()
            else:
                modules.printRed(col, "Backup file not found!")
                functions.menuOrExit()

        # This will help in displaying input prompts.
        def displayCurrentPlace(prompt, *args):
            currentPlace = col.endl + "|" + \
                           modules.returnRed(col, "MENU")
            BASH_PROMPT = modules.returnRed(col, " ~# ")
            for i in args:
                currentPlace += col.endl + "|" + \
                                modules.returnRed(col, i)
            currentPlace += col.endl + "|(" + \
                            modules.returnGreen(col, prompt) + \
                            ")" + BASH_PROMPT
            return currentPlace

        # A basic check to see if airscript-ng already exists in /usr/local/bin
        def checkExistingSymlink():
            if bashReturnValue("ls /usr/local/bin/airscript-ng") == "0":
                return True
            else:
                return False

        # Install all dependencies from GitHub instead of git.kali.org
        # If dependencies are already built, remove and replace them.
        def fetchGitHubDeps():
            clearTerm()
            try:
                modules.createNewLine()
                modules.printBlue(col, "This will clone aircrack-ng, reaver, pixiewps and mdk4 from GitHub.")
                modules.printBlue(col, "This is not normally required, as the script will automatically get")
                modules.printBlue(col, "any missing dependencies from git.kali.org. However, you can get them")
                modules.printBlue(col, "from GitHub instead of git.kali.org, if you want.")
                modules.createNewLine()
                modules.printYellow(col, "Warning: This may result in compatibility or instability issues!")
                modules.printYellow(col, "Warning: Compilation may take longer due to different procedures.")
                modules.createNewLine()
                if modules.yesNo("Confirm download from GitHub?", col):
                    modules.cloneAircrackGitHub()
                    modules.cloneReaverGitHub()
                    modules.clonePixiewpsGitHub()
                    modules.cloneMDK4Deps()
                    modules.createNewLine()
                    modules.printSuccess(col, "Successfully built all dependencies.")
            except(KeyboardInterrupt, EOFError, Exception):
                modules.createNewLine()
            finally:
                functions.menuOrExit()

        # Delete the dependencies folder, if the user wants.
        def removeResidualFiles():
            clearTerm()
            modules.createNewLine()
            if modules.yesNo("Confirm delete all residual files?", col):
                bashRun("rm ~/.airscriptNG/ -rf 2>/dev/null")
                modules.printSuccess(col, "Successfully removed the files.")
            functions.menuOrExit()

        # Allow the use full manual control over their wireless cards.
        def manualCardControl():
            functions.getDependencies()
            try:
                interfaceMethod = attacks.interfaceObj(col)
                while True:
                    interfaceMethod.displayMenu()
            except(KeyboardInterrupt, EOFError, Exception):
                modules.createNewLine()
            finally:
                functions.menuOrExit()
        # Finish this function!


    # Create the main class, which will store all the main functions of the program
    class main:
        # This function is responsible for hosting the evil-twin/fake AP
        def EvilTwinFakeAP():
            functions.getDependencies()
            try:
                apMethod = attacks.apObj(col)
                apMethod.setInitialFiles()
                apMethod.showLogo()
                apMethod.selectOptions()
                apMethod.setupConfigFiles()
                apMethod.hostFakeAp()
                apMethod.cleanupFakeAp()
            except(KeyboardInterrupt, EOFError, Exception):
                try:
                    apMethod.cleanupFakeAp()
                except(KeyboardInterrupt, EOFError, Exception):
                    modules.createNewLine()
            finally:
                functions.menuOrExit()

        # This is here to remind me of how XTERM handles its geometry. Interesting.
        # xterm -geometry 125x35+4320 -bg '#FFFFFF' -fg '#000000' THIS MAKES IT APPEAR TOP RIGHT
        # xterm -geometry 125x35+4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM RIGHT
        # xterm -geometry 125x35-4320+7640 -bg '#FFFFFF' -fg '#000000' BOTTOM LEFT
        # xterm -geometry 125x35-7640 -bg '#FFFFFF' -fg '#000000' TOP LEFT
        # This function will allow a user to crack a WPA/WPA2 handshake file (.cap file)
        def crackCaptureFile():
            functions.getDependencies()
            try:
                capMethod = attacks.capObj(col)
                capMethod.showLogo()
                modules.createNewLine()
                print("{}Type [1] - Crack the WPA-HANDSHAKE with CPU".format(
                    col.blue_deep))
                print("{}Type [2] - Crack the WPA-HANDSHAKE with GPU (Much faster)".format(
                    col.green_deep))
                print("\n{}Type [99] - Return to menu {}".format(
                    col.highlight,
                    col.endl))
                while True:
                    modules.createNewLine()
                    getOption = input(functions.displayCurrentPlace(
                        "ENTER CHOICE",
                        "PRE-EXISTING_HANDSHAKE"))
                    if getOption.isdigit() and int(getOption) in [1, 2, 99]:
                        break
                if int(getOption) == 1:
                    capMethod.enumerateMissingOptions()
                    capMethod.cpuCrack()
                elif int(getOption) == 2:
                    capMethod.enumerateMissingOptions()
                    capMethod.gpuCrack()
                # FINISH THIS
            except(KeyboardInterrupt, EOFError, Exception) as e:
                bashRun("killall aircrack-ng 2>/dev/null")
                bashRun("kill $(ps aux | grep -i hashcat |"
                        " awk -F ' ' {'print $2'}) 2>/dev/null")
            finally:
                functions.menuOrExit()

        # This function used to revert a backup of the .bashrc file to its original location.
        # However this was deprecated in favor of symbolic links.
        # This is cleaner and easier to maintain as well as being a more efficient method.
        # Now, this function removes any created symlinks from the function below.
        def removeSymlink():
            clearTerm()
            modules.createNewLine()
            modules.printBlue(col, "This option will remove the symlink created in option [7].")
            modules.printBlue(col, "If you haven't used option [7], then this isn't necessary.")
            modules.printBlue(col, "However, this should be safe to run.")
            modules.printBlue(col, "Unless you already have another airscript-ng in /usr/local/bin.")
            modules.createNewLine()
            try:
                if modules.yesNo("Remove the symbolic link?", col):
                    if functions.checkExistingSymlink():
                        modules.createNewLine()
                        modules.printSuccess(col, "Found airscript-ng in /usr/local/bin.")
                        if bashReturnValue("rm -f /usr/local/bin/airscript-ng") == "0":
                            modules.printSuccess(col, "Successfully deleted the symlink.")
                            modules.printGreen(col, "Typing 'airscript-ng' will no longer invoke it.")
                        else:
                            raise ValueError
                    else:
                        raise FileNotFoundError
            except(FileNotFoundError):
                modules.createNewLine()
                modules.printYellow(col, "Symlink not found. No need to remove anything.")
            except(ValueError):
                modules.createNewLine()
                modules.printYellow(col, "An error occured while removing the symlink.")
                modules.printYellow(col, "Try running this manually: unlink /usr/local/bin/airscript-ng")
            finally:
                functions.menuOrExit()

        # This function creates a symlink, which allows you to invoke this program like any other binary.
        # Using lots of nested-ifs is far from ideal, however it's all I can think of at present.
        def createSymlink():
            clearTerm()
            modules.createNewLine()
            modules.printBlue(col, "Creating a symbolic link allows you to run airscript-ng from anywhere.")
            modules.printBlue(col, "Essentially, this adds an entry in /usr/local/bin.")
            modules.printBlue(col, "Next time you want to run airscript-ng, just type 'airscript-ng'.")
            modules.printBlue(col, "You can run this from anywhere, any folder you want.")
            modules.printBlue(col, "If you change your mind, you can always delete this using option [8].")
            modules.createNewLine()
            try:
                if sys.argv[0].lower().startswith("./"):
                    FILE_NAME = sys.argv[0][2:]
                elif sys.argv[0].lower().startswith("/usr/local/bin/"):
                    raise TypeError
                else:
                    FILE_NAME = sys.argv[0]
                if modules.yesNo("Create the symbolic link?", col):
                    if not functions.checkExistingSymlink():
                        modules.createNewLine()
                        modules.printSuccess(col, "Adding Symbolic link -> /usr/local/bin/airscript-ng")
                        if bashReturnValue("ls /usr/local/bin") == "0":
                            if bashReturnValue("echo $PATH | grep \"/usr/local/bin\"") == "0":
                                if bashReturnValue("ln -sf $(find $(pwd) -name {}) /usr/local/bin/airscript-ng".format(
                                        FILE_NAME)) == "0":
                                    modules.printSuccess(col, "Successfully created the symlink.")
                                    modules.printGreen(col, "Now you can type 'airscript-ng' from anywhere.")
                                    modules.printGreen(col, "Go ahead, quit and try typing: airscript-ng")
                                else:
                                    raise ValueError
                            else:
                                raise FileNotFoundError
                        else:
                            raise NotADirectoryError
                    else:
                        raise FileExistsError
            except(FileExistsError):
                modules.createNewLine()
                modules.printYellow(col, "Symbolic link already exists. Will not overwrite.")
                modules.printYellow(col, "Is this an error? You can delete the link manually.")
                modules.printYellow(col, "Try running this: unlink /usr/local/bin/airscript-ng")
            except(ValueError):
                modules.createNewLine()
                modules.printYellow(col, "An error occured while creating the symlink.")
                modules.printYellow(col, "Run this manually:")
                modules.printYellow(col, "ln -sf $(find $(pwd) -name {}) /usr/local/bin/airscript-ng".format(
                    FILE_NAME))
            except(FileNotFoundError):
                modules.createNewLine()
                modules.printYellow(col, "Unable to find /usr/local/bin in the $PATH env variable.")
                modules.printYellow(col, "If $PATH doesn't exist, then how are you running this?")
                modules.printYellow(col, "Otherwise, you can add to your $PATH variable by following this guide.")
                modules.printYellow(col,
                                    "Visit: https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix")
            except(NotADirectoryError):
                modules.createNewLine()
                modules.printYellow(col, "Unable to find the /usr/local/bin directory.")
                modules.printYellow(col, "Please choose a linux distro that utilises this directory.")
                modules.printYellow(col, "Otherwise, I can't add the Symlink.")
            except(TypeError):
                modules.createNewLine()
                modules.printYellow(col, "Wrong method of invocation.")
                modules.printYellow(col, "You're probably running this using 'airscript-ng'.")
                modules.printYellow(col, "That won't work. You'll have to run it manually for this occasion.")
                modules.printYellow(col, "Please head to where Airscript-ng is stored.")
                modules.printYellow(col, "Then run it manually with: ./airscript-ng")
                modules.printYellow(col, "If you're confused, please consult the README.md file.")
            finally:
                functions.menuOrExit()

        # This function is to use the reaver tool, to crack wps.
        def reaver():
            functions.getDependencies()
            try:
                reaverMethod = attacks.wpsObj(col)
                reaverMethod.showLogo()
                reaverMethod.getWpsTargets()
                reaverMethod.parseWpsCsv()
                reaverMethod.pixieDust()
                reaverMethod.cleanupWpsFiles()
            except(KeyboardInterrupt, EOFError, Exception) as e:
                try:
                    reaverMethod.cleanupWpsFiles()
                except(KeyboardInterrupt, EOFError, Exception):
                    modules.createNewLine()
            finally:
                functions.menuOrExit()

        # This will handle Aircrack-ng, for most users this will be the go-to choice.
        # Again, this isn't the most efficient way, and I will re-write this at some point.
        def aircrackng():
            functions.getDependencies()
            try:
                aircrackMethod = attacks.aircrackObj(col)
                aircrackMethod.showLogo()
                aircrackMethod.createTempFiles()
                aircrackMethod.selectInitialCard()
                aircrackMethod.gatherInitialData()
                aircrackMethod.parseCsvData()
                aircrackMethod.selectTargetNetwork()
                aircrackMethod.callCompleteCleanup()
                clearTerm()
                modules.printDeepBlue(col, "{1}Did you see WPA Handshake: {0} at the top right?".format(
                    aircrackMethod.selectedNetworkTarget[1],
                    col.green_deep))
                modules.printDeepBlue(col, modules.returnBold(col, "If you didn't see that,"
                                                                   "then {}cleanup with CTRL+C{} and try again.".format(
                    col.red_deep, col.endl_deep)))
                decryptHandshake = attacks.capObj(col, aircrackMethod.captureFilePath)
                decryptHandshake.enumerateMissingOptions()
                clearTerm()
                modules.printDeepBlue(col, "Which method do you want to crack the Handshake with:\n")
                while True:
                    choice_of_cpu_gpu = input("{0}Crack using{1}: CPU-->[c] (all CPUs)|"
                                              " GPU-->[g] (GTX 9xx,10xx+/AMD ROCM GPU) {2}${1} ".format(
                        col.blue_deep,
                        col.endl,
                        col.green)).lower()
                    if choice_of_cpu_gpu.startswith(("c", "g")):
                        break
                if choice_of_cpu_gpu.startswith("c"):
                    decryptHandshake.cpuCrack()
                elif choice_of_cpu_gpu.startswith("g"):
                    decryptHandshake.gpuCrack()
            except(KeyboardInterrupt, EOFError, Exception) as e:
                try:
                    aircrackMethod.callCompleteCleanup()
                except(KeyboardInterrupt, EOFError, Exception):
                    modules.createNewLine()
            finally:
                functions.menuOrExit()

        # This will handle mdk4. A very useful tool with quite a few interesting options.
        def mdk4():
            functions.getDependencies()
            try:
                mdkMethod = attacks.mdkObj(col)
                mdkMethod.showLogo()
                mdkMethod.selectAttackMode()
            except(KeyboardInterrupt, EOFError, Exception) as e:
                try:
                    mdkMethod.cleanupCard()
                except(KeyboardInterrupt, EOFError, Exception):
                    modules.createNewLine()
            finally:
                functions.menuOrExit()


    # Define the main menu, where user will be presented with options and function of script.
    def mainMenu():
        try:
            clearTerm()
            # Check if user has root permissions.
            if os.getuid() != 0:
                print("{}[?]{} Please make sure you have followed the steps:\n".format(
                    col.yellow_deep,
                    col.endl))
                print("\t{0}->{1} [{0}i{1}] Made script executable with '{2}sudo chmod +x {3}{1}' ".format(
                    col.blue,
                    col.endl,
                    col.red,
                    sys.argv[0]))
                print("\t{0}->{1} [{0}i{1}] Ran it with '{2}sudo {3}{1}' \n".format(
                    col.blue,
                    col.endl,
                    col.red,
                    scriptInvocation))
                print(modules.returnYellow(col, "\tAlternatively,"))
                print(
                    "\t{0}->{1} [{0}i{1}] If you have symlinked the program, just do '{2}sudo airscript-ng{1}' \n".format(
                        col.blue,
                        col.endl,
                        col.red))
                modules.normalQuit(1)
            print("Hello {}{}{}!\n".format(col.yellow, userName, col.endl))
            displayWarranty()  # Display the warranty information, as recommened by the GPLv3 license.
            print("{0}Your CPU{1}: {2}{3}{1}".format(col.red, col.endl, col.green, cpuModel))
            print("{0}Your OS{1}: {2}{3}{1}".format(col.red, col.endl, col.green, userDistro))
            print("{0}Your Kernel{1}: {2}{3}{1}".format(col.red, col.endl, col.green, userKernel))
            print(
                "{0}Your Architecture{1}: {2}{3}\\{4}{1}".format(col.red, col.endl, col.green, userArch, userArchDpkg))
            print("{0}Dependencies{1}: {2}{3}{1}".format(col.red, col.endl, col.green, dependenciesInstalled()))
            print("{0}Script version{1}: {2}{3}{1}".format(col.red, col.endl, col.green, scriptVersion))
            # A 2d list spanning across multiple lines that stores all the info for the menu.
            # Probably not the most efficient solution here, but its simple to maintain.
            menuTextItemArray = \
                [[col.pink_deep, 'Aircrack-ng to crack WPA/WPA2', '1', 'main.aircrackng'],
                 [col.blue_deep, 'Reaver with pixie dust to crack WPS', '2', 'main.reaver'],
                 [col.endl_deep, 'Host a Evil-Twin/MITM AP to phish credentials, sniff traffic and more.', '3',
                  'main.EvilTwinFakeAP'],
                 [col.red_deep, 'Crack an existing WPA/WPA2 handshake using CPU/GPU.', '4', 'main.crackCaptureFile'],
                 [col.green_deep, 'Use mdk4 to create a beacon flood, denial-of-service and more.', '5', 'main.mdk4'],
                 [col.yellow_deep, 'Manipulate the system\'s WiFi-cards with manual control.', '6',
                  'functions.manualCardControl'],
                 [col.blue_deep, 'Download and build the dependencies from GitHub.', '7', 'functions.fetchGitHubDeps'],
                 [col.yellow_deep, 'Update/upgrade all system packages and this script', '8',
                  'functions.updateAptPackagesFull'],
                 [col.green_deep, 'Setup Hashcat and Hashcat-utils to use GPU for cracking', '9',
                  'functions.hashcatDownloadFunction'],
                 [col.light_blue, 'Add a symlink to invoke from anywhere', '10', 'main.createSymlink'],
                 [col.pink_deep, 'Delete the symlink from option [10]', '11', 'main.removeSymlink'],
                 [col.black_deep, 'Turn the colors on/off', '12', 'functions.switchColors'],
                 [col.endl_deep, 'If apt is broken, use this to fix it', '13', 'functions.revertKaliSources'],
                 [col.red_deep, 'Delete the folder containing dependencies.', '14', 'functions.removeResidualFiles'],
                 [col.highlight + '\n', 'Exit \033[0m' + col.endl, '99', 'functions.silentExit']]
            # The menu, in short.
            print("\n%s[?] %sWhat tool would you like to use? Please run as root." % (col.yellow_deep, col.endl))
            print(
                "\n{}-----------------------------------------ATTACKS-----------------------------------------{}\n".format(
                    col.yellow_deep,
                    col.endl))
            for i in range(1, int(menuTextItemArray[-2][2]) + 2):
                print("%sType [%s] - %s" % (
                menuTextItemArray[i - 1][0], menuTextItemArray[i - 1][2], menuTextItemArray[i - 1][1]))
                if i == 6:
                    print(
                        "\n{}----------------------------------------DOWNLOADS----------------------------------------{}\n".format(
                            col.green_deep,
                            col.endl))
                if i == 9:
                    print(
                        "\n{}--------------------------------------INSTALLATIONS--------------------------------------{}\n".format(
                            col.blue_deep,
                            col.endl))
            while True:
                mainMenuChoice = input('\n|%sMENU%s|(Choose an option) >>' % (col.red, col.endl))
                for n in menuTextItemArray:
                    if mainMenuChoice == n[2]:
                        functionLocation = n[3].split(".")[1]
                        if n[3].split(".")[0] == 'main':
                            getattr(main, functionLocation)()
                        elif n[3].split(".")[0] == 'functions':
                            getattr(functions, functionLocation)()
                mainMenu()
        except(KeyboardInterrupt, EOFError):
            try:
                mainMenu()
            except(KeyboardInterrupt, EOFError):
                mainMenu()


    mainMenu()

if f == "2":

    import sys
    import re
    import argparse
    import time
    import struct
    from threading import Thread

    ERROR_USAGE = 0
    ERROR_ARG = 1
    ERROR_INTERFACE = 2
    ERROR_FIFO = 3
    ERROR_DELAY = 4

    CTRL_CMD_INITIALIZED = 0
    CTRL_CMD_SET = 1
    CTRL_CMD_ADD = 2
    CTRL_CMD_REMOVE = 3
    CTRL_CMD_ENABLE = 4
    CTRL_CMD_DISABLE = 5
    CTRL_CMD_STATUSBAR = 6
    CTRL_CMD_INFORMATION = 7
    CTRL_CMD_WARNING = 8
    CTRL_CMD_ERROR = 9

    CTRL_ARG_MESSAGE = 0
    CTRL_ARG_DELAY = 1
    CTRL_ARG_VERIFY = 2
    CTRL_ARG_BUTTON = 3
    CTRL_ARG_HELP = 4
    CTRL_ARG_RESTORE = 5
    CTRL_ARG_LOGGER = 6
    CTRL_ARG_NONE = 255

    initialized = False
    message = ''
    delay = 0.0
    verify = False
    button = False
    button_disabled = False

    """
    This code has been taken from http://stackoverflow.com/questions/5943249/python-argparse-and-controlling-overriding-the-exit-status-code - originally developed by Rob Cowie http://stackoverflow.com/users/46690/rob-cowie
    """


    class ArgumentParser(argparse.ArgumentParser):
        def _get_action_from_name(self, name):
            """Given a name, get the Action instance registered with this parser.
            If only it were made available in the ArgumentError object. It is
            passed as it's first arg...
            """
            container = self._actions
            if name is None:
                return None
            for action in container:
                if '/'.join(action.option_strings) == name:
                    return action
                elif action.metavar == name:
                    return action
                elif action.dest == name:
                    return action

        def error(self, message):
            exc = sys.exc_info()[1]
            if exc:
                exc.argument = self._get_action_from_name(exc.argument_name)
                raise exc
            super(ArgumentParser, self).error(message)


    #### EXTCAP FUNCTIONALITY

    """@brief Extcap configuration
    This method prints the extcap configuration, which will be picked up by the
    interface in Wireshark to present a interface specific configuration for
    this extcap plugin
    """


    def extcap_config(interface, option):
        args = []
        values = []
        multi_values = []

        args.append((0, '--delay', 'Time delay', 'Time delay between packages', 'integer', '{range=1,15}{default=5}'))
        args.append((1, '--message', 'Message', 'Package message content', 'string',
                     '{required=true}{placeholder=Please enter a message here ...}'))
        args.append((2, '--verify', 'Verify', 'Verify package content', 'boolflag', '{default=yes}'))
        args.append((3, '--remote', 'Remote Channel', 'Remote Channel Selector', 'selector',
                     '{reload=true}{placeholder=Load interfaces ...}'))
        args.append((4, '--fake_ip', 'Fake IP Address', 'Use this ip address as sender', 'string',
                     '{save=false}{validation=\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b}'))
        args.append((5, '--ltest', 'Long Test', 'Long Test Value', 'long',
                     '{default=123123123123123123}{group=Numeric Values}'))
        args.append(
            (6, '--d1test', 'Double 1 Test', 'Long Test Value', 'double', '{default=123.456}{group=Numeric Values}'))
        args.append(
            (7, '--d2test', 'Double 2 Test', 'Long Test Value', 'double', '{default= 123,456}{group=Numeric Values}'))
        args.append((8, '--password', 'Password', 'Package message password', 'password', ''))
        args.append((9, '--ts', 'Start Time', 'Capture start time', 'timestamp', '{group=Time / Log}'))
        args.append((10, '--logfile', 'Log File Test', 'The Log File Test', 'fileselect', '{group=Time / Log}'))
        args.append((11, '--radio', 'Radio Test', 'Radio Test Value', 'radio', '{group=Selection}'))
        args.append((12, '--multi', 'MultiCheck Test', 'MultiCheck Test Value', 'multicheck', '{group=Selection}'))

        if option == "remote":
            values.append((3, "if1", "Remote Interface 1", "false"))
            values.append((3, "if2", "Remote Interface 2", "true"))
            values.append((3, "if3", "Remote Interface 3", "false"))
            values.append((3, "if4", "Remote Interface 4", "false"))

        if option == "radio":
            values.append((11, "r1", "Radio Option 1", "false"))
            values.append((11, "r2", "Radio Option 2", "false"))
            values.append((11, "r3", "Radio Option 3", "true"))

        if len(option) <= 0:
            for arg in args:
                print("arg {number=%d}{call=%s}{display=%s}{tooltip=%s}{type=%s}%s" % arg)

            values.append((3, "if1", "Remote1", "true"))
            values.append((3, "if2", "Remote2", "false"))

            values.append((11, "r1", "Radio1", "false"))
            values.append((11, "r2", "Radio2", "true"))

        if len(option) <= 0:
            multi_values.append(((12, "m1", "Checkable Parent 1", "false", "true"), None))
            multi_values.append(((12, "m1c1", "Checkable Child 1", "false", "true"), "m1"))
            multi_values.append(((12, "m1c1g1", "Uncheckable Grandchild", "false", "false"), "m1c1"))
            multi_values.append(((12, "m1c2", "Checkable Child 2", "false", "true"), "m1"))
            multi_values.append(((12, "m2", "Checkable Parent 2", "false", "true"), None))
            multi_values.append(((12, "m2c1", "Checkable Child 1", "false", "true"), "m2"))
            multi_values.append(((12, "m2c1g1", "Checkable Grandchild", "false", "true"), "m2c1"))
            multi_values.append(((12, "m2c2", "Uncheckable Child 2", "false", "false"), "m2"))
            multi_values.append(((12, "m2c2g1", "Uncheckable Grandchild", "false", "false"), "m2c2"))

        for value in values:
            print("value {arg=%d}{value=%s}{display=%s}{default=%s}" % value)

        for (value, parent) in multi_values:
            sentence = "value {arg=%d}{value=%s}{display=%s}{default=%s}{enabled=%s}" % value
            extra = "{parent=%s}" % parent if parent else ""
            print("".join((sentence, extra)))


    def extcap_version():
        print("extcap {version=1.0}{help=https://www.wireshark.org}{display=Example extcap interface}")


    def extcap_interfaces():
        print("extcap {version=1.0}{help=https://www.wireshark.org}{display=Example extcap interface}")
        print("interface {value=example1}{display=Example interface 1 for extcap}")
        print("interface {value=example2}{display=Example interface 2 for extcap}")
        print(
            "control {number=%d}{type=string}{display=Message}{tooltip=Package message content. Must start with a capital letter.}{placeholder=Enter package message content here ...}{validation=^[A-Z]+}" % CTRL_ARG_MESSAGE)
        print(
            "control {number=%d}{type=selector}{display=Time delay}{tooltip=Time delay between packages}" % CTRL_ARG_DELAY)
        print(
            "control {number=%d}{type=boolean}{display=Verify}{default=true}{tooltip=Verify package content}" % CTRL_ARG_VERIFY)
        print("control {number=%d}{type=button}{display=Turn on}{tooltip=Turn on or off}" % CTRL_ARG_BUTTON)
        print("control {number=%d}{type=button}{role=help}{display=Help}{tooltip=Show help}" % CTRL_ARG_HELP)
        print(
            "control {number=%d}{type=button}{role=restore}{display=Restore}{tooltip=Restore default values}" % CTRL_ARG_RESTORE)
        print("control {number=%d}{type=button}{role=logger}{display=Log}{tooltip=Show capture log}" % CTRL_ARG_LOGGER)
        print("value {control=%d}{value=1}{display=1}" % CTRL_ARG_DELAY)
        print("value {control=%d}{value=2}{display=2}" % CTRL_ARG_DELAY)
        print("value {control=%d}{value=3}{display=3}" % CTRL_ARG_DELAY)
        print("value {control=%d}{value=4}{display=4}" % CTRL_ARG_DELAY)
        print("value {control=%d}{value=5}{display=5}{default=true}" % CTRL_ARG_DELAY)
        print("value {control=%d}{value=60}{display=60}" % CTRL_ARG_DELAY)


    def extcap_dlts(interface):
        if interface == '1':
            print("dlt {number=147}{name=USER0}{display=Demo Implementation for Extcap}")
        elif interface == '2':
            print("dlt {number=148}{name=USER1}{display=Demo Implementation for Extcap}")


    def validate_capture_filter(capture_filter):
        if capture_filter != "filter" and capture_filter != "valid":
            print("Illegal capture filter")


    """
    ### FAKE DATA GENERATOR
    Extcap capture routine
     This routine simulates a capture by any kind of user defined device. The parameters
     are user specified and must be handled by the extcap.
     The data captured inside this routine is fake, so change this routine to present
     your own input data, or call your own capture program via Popen for example. See
     for more details.
    """


    def unsigned(n):
        return int(n) & 0xFFFFFFFF


    def pcap_fake_header():

        header = bytearray()
        header += struct.pack('<L', int('a1b2c3d4', 16))
        header += struct.pack('<H', unsigned(2))  # Pcap Major Version
        header += struct.pack('<H', unsigned(4))  # Pcap Minor Version
        header += struct.pack('<I', int(0))  # Timezone
        header += struct.pack('<I', int(0))  # Accuracy of timestamps
        header += struct.pack('<L', int('0000ffff', 16))  # Max Length of capture frame
        header += struct.pack('<L', unsigned(1))  # Ethernet
        return header


    # Calculates and returns the IP checksum based on the given IP Header
    def ip_checksum(iph):
        # split into bytes
        words = splitN(''.join(iph.split()), 4)  # TODO splitN() func undefined, this code will fail
        csum = 0
        for word in words:
            csum += int(word, base=16)
        csum += (csum >> 16)
        csum = csum & 0xFFFF ^ 0xFFFF
        return csum


    def pcap_fake_package(message, fake_ip):

        pcap = bytearray()
        # length = 14 bytes [ eth ] + 20 bytes [ ip ] + messagelength

        caplength = len(message) + 14 + 20
        timestamp = int(time.time())

        pcap += struct.pack('<L', unsigned(timestamp))  # timestamp seconds
        pcap += struct.pack('<L', 0x00)  # timestamp nanoseconds
        pcap += struct.pack('<L', unsigned(caplength))  # length captured
        pcap += struct.pack('<L', unsigned(caplength))  # length in frame

        # ETH
        pcap += struct.pack('h', 0)  # source mac
        pcap += struct.pack('h', 0)  # source mac
        pcap += struct.pack('h', 0)  # source mac
        pcap += struct.pack('h', 0)  # dest mac
        pcap += struct.pack('h', 0)  # dest mac
        pcap += struct.pack('h', 0)  # dest mac
        pcap += struct.pack('<h', unsigned(8))  # protocol (ip)

        # IP
        pcap += struct.pack('b', int('45', 16))  # IP version
        pcap += struct.pack('b', int('0', 16))  #
        pcap += struct.pack('>H', unsigned(len(message) + 20))  # length of data + payload
        pcap += struct.pack('<H', int('0', 16))  # Identification
        pcap += struct.pack('b', int('40', 16))  # Don't fragment
        pcap += struct.pack('b', int('0', 16))  # Fragment Offset
        pcap += struct.pack('b', int('40', 16))
        pcap += struct.pack('B', 0xFE)  # Protocol (2 = unspecified)
        pcap += struct.pack('<H', int('0000', 16))  # Checksum

        parts = fake_ip.split('.')
        ipadr = (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
        pcap += struct.pack('>L', ipadr)  # Source IP
        pcap += struct.pack('>L', int('7F000001', 16))  # Dest IP

        pcap += message
        return pcap


    def control_read(fn):
        try:
            header = fn.read(6)
            sp, _, length, arg, typ = struct.unpack('>sBHBB', header)
            if length > 2:
                payload = fn.read(length - 2).decode('utf-8', 'replace')
            else:
                payload = ''
            return arg, typ, payload
        except Exception:
            return None, None, None


    def control_read_thread(control_in, fn_out):
        global initialized, message, delay, verify, button, button_disabled
        with open(control_in, 'rb', 0) as fn:
            arg = 0
            while arg is not None:
                arg, typ, payload = control_read(fn)
                log = ''
                if typ == CTRL_CMD_INITIALIZED:
                    initialized = True
                elif arg == CTRL_ARG_MESSAGE:
                    message = payload
                    log = "Message = " + payload
                elif arg == CTRL_ARG_DELAY:
                    delay = float(payload)
                    log = "Time delay = " + payload
                elif arg == CTRL_ARG_VERIFY:
                    # Only read this after initialized
                    if initialized:
                        verify = (payload[0] != '\0')
                        log = "Verify = " + str(verify)
                        control_write(fn_out, CTRL_ARG_NONE, CTRL_CMD_STATUSBAR, "Verify changed")
                elif arg == CTRL_ARG_BUTTON:
                    control_write(fn_out, CTRL_ARG_BUTTON, CTRL_CMD_DISABLE, "")
                    button_disabled = True
                    if button:
                        control_write(fn_out, CTRL_ARG_BUTTON, CTRL_CMD_SET, "Turn on")
                        button = False
                        log = "Button turned off"
                    else:
                        control_write(fn_out, CTRL_ARG_BUTTON, CTRL_CMD_SET, "Turn off")
                        button = True
                        log = "Button turned on"

                if len(log) > 0:
                    control_write(fn_out, CTRL_ARG_LOGGER, CTRL_CMD_ADD, log + "\n")


    def control_write(fn, arg, typ, payload):
        packet = bytearray()
        packet += struct.pack('>sBHBB', b'T', 0, len(payload) + 2, arg, typ)
        if sys.version_info[0] >= 3 and isinstance(payload, str):
            packet += payload.encode('utf-8')
        else:
            packet += payload
        fn.write(packet)


    def control_write_defaults(fn_out):
        global initialized, message, delay, verify

        while not initialized:
            time.sleep(.1)  # Wait for initial control values

        # Write startup configuration to Toolbar controls
        control_write(fn_out, CTRL_ARG_MESSAGE, CTRL_CMD_SET, message)
        control_write(fn_out, CTRL_ARG_DELAY, CTRL_CMD_SET, str(int(delay)))
        control_write(fn_out, CTRL_ARG_VERIFY, CTRL_CMD_SET, struct.pack('B', verify))

        for i in range(1, 16):
            item = '%d\x00%d sec' % (i, i)
            control_write(fn_out, CTRL_ARG_DELAY, CTRL_CMD_ADD, item)

        control_write(fn_out, CTRL_ARG_DELAY, CTRL_CMD_REMOVE, str(60))


    def extcap_capture(interface, fifo, control_in, control_out, in_delay, in_verify, in_message, remote, fake_ip):
        global message, delay, verify, button_disabled
        delay = in_delay if in_delay != 0 else 5
        message = in_message
        verify = in_verify
        counter = 1
        fn_out = None

        with open(fifo, 'wb', 0) as fh:
            fh.write(pcap_fake_header())

            if control_out is not None:
                fn_out = open(control_out, 'wb', 0)
                control_write(fn_out, CTRL_ARG_LOGGER, CTRL_CMD_SET, "Log started at " + time.strftime("%c") + "\n")

            if control_in is not None:
                # Start reading thread
                thread = Thread(target=control_read_thread, args=(control_in, fn_out))
                thread.start()

            if fn_out is not None:
                control_write_defaults(fn_out)

            while True:
                if fn_out is not None:
                    log = "Received packet #" + str(counter) + "\n"
                    control_write(fn_out, CTRL_ARG_LOGGER, CTRL_CMD_ADD, log)
                    counter = counter + 1

                    if button_disabled:
                        control_write(fn_out, CTRL_ARG_BUTTON, CTRL_CMD_ENABLE, "")
                        control_write(fn_out, CTRL_ARG_NONE, CTRL_CMD_INFORMATION, "Turn action finished.")
                        button_disabled = False

                out = ("%s|%04X%s|%s" % (remote.strip(), len(message), message, verify)).encode("utf8")
                fh.write(pcap_fake_package(out, fake_ip))
                time.sleep(delay)

        thread.join()
        if fn_out is not None:
            fn_out.close()


    def extcap_close_fifo(fifo):
        # This is apparently needed to workaround an issue on Windows/macOS
        # where the message cannot be read. (really?)
        fh = open(fifo, 'wb', 0)
        fh.close()


    ####

    def usage():
        print(
            "Usage: %s <--extcap-interfaces | --extcap-dlts | --extcap-interface | --extcap-config | --capture | --extcap-capture-filter | --fifo>" %
            sys.argv[0])


    if __name__ == '__main__':
        interface = ""
        option = ""

        # Capture options
        delay = 0
        message = ""
        fake_ip = ""
        ts = 0

        parser = ArgumentParser(
            prog="Extcap Example",
            description="Extcap example program for python"
        )

        # Extcap Arguments
        parser.add_argument("--capture", help="Start the capture routine", action="store_true")
        parser.add_argument("--extcap-interfaces", help="Provide a list of interfaces to capture from",
                            action="store_true")
        parser.add_argument("--extcap-interface", help="Provide the interface to capture from")
        parser.add_argument("--extcap-dlts", help="Provide a list of dlts for the given interface", action="store_true")
        parser.add_argument("--extcap-config", help="Provide a list of configurations for the given interface",
                            action="store_true")
        parser.add_argument("--extcap-capture-filter", help="Used together with capture to provide a capture filter")
        parser.add_argument("--fifo", help="Use together with capture to provide the fifo to dump data to")
        parser.add_argument("--extcap-control-in", help="Used to get control messages from toolbar")
        parser.add_argument("--extcap-control-out", help="Used to send control messages to toolbar")
        parser.add_argument("--extcap-version", help="Shows the version of this utility", nargs='?', default="")
        parser.add_argument("--extcap-reload-option", help="Reload elements for the given option")

        # Interface Arguments
        parser.add_argument("--verify", help="Demonstrates a verification bool flag", action="store_true")
        parser.add_argument("--delay", help="Demonstrates an integer variable", type=int, default=0,
                            choices=[0, 1, 2, 3, 4, 5, 6])
        parser.add_argument("--remote", help="Demonstrates a selector choice", default="if1",
                            choices=["if1", "if2", "if3", "if4"])
        parser.add_argument("--message", help="Demonstrates string variable", nargs='?', default="")
        parser.add_argument("--fake_ip", help="Add a fake sender IP address", nargs='?', default="127.0.0.1")
        parser.add_argument("--ts", help="Capture start time", action="store_true")

        try:
            args, unknown = parser.parse_known_args()
        except argparse.ArgumentError as exc:
            print("%s: %s" % (exc.argument.dest, exc.message), file=sys.stderr)
            fifo_found = 0
            fifo = ""
            for arg in sys.argv:
                if arg == "--fifo" or arg == "--extcap-fifo":
                    fifo_found = 1
                elif fifo_found == 1:
                    fifo = arg
                    break
            extcap_close_fifo(fifo)
            sys.exit(ERROR_ARG)

        if len(sys.argv) <= 1:
            parser.exit("No arguments given!")

        if args.extcap_version and not args.extcap_interfaces:
            extcap_version()
            sys.exit(0)

        if not args.extcap_interfaces and args.extcap_interface is None:
            parser.exit("An interface must be provided or the selection must be displayed")
        if args.extcap_capture_filter and not args.capture:
            validate_capture_filter(args.extcap_capture_filter)
            sys.exit(0)

        if args.extcap_interfaces or args.extcap_interface is None:
            extcap_interfaces()
            sys.exit(0)

        if len(unknown) > 1:
            print("Extcap Example %d unknown arguments given" % len(unknown))

        m = re.match('example(\d+)', args.extcap_interface)
        if not m:
            sys.exit(ERROR_INTERFACE)
        interface = m.group(1)

        message = args.message
        if args.message is None or len(args.message) == 0:
            message = "Extcap Test"

        fake_ip = args.fake_ip
        if args.fake_ip is None or len(args.fake_ip) < 7 or len(args.fake_ip.split('.')) != 4:
            fake_ip = "127.0.0.1"

        ts = args.ts

        if args.extcap_reload_option and len(args.extcap_reload_option) > 0:
            option = args.extcap_reload_option

        if args.extcap_config:
            extcap_config(interface, option)
        elif args.extcap_dlts:
            extcap_dlts(interface)
        elif args.capture:
            if args.fifo is None:
                sys.exit(ERROR_FIFO)
            # The following code demonstrates error management with extcap
            if args.delay > 5:
                print("Value for delay [%d] too high" % args.delay, file=sys.stderr)
                extcap_close_fifo(args.fifo)
                sys.exit(ERROR_DELAY)

            try:
                extcap_capture(interface, args.fifo, args.extcap_control_in, args.extcap_control_out, args.delay,
                               args.verify, message, args.remote, fake_ip)
            except KeyboardInterrupt:
                pass
        else:
            usage()
            sys.exit(ERROR_USAGE)




