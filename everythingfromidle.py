Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
[]
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
[]
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
[]
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
alues.t_start;e=d?e+d:CavalryLogger.now();this.setValue(a,e,b,c);this.tti_event&&a==this.tti_event&&(this.lastTtiValue=e,this.setTimeStamp("t_tti",b));return this},CavalryLogger.prototype.mark=typeof 
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
alues.t_start;e=d?e+d:CavalryLogger.now();this.setValue(a,e,b,c);this.tti_event&&a==this.tti_event&&(this.lastTtiValue=e,this.setTimeStamp("t_tti",b));return this},CavalryLogger.prototype.mark=typeof console==="object"&&console.timeStamp?function(a){console.timeStamp(a)}:function(){},CavalryLogger.prototype.addPiggyback=function(a,b){this.piggy_values[a]=b;return this},CavalryLogger.instances={},CavalryLogger.id=0,CavalryLogger.disableArtilleryOnUntilOffLogging=!1,CavalryLogger.getInstance=function(a){typeof a==="undefined"&&(a=CavalryLogger.id);CavalryLogger.instances[a]||(CavalryLogger.instances[a]=new CavalryLogger(a));return CavalryLogger.instances[a]},CavalryLogger.setPageID=function(a){if(CavalryLogger.id===0){var b=CavalryLogger.getInstance();CavalryLogger.instances[a]=b;CavalryLogger.instances[a].lid=a;delete CavalryLogger.instances[0]}CavalryLogger.id=a},CavalryLogger.now=function(){return window.performance&&performance.timing&&performance.timing.navigationStart&&performance.now?performance.now()+performance.timing.navigationStart:new Date().getTime()},CavalryLogger.prototype.measureResources=function(){},CavalryLogger.prototype.profileEarlyResources=function(){},CavalryL
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
False
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
True
>>> p
<Response [200]>
>>> 
= RESTART: C:\Users\Rajdeep\Documents\Python Code\selenium\facebook tagall\lister.py
log in to your account from the browser window (you might need to enable cookies and then type something and press enter here: 
>>> driver.get("https://www.facebook.com/rajdeeprusted/friends")
Traceback (most recent call last):
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 426, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 421, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1344, in getresponse
    response.begin()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 306, in begin
    version, status, reason = self._read_status()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 267, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\socket.py", line 589, in readinto
    return self._sock.recv_into(b)
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    driver.get("https://www.facebook.com/rajdeeprusted/friends")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 333, in get
    self.execute(Command.GET, {'url': url})
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 319, in execute
    response = self.command_executor.execute(driver_command, params)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 374, in execute
    return self._request(command_info[0], url, body=data)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 397, in _request
    resp = self._conn.request(method, url, body=body, headers=headers)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\request.py", line 80, in request
    method, url, fields=fields, headers=headers, **urlopen_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\request.py", line 171, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\poolmanager.py", line 336, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 725, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\util\retry.py", line 403, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\packages\six.py", line 734, in reraise
    raise value.with_traceback(tb)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 426, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 421, in _make_request
    httplib_response = conn.getresponse()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1344, in getresponse
    response.begin()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 306, in begin
    version, status, reason = self._read_status()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 267, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\socket.py", line 589, in readinto
    return self._sock.recv_into(b)
urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
>>> driver.get("https://www.facebook.com/rajdeeprusted/friends")
Traceback (most recent call last):
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connection.py", line 160, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\util\connection.py", line 84, in create_connection
    raise err
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\util\connection.py", line 74, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 392, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1252, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1298, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1247, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 966, in send
    self.connect()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connection.py", line 187, in connect
    conn = self._new_conn()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connection.py", line 172, in _new_conn
    self, "Failed to establish a new connection: %s" % e
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x00000247A9253188>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    driver.get("https://www.facebook.com/rajdeeprusted/friends")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 333, in get
    self.execute(Command.GET, {'url': url})
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 319, in execute
    response = self.command_executor.execute(driver_command, params)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 374, in execute
    return self._request(command_info[0], url, body=data)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 397, in _request
    resp = self._conn.request(method, url, body=body, headers=headers)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\request.py", line 80, in request
    method, url, fields=fields, headers=headers, **urlopen_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\request.py", line 171, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\poolmanager.py", line 336, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 765, in urlopen
    **response_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 765, in urlopen
    **response_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 765, in urlopen
    **response_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 725, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\util\retry.py", line 439, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=52655): Max retries exceeded with url: /session/b4ed63c60e373bbc784a3cfe6865ad6b/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000247A9253188>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
>>> driver.get("https://www.facebook.com/rajdeeprusted/friends")
Traceback (most recent call last):
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connection.py", line 160, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\util\connection.py", line 84, in create_connection
    raise err
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\util\connection.py", line 74, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 677, in urlopen
    chunked=chunked,
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 392, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1252, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1298, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1247, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 966, in send
    self.connect()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connection.py", line 187, in connect
    conn = self._new_conn()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connection.py", line 172, in _new_conn
    self, "Failed to establish a new connection: %s" % e
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x00000247A9267548>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    driver.get("https://www.facebook.com/rajdeeprusted/friends")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 333, in get
    self.execute(Command.GET, {'url': url})
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 319, in execute
    response = self.command_executor.execute(driver_command, params)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 374, in execute
    return self._request(command_info[0], url, body=data)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 397, in _request
    resp = self._conn.request(method, url, body=body, headers=headers)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\request.py", line 80, in request
    method, url, fields=fields, headers=headers, **urlopen_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\request.py", line 171, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\poolmanager.py", line 336, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 765, in urlopen
    **response_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 765, in urlopen
    **response_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 765, in urlopen
    **response_kw
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\connectionpool.py", line 725, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\urllib3\util\retry.py", line 439, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=52655): Max retries exceeded with url: /session/b4ed63c60e373bbc784a3cfe6865ad6b/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000247A9267548>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
>>> driver = webdriver.Chrome(executable_path='..\chromedriver.exe')
>>> driver.get("https://www.facebook.com/rajdeeprusted/friends")
>>> driver.get("https://www.facebook.com/rajdeeprusted/friends")
>>> driver.find_elements(By.XPATH, "//a/span/text()")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    driver.find_elements(By.XPATH, "//a/span/text()")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 1007, in find_elements
    'value': value})['value'] or []
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.InvalidSelectorException: Message: invalid selector: The result of the xpath expression "//a/span/text()" is: [object Text]. It should be an element.
  (Session info: chrome=81.0.4044.138)

