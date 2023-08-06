import socket
import enum
import base64
import json as JSON
class HttpCodes:
    class ByNumber:
     Code100=bytes("HTTP/1.1 100 Continue",'utf-8')
     '''Status 100: Continue
     An interim response. Indicates to the client that the initial part of the request has been received and has not yet been rejected by the server. The client SHOULD continue by sending the remainder of the request or, if the request has already been completed, ignore this response. The server MUST send a final response after the request has been completed.'''
     Code101=bytes("HTTP/1.1 101 Switching Protocol",'utf-8')
     '''Status 101: Switching Protocol
     Sent in response to an Upgrade request header from the client, and indicates the protocol the server is switching to.'''
     Code102=bytes("HTTP/1.1 Processing",'utf-8')
     '''Status 102: Processing
     Indicates that the server has received and is processing the request, but no response is available yet.'''
     Code103=bytes("HTTP/1.1 103 Early Hints",'utf-8')
     '''Status 103: Early Hints
     Primarily intended to be used with the Link header. It suggests the user agent start preloading the resources while the server prepares a final response.'''
     Code200=bytes("HTTP/1.1 200 OK",'utf-8')
     '''Status 200: OK
     Indicates that the request has succeeded.'''
     Code201=bytes("HTTP/1.1 201 Created",'utf-8')
     '''Status 201: Created
     Indicates that the request has succeeded and a new resource has been created as a result.'''
     Code202=bytes("HTTP/1.1 202 Accepted",'utf-8')
     '''Status 202: Accepted
     Indicates that the request has been received but not completed yet. It is typically used in log running requests and batch processing.'''
     Code203=bytes("HTTP/1.1 203 Non-Authoritative Information",'utf-8')
     '''Status 203: Non-Authoritative Information
     Indicates that the returned metainformation in the entity-header is not the definitive set as available from the origin server, but is gathered from a local or a third-party copy. The set presented MAY be a subset or superset of the original version.'''
     Code204=bytes("HTTP/1.1 204 No Content",'utf-8')
     '''Status 204: No Content
     The server has fulfilled the request but does not need to return a response body. The server may return the updated meta information.'''
     Code205=bytes("HTTP/1.1 205 Reset Content",'utf-8')
     '''Status 205: Reset Content
     Indicates the client to reset the document which sent this request.'''
     Code206=bytes("HTTP/1.1 206 Partial Content",'utf-8')
     '''Status 206: Partial content
     It is used when the Range header is sent from the client to request only part of a resource.'''
     Code207=bytes("HTTP/1.1 207 Multi-Status",'utf-8')
     '''Status 207: Multi-Status
     An indicator to a client that multiple operations happened, and that the status for each operation can be found in the body of the response.'''
     Code208=bytes("HTTP/1.1 208 Already Reported",'utf-8')
     '''Status 208: Already Reported
     Allows a client to tell the server that the same resource (with the same binding) was mentioned earlier. It never appears as a true HTTP response code in the status line, and only appears in bodies.'''
     Code226=bytes("HTTP/1.1 226 IM Used",'utf-8')
     '''Status 226: IM Used
     The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.'''
     Code300=bytes("HTTP/1.1 300 Multiple Choices",'utf-8')
     '''Status 300: Multplie Choices
     The request has more than one possible response. The user-agent or user should choose one of them.'''
     Code301=bytes("HTTP/1.1 301 Moved Permanently",'utf-8')
     '''Status 301: Moved Permanently
     The URL of the requested resource has been changed permanently. The new URL is given by the Location header field in the response. This response is cacheable unless indicated otherwise.'''
     Code302=bytes("HTTP/1.1 302 Found",'utf-8')
     '''Status 302: Found
     The URL of the requested resource has been changed temporarily. The new URL is given by the Location field in the response. This response is only cacheable if indicated by a Cache-Control or Expires header field.'''
     Code303=bytes("HTTP/1.1 303 See Other",'utf-8')
     '''Status 303: See Other
     The response can be found under a different URI and SHOULD be retrieved using a GET method on that resource.'''
     Code304=bytes("HTTP/1.1 304 Not Modified",'utf-8')
     '''Status 304: Not Modified
     Indicates the client that the response has not been modified, so the client can continue to use the same cached version of the response.'''
     Code305=bytes("HTTP/1.1 305 Use Proxy",'utf-8')
     '''Status 305: Use Proxy
     Indicates that a requested response must be accessed by a proxy.'''
     Code306=bytes("HTTP/1.1 306",'utf-8')
     '''Status 306 (Unused)
     It is a reserved status code and is not used anymore.'''
     Code307=bytes("HTTP/1.1 307 Temporary Redirect",'utf-8')
     '''Status 307: Temporary Redirect
     Indicates the client to get the requested resource at another URI with same method that was used in the prior request. It is similar to 302 Found with one exception that the same HTTP method will be used that was used in the prior request.'''
     Code308=bytes("HTTP/1.1 308 Permanent Redirect",'utf-8')
     '''Status 308: Permanent Redirect
     Indicates that the resource is now permanently located at another URI, specified by the Location header. It is similar to 301 Moved Permanently with one exception that the same HTTP method will be used that was used in the prior request.'''
     Code400=bytes("HTTP/1.1 400 Bad Request",'utf-8')
     '''Status 400: Bad Request
     The request could not be understood by the server due to incorrect syntax. The client SHOULD NOT repeat the request without modifications.'''
     Code401=bytes("HTTP/1.1 401 Unauthorized",'utf-8')
     '''Status 401: Unauthorized
     Indicates that the request requires user authentication information. The client MAY repeat the request with a suitable Authorization header field'''
     Code402=bytes("HTTP/1.1 402 Payment Required",'utf-8')
     '''Status 402: Payment Required
     Reserved for future use. It is aimed for using in the digital payment systems.'''
     Code403=bytes("HTTP/1.1 403 Forbidden",'utf-8')
     '''Status 403: Forbidden
     Unauthorized request. The client does not have access rights to the content. Unlike 401, the client's identity is known to the server.'''
     Code404=bytes("HTTP/1.1 404 Not Found",'utf-8')
     '''Status 404: Not Found
     The server can not find the requested resource.'''
     Code405=bytes("HTTP/1.1 405 Method Not Allowed",'utf-8')
     '''Status 405: Method Not Allowed
     The request HTTP method is known by the server but has been disabled and cannot be used for that resource.'''
     Code406=bytes("HTTP/1.1 406 Not Acceptable",'utf-8')
     '''Status 406: Not Acceptable
     The server doesn't find any content that conforms to the criteria given by the user agent in the Accept header sent in the request.'''
     Code407=bytes("HTTP/1.1 407 Proxy Authentication Required",'utf-8')
     '''Status 407: Proxy Authentication Required
     Indicates that the client must first authenticate itself with the proxy.'''
     Code408=bytes("HTTP/1.1 408 Request Timeout",'utf-8')
     '''Status 408: Request Timeout 
     Indicates that the server did not receive a complete request from the client within the server's allotted timeout period.'''
     Code409=bytes("HTTP/1.1 409 Conflict",'utf-8')
     '''Status 409: Conflict
     The request could not be completed due to a conflict with the current state of the resource.'''
     Code410=bytes("HTTP/1.1 410 Gone",'utf-8')
     '''Status 410: Gone
     The requested resource is no longer available at the server.'''
     Code411=bytes("HTTP/1.1 411 Length Required",'utf-8')
     '''Status 411: Length Required
     The server refuses to accept the request without a defined Content- Length. The client MAY repeat the request if it adds a valid Content-Length header field.'''
     Code412=bytes("HTTP/1.1 412 Precondition Failed",'utf-8')
     '''Status 412: Precondition Failed
     The client has indicated preconditions in its headers which the server does not meet.'''
     Code413=bytes("HTTP/1.1 413 Request Entity Too Large",'utf-8')
     '''Status 413: Request Entity Too Large
     Request entity is larger than limits defined by server.'''
     Code414=bytes("HTTP/1.1 414 Request-URI Too Long",'utf-8')
     '''Status 414: Request-URI Too Long
     The URI requested by the client is longer than the server can interpret.'''
     Code415=bytes("HTTP/1.1 415 Unsupported Media Type",'utf-8')
     '''Status 415: Unsupported Media Type
     The media-type in Content-type of the request is not supported by the server.'''
     Code416=bytes("HTTP/1.1 416 Requested Range Not Satisfiable",'utf-8')
     '''Status 416: Requested Range Not Satisfiable
     The range specified by the Range header field in the request can't be fulfilled.'''
     Code417=bytes("HTTP/1.1 417 Expectation Failed",'utf-8')
     '''Status 417: Expectation Failed
     The expectation indicated by the Expect request header field can't be met by the server.'''
     Code418=bytes("HTTP/1.1 418 I'm a teapot",'utf-8')
     '''Status 418: I'm a teapot
     It was defined as April's lool joke and is not expected to be implemented by actual HTTP servers. (RFC 2324)'''
     Code420=bytes("HTTP/1.1 420 Enhance Your Calm",'utf-8')
     '''Status 420: Enhance Your Calm
     Returned by the Twitter Search and Trends API when the client is being rate limited.'''
     Code422=bytes("HTTP/1.1 422 Unprocessable Entity",'utf-8')
     '''Status 422: Unprocessable Entity
     The server understands the content type and syntax of the request entity, but still server is unable to process the request for some reason.'''
     Code423=bytes("HTTP/1.1 423 Locked",'utf-8')
     '''Status 423: Locked
     The resource that is being accessed is locked.'''
     Code424=bytes("HTTP/1.1 424 Failed Dependency",'utf-8')
     '''Status 424: Failed Dependency
     The request failed due to failure of a previous request.'''
     Code425=bytes("HTTP/1.1 425 Too Early",'utf-8')
     '''Status 425: Too Early
     Indicates that the server is unwilling to risk processing a request that might be replayed.'''
     Code426=bytes("HTTP/1.1 426 Upgrade Required",'utf-8')
     '''Status 426: Upgrade Required
     The server refuses to perform the request. The server will process the request after the client upgrades to a different protocol.'''
     Code428=bytes("HTTP/1.1 428 Precondition Required",'utf-8')
     '''Status 428: Precondition Required
     The origin server requires the request to be conditional.'''
     Code429=bytes("HTTP/1.1 429 Too Many Requests",'utf-8')
     '''Status 429: Too Many Requests
     The user has sent too many requests in a given amount of time ("rate limiting").'''
     Code431=bytes("HTTP/1.1 431 Request Header Fields Too Large",'utf-8')
     '''Status 431: Request Header Fields Too Large
     The server is unwilling to process the request because its header fields are too large.'''
     Code444=bytes("HTTP/1.1 444 No Response",'utf-8')
     '''Status 444: No Response
     The Nginx server returns no information to the client and closes the connection.'''
     Code449=bytes("HTTP/1.1 449 Retry With",'utf-8')
     '''Status 449: Retry With
     The request should be retried after performing the appropriate action.'''
     Code450=bytes("HTTP/1.1 450 Blocked By Windows Parental Controls",'utf-8')
     '''Status 450: Blocked By Windows Parental Controls
     Windows Parental Controls are turned on and are blocking access to the given webpage.'''
     Code451=bytes("HTTP/1.1 451 Unavailable For Legal Reasons",'utf-8')
     '''Status 451: Unavailable For Legal Reasons
     The user-agent requested a resource that cannot legally be provided.'''
     Code499=bytes("HTTP/1.1 499 Client Closed Request",'utf-8')
     '''Status 449: Client Closed Request
     The connection is closed by the client while HTTP server is processing its request, making the server unable to send the HTTP header back.'''
     Code500=bytes("HTTP/1.1 500 Internal Server Error",'utf-8')
     '''Status 500: Internal Server Error
     The server encountered an unexpected condition that prevented it from fulfilling the request.'''
     Code501=bytes("HTTP/1.1 501 Not Implemented",'utf-8')
     '''Status 501: Not Implemented
     The HTTP method is not supported by the server and cannot be handled.'''
     Code502=bytes("HTTP/1.1 502 Bad Gateway",'utf-8')
     '''Status 502: Bad Gateway
     The server got an invalid response while working as a gateway to get the response needed to handle the request.'''
     Code503=bytes("HTTP/1.1 503 Service Unavailible",'utf-8')
     '''Status 503: Service Unavailible
     The server is not ready to handle the request.'''
     Code504=bytes("HTTP/1.1 504 Gateway Timeout",'utf-8')
     '''Status 504: Gateway Timeout
     The server is acting as a gateway and cannot get a response in time for a request.'''
     Code505=bytes("HTTP/1.1 505 HTTP Version Not Supported",'utf-8')
     '''Status 505: HTTP Version Not Supported
     The HTTP version used in the request is not supported by the server.'''
     Code506=bytes("HTTP/1.1 506 Variant Also Negotiates",'utf-8')
     '''Status 506: Variant Also Negotiates
     Indicates that the server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper endpoint in the negotiation process.'''
     Code507=bytes("HTTP/1.1 507 Insufficient Storage",'utf-8')
     '''Status 507: Insufficient Storage
     The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.'''
     Code508=bytes("HTTP/1.1 508 Loop Detected",'utf-8')
     '''Status 508: Loop Detected
     The server detected an infinite loop while processing the request.'''
     Code510=bytes("HTTP/1.1 510 Not Extended",'utf-8')
     '''Status 510: Not Extended
     Further extensions to the request are required for the server to fulfill it.'''
     Code511=bytes("HTTP/1.1 511 Network Authentication Required",'utf-8')
     '''Status 511: Network Authentication Required
     Indicates that the client needs to authenticate to gain network access.'''

    #Define by name
    class ByName:
     Continue=bytes("HTTP/1.1 100 Continue",'utf-8')
     '''Status 100: Continue
     An interim response. Indicates to the client that the initial part of the request has been received and has not yet been rejected by the server. The client SHOULD continue by sending the remainder of the request or, if the request has already been completed, ignore this response. The server MUST send a final response after the request has been completed.'''
     Switching_Protocol=bytes("HTTP/1.1 101 Switching Protocol",'utf-8')
     '''Status 101: Switching Protocol
     Sent in response to an Upgrade request header from the client, and indicates the protocol the server is switching to.'''
     Processing=bytes("HTTP/1.1 Processing",'utf-8')
     '''Status 102: Processing
     Indicates that the server has received and is processing the request, but no response is available yet.'''
     Early_Hints=bytes("HTTP/1.1 103 Early Hints",'utf-8')
     '''Status 103: Early Hints
     Primarily intended to be used with the Link header. It suggests the user agent start preloading the resources while the server prepares a final response.'''
     Ok=bytes("HTTP/1.1 200 OK",'utf-8')
     '''Status 200: OK
     Indicates that the request has succeeded.'''
     Created=bytes("HTTP/1.1 201 Created",'utf-8')
     '''Status 201: Created
     Indicates that the request has succeeded and a new resource has been created as a result.'''
     Accepted=bytes("HTTP/1.1 202 Accepted",'utf-8')
     '''Status 202: Accepted
     Indicates that the request has been received but not completed yet. It is typically used in log running requests and batch processing.'''
     NonAuthoritative_Information=bytes("HTTP/1.1 203 Non-Authoritative Information",'utf-8')
     '''Status 203: Non-Authoritative Information
     Indicates that the returned metainformation in the entity-header is not the definitive set as available from the origin server, but is gathered from a local or a third-party copy. The set presented MAY be a subset or superset of the original version.'''
     No_Content=bytes("HTTP/1.1 204 No Content",'utf-8')
     '''Status 204: No Content
     The server has fulfilled the request but does not need to return a response body. The server may return the updated meta information.'''
     Reset_Content=bytes("HTTP/1.1 205 Reset Content",'utf-8')
     '''Status 205: Reset Content
     Indicates the client to reset the document which sent this request.'''
     Partial_Content=bytes("HTTP/1.1 206 Partial Content",'utf-8')
     '''Status 206: Partial content
     It is used when the Range header is sent from the client to request only part of a resource.'''
     MultiStatus=bytes("HTTP/1.1 207 Multi-Status",'utf-8')
     '''Status 207: Multi-Status
     An indicator to a client that multiple operations happened, and that the status for each operation can be found in the body of the response.'''
     Already_Reported=bytes("HTTP/1.1 208 Already Reported",'utf-8')
     '''Status 208: Already Reported
     Allows a client to tell the server that the same resource (with the same binding) was mentioned earlier. It never appears as a true HTTP response code in the status line, and only appears in bodies.'''
     IM_Used=bytes("HTTP/1.1 226 IM Used",'utf-8')
     '''Status 226: IM Used
     The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.'''
     Multiple_Choices=bytes("HTTP/1.1 300 Multiple Choices",'utf-8')
     '''Status 300: Multplie Choices
     The request has more than one possible response. The user-agent or user should choose one of them.'''
     Moved_Permanently=bytes("HTTP/1.1 301 Moved Permanently",'utf-8')
     '''Status 301: Moved Permanently
     The URL of the requested resource has been changed permanently. The new URL is given by the Location header field in the response. This response is cacheable unless indicated otherwise.'''
     Found=bytes("HTTP/1.1 302 Found",'utf-8')
     '''Status 302: Found
     The URL of the requested resource has been changed temporarily. The new URL is given by the Location field in the response. This response is only cacheable if indicated by a Cache-Control or Expires header field.'''
     See_Other=bytes("HTTP/1.1 303 See Other",'utf-8')
     '''Status 303: See Other
     The response can be found under a different URI and SHOULD be retrieved using a GET method on that resource.'''
     Not_Modified=bytes("HTTP/1.1 304 Not Modified",'utf-8')
     '''Status 304: Not Modified
     Indicates the client that the response has not been modified, so the client can continue to use the same cached version of the response.'''
     Use_Proxy=bytes("HTTP/1.1 305 Use Proxy",'utf-8')
     '''Status 305: Use Proxy
     Indicates that a requested response must be accessed by a proxy.'''
     Unused=bytes("HTTP/1.1 306",'utf-8')
     '''Status 306 (Unused)
     It is a reserved status code and is not used anymore.'''
     Temporary_Redirect=bytes("HTTP/1.1 307 Temporary Redirect",'utf-8')
     '''Status 307: Temporary Redirect
     Indicates the client to get the requested resource at another URI with same method that was used in the prior request. It is similar to 302 Found with one exception that the same HTTP method will be used that was used in the prior request.'''
     Permanent_Redirect=bytes("HTTP/1.1 308 Permanent Redirect",'utf-8')
     '''Status 308: Permanent Redirect
     Indicates that the resource is now permanently located at another URI, specified by the Location header. It is similar to 301 Moved Permanently with one exception that the same HTTP method will be used that was used in the prior request.'''
     Bad_Request=bytes("HTTP/1.1 400 Bad Request",'utf-8')
     '''Status 400: Bad Request
     The request could not be understood by the server due to incorrect syntax. The client SHOULD NOT repeat the request without modifications.'''
     Unauthorized=bytes("HTTP/1.1 401 Unauthorized",'utf-8')
     '''Status 401: Unauthorized
     Indicates that the request requires user authentication information. The client MAY repeat the request with a suitable Authorization header field'''
     Payment_Required=bytes("HTTP/1.1 402 Payment Required",'utf-8')
     '''Status 402: Payment Required
     Reserved for future use. It is aimed for using in the digital payment systems.'''
     Forbidden=bytes("HTTP/1.1 403 Forbidden",'utf-8')
     '''Status 403: Forbidden
     Unauthorized request. The client does not have access rights to the content. Unlike 401, the client's identity is known to the server.'''
     Not_Found=bytes("HTTP/1.1 404 Not Found",'utf-8')
     '''Status 404: Not Found
     The server can not find the requested resource.'''
     Method_Not_Allowed=bytes("HTTP/1.1 405 Method Not Allowed",'utf-8')
     '''Status 405: Method Not Allowed
     The request HTTP method is known by the server but has been disabled and cannot be used for that resource.'''
     Not_Acceptable=bytes("HTTP/1.1 406 Not Acceptable",'utf-8')
     '''Status 406: Not Acceptable
     The server doesn't find any content that conforms to the criteria given by the user agent in the Accept header sent in the request.'''
     Proxy_Authentication_Required=bytes("HTTP/1.1 407 Proxy Authentication Required",'utf-8')
     '''Status 407: Proxy Authentication Required
     Indicates that the client must first authenticate itself with the proxy.'''
     Request_Timeout=bytes("HTTP/1.1 408 Request Timeout",'utf-8')
     '''Status 408: Request Timeout 
     Indicates that the server did not receive a complete request from the client within the server's allotted timeout period.'''
     Conflict=bytes("HTTP/1.1 409 Conflict",'utf-8')
     '''Status 409: Conflict
     The request could not be completed due to a conflict with the current state of the resource.'''
     Gone=bytes("HTTP/1.1 410 Gone",'utf-8')
     '''Status 410: Gone
     The requested resource is no longer available at the server.'''
     Length_Required=bytes("HTTP/1.1 411 Length Required",'utf-8')
     '''Status 411: Length Required
     The server refuses to accept the request without a defined Content- Length. The client MAY repeat the request if it adds a valid Content-Length header field.'''
     Precondition_Failed=bytes("HTTP/1.1 412 Precondition Failed",'utf-8')
     '''Status 412: Precondition Failed
     The client has indicated preconditions in its headers which the server does not meet.'''
     Request_Entity_Too_Large=bytes("HTTP/1.1 413 Request Entity Too Large",'utf-8')
     '''Status 413: Request Entity Too Large
     Request entity is larger than limits defined by server.'''
     RequestURI_Too_Long=bytes("HTTP/1.1 414 Request-URI Too Long",'utf-8')
     '''Status 414: Request-URI Too Long
     The URI requested by the client is longer than the server can interpret.'''
     Unsupported_Media_Type=bytes("HTTP/1.1 415 Unsupported Media Type",'utf-8')
     '''Status 415: Unsupported Media Type
     The media-type in Content-type of the request is not supported by the server.'''
     Requested_Range_Not_Satisfiable=bytes("HTTP/1.1 416 Requested Range Not Satisfiable",'utf-8')
     '''Status 416: Requested Range Not Satisfiable
     The range specified by the Range header field in the request can't be fulfilled.'''
     Expectation_Failed=bytes("HTTP/1.1 417 Expectation Failed",'utf-8')
     '''Status 417: Expectation Failed
     The expectation indicated by the Expect request header field can't be met by the server.'''
     Im_a_teapot=bytes("HTTP/1.1 418 I'm a teapot",'utf-8')
     '''Status 418: I'm a teapot
     It was defined as April's lool joke and is not expected to be implemented by actual HTTP servers. (RFC 2324)'''
     Enhance_Your_Calm=bytes("HTTP/1.1 420 Enhance Your Calm",'utf-8')
     '''Status 420: Enhance Your Calm
     Returned by the Twitter Search and Trends API when the client is being rate limited.'''
     Unprocessable_Entity=bytes("HTTP/1.1 422 Unprocessable Entity",'utf-8')
     '''Status 422: Unprocessable Entity
     The server understands the content type and syntax of the request entity, but still server is unable to process the request for some reason.'''
     Locked=bytes("HTTP/1.1 423 Locked",'utf-8')
     '''Status 423: Locked
     The resource that is being accessed is locked.'''
     Failed_Dependency=bytes("HTTP/1.1 424 Failed Dependency",'utf-8')
     '''Status 424: Failed Dependency
     The request failed due to failure of a previous request.'''
     Too_Early=bytes("HTTP/1.1 425 Too Early",'utf-8')
     '''Status 425: Too Early
     Indicates that the server is unwilling to risk processing a request that might be replayed.'''
     Upgrade_Required=bytes("HTTP/1.1 426 Upgrade Required",'utf-8')
     '''Status 426: Upgrade Required
     The server refuses to perform the request. The server will process the request after the client upgrades to a different protocol.'''
     Precondition_Required=bytes("HTTP/1.1 428 Precondition Required",'utf-8')
     '''Status 428: Precondition Required
     The origin server requires the request to be conditional.'''
     Too_Many_Requests=bytes("HTTP/1.1 429 Too Many Requests",'utf-8')
     '''Status 429: Too Many Requests
     The user has sent too many requests in a given amount of time ("rate limiting").'''
     Request_Header_Fields_Too_Large=bytes("HTTP/1.1 431 Request Header Fields Too Large",'utf-8')
     '''Status 431: Request Header Fields Too Large
     The server is unwilling to process the request because its header fields are too large.'''
     No_Response=bytes("HTTP/1.1 444 No Response",'utf-8')
     '''Status 444: No Response
     The Nginx server returns no information to the client and closes the connection.'''
     Retry_With=bytes("HTTP/1.1 449 Retry With",'utf-8')
     '''Status 449: Retry With
     The request should be retried after performing the appropriate action.'''
     Blocked_By_Windows_Parental_Controls=bytes("HTTP/1.1 450 Blocked By Windows Parental Controls",'utf-8')
     '''Status 450: Blocked By Windows Parental Controls
     Windows Parental Controls are turned on and are blocking access to the given webpage.'''
     Unavailable_For_Legal_Reasons=bytes("HTTP/1.1 451 Unavailable For Legal Reasons",'utf-8')
     '''Status 451: Unavailable For Legal Reasons
     The user-agent requested a resource that cannot legally be provided.'''
     Client_Closed_Request=bytes("HTTP/1.1 499 Client Closed Request",'utf-8')
     '''Status 449: Client Closed Request
     The connection is closed by the client while HTTP server is processing its request, making the server unable to send the HTTP header back.'''
     Internal_Server_Error=bytes("HTTP/1.1 500 Internal Server Error",'utf-8')
     '''Status 500: Internal Server Error
     The server encountered an unexpected condition that prevented it from fulfilling the request.'''
     Not_Implemented=bytes("HTTP/1.1 501 Not Implemented",'utf-8')
     '''Status 501: Not Implemented
     The HTTP method is not supported by the server and cannot be handled.'''
     Bad_Gateway=bytes("HTTP/1.1 502 Bad Gateway",'utf-8')
     '''Status 502: Bad Gateway
     The server got an invalid response while working as a gateway to get the response needed to handle the request.'''
     Service_Unavailible=bytes("HTTP/1.1 503 Service Unavailible",'utf-8')
     '''Status 503: Service Unavailible
     The server is not ready to handle the request.'''
     Gateway_Timeout=bytes("HTTP/1.1 504 Gateway Timeout",'utf-8')
     '''Status 504: Gateway Timeout
     The server is acting as a gateway and cannot get a response in time for a request.'''
     HTTP_Version_Not_Supported=bytes("HTTP/1.1 505 HTTP Version Not Supported",'utf-8')
     '''Status 505: HTTP Version Not Supported
     The HTTP version used in the request is not supported by the server.'''
     Variant_Also_Negotiates=bytes("HTTP/1.1 506 Variant Also Negotiates",'utf-8')
     '''Status 506: Variant Also Negotiates
     Indicates that the server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper endpoint in the negotiation process.'''
     Insufficient_Storage=bytes("HTTP/1.1 507 Insufficient Storage",'utf-8')
     '''Status 507: Insufficient Storage
     The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.'''
     Loop_Detected=bytes("HTTP/1.1 508 Loop Detected",'utf-8')
     '''Status 508: Loop Detected
     The server detected an infinite loop while processing the request.'''
     Not_Extended=bytes("HTTP/1.1 510 Not Extended",'utf-8')
     '''Status 510: Not Extended
     Further extensions to the request are required for the server to fulfill it.'''
     Network_Authentication_Required=bytes("HTTP/1.1 511 Network Authentication Required",'utf-8')
     '''Status 511: Network Authentication Required
     Indicates that the client needs to authenticate to gain network access.'''
