# Capsolver Python3
Capsolver python3 library

## Installation

Use pip to install the library:

```sh
pip3 install --upgrade capsolver-python3
```

Install from source with:

```sh
python setup.py install
```

## Usage


#### ImageToText

```python
from capsolver_python import ImageToTextTask

capsolver = ImageToTextTask("API_KEY")
task_id = capsolver.create_task(image_path="img.png")
result = capsolver.join_task_result(task_id)
print(result.get("text"))
```

#### Recaptcha v2

```python
from capsolver_python import RecaptchaV2Task

capsolver = RecaptchaV2Task("API_KEY")
task_id = capsolver.create_task("website_url", "website_key")
result = capsolver.join_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```

#### Recaptcha v2 enterprise

```python
from capsolver_python import RecaptchaV2EnterpriseTask

capsolver = RecaptchaV2EnterpriseTask("API_KEY")
task_id = capsolver.create_task("website_url", "website_key", {"s": "payload value"}, "api_domain")
result = capsolver.join_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```

#### GeeTest

```python
from capsolver_python import GeeTestTask

capsolver = GeeTestTask("API_KEY")
task_id = capsolver.create_task("website_url", "gt", "challenge")
result= capsolver.join_task_result(task_id)
print(result.get("challenge"))
print(result.get("seccode"))
print(result.get("validate"))
```