>>> driver.find_elements(By.XPATH, "//a/span/")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    driver.find_elements(By.XPATH, "//a/span/")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 1007, in find_elements
    'value': value})['value'] or []
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.InvalidSelectorException: Message: invalid selector: Unable to locate an element with the xpath expression //a/span/ because of the following error:
SyntaxError: Failed to execute 'evaluate' on 'Document': The string '//a/span/' is not a valid XPath expression.
  (Session info: chrome=81.0.4044.138)

>>> driver.find_elements(By.XPATH, "//a/span")
[<selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="2ba3f1dc-1e61-4966-b5af-b64d41c8824f")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="ae14386a-a392-412e-9caa-b8d880bb3557")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="18753b01-cebd-43f5-9cc2-1c2066fc218a")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="f14cf16b-5e49-4032-8274-056e12c44649")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="628b74a3-2dbf-462b-b29d-caf7446f8b29")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="b69c2384-2889-4e36-9098-2e3d9bd9efad")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="f66f983e-46e8-47cc-986f-e6f2daa46028")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="b95b3af2-05ef-4fce-86ad-2a8344c95691")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="305d2839-07d6-4469-8c33-2b5daae2ae55")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="2a7a9d6d-82d6-45ed-acc6-0c3ff400bc79")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="80270115-517f-4b01-985b-052e170c849d")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="82ca67b6-09f0-497d-ade0-565422717280")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="e9afab12-2404-4885-9659-217295232f17")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="7d98d809-ed05-46d0-8d9b-02a545b7d086")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="4aec8654-abe2-4965-934d-da10267b3fa7")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="6097e278-3074-4bb8-ad64-c555a5e976dc")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="7b4d6ba4-7926-4797-9ffa-9418b026ba60")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="0b1bf0f2-2d46-4fa6-82d1-f3106aac58bd")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="34e8bed5-7138-4bf2-bc9c-dc8d4f0744c0")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="dc9f1cb0-e67f-4302-be6d-c0ad122e0c25")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="d4ea6309-39be-47a1-bc15-addd41f0f252")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="cedd912b-4b1e-4cd8-9eff-995d64d6a9fd")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="48430e68-b982-4f8f-b9fc-0c64111a0de7")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="7c68f31b-4a59-4d4f-9980-705d61999f0c")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="d4c760ed-6660-47d0-8d62-a0cb6219e714")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="a2e6501f-b039-4943-82ca-d4d5c7cfcd1d")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="df8fc4a6-ee05-4429-bb3d-61dfb25b35a5")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="8870ed5d-82e8-4c4a-98d6-0246d9d0f664")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="7199a8cb-70d7-4c45-a2ad-c505851d3014")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="e1f7ffdb-9694-4194-80aa-e5eb0769279b")>, <selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="3eb3ed1b-a02d-4513-95bf-736de158d43a")>]
>>> driver.find_elements(By.XPATH, "//a/span/text()").text()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    driver.find_elements(By.XPATH, "//a/span/text()").text()
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 1007, in find_elements
    'value': value})['value'] or []
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.InvalidSelectorException: Message: invalid selector: The result of the xpath expression "//a/span/text()" is: [object Text]. It should be an element.
  (Session info: chrome=81.0.4044.138)

