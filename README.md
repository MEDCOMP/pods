#PODS

Pods are taskflows which look at peas as individual tasks

## Setup taskflow

Install taskflow and requests

```Shell
pip install taskflow requests
```

edit line 17 of normalization.py to change the value of the url variable to the value of the normalization pea service url obtained as follows:

```Shell
minikube service pea-deployment --url
```

Now execute the normalization pod as follows:

```Shell
python normalization.py
```

