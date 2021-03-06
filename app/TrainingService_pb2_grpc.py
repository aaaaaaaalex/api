# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import TrainingService_pb2 as TrainingService__pb2


class TrainingServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.TrainModel = channel.unary_unary(
        '/TrainingService/TrainModel',
        request_serializer=TrainingService__pb2.TrainRequest.SerializeToString,
        response_deserializer=TrainingService__pb2.TrainResponse.FromString,
        )
    self.GetActiveTrainingInstances = channel.unary_unary(
        '/TrainingService/GetActiveTrainingInstances',
        request_serializer=TrainingService__pb2.InstanceFilter.SerializeToString,
        response_deserializer=TrainingService__pb2.TrainingInstanceList.FromString,
        )


class TrainingServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def TrainModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetActiveTrainingInstances(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TrainingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'TrainModel': grpc.unary_unary_rpc_method_handler(
          servicer.TrainModel,
          request_deserializer=TrainingService__pb2.TrainRequest.FromString,
          response_serializer=TrainingService__pb2.TrainResponse.SerializeToString,
      ),
      'GetActiveTrainingInstances': grpc.unary_unary_rpc_method_handler(
          servicer.GetActiveTrainingInstances,
          request_deserializer=TrainingService__pb2.InstanceFilter.FromString,
          response_serializer=TrainingService__pb2.TrainingInstanceList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TrainingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
