from xmlrpc.client import ServerProxy

import xmlrpc

proxy = ServerProxy('http://localhost:3000',
                    allow_none=True,
                    verbose=True)

if __name__ == '__main__':
    print(proxy.list_directory('/Users/SMarya/WORK/'))
    # print(proxy.list_directory2('/Users/SMarya/WORK/'))
    # # print(proxy.list_directory('/Users/SMarya/WORK2/'))
    # print(proxy.return_none())
    # print(proxy._return_none2())
    '''
    xmlrpc.client.Fault: 
    <Fault 1: "<class 'TypeError'>:cannot marshal None unless allow_none is enabled">
    
    you need to be aware of translation of python types and xml supported types
    To pass instances across, only instance dictionary is passed along
    so we need to implement some form of pickling, to convert it
    binary data is handled with special Binary class
    any server methods prefixed with _ won't be available to clients(pvt methods)
    xmlrpc.client.Fault: 
    <Fault 1: '<class \'Exception\'>:method "_return_none2" is not supported'>
    '''
