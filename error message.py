# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:49:21 2015

@author: Deepti Boddapati
/deeptiboddapati
"""

[18/Jun/2015 14:40:06]"POST /addbill/ HTTP/1.1" 500 136981
Traceback (most recent call last):
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 138, in run
    self.finish_response()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 180, in finish_response
    self.write(data)
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 274, in write
    self.send_headers()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 332, in send_headers
    self.send_preamble()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 255, in send_preamble
    ('Date: %s\r\n' % format_date_time(time.time())).encode('iso-8859-1')
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 453, in _write
    self.stdout.write(data)
  File "C:\Users\Corbin\Anaconda3\lib\socket.py", line 394, in write
    return self._sock.send(b)
ConnectionAbortedError: [WinError 10053] An established connection was aborted by the software in your host machine
[18/Jun/2015 14:40:06]"POST /addbill/ HTTP/1.1" 500 59
----------------------------------------
Exception happened during processing of request from ('127.0.0.1', 60505)
Traceback (most recent call last):
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 138, in run
    self.finish_response()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 180, in finish_response
    self.write(data)
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 274, in write
    self.send_headers()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 332, in send_headers
    self.send_preamble()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 255, in send_preamble
    ('Date: %s\r\n' % format_date_time(time.time())).encode('iso-8859-1')
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 453, in _write
    self.stdout.write(data)
  File "C:\Users\Corbin\Anaconda3\lib\socket.py", line 394, in write
    return self._sock.send(b)
ConnectionAbortedError: [WinError 10053] An established connection was aborted by the software in your host machine

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 141, in run
    self.handle_error()
  File "C:\Users\Corbin\Anaconda3\lib\site-packages\django\core\servers\basehttp.py", line 95, in handle_error
    super(ServerHandler, self).handle_error()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 368, in handle_error
    self.finish_response()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 180, in finish_response
    self.write(data)
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 274, in write
    self.send_headers()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 331, in send_headers
    if not self.origin_server or self.client_is_modern():
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 344, in client_is_modern
    return self.environ['SERVER_PROTOCOL'].upper() != 'HTTP/0.9'
TypeError: 'NoneType' object is not subscriptable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Corbin\Anaconda3\lib\socketserver.py", line 617, in process_request_thread
    self.finish_request(request, client_address)
  File "C:\Users\Corbin\Anaconda3\lib\socketserver.py", line 344, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "C:\Users\Corbin\Anaconda3\lib\site-packages\django\core\servers\basehttp.py", line 102, in __init__
    super(WSGIRequestHandler, self).__init__(*args, **kwargs)
  File "C:\Users\Corbin\Anaconda3\lib\socketserver.py", line 673, in __init__
    self.handle()
  File "C:\Users\Corbin\Anaconda3\lib\site-packages\django\core\servers\basehttp.py", line 182, in handle
    handler.run(self.server.get_app())
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\handlers.py", line 144, in run
    self.close()
  File "C:\Users\Corbin\Anaconda3\lib\wsgiref\simple_server.py", line 35, in close
    self.status.split(' ',1)[0], self.bytes_sent
AttributeError: 'NoneType' object has no attribute 'split'
----------------------------------------