>>> driver.find_elements(By.XPATH, "//a/span").text
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    driver.find_elements(By.XPATH, "//a/span").text
AttributeError: 'list' object has no attribute 'text'
>>> driver.find_element'(By.XPATH, "//a/span").text
SyntaxError: EOL while scanning string literal
>>> driver.find_element(By.XPATH, "//a/span").text
''
>>> for item in driver.find_elements(By.XPATH, "//a/span"):
	print(item.text)

	








Raunak Mitra
3 mutual friends

Debashish Sarkar
113 mutual friends

Jisan Mondal
95 mutual friends

Soumik Ghosh
1 mutual friend

Yash Kalbere
3 mutual friends

Sayantan Bagchi
113 mutual friends

Tanujit Mitra
66 mutual friends

Abhijit Kalita
2 mutual friends
>>> for friend in driver.find_elements(By.XPATH, "//div/div/a/span"):
	print(friend.text)

	


Raunak Mitra
3 mutual friends

Debashish Sarkar
113 mutual friends

Jisan Mondal
95 mutual friends

Soumik Ghosh
1 mutual friend

Yash Kalbere
3 mutual friends

Sayantan Bagchi
113 mutual friends

Tanujit Mitra
66 mutual friends

Abhijit Kalita
2 mutual friends

Shantanu Singh
123 mutual friends

Sloke Tamang
105 mutual friends

Saumyadeep Chakraborty
73 mutual friends

Gaurab Banerjee
102 mutual friends

Projjwal Dhar
18 mutual friends

Enza Haque
34 mutual friends

Abhijit Kalita

Monojyoti Bhattacharjee
3 mutual friends

Shouvik Kar
92 mutual friends

Sourav Moitra
35 mutual friends

Rahul Dhar II
47 mutual friends

Anandd Sharma
55 mutual friends

Tamanna Das
61 mutual friends

Sayantika Chandra
85 mutual friends

Odyssey Roy
5 mutual friends

Šaų Řav
60 mutual friends

Ivan Deutsch
26 mutual friends

Pratyush Mukherjee
82 mutual friends

Chandramouli Neil Chaudhuri
1 mutual friend

