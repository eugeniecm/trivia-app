# trivia-app


#to activate the repo on the terminal please run 

```
conda activate trivia-env
```



# Trivia Game (Python)

This trivia game allows you to builld a website to access random trivia questions to play with your friends. You can customize it to fit certain catagories if you want to.

![](https://user-images.githubusercontent.com/97541454/166502391-4593aaf3-7930-4620-96bd-d4acd5506108.png)

## Installation

Create a copy of this [template repo](https://github.com/eugeniecm/trivia-app.git), then clone or download your new repo onto your local computer (for example to the Desktop), and navigate there from the command-line:

```sh
cd ~/Desktop/trivia-app-py/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "trivia-env":

```sh
conda create -n trivia-env python=3.8
conda activate trivia-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:

# required vars:
FLASK_APP=web_app flask run
```

## Usage

Printing the questions and answers (to test the Trivia API):

```sh
python -m app.trivia_service

## Testing

Running tests:

```sh
pytest

# in CI mode:
CI=true pytest
```

## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server (Heroku)

## [License](/LICENSE.md)

Please refer to the license file

## To run local file

```sh
FLASK_APP=web_app flask run
```