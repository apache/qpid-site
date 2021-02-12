;;
;; Licensed to the Apache Software Foundation (ASF) under one
;; or more contributor license agreements.  See the NOTICE file
;; distributed with this work for additional information
;; regarding copyright ownership.  The ASF licenses this file
;; to you under the Apache License, Version 2.0 (the
;; "License"); you may not use this file except in compliance
;; with the License.  You may obtain a copy of the License at
;; 
;;   http://www.apache.org/licenses/LICENSE-2.0
;; 
;; Unless required by applicable law or agreed to in writing,
;; software distributed under the License is distributed on an
;; "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
;; KIND, either express or implied.  See the License for the
;; specific language governing permissions and limitations
;; under the License.
;;

# Qpid Dispatch 1.15.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1654](https://issues.apache.org/jira/browse/DISPATCH-1654) - tcp protocol bridging (ingress and egress)
 - [DISPATCH-1743](https://issues.apache.org/jira/browse/DISPATCH-1743) - Add HTTP/2 support to the router
 - [DISPATCH-1744](https://issues.apache.org/jira/browse/DISPATCH-1744) - Add HTTP/1.1 support to the router
 - [DISPATCH-1767](https://issues.apache.org/jira/browse/DISPATCH-1767) - [console] add typescript to console dependencies
 - [DISPATCH-1779](https://issues.apache.org/jira/browse/DISPATCH-1779) - http stats/metrics
 - [DISPATCH-1780](https://issues.apache.org/jira/browse/DISPATCH-1780) - multicast support for http 1.1 adaptor
 - [DISPATCH-1781](https://issues.apache.org/jira/browse/DISPATCH-1781) - Scraper could inject any log module output into data web page
 - [DISPATCH-1790](https://issues.apache.org/jira/browse/DISPATCH-1790) - HTTP1.x needs raw octet counters on a per-request basis
 - [DISPATCH-1794](https://issues.apache.org/jira/browse/DISPATCH-1794) - Router annotation window padding is off by one
 - [DISPATCH-1795](https://issues.apache.org/jira/browse/DISPATCH-1795) - Avoid clutter in debug output by not printing traceback of suppressed leaks
 - [DISPATCH-1804](https://issues.apache.org/jira/browse/DISPATCH-1804) - Add AMQ Footer support to Body Data API 
 - [DISPATCH-1806](https://issues.apache.org/jira/browse/DISPATCH-1806) - TCP adaptor mishandles outgoing body_data
 - [DISPATCH-1807](https://issues.apache.org/jira/browse/DISPATCH-1807) - TCP adaptor has no system tests
 - [DISPATCH-1812](https://issues.apache.org/jira/browse/DISPATCH-1812) - Add the "C" prefix in log messages to connection identifiers in server.c 
 - [DISPATCH-1813](https://issues.apache.org/jira/browse/DISPATCH-1813) - Rename qd_http_lsnr to qd_http_listener
 - [DISPATCH-1815](https://issues.apache.org/jira/browse/DISPATCH-1815) - Send PING frames to keep the router-http2 server connection alive
 - [DISPATCH-1817](https://issues.apache.org/jira/browse/DISPATCH-1817) - TCP adaptor leaks pooled qd_message_body_data_t objects
 - [DISPATCH-1841](https://issues.apache.org/jira/browse/DISPATCH-1841) - HTTP1: close corresponding connection when connector deleted
 - [DISPATCH-1853](https://issues.apache.org/jira/browse/DISPATCH-1853) - [test] SkipIfNeeded decorator prints comment too often
 - [DISPATCH-1854](https://issues.apache.org/jira/browse/DISPATCH-1854) - Delivery id numbers could be added for better log message comprehension
 - [DISPATCH-1882](https://issues.apache.org/jira/browse/DISPATCH-1882) - Tcp adaptor self test fails when all tests skipped
 - [DISPATCH-1883](https://issues.apache.org/jira/browse/DISPATCH-1883) - [Test] Travis Xenial AMD64 should have Python 'selectors' module
 - [DISPATCH-1898](https://issues.apache.org/jira/browse/DISPATCH-1898) - support event channel option  in http1 adaptor
 - [DISPATCH-1907](https://issues.apache.org/jira/browse/DISPATCH-1907) - Make policy enforceable in internal message receivers
 - [DISPATCH-1911](https://issues.apache.org/jira/browse/DISPATCH-1911) - Allow internal message endpoints using core-subscribe to set terminal disposition of received deliveries
 - [DISPATCH-1912](https://issues.apache.org/jira/browse/DISPATCH-1912) - Fix TSAN failures in the test suite
 - [DISPATCH-1929](https://issues.apache.org/jira/browse/DISPATCH-1929) - Allow producing a release build with asserts enabled

## Bugs fixed

 - [DISPATCH-1750](https://issues.apache.org/jira/browse/DISPATCH-1750) - Update PatternFly packages for the 1.15.0 release
 - [DISPATCH-1751](https://issues.apache.org/jira/browse/DISPATCH-1751) - unexpected incoming-window in begin frame when running Dispatch on 32 bit system
 - [DISPATCH-1784](https://issues.apache.org/jira/browse/DISPATCH-1784) - HTTP1.x adaptor does not handle folded header lines
 - [DISPATCH-1788](https://issues.apache.org/jira/browse/DISPATCH-1788) - HTTP1.x adaptor fails to honor HTTP/1.0 connection semantics
 - [DISPATCH-1791](https://issues.apache.org/jira/browse/DISPATCH-1791) - HTTP1.x adaptor leaks message buffers and deliveries
 - [DISPATCH-1793](https://issues.apache.org/jira/browse/DISPATCH-1793) - Bump python-checker version support to include python3.8
 - [DISPATCH-1801](https://issues.apache.org/jira/browse/DISPATCH-1801) - Link routed outcomes do not propagate all associated state
 - [DISPATCH-1802](https://issues.apache.org/jira/browse/DISPATCH-1802) - Router crash during HTTP connection activation
 - [DISPATCH-1803](https://issues.apache.org/jira/browse/DISPATCH-1803) - HTTP1.x adaptor stall when body data section &gt; Q2 limit
 - [DISPATCH-1810](https://issues.apache.org/jira/browse/DISPATCH-1810) - HTTP1.x: qdr_delivery_t's are not processed (leaked)
 - [DISPATCH-1811](https://issues.apache.org/jira/browse/DISPATCH-1811) - HTTP2 does not work in an edge to interior network
 - [DISPATCH-1816](https://issues.apache.org/jira/browse/DISPATCH-1816) - HTTP1.x race between activation timer and raw connection events
 - [DISPATCH-1820](https://issues.apache.org/jira/browse/DISPATCH-1820) - TCP adaptor test time out with single one-byte message
 - [DISPATCH-1823](https://issues.apache.org/jira/browse/DISPATCH-1823) - TCP adaptor does not honor discard flag in core callbacks
 - [DISPATCH-1824](https://issues.apache.org/jira/browse/DISPATCH-1824) - TCP adaptor leaks tcp connectors and listeners at shutdown
 - [DISPATCH-1825](https://issues.apache.org/jira/browse/DISPATCH-1825) - TCP adaptor tests use selectors module not available in python 2.7
 - [DISPATCH-1826](https://issues.apache.org/jira/browse/DISPATCH-1826) - Various instabilities in the tcp protocol adaptor
 - [DISPATCH-1829](https://issues.apache.org/jira/browse/DISPATCH-1829) - multi-hop TCP does not seem to work
 - [DISPATCH-1830](https://issues.apache.org/jira/browse/DISPATCH-1830) - TCP adaptor test can not create concurrent client sessions
 - [DISPATCH-1831](https://issues.apache.org/jira/browse/DISPATCH-1831) - TCP adaptor test topology needs a longer backbone of interior routers
 - [DISPATCH-1833](https://issues.apache.org/jira/browse/DISPATCH-1833) - stream_data buffer fanout count wrap buffer leak
 - [DISPATCH-1840](https://issues.apache.org/jira/browse/DISPATCH-1840) - HTTP1: shutdown crash when HTTP1 connection activated
 - [DISPATCH-1845](https://issues.apache.org/jira/browse/DISPATCH-1845) - HTTP1: fails to deal with unsolicited responses from the server
 - [DISPATCH-1846](https://issues.apache.org/jira/browse/DISPATCH-1846) - TCP adaptor basic connectivity test improvements
 - [DISPATCH-1848](https://issues.apache.org/jira/browse/DISPATCH-1848) - TCP test echo client/server mishandle socket errors
 - [DISPATCH-1849](https://issues.apache.org/jira/browse/DISPATCH-1849) - Router crash when fetching large message HTTP2 GET request
 - [DISPATCH-1851](https://issues.apache.org/jira/browse/DISPATCH-1851) - TCP adaptor logs do not identify connection ID
 - [DISPATCH-1856](https://issues.apache.org/jira/browse/DISPATCH-1856) - qd_message_received occasionally inserts empty message buffers
 - [DISPATCH-1859](https://issues.apache.org/jira/browse/DISPATCH-1859) - HTTP1: crash on access to null codec state on server-facing connection
 - [DISPATCH-1867](https://issues.apache.org/jira/browse/DISPATCH-1867) - Router is crashing at startup on RHEL 8 
 - [DISPATCH-1868](https://issues.apache.org/jira/browse/DISPATCH-1868) - New system test system_tests_grpc is failing on Fedora 33
 - [DISPATCH-1869](https://issues.apache.org/jira/browse/DISPATCH-1869) - Adaptors must set message discard if message is invalid
 - [DISPATCH-1872](https://issues.apache.org/jira/browse/DISPATCH-1872) - TCP Adaptor mishandles dropped server connections.
 - [DISPATCH-1874](https://issues.apache.org/jira/browse/DISPATCH-1874) - [http2] qd_buffer_t and qd_compose_t objects leaks when clients are abruptly terminated
 - [DISPATCH-1875](https://issues.apache.org/jira/browse/DISPATCH-1875) - [tcp, http1, http2] Protocol Adaptors leaking pn_data_t objects 
 - [DISPATCH-1876](https://issues.apache.org/jira/browse/DISPATCH-1876) - TCP adaptor crash handling fast socket open/close
 - [DISPATCH-1879](https://issues.apache.org/jira/browse/DISPATCH-1879) - system_tests_http2 failing with ASAN use after free error and memory leak
 - [DISPATCH-1880](https://issues.apache.org/jira/browse/DISPATCH-1880) - HTTP1: fails to propagate PN_REJECTED due to race
 - [DISPATCH-1881](https://issues.apache.org/jira/browse/DISPATCH-1881) - libnghttp2 is required to compile Dispatch
 - [DISPATCH-1884](https://issues.apache.org/jira/browse/DISPATCH-1884) - TCP Adaptor fails asan leak tests
 - [DISPATCH-1886](https://issues.apache.org/jira/browse/DISPATCH-1886) - Review and fix races between connection activation and closure
 - [DISPATCH-1894](https://issues.apache.org/jira/browse/DISPATCH-1894) - Make libnghttp2 library not required
 - [DISPATCH-1899](https://issues.apache.org/jira/browse/DISPATCH-1899) - Coverity issues on master branch
 - [DISPATCH-1900](https://issues.apache.org/jira/browse/DISPATCH-1900) - qd_calloc: Assertion `nmemb &amp;&amp; size' failed.
 - [DISPATCH-1901](https://issues.apache.org/jira/browse/DISPATCH-1901) - Bad configuration self test does not recognize all types of connection failure
 - [DISPATCH-1902](https://issues.apache.org/jira/browse/DISPATCH-1902) - qdr_link_complete_sent_message fails to update delivery work value
 - [DISPATCH-1904](https://issues.apache.org/jira/browse/DISPATCH-1904) - Compilation error on qpid-dispatch master on Fedora 32
 - [DISPATCH-1906](https://issues.apache.org/jira/browse/DISPATCH-1906) - Coverity error relating to adding delivery id in trace logs
 - [DISPATCH-1916](https://issues.apache.org/jira/browse/DISPATCH-1916) - Coverity flags use-after-free errors on delivery decref
 - [DISPATCH-1920](https://issues.apache.org/jira/browse/DISPATCH-1920) - Enable TSAN tests in travis configuration
 - [DISPATCH-1924](https://issues.apache.org/jira/browse/DISPATCH-1924) - CI failure in disposition state forwarding tests
 - [DISPATCH-1927](https://issues.apache.org/jira/browse/DISPATCH-1927) - TCP adaptor Assertion `(link-&gt;undelivered).head' failed.
 - [DISPATCH-1937](https://issues.apache.org/jira/browse/DISPATCH-1937) - system_tests_grpc failure due to leak from handle_outgoing_http -&gt; qd_iterator_copy
 - [DISPATCH-1938](https://issues.apache.org/jira/browse/DISPATCH-1938) - Unify .eslintrc settings
 - [DISPATCH-1944](https://issues.apache.org/jira/browse/DISPATCH-1944) - Qpid dispatch console dashboard is showing incorrect number of in/out counts at the "most active addresses" section
 - [DISPATCH-1945](https://issues.apache.org/jira/browse/DISPATCH-1945) - Cleanup some GUI glitches on console's visualization pages
 - [DISPATCH-1946](https://issues.apache.org/jira/browse/DISPATCH-1946) - [docker] Schema compile fails in ubuntu xenial container
 - [DISPATCH-1950](https://issues.apache.org/jira/browse/DISPATCH-1950) - Knock down the minimum required version of the nghttp2 library to 1.33.0
 - [DISPATCH-1951](https://issues.apache.org/jira/browse/DISPATCH-1951) - system_tests_http2 failing with router crash
 - [DISPATCH-1952](https://issues.apache.org/jira/browse/DISPATCH-1952) - qd_bitmask_t leak on streaming message arrival