# Spyfell
A webapp implementation of a game about ferreting out sneaky spies
## Installation
NOTE:  project requires python 3

1.  Install dependencies
```
pip install -r requirements.txt
```
2.  Create databases
```
cd spyfell
python manage.py migrate game
```
3.  Start web server
```
python manage.py runserver
```
4.  Optionally, to forward to publish internet
```
ngrok http [port] -host-header="localhost:[port]"
```