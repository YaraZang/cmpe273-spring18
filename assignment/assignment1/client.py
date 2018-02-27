from __future__ import print_function

import grpc
import drone_pb2
import drone_pb2_grpc
import sys

def run(host, port):
    channel = grpc.insecure_channel('%s:%d' % (host, port))
    stub = drone_pb2_grpc.CalculatorStub(channel)

    responses = stub.CoordinateCalculator(drone_pb2.Request())
    flag = True
    x = -1
    y = -1
    z = -1
    for response in responses:
        if(flag):
            print('Client id [%d] connected to the server.'%(response.id))
            flag = False
        if(x!=response.x or y!=response.y or z!=response.z):
            print('[received] moving to [%d,%d,%d]'%(response.x,response.y,response.z))
            x=response.x
            y=response.y
            z=response.z

port = 50050
try:
    print (sys.argv[1])
    port = int(sys.argv[1])
except:
    port = 50050

run('localhost',port)
