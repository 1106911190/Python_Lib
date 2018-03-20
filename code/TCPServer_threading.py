# coding=utf-8

from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler


class Server(ThreadingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting .')

server = Server(('', 8899), Handler)
server.serve_forever()
