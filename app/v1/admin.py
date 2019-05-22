from flask import Blueprint, request
import json
import grpc
import random

from TrainingService_pb2 import TrainRequest, TrainResponse, TrainingInstanceInfo, TrainingInstanceList, InstanceFilter
from TrainingService_pb2_grpc import TrainingServiceStub

trainingServiceChannel = grpc.insecure_channel("training_instance:8081")
trainingService = TrainingServiceStub(trainingServiceChannel)

app = Blueprint('admin-app', __name__, url_prefix='/v1')


quotes = [
    "Gentlemen, you can't fight in here! This is the War Room.",
    "...Nobody calls me Lebowski. You got the wrong guy. I'm the Dude, man.",
    "Joey, do you like movies about gladiators?",
    "I'm in a glass case of emotion!",
    "If I'm not back in five minutes, just wait longer.",
    "Electrolytes, it’s what plants crave!",
    "If you can dodge a wrench, you can dodge a ball.",
    "Take my strong hand.",
    "Did we just become best friends?"
]


@app.route("/")
def sayHello():
    i = random.randint(0, len(quotes)-1)
    res = '<html><body><h1>{}: "{}"</h1></body></html>'.format(i, quotes[i])
    return res


@app.route('/spawnInstance', methods=["POST"])
def newTrainingInstance ():
    classlist = request.form.getlist('class')
    classlistjson = json.dumps(classlist) if classlist else None
    checkpoint_name = request.form.get('checkpointName')
    instance_name = request.form.get('instanceName')

    res = trainingService.TrainModel(
        TrainRequest(
            classlist = classlistjson,
            checkpoint_name = checkpoint_name,
            instance_name = instance_name
        ))
    instance_name = res.instance_name

    return json.dumps({'response': res.response, 'instance_name': instance_name })


@app.route('/changeModel', methods=['POST'])
def changeModel():
    return "sddf"