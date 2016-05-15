# Bill Tracker

## Table of Contents

* [Top Priority Issues](#top-priority-issues)
* [Getting Started](#getting-started)
* [Team Members](#team-members)

## <a name="top-priority-issues"></a>Top Priority Issues
Our issues that need addressing page is here https://github.com/bill-tracker/bill-tracker/issues
From that list, high priority tickets are
- search https://github.com/bill-tracker/bill-tracker/issues/150
- rap genious style annotations https://github.com/bill-tracker/bill-tracker/issues/263
- mobile https://github.com/bill-tracker/bill-tracker/issues/261
- user registration https://github.com/bill-tracker/bill-tracker/issues/155

If you have any questions about anything or need help getting started, you'll probably want to join our slack channel at https://billtracker.slack.com/  You'll need an invite from Dee for that.  You can email me at mcdermottsolutions@gmail.com and I can ask Dee to send you the slack invite.  Sorry about the runaround, we're super excited that you're interested and would really love some new blood in this project!

## <a name="getting-started"></a>Getting Started on your Local Computer

**Install Python 3:**

https://www.python.org/downloads/ or

http://conda.pydata.org/miniconda.html

Note: This project is Python 2-compatible as of 2015-08-18. However, the core
team will develop this project in Python 3, so it is recommended that you do the
same.

**Clone our repo:**

    git clone https://github.com/bill-tracker/bill-tracker.git

**Install all *local* dependencies:**

    pip install -r requirements_local.txt

or (needs verification):

https://groups.google.com/a/continuum.io/forum/#!topic/conda/PiM9sjWyXFU

    conda create -n new environment --file requirements_local.txt

Or, you can install the dependencies manually if you wish / need.

**Initialization:**

    python reset_migrations.py

**Run server:**

    python manage.py runserver

**Check out this app on your browser:**

Go to: http://localhost:8000/

**Django shell** (Optional, good for checking the contents of the models during development or testing, or just generally trying things out):

    python manage.py shell

**Alternative method if the above doesn't work for you**

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

python3 manage.py flush
```

## <a name="team-members"></a>Team Members

* Deepti Boddapati [@deeptiboddapati](https://github.com/deeptiboddapati)
* Filip Drozdowski [@fdrozdowski](https://github.com/fdrozdowski)
* Ed Solis [@edsfocci](https://github.com/edsfocci)
* Mark McDermott [@mcdermottsolutions](https://github.com/mcdermottsolutions)
* Logan Robinson [@loganrobinson](https://www.linkedin.com/in/loganrobinson)
* Nick Kasten [@kastentx](https://github.com/kastentx)
* Laura Arth [@Lautte](https://github.com/Lautte)
* Rahul Putha [@rahulputha](https://github.com/rahulputha)
