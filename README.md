# Beautiful Soup

Beautiful Soup is a Python library that is used for **web scraping purposes to pull the data out of HTML and XML files.** It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

# Installation
## On Local Machine

Open Command Prompt and set a path where project is cloned or downloaded.

For Example, My Project is located on the desktop.

```Command Prompt
    C:\Users\Shaan\Desktop\BeautifulSoup
```

## Run the following commands to have the server up and running.

Make sure that in your system **python** is installed and the python--version should be **3.6** or **above**.

With the help of pip, a tool to manage and install python packages, to install **virtualenv**.

```Command Prompt
    C:\Users\Shaan\Desktop\BeautifulSoupk>pip install virtualenv
```
After installing **virtualenv** let's create it.

```Command Prompt
    C:\Users\Shaan\Desktop\BeautifulSoup>python3 -m venv venv
```

Now your Project_Task directory looks like:

* BeautfulSoup
    * fakejobs.py
    * indeed.py
    * venv
    * requirements.txt

Virtual Environement is created, to **activate** it.

```Command Prompt
    C:\Users\Shaan\Desktop\BeautifulSoup>source venv/bin/activate
```

Your command Prompt looks like:

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\BeautifulSoup>
```

For installing all dependencies.

```Command Prompt
    (venv) C:\Users\Shaan\Desktop\BeautifulSoup>pip install -r requirements.txt
```
