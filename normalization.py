import requests
import json
from random import randint

from taskflow import engines
from taskflow.patterns import linear_flow as lf
from taskflow.patterns import unordered_flow as uf
from taskflow import task

class normalize(task.Task):
    def __init__(self, name, show_name=True, inject=None):
        super(normalize, self).__init__(name, inject=inject)
        self._show_name = show_name

    def execute(self, output):
        headers = {'content-type': 'application/json'}
        url = 'http://192.168.99.101:31142'
        data = {"array":output}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        print("%s: %s" % (self.name, response.text))

normalizationPod = lf.Flow('hello')

dataList = [('task1', [randint(0,9),randint(0,9),randint(0,9)]), ('task2', [randint(0,9),randint(0,9),randint(0,9)]), ('task3', [randint(0,9),randint(0,9),randint(0,9)])]
for (name, data) in dataList:
    print data
    normalizationPod.add(normalize("%s@hello" % name, inject={'output': data}))

print "\nExecuting the pod..."
e = engines.load(normalizationPod, engine='serial')
e.run()