Souvik SaVi Karmakar
19 mutual friends

Bandhan Biswas
68 mutual friends

Dwaipayan Mukherjee
25 mutual friends

Ritobroto Das
21 mutual friends

Shawli Sinha
58 mutual friends

Utsav Thakkar
116 mutual friends

Rahul Basu Ray
93 mutual friends

Pratyay Goswami
182 mutual friends

Manimekhala Chakraborty
65 mutual friends

Swapnil Saha
151 mutual friends

Kunal Pal
39 mutual friends

Nilankoor Biswas
24 mutual friends

Debdeepa Paul
96 mutual friends

Ankita Bhattacharyya
4 mutual friends

Aditya Kumar Bhatt
62 mutual friends

Sanket Sarkar
91 mutual friends

Aparajita Saha
52 mutual friends

Pratishruti Sarkar
45 mutual friends

Jinia Chaudhuri
116 mutual friends

Tithi Dutta
98 mutual friends

Mani Sha Halder
3 mutual friends

Er Deepak Budakia
7 mutual friends

Yash Kanoria
131 mutual friends

Sushovan Dey
62 mutual friends

Anubrata Dutta
76 mutual friends

Nishan Das
1 mutual friend

Sudip Banik Bumba
38 mutual friends

Sagar Dutta
135 mutual friends

Abhishek Thakre
115 mutual friends

Debjit Chakraborty
40 mutual friends

Subhomoy Chakrabarti
63 mutual friends

Uttam Singh
70 mutual friends

Deboleena Ghosh
192 mutual friends

Annesha Gupta
60 mutual friends

Sayan Barat
33 mutual friends

Husain Madraswala
88 mutual friends

Boudhayan Dev
3 mutual friends

Ananya Dey
46 mutual friends

ArkaJyoti Kundu
20 mutual friends

Shinjini Roy
87 mutual friends

Bikash Basfore
40 mutual friends

Nilanjana Das Sarkar

Addri Saha
40 mutual friends

Pranay Paul
39 mutual friends

Titli Sarkar
77 mutual friends

Piya De
65 mutual friends

Rittik Biswas
5 mutual friends

Keerat Marwah
9 mutual friends

Swarnava Mukherjee
1 mutual friend

Sandeep Chatterjee
15 mutual friends

Suvankar Dey Pritam
24 mutual friends

Soham Biswas
10 mutual friends

Avijit Das
52 mutual friends

Brotin Bhattacharya
73 mutual friends

Rishav Gupta
42 mutual friends

Debarpan Bandyopadhyay
78 mutual friends

Ankit Sharma
6 mutual friends

Sayandeep Majumdar
13 mutual friends

Kuntal Roy
151 mutual friends

Sankha Subhra Sarkar
186 mutual friends

Suvodeep Saha
55 mutual friends

Subhadeep Ghosh
47 mutual friends

Rohit Kaushal
38 mutual friends

Tamal Baran Bhattacharya
166 mutual friends

Anindita Sengupta
49 mutual friends

Meghna Das
53 mutual friends

Vivek Kalyanarangan
1 mutual friend

Saswata Kumar Sarkar
144 mutual friends

Meghasree Moitra
192 mutual friends

Sujoy Bhattacharyya
176 mutual friends

Udipta Ghosh
2 mutual friends

Swastick Mitra
22 mutual friends

Priyanka De
134 mutual friends

Malovika Bagchi
8 mutual friends

Rajdip Ray
102 mutual friends

Mriganka Mrv Joardar
177 mutual friends

Sanjana Das
164 mutual friends

Pritha Sarkar
104 mutual friends

Bhaskar Debnath
82 mutual friends

Subhojit Dam
54 mutual friends

Luca Martinez Bergamin
2 mutual friends

Purbasa Seal
43 mutual friends

Ritwick Bhattacharyya
10 mutual friends

Soumen Mete
118 mutual friends

Shubham Chanda
68 mutual friends

Harinder Singh Batra
7 mutual friends

Krishnanu Chatterjee
83 mutual friends

