To run: On MacOS, download the zip file from GitHub, 
unzip, right click and select "New terminal at folder", 
once the terminal opens, paste: 
python3.13 -m venv .venv && ./.venv/bin/python -m pip install -r requirements.txt && ./.venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000
and press enter.

