#
# Copyright 2016 Python Software Foundation
#
# Licensed under the Python Software Foundation License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  https://docs.python.org/3/license.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from enum import IntEnum


class HTTPStatus(IntEnum):
    """HTTP status codes and reason phrases

    Status codes from the following RFCs are all observed:

        * RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
        * RFC 6585: Additional HTTP Status Codes
        * RFC 3229: Delta encoding in HTTP
        * RFC 4918: HTTP Extensions for WebDAV, obsoletes 2518
        * RFC 5842: Binding Extensions to WebDAV
        * RFC 7238: Permanent Redirect
        * RFC 2295: Transparent Content Negotiation in HTTP
        * RFC 2774: An HTTP Extension Framework
    """
    def __new__(cls, value, phrase, description=''):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        obj.description = description
        return obj

    # informational
    CONTINUE = (100, 'Continue', 'Request received, please continue')
    SWITCHING_PROTOCOLS = (101, 'Switching Protocols', 'Switching to new protocol; obey Upgrade header')
    PROCESSING = (102, 'Processing')

    # success
    OK = (200, 'OK', 'Request fulfilled, document follows')
    CREATED = (201, 'Created', 'Document created, URL follows')
    ACCEPTED = (202, 'Accepted', 'Request accepted, processing continues off-line')
    NON_AUTHORITATIVE_INFORMATION = (203, 'Non-Authoritative Information', 'Request fulfilled from cache')
    NO_CONTENT = (204, 'No Content', 'Request fulfilled, nothing follows')
    RESET_CONTENT = (205, 'Reset Content', 'Clear input form for further input')
    PARTIAL_CONTENT = (206, 'Partial Content', 'Partial content follows')
    MULTI_STATUS = (207, 'Multi-Status')
    ALREADY_REPORTED = (208, 'Already Reported')
    IM_USED = (226, 'IM Used')

    # redirection
    MULTIPLE_CHOICES = (300, 'Multiple Choices', 'Object has several resources -- see URI list')
    MOVED_PERMANENTLY = (301, 'Moved Permanently', 'Object moved permanently -- see URI list')
    FOUND = (302, 'Found', 'Object moved temporarily -- see URI list')
    SEE_OTHER = (303, 'See Other', 'Object moved -- see Method and URL list')
    NOT_MODIFIED = (304, 'Not Modified', 'Document has not changed since given time')
    USE_PROXY = (305, 'Use Proxy', 'You must use proxy specified in Location to access this resource')
    TEMPORARY_REDIRECT = (307, 'Temporary Redirect', 'Object moved temporarily -- see URI list')
    PERMANENT_REDIRECT = (308, 'Permanent Redirect', 'Object moved temporarily -- see URI list')

    # client error
    BAD_REQUEST = (400, 'Bad Request', 'Bad request syntax or unsupported method')
    UNAUTHORIZED = (401, 'Unauthorized', 'No permission -- see authorization schemes')
    PAYMENT_REQUIRED = (402, 'Payment Required', 'No payment -- see charging schemes')
    FORBIDDEN = (403, 'Forbidden', 'Request forbidden -- authorization will not help')
    NOT_FOUND = (404, 'Not Found', 'Nothing matches the given URI')
    METHOD_NOT_ALLOWED = (405, 'Method Not Allowed', 'Specified method is invalid for this resource')
    NOT_ACCEPTABLE = (406, 'Not Acceptable', 'URI not available in preferred format')
    PROXY_AUTHENTICATION_REQUIRED = (407, 'Proxy Authentication Required',
                                     'You must authenticate with this proxy before proceeding')
    REQUEST_TIMEOUT = (408, 'Request Timeout', 'Request timed out; try again later')
    CONFLICT = (409, 'Conflict', 'Request conflict')
    GONE = (410, 'Gone', 'URI no longer exists and has been permanently removed')
    LENGTH_REQUIRED = (411, 'Length Required', 'Client must specify Content-Length')
    PRECONDITION_FAILED = (412, 'Precondition Failed', 'Precondition in headers is false')
    REQUEST_ENTITY_TOO_LARGE = (413, 'Request Entity Too Large', 'Entity is too large')
    REQUEST_URI_TOO_LONG = (414, 'Request-URI Too Long', 'URI is too long')
    UNSUPPORTED_MEDIA_TYPE = (415, 'Unsupported Media Type', 'Entity body in unsupported format')
    REQUESTED_RANGE_NOT_SATISFIABLE = (416, 'Requested Range Not Satisfiable', 'Cannot satisfy request range')
    EXPECTATION_FAILED = (417, 'Expectation Failed', 'Expect condition could not be satisfied')
    UNPROCESSABLE_ENTITY = (422, 'Unprocessable Entity')
    LOCKED = (423, 'Locked')
    FAILED_DEPENDENCY = (424, 'Failed Dependency')
    UPGRADE_REQUIRED = (426, 'Upgrade Required')
    PRECONDITION_REQUIRED = (428, 'Precondition Required', 'The origin server requires the request to be conditional')
    TOO_MANY_REQUESTS = (429, 'Too Many Requests',
                         'The user has sent too many requests in a given amount of time ("rate limiting")')
    REQUEST_HEADER_FIELDS_TOO_LARGE = (431, 'Request Header Fields Too Large',
                                       'The server is unwilling to process the request because its header '
                                       'fields are too large')

    # server errors
    INTERNAL_SERVER_ERROR = (500, 'Internal Server Error', 'Server got itself in trouble')
    NOT_IMPLEMENTED = (501, 'Not Implemented', 'Server does not support this operation')
    BAD_GATEWAY = (502, 'Bad Gateway', 'Invalid responses from another server/proxy')
    SERVICE_UNAVAILABLE = (503, 'Service Unavailable', 'The server cannot process the request due to a high load')
    GATEWAY_TIMEOUT = (504, 'Gateway Timeout', 'The gateway server did not receive a timely response')
    HTTP_VERSION_NOT_SUPPORTED = (505, 'HTTP Version Not Supported', 'Cannot fulfill request')
    VARIANT_ALSO_NEGOTIATES = (506, 'Variant Also Negotiates')
    INSUFFICIENT_STORAGE = (507, 'Insufficient Storage')
    LOOP_DETECTED = (508, 'Loop Detected')
    NOT_EXTENDED = (510, 'Not Extended')
    NETWORK_AUTHENTICATION_REQUIRED = (511, 'Network Authentication Required',
                                       'The client needs to authenticate to gain network access')
