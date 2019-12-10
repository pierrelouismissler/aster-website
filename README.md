# aster-website

`Author: Meryll Dindin`

## Set up your environment:

```bash
git clone https://github.com/Project-AsTeR/website.git
virtualenv -p python3 website
cd website
source bin/activate
pip install -r requirements.txt
```

_Current support is done on Ubuntu 18.04._

## Install Docker:

```bash
$ sudo apt-get update
$ sudo apt-get install docker-io
```

## For Jupyter lovers, add the environment to your kernels:

```bash
$ pip install jupyter notebook ipython ipykernel
$ python -m ipykernel install --user --name=aster-website
```

## Configure your environment variables:

Create the file `environment.json` to configure your entire dev/prod environment:

```python
{
    "SECRET_KEY": "",
    "MAIL_SERVER": "",
    "MAIL_PORT": ,
    "MAIL_USE_SSL": ,
    "MAIL_USE_TLS": ,
    "MAIL_USERNAME": "",
    "MAIL_PASSWORD": "",
    "GOOGLE_MAP": ""
}
```

## Run your Flask application through a Docker image:

There are two options for you. We made the current service fully available through a public Docker image, that you can retrieve using:

```bash
docker pull coricos/aster:aster-website
```

Otherwise, let's get you through the process of building it:

### Build a fresh Docker image:

```bash
$ docker build -t aster-website --no-cache .
```

### Test your image locally:

Create the file `container.env` to run your Docker container with the right environment variables with `./setenv.sh container`. The bash file actually relies on the previously defined `environment.json` file.

```bash
$ docker run --env-file=container.env -t -i -p 5000:5000 aster-website
$ python -c "import requests, json; print(json.loads(requests.get('http://localhost:5000/health').content));"
  {'result': 'online'}
```

### Create and push your own Docker image on DockerHub:

```bash
$ docker build -t aster-website .
$ docker tag aster-website {username}/{repository}:aster-website
$ docker push {username}/{repository}:aster-website
```

## Build your AWS service endpoint:

```bash
$ ./setenv.sh prod
```

Once the Elastic Beanstalk instance created, check its availability through:

```bash
$ python -c "import requests, json; print(json.loads(requests.get('https://{your-hosted-url}/health').content));"
  {'result': 'online'}
```

## Host the website online:

Currently, the website is hosted on **AWS** through their **Elastic Beanstalk** service. Emptied configuration files are provided with the project, as we obviously cannot share our credentials. Feel free to contact us for any missing element. I outsourced a more thorough tutorial on [Medium](https://medium.com/@merylldin/from-dev-to-prod-all-you-need-to-know-to-get-your-flask-application-running-on-aws-ecedd4eec55) for the ones interested in hosting their own website on **AWS EB**.

## Latest front page rendered:

![LOGO](./assets/aster-front.png)