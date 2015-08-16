# Bill Tracker

## Table of Contents

* [Getting Started](#getting-started)
* [Team Members](#team-members)

## <a name="getting-started"></a>Getting Started on your Local Computer

**Install Python 3**:

https://www.python.org/downloads/
or

http://conda.pydata.org/miniconda.html

**Clone our repo**:

    git clone https://github.com/bill-tracker/bill-tracker.git

**Install all *local* dependencies**:

    pip install -r requirements_local.txt

or (needs verification):

https://groups.google.com/a/continuum.io/forum/#!topic/conda/PiM9sjWyXFU

    conda create -n new environment --file requirements_local.txt

Or, you can install the dependencies manually if you wish / need.

**Initialization**:

    python reset_migrations.py

**Run server**:

    python manage.py runserver

**Check out this app on your browser

Go to: http://localhost:8000/

**Django shell** (Optional, good for checking the contents of the models during development or testing, or just generally trying things out):

    python manage.py shell

## <a name="team-members"></a>Team Members

* Deepti Boddapati [@deeptiboddapati](https://github.com/deeptiboddapati)
* Filip Drozdowski [@fdrozdowski](https://github.com/fdrozdowski)
* Ed Solis [@edsfocci](https://github.com/edsfocci)
* Mark McDermott [@mcdermottsolutions](https://github.com/mcdermottsolutions)
* Logan Robinson [@loganrobinson](https://www.linkedin.com/in/loganrobinson)
* Nick Kasten [@kastentx](https://github.com/kastentx)
* Laura Arth [@Lautte](https://github.com/Lautte)
* Rahul Putha [@rahulputha](https://github.com/rahulputha)