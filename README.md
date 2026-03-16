To run: 
- On MacOS, download the zip file from GitHub,
- unzip,
- right click and select "New terminal at folder",
- once the terminal opens, paste:
- python3.13 -m venv .venv && ./.venv/bin/python -m pip install -r requirements.txt && ./.venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000
- and press enter.

Please login using the following details: Email: john.doe@email.com Password: HelloWorld

This project is part of a small portfolio tool that allows a user to upload two CSV files, validate the data before submission, and store them on the server under a named portfolio. The frontend is built with React and MUI DataGrid to allow inline editing and validation, while the backend is a FastAPI service that handles file upload and storage.

Reasoning for tools: 
- Pydantic: Pydantic allows me to have strict control over the data structures being handled in the API, this also provides helpful error messages when data does not match expected structure.
- SQL Alchemy: SQL ALchemy is an ORM with excellent tooling, with past experience I felt it was the perfect choice given how comfortable I am in using it and how simple it is to implement.
- SQLite/Async: I utilised an async version of SQLite purely because it felt more natural when compared to my previous experience with live systems and databases.
- Papa parse: Papa parse is a library that allows me to parse CSV FileObjects into arrays, this allowed me to then render and manipulate the data within before uploading to the server.
- MUI/MUI DataGrid: I utilised MUI purely for inputs and buttons to prevent having to create my own, Inputs require extensive customisation and generalisation to work across the webapp, using a library here felt like the right choice. DataGrid was chosen for all the table rendering, this library provides all the necessary tooling to validate and manipulate table data.
- Axios: Axios is a library I am very familiar with. I have used this library in production systems and understand its tooling well, it felt like the right choice here.

Brief Assumptions:

- A "User" must be able to upload... - I understood this as not only a user from an interaction perspective but also from a auth and application perspective, therefore I implemented an incredibly simple auth system using the bcrypt python library to create and compare password hashes to authenticate users.
- Portfolio management - I assumed two things, 1: the user must be able to create a portfolio while following a specific workflow, 2: The user must be able to view other uploaded portfolios, hence why I implemented a table in the home page.

What would I improve?:

- Because of the DataGrid requiring strict and KNOWN column structures, I had to validate the columns directly using a method that had the column types predefined. This felt inefficent and rather messy, if I had more time, I would have liked to have figured out a more general way of doing this, if there is such a thing.
- While I was trying to show my front end skills in the FileUpload component, I realised that given the requirements on specific CSV files and column structures, I should have required a fixed upload method for a specific file type and name. I had committed myself to the FileUpload component structure early on and could not reasonably pivot upon realisation, especially given the work done at that point in time.
- Given the ability to upload practically any file the user wants with the help of the FileUpload component, the app can and will break to some degree if a file with the wrong structure or filename is provided. I would like to have spent more time validating column names to then determine that the CSV file is an expected structure, thereby disregarding the filename as irrelevant.
- I also would liked to have spent more time on the front end UI, I tried my best given the circumstances, but there is so much room for improvement (scss files being rushed, component structure not entirely modular, preview icon not switching to close etc)
- Server-side validation would have been ideal on the files uploaded, the ability to create a method within the PortfolioService class to validate the csv's and their structure to ensure that they are what is expected would have been a great validation approach.