Sayan Dutta
119 mutual friends

Vasundhara Agarwal
2 mutual friends

Bipul Mukherjee
64 mutual friends

Swastik Hazra
39 mutual friends

Sîñgh Shwétá
24 mutual friends

Babai Hazra
110 mutual friends

Sajid Imran
5 mutual friends

Sahil Hassan
30 mutual friends

Rhythm Gupta
55 mutual friends

Shreeja Paul
100 mutual friends

Chitrak Shaw
18 mutual friends

Aadarsh Pradhan
70 mutual friends

Sayani Dutta
94 mutual friends

Pallabi Nandi
113 mutual friends

Subhadip Shaw
96 mutual friends

Joyee Biswas
3 mutual friends

Amit ThaPa
119 mutual friends

Sayanta Majumder
28 mutual friends

Abhinandan Das
148 mutual friends

Aritra Basu
116 mutual friends

Sourav Kundu
97 mutual friends

Shubhrajyoti Ghosh
49 mutual friends

Anilavo Chatterjee
24 mutual friends

Utkarsh Bardewa
123 mutual friends

Prasun Kundu
61 mutual friends

Parizat Rana
64 mutual friends

Shràbànà Dàs
31 mutual friends

Udita Basu
53 mutual friends

Sandip Banik
8 mutual friends

Ashmita Nair
99 mutual friends

Shreshtha Mukherjee
56 mutual friends

Kaushik Dutta Roy
15 mutual friends

Utsha Chakraborty
74 mutual friends

Manjistha Roy
103 mutual friends

Madhumita Dey Deb
8 mutual friends

Supriyo Roy
54 mutual friends

Aniket Verma
10 mutual friends

Arbaz Khan
93 mutual friends

Rimi Paul
115 mutual friends

Bipul Mukherjee II
56 mutual friends

Sourav Das
63 mutual friends

Ishika Dutta
58 mutual friends

Mayukh Talukdar
21 mutual friends

Addrian Rogers
23 mutual friends

Saswata Mondal
66 mutual friends

Sarthak Dan
62 mutual friends

Sinjana Mondal
54 mutual friends

Oindrila Chatterjee
67 mutual friends

Sneha Roy
67 mutual friends

Purvii Sarkar
36 mutual friends

Dasgupta Ankitaa
32 mutual friends

Ronit SenGupta
54 mutual friends

Triparna Chakraborty
46 mutual friends

Soumyajit Sarkar
91 mutual friends

Soutik Talukder
51 mutual friends

Prerna Maity
16 mutual friends

Ishita Nandi

Dey Misti
119 mutual friends

Ankita Barman
66 mutual friends

Piyal Prashed Dutta
47 mutual friends

Kuheli Bhowmick
102 mutual friends

Debraj Nandi
124 mutual friends

Ananya Chourasia
49 mutual friends

Shreeja Paul
64 mutual friends

Sholanki Das
113 mutual friends

Jessie Jocelyne Minj
19 mutual friends

Riya Das
63 mutual friends

Shreyoshi Saha
71 mutual friends

Anirban Chakraborty
157 mutual friends

Ankita Dutta
75 mutual friends

Sayoni Chatterjee
65 mutual friends

Priyanka Jha
51 mutual friends

Paulami Barman Pramanik
123 mutual friends

Medha Das
47 mutual friends

Ankita Dasgupta
114 mutual friends

Tamisra Santra
50 mutual friends

Pratik Biswas
14 mutual friends

Rajashree Chowdhury
42 mutual friends

Debasmita Das
54 mutual friends

Jòyèèta Bose
91 mutual friends

Chitrak Saarkar
80 mutual friends

Mayuri Mutkule
76 mutual friends

Tamoghna Chanda
85 mutual friends

Ragini Dutta
77 mutual friends

Kavita Choudhary
52 mutual friends

Riya Bhowmick
82 mutual friends

Nikita Chowdhury
34 mutual friends

Sushmita Chhetri
52 mutual friends

