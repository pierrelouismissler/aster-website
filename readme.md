# aster-website

`Author: Meryll Dindin`

## Set up your environment:

```bash
git clone https://github.com/Project-AsTeR/aster-website.git
virtualenv -p python3 aster-website
cd aster-website
mkdir config
source bin/activate
pip install -r requirements.txt
```

## Configure Flask:

**config/config-main.json**

```python
{
	"secret-key": "5y2znLF4Q8xec"
}
```

**config/config-mail.json**

```python
{
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 587,
    "MAIL_USE_SSL": false,
    "MAIL_USE_TLS": true,
    "MAIL_USERNAME": "xxx",
    "MAIL_PASSWORD": "xxx"
}
```

## From dev to prod:

## Latest front page rendered:

![LOGO](./assets/aster-front.png)