#create response is dict -> headers / response
#cli request to dict is headers / request -> dict
def CreateResponse(status_code : str,headers : dict or None=None,data : bytes or str=None):
    if headers == None:
        headers={}
    res=str(status_code)[2:][:-1] + "\n"
    stringified_headers=""
    for i in headers.keys():
        stringified_headers+=i+": " + headers[i] + "\n"
    res+=stringified_headers
    if not data==None:
        res+="\n\n"
        if type(data)==str:
            res=bytes(res + data,"utf-8")
        elif type(data)==bytes:
            res=bytes(res,"utf-8") + data
    else:
        res=bytes(res,"utf-8")
    return res
def CliRequestToDict (rawtext):
    out = {}
    scmd = rawtext.replace("\\r","").split("\\n")
    out["type"] = scmd[0].split(" ")[0]
    out["path"] = scmd[0].split(" ")[1]
    out["HTTP_version"] = scmd[0].split(" ")[2].split("/")[1]
    header = {}
    scmd.pop(0)
    if out["type"] == "POST":
        out["JSON"] = scmd[len(scmd)-1]
        scmd = scmd.pop(len(scmd)-1)
    for i in scmd:
        if len(i) > 0:   
            after = len(i.split(":")[0]) + 2
            #print(after)
            header[i.split(":")[0]] = i[after:]
    out["headers"] = header
    return out