Priyanka Saha
80 mutual friends

Shrestha Kundu
97 mutual friends

Kumar Saurabh
78 mutual friends

AriSha GhOsh
124 mutual friends

Ankhee Biswas
139 mutual friends

Darshana Ghosh
58 mutual friends

Ely Dutta
133 mutual friends

Pŕïťhù Lá
52 mutual friends

Puja Poddar
26 mutual friends

Saheli Bakshi
45 mutual friends

Puja Sen
48 mutual friends

Shapath Ghosh
74 mutual friends

Pratik Saha
112 mutual friends

Sayani Debnath
142 mutual friends

Snowme Roy
91 mutual friends

Shreyashi Das
73 mutual friends

Sanandita Dey
55 mutual friends

Anindita Saha
106 mutual friends

Akash D Cruz
51 mutual friends

Chandrachur Mukherjee
74 mutual friends

Javed JS
62 mutual friends

Shamadrita Ghosh Ghosh
46 mutual friends

Sudeep Dutta
126 mutual friends

Deboshmita Das
28 mutual friends

Nairita Mukherjee
44 mutual friends

Susmita Singha
88 mutual friends

Tiasha Roy
63 mutual friends

Mrjain MJ
22 mutual friends

Julee Dutta
191 mutual friends

Subhadeep Ash
57 mutual friends

Pallabi Sinha
116 mutual friends

Sujata Chauhan
35 mutual friends

Barnini Ghosh
72 mutual friends

Sowmitra Sarker
121 mutual friends

Harsh Jaiswal
149 mutual friends

Snigdha Sil
95 mutual friends

Jyotirmay Sen
68 mutual friends

Eishita Sharma
73 mutual friends

Subhrajit Datta
90 mutual friends

Pritish Sharma
117 mutual friends

Sourav Maiti
148 mutual friends

Abishek Agarwal
80 mutual friends

Souvik Laskar
67 mutual friends

Ro H An II
67 mutual friends

AñYå Kãpøør
83 mutual friends

Soumita Chakraborty
144 mutual friends

Rithika Sharma
48 mutual friends

Dishani Dutta
29 mutual friends

Adway Rakshit
63 mutual friends

Soni Gupta
84 mutual friends

Ronit Paul
86 mutual friends

Roman Kujur
47 mutual friends

Promiť Mondal
92 mutual friends

AnkiTa Sharma
111 mutual friends

Tanmoy Chowdhury
227 mutual friends

Deep Raj Oraon
132 mutual friends

Soumallya Misra
41 mutual friends

Diksha Thapa Mangar
129 mutual friends

Manasi Daripa
38 mutual friends

Shailja Agarwal
30 mutual friends

Subham Saha
206 mutual friends

Arbind Prasad
128 mutual friends

Ambika Sharma
66 mutual friends

Mousumi Das
93 mutual friends

Prernaa Choudhary
55 mutual friends

Jaswinder Kaur
32 mutual friends

Soumyadip Das
157 mutual friends

Lovely Chatterjee
91 mutual friends

Ben Cry
22 mutual friends

Sarmistha Dey
71 mutual friends

Monalisa Ghosh
70 mutual friends

Sarthak Dubey
72 mutual friends

Shalini Pradhan
85 mutual friends

Soumita Jana
39 mutual friends

Nilanjana Chakraborty
38 mutual friends

Soumita Chakraborty
87 mutual friends

Sushmita Das
112 mutual friends

Gunjan Jacob
56 mutual friends

Samrat Sarkar
136 mutual friends

Tonmoy Saha
193 mutual friends

Subhojit Saha
87 mutual friends

Ambika Sarkar
148 mutual friends

Avilash Chakraborty
67 mutual friends

Eric Lomga
36 mutual friends

Arnab Mukherjee
86 mutual friends

Ishita Das
157 mutual friends

Siddhant Mukherjee
142 mutual friends

Nita Samuel
113 mutual friends

Soumya Mariner Mukhopadhyay
162 mutual friends

