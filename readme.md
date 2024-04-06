## Local server for camlink.

Used to link cameras found in the same event using LAN.

## Getting Started

- Create a new folder and make sure it is not a git repo
- Create a new virtual environment in the folder
  - `python -m venv env`
- Activate the virtual environment
  - `env\Scripts\activate.bat`
- You should now see (env) at the left side of the terminal. If you don't see (env) and you are using the terminal inside vs code switch the terminal you are using from powershell to cmd.
- Clone the repo
  - `git clone git@github.com:Cam-Link/local-server.git` if you are using ssh or `git clone https://github.com/Cam-Link/local-server.git` for https
- At this point the local-server folder will appear.
- Change the directory to local-server
  - `cd local-server`
- Install the requirements
  - `pip install -r requirements.txt`
- Create a new folder named `videos` inside `local-server/camlink`
- Create a new folder named `screen` inside `local-server/screenshare`
- You can now run the local server
  - `python manage.py runserver`
