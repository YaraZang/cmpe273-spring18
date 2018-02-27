import time
import grpc
import drone_pb2
import drone_pb2_grpc
import sys
import re

from concurrent import futures

class Server(drone_pb2_grpc.CalculatorServicer):
    def __init__(self,x,y,z,pdx,pdy,pdz):
        self.id = 0
        self.x = x
        self.y = y
        self.z = z
        self.pdx = pdx
        self.pdy = pdy
        self.pdz = pdz

    def change(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def CoordinateCalculator(self, request, context):
        drone_id = self.id
        self.id = self.id + 1
        while 1:
            yield drone_pb2.Response(id=drone_id,x=self.x+self.pdx*drone_id,y=self.y+self.pdy*drone_id,z=self.z+self.pdz*drone_id)
            time.sleep(2)



def run(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    x = 0
    y = 0
    z = 0
    pdx = 10
    pdy = 0
    pdz = 0
    try:
        start_cooridnate = sys.argv[1]
        startlist = start_cooridnate.split(',')
        x  = int(startlist[0])
        y  = int(startlist[1])
        z  = int(startlist[2])
    except:
        x = 0
        y = 0
        z = 0
    try:
        peer_distance = sys.argv[2]
        peerlist = peer_distance.split(',')
        pdx = int(peerlist[0])
        pdy = int(peerlist[1])
        pdz = int(peerlist[2])
    except:
        pdx = 10
        pdy = 0
        pdz = 0
    s = Server(x,y,z,pdx,pdy,pdz)
    drone_pb2_grpc.add_CalculatorServicer_to_server(s, server)
    server.add_insecure_port('%s:%d' % (host, port))
    # server.add_insecure_port('[::]:50050')
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        print("Server started at...%d" % port)
        while True:
            new_coordinate = input("Enter New Coordinate [x, y, z] > ")
            try:
                newlist = re.findall(r'\d+', new_coordinate)
                x = int(newlist[0])
                y = int(newlist[1])
                z = int(newlist[2])
                print('get command flying to %d,%d,%d'%(x,y,z))
                s.change(x,y,z)
            except:
                continue
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('localhost', 50050)
