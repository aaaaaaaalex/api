from keras.models import model_from_json
from os import environ, walk
from tensorflow import logging as tflogging

import operator

class Predictor:
    def __init__(self, config):
        environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        tflogging.set_verbosity(tflogging.ERROR)

        self.currentModel = config['currentModel']
        self.models_dir = '/instances/'
        self.classifier = None
        self.classlist  = None
        self.minCertainty = 0.2


    def __classlist__(self):
        classes_path = self.models_dir + self.currentModel + '/dataset'
        class_dirs = [(d[0].split('/'))[-1] for d in walk(classes_path)]
        class_dirs = class_dirs[1:]
        self.classlist = sorted(class_dirs)
        return self.classlist


    # init classifier from config
    def __classifier__(self):
        classifier_path = self.models_dir + self.currentModel + '/'
        arch_path = classifier_path + "out/arch.json"
        weights_path = classifier_path + "out/weights.h5"

        f = open(arch_path, 'r')
        arch_json = f.read()
        f.close()
        
        model = model_from_json(arch_json)
        model.load_weights(weights_path)
        #model.compile(optimizer=SGD(lr=0.01, decay=0.0009), loss="categorical_crossentropy", metrics=['categorical_accuracy'])

        self.classifier = model
        return model


    def predict(self, x_input):
        if not self.classifier: self.__classifier__()
        if not self.classlist: self.__classlist__()
        
        prediction = self.classifier.predict(x_input)[0].astype(float)
        highest = sorted(
                    zip(self.classlist, prediction),
                    key=operator.itemgetter(1),
                    reverse=True)

        highest_classes = ([proba[0] for proba in highest if proba[1] > self.minCertainty])
        highest_probs   = ([proba[1] for proba in highest if proba[1] > self.minCertainty])

        return (highest_classes, highest_probs)


