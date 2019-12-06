# PROJECT: website

`Author: Meryll Dindin, Oskar Radermecker`

## Set up your Python3+ environment:

```bash
git clone https://github.com/Project-AsTeR/website.git
virtualenv -p python3 website
cd website
source bin/activate
pip install -r requirements.txt
```

## Run the Flask server locally:

```bash
python application.py
```

## Get the environment variables right:

This is mainly a good code practice, but you generally do not want to hardcode your credentials in your code. At least that is widely accepted in production settings. The way to go is to design environment variables, that are easily accessible from the running instance but written nowhere in your code. However, because there is a real difference between a development and a production environment, here are some advices about how to do it properly.

My suggestion would be to use a virtualenv, and to configure your `bin/activate` to incorporate the variables once activated, and unset them when deativated. The way I usually do it is by first creating a **.json** file (that you have to make sure to incorporate in `.ebignore` and `.gitignore`) aggregating all your environment variables. The file structure has been shared through `environment-shared.json`.

Then use `./deploy-env.sh dev` and copy-paste the chunks directly into your `bin/activate` file. Once done, deactivate and reactivate your environment. Now you can work easily in your development environment with those environment variables. To verify if those variables have been exported, use:

```bash
python -c "import os, pprint; env_var=os.environ; pprint.pprint(dict(env_var), width=1);"
```

## Host the website online:

Currently, the website is hosted on **AWS** through their **Elastic Beanstalk** service. Emptied configuration files are provided with the project, as we obviously cannot share our credentials. Feel free to contact us for any missing element. I outsourced a more thorough tutorial on [Medium](https://medium.com/@merylldin/from-dev-to-prod-all-you-need-to-know-to-get-your-flask-application-running-on-aws-ecedd4eec55) for the ones interested in hosting their own website on **AWS EB**.

## Latest front page rendered:

![LOGO](./assets/aster-front.png)
