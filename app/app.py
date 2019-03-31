from flask import Flask
import json
import grpc

from TrainingService_pb2 import TrainRequest, TrainResponse, TrainingInstanceInfo, TrainingInstanceList, InstanceFilter
from TrainingService_pb2_grpc import TrainingServiceStub

app = Flask(__name__)

trainingServiceChannel = grpc.insecure_channel("training_instance:8081")
trainingService = TrainingServiceStub(trainingServiceChannel)

@app.route('/')
def newTrainingInstance ():
    classlist = json.dumps(["airplane", "animal",
                            "building", "car",
                            "crowd", "dish_food",
                            "drink", "flower",
                            "house", "human",
                            "musical_instrument",
                            "plant", "shoe"])

    res = trainingService.TrainModel(
        TrainRequest(
            classlist=classlist, 
            classlist_locations="/thing, /thang, /nope"))
    return res.response

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8080)
    except KeyboardInterrupt:
        print("bye!")
        exit()