global imageformats
imageformats="jpg,jpeg,jpe,jif,jfif,jfi,png,gif,webp,tiff,tif,psd,raw,arw,cr2,nrw,k25,bmp,dib,heif,heic,ind,indd,indt,jp2,j2k,jpf,jpx,jpm,mj2,svg,svgz,ai,eps,pdf".split(",")
global videoformats
videoformats="webm,mkv,flv,vob,ogv,ogg,drc,gifv,mng,avi,MTS,M2TS,TS,mov,qt,wmv,yuv,rm,rmvb,viv,asf,amv,mp4,m4p,m4v,mpg,mpg2,mpeg,mpe,mpv,m2v,m4v,svi,3gp,3g2,mxf,roq,nsv,f4v,f4p,f4a,f4b".split(",")
class App:
 
  global s
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  global paths 
  paths = {}
  global users
  users = []
  global lhost
  lhost = socket.gethostbyname(socket.gethostname())
  global lport
  lport = 80
  def File(path : str):
      return {"path": path, "__IsFile__BuiltinData__": True}
  def Route(original_func, path : str, methods : list=["GET"], secure : bool=False, security_level : int=1): # : object, 
    def wrapper_func(*args, **kwargs):
        return original_func(*args, **kwargs)
    #paths[path]={"function": func, "secure": secure}
    #print(type(original_func))
    paths[path]={"function": original_func, "secure": secure, "security_level": security_level ,"methods": methods}
    return wrapper_func
  '''Hook a function to a website path ("/", "/api", etc)
  path: the path, ex "/" or "/api/getData"
  methods: by default GET only, example value ["GET","POST","DELETE"]
  secure: whether the page requires authentication or not, False by default
  security_level: only users with an access level above the security_level will be able to see the page, 1 by default'''
  def SetUsers(users_to_set : list):
      users=users_to_set
  def SetUser(name : str, password : str, access_level : int=1):
      alreadyExists=False
      for i in self.users:
          if i["name"]==name:
              alreadyExists=True
              i["password"]=password
              i["access_level"]=access_level
      if not alreadyExists:
          users.append({"name": name, "password": password, "access_level": access_level})
  def BindToAddress(host : str=socket.gethostbyname(socket.gethostname()),port : int=80):
      lhost=host
      lport=port
      s.bind((host,port))
  def AddHostFiles():
      print("Not Implemented")
  def OpenServer():
      if lport == 80:
        print(f"Running on: http://{lhost}/")
      else:
        print(f"Running on: http://{lhost}:{lport}/")
      while True:
          try:
            running=True
            s.listen()
            conn, addr = s.accept()
            s.settimeout(2)
            req = CliRequestToDict(str(conn.recv(1024))[2:][:-1])
            print(req)
            if req["path"] in paths.keys():
                if req["type"] in paths[req["path"]]["methods"]:
                    AuthSuccess=True
                    closed=False
                    if paths[req["path"]]["secure"]:
                        if "Authorization" in req["headers"].keys():
                            req["headers"]["Authorization"] = req["headers"]["Authorization"].split(" ")[1]
                            usern,passw=str(base64.b64decode(req["headers"]["Authorization"]))[2:][:-1].split(":")
                            AuthSuccess=False
                            for i in users:
                                if i["name"] == usern and i["password"] == passw and i["access_level"] >= paths[req["path"]]["security_level"]:
                                    AuthSuccess=True
                            #usern=authsp[0]
                            #passw=authsp[1]
                            #print(usern)
                            #print(passw)
                        else:
                            conn.sendall(CreateResponse(HttpCodes.ByName.Unauthorized,{"WWW-Authenticate": "Basic"}))
                            closed=True
                    if AuthSuccess and not closed:
                        ft=paths[req["path"]]["function"](req)
                        ctype="text/html"
                        if type(ft) == dict:
                            if "__IsFile__BuiltinData__" in ft.keys():
                             if ft["path"].split(".")[len(ft["path"].split("."))-1] in imageformats:
                                ctype = "image/"+ft["path"].split(".")[len(ft["path"].split("."))-1]
                             elif ft["path"].split(".")[len(ft["path"].split("."))-1] in videoformats:
                                ctype = "video/"+ft["path"].split(".")[len(ft["path"].split("."))-1]
                             with open(ft["path"],"rb") as f:
                                ft=f.read()
                            else:
                             ft=JSON.dumps(ft)

                        conn.sendall(CreateResponse(HttpCodes.ByName.Ok,headers={"Content-Type": ctype},data=ft))
                    else:
                        if not closed:
                            conn.sendall(HttpCodes.ByName.Forbidden)
                else:
                    conn.sendall(HttpCodes.ByName.Method_Not_Allowed)
            else:
                conn.sendall(HttpCodes.ByName.Not_Found)
            conn.close()
            s.settimeout(None)
            s.bind((lhost,lport))
          except Exception as e:
              error=True
              print(e)
  