Prasenjit Saha
142 mutual friends

Priscilla Konyak
79 mutual friends

Samhoti Lahiri
61 mutual friends

Pritam De
124 mutual friends

Sourav Dutta
115 mutual friends

Madhurima Das Burman
86 mutual friends

Debolina Rakshit
137 mutual friends
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    print(friend.text)
KeyboardInterrupt
>>> with open('/frans.txt', 'w') as f:
	for item in driver.find_elements(By.XPATH, "//div/div/a/span"):
		f.write(item.text)

		
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    with open('/frans.txt', 'w') as f:
PermissionError: [Errno 13] Permission denied: '/frans.txt'
>>> with open('/frans.txt', 'w') as f:
	for item in driver.find_elements(By.XPATH, "//div/div/a/span"):
		f.write(item.text)

		
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    with open('/frans.txt', 'w') as f:
PermissionError: [Errno 13] Permission denied: '/frans.txt'
>>> open('frans.txt', 'r')
<_io.TextIOWrapper name='frans.txt' mode='r' encoding='cp1252'>
>>> open('frans.txt', 'w')
<_io.TextIOWrapper name='frans.txt' mode='w' encoding='cp1252'>
>>> with open('/frans.txt', 'w') as f:
	for item in driver.find_elements(By.XPATH, "//div/div/a/span"):
		f.write(item.text)

		
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    with open('/frans.txt', 'w') as f:
PermissionError: [Errno 13] Permission denied: '/frans.txt'
>>> with open('/frans.txt', 'a') as f:
	for item in driver.find_elements(By.XPATH, "//div/div/a/span"):
		f.write(item.text)

		
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    with open('/frans.txt', 'a') as f:
PermissionError: [Errno 13] Permission denied: '/frans.txt'
>>> with open('frans.txt', 'w') as f:
	for item in driver.find_elements(By.XPATH, "//div/div/a/span"):
		f.write(item.text)

		
0
0
12
16
0
16
18
0
12
17
0
12
15
0
12
16
0
15
18
0
13
17
0
14
16
0
14
18
0
12
18
0
22
17
0
15
18
0
13
17
0
10
17
0
14
0
23
16
0
11
17
0
13
17
0
13
17
0
13
17
0
11
17
0
17
17
0
11
16
0
Traceback (most recent call last):
  File "<pyshell#33>", line 3, in <module>
    f.write(item.text)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u0173' in position 2: character maps to <undefined>
>>> with open('frans.txt', 'w') as f:
	for item in driver.find_elements(By.XPATH, "//div/div/a/span"):
		f.write(item.text + "\n")

		
1
1
13
17
1
17
19
1
13
18
1
13
16
1
13
17
1
16
19
1
14
18
1
15
17
1
15
19
1
13
19
1
23
18
1
16
19
1
14
18
1
11
18
1
15
1
24
17
1
12
18
1
14
18
1
14
18
1
14
18
1
12
18
1
18
18
1
12
17
1
Traceback (most recent call last):
  File "<pyshell#35>", line 3, in <module>
    f.write(item.text + "\n")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u0173' in position 2: character maps to <undefined>
>>> frans = []
>>> with open('frans.txt', 'r') as f:
	print(f)

	
<_io.TextIOWrapper name='frans.txt' mode='r' encoding='cp1252'>
>>> with open('frans.txt', 'r') as f:
	for item in f:
		print(item)

		




Raunak Mitra

3 mutual friends



Debashish Sarkar

113 mutual friends



Jisan Mondal

95 mutual friends



Soumik Ghosh

1 mutual friend



Yash Kalbere

3 mutual friends



Sayantan Bagchi

113 mutual friends



Tanujit Mitra

66 mutual friends



Abhijit Kalita

2 mutual friends



Shantanu Singh

123 mutual friends



Sloke Tamang

105 mutual friends



Saumyadeep Chakraborty

73 mutual friends



Gaurab Banerjee

102 mutual friends



Projjwal Dhar

18 mutual friends



