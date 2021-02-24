from xmlrpc.server import SimpleXMLRPCServer
import os

# Define Server config, create server instance
server = SimpleXMLRPCServer(('localhost', 3000),
                            logRequests=True,
                            allow_none=True, )


# Define any functions we want available
def list_directory(dir):
    return os.listdir(dir)


def return_none():
    return None


class TestClass:
    def list_directory2(self, dir):
        return os.listdir(dir)

    def _return_none2(self):
        return None


# Register these functions with server instance
server.register_function(list_directory, 'ls')
server.register_function(return_none)

server.register_instance(TestClass())
# start accepting connections from clients
if __name__ == '__main__':
    try:
        print('Serving...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')
