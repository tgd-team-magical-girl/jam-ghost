# jam-ghost

A ghost themed video game about magical girls and big boss fights.

## Prepping for use

First, install Python 3.9 from [here](https://www.python.org/downloads/).

Once installed, you'll need a virtual environment. Once inside the project directory:

On Windows with powershell, use `py -3.9 -m venv .venv` on linux or Mac, use `python3.9 -m venv .venv`

Next, you should activate your environment.

Windows:

    .\.venv\Scripts\activate

Mac/Linux:

    source .venv/bin/activate

Next, you'll want to install briefcase with `pip install briefcase`.

From there, move into the magicalgirlbossfight directory and run `briefcase dev` to run the current source.