Enza Haque

34 mutual friends



Abhijit Kalita



Monojyoti Bhattacharjee

3 mutual friends



Shouvik Kar

92 mutual friends



Sourav Moitra

35 mutual friends



Rahul Dhar II

47 mutual friends



Anandd Sharma

55 mutual friends



Tamanna Das

61 mutual friends



Sayantika Chandra

85 mutual friends



Odyssey Roy

5 mutual friends



>>> with open('frans.txt', 'r') as f:
	for item in f:
		if item and if item[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			
SyntaxError: invalid syntax
>>> with open('frans.txt', 'r') as f:
	for item in f:
		if item and item[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			print(item)

			
Raunak Mitra

Debashish Sarkar

Jisan Mondal

Soumik Ghosh

Yash Kalbere

Sayantan Bagchi

Tanujit Mitra

Abhijit Kalita

Shantanu Singh

Sloke Tamang

Saumyadeep Chakraborty

Gaurab Banerjee

Projjwal Dhar

Enza Haque

Abhijit Kalita

Monojyoti Bhattacharjee

Shouvik Kar

Sourav Moitra

Rahul Dhar II

Anandd Sharma

Tamanna Das

Sayantika Chandra

Odyssey Roy

>>> with open('frans.txt', 'r') as f:
	for item in f:
		if item and item[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			print(item.strip())

			
Raunak Mitra
Debashish Sarkar
Jisan Mondal
Soumik Ghosh
Yash Kalbere
Sayantan Bagchi
Tanujit Mitra
Abhijit Kalita
Shantanu Singh
Sloke Tamang
Saumyadeep Chakraborty
Gaurab Banerjee
Projjwal Dhar
Enza Haque
Abhijit Kalita
Monojyoti Bhattacharjee
Shouvik Kar
Sourav Moitra
Rahul Dhar II
Anandd Sharma
Tamanna Das
Sayantika Chandra
Odyssey Roy
>>> with open('frans.txt', 'r') as f:
	for item in f:
		if item and item[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			frans.append(item.strip())

			
>>> frans
['Raunak Mitra', 'Debashish Sarkar', 'Jisan Mondal', 'Soumik Ghosh', 'Yash Kalbere', 'Sayantan Bagchi', 'Tanujit Mitra', 'Abhijit Kalita', 'Shantanu Singh', 'Sloke Tamang', 'Saumyadeep Chakraborty', 'Gaurab Banerjee', 'Projjwal Dhar', 'Enza Haque', 'Abhijit Kalita', 'Monojyoti Bhattacharjee', 'Shouvik Kar', 'Sourav Moitra', 'Rahul Dhar II', 'Anandd Sharma', 'Tamanna Das', 'Sayantika Chandra', 'Odyssey Roy']
>>> driver.find_element(By.XPATH, "//div[@role='textbox']")
<selenium.webdriver.remote.webelement.WebElement (session="07f3ff7e88b5fbb0874c94248c8fe29b", element="357235b8-0b1d-4f3f-be6f-89227ec69e4c")>
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 479, in send_keys
    'value': keys_to_typing(value)})
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: chrome=81.0.4044.138)

>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 479, in send_keys
    'value': keys_to_typing(value)})
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: chrome=81.0.4044.138)

>>> 	driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
	
SyntaxError: unexpected indent
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 479, in send_keys
    'value': keys_to_typing(value)})
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: chrome=81.0.4044.138)

>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 479, in send_keys
    'value': keys_to_typing(value)})
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\Rajdeep\AppData\Local\Programs\Python\Python37\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: chrome=81.0.4044.138)

>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys("hello")
>>> fran = frans[0]
>>> fran
'Raunak Mitra'
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(fran)
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(fran)
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(fran)
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(Keys.RETURN)
>>> for fran in frans:
	driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(fran)
>>> driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(Keys.RETURN)
SyntaxError: invalid syntax
>>> for fran in frans:
	driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(fran)
	driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(Keys.RETURN)

	
>>> 