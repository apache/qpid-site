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

# Qpid Proton 0.19.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note**: This release contains the initial release of a new Ruby messaging API. The interfaces in this API are subject to change. We plan to take user feedback and make any resulting API changes in upcoming releases.

Some of the Proton bindings have been unmaintained for some time.  We are deprecating them with this release, and we plan to remove them in an upcoming release.  The deprecated bindings are JavaScript, Node.js, PHP, and Perl.

In addition, the Messenger API (in any binding) is now deprecated.  We encourage you to use the newer reactive APIs instead.


## New features and improvements

 - [PROTON-869](https://issues.apache.org/jira/browse/PROTON-869) - [proton-c] should be straightforward to associate handlers with acceptors
 - [PROTON-1064](https://issues.apache.org/jira/browse/PROTON-1064) - ruby: native IO based on connection_driver.c 
 - [PROTON-1429](https://issues.apache.org/jira/browse/PROTON-1429) - [go] Support marshaling and unmarshaling to/from the timestamp AMQP type in message body
 - [PROTON-1430](https://issues.apache.org/jira/browse/PROTON-1430) - [go] Support marshaling and unmarshaling to/from the uuid AMQP type in message body
 - [PROTON-1432](https://issues.apache.org/jira/browse/PROTON-1432) - [go] Support marshaling and unmarshaling to/from the char AMQP type in message body
 - [PROTON-1549](https://issues.apache.org/jira/browse/PROTON-1549) - Document legal values for the reconnect parameter
 - [PROTON-1651](https://issues.apache.org/jira/browse/PROTON-1651) - Correct spelling errors
 - [PROTON-1654](https://issues.apache.org/jira/browse/PROTON-1654) - Windows build does not compile the examples that require C++11
 - [PROTON-1670](https://issues.apache.org/jira/browse/PROTON-1670) - Configurable TLS versions
 - [PROTON-1678](https://issues.apache.org/jira/browse/PROTON-1678) - [cpp] Enable setting link names
 - [PROTON-1680](https://issues.apache.org/jira/browse/PROTON-1680) - [python] Handle various string inputs for allowed SASL mechanisms and add docs
 - [PROTON-1681](https://issues.apache.org/jira/browse/PROTON-1681) - [cpp] access to terminus capabilities
 - [PROTON-1684](https://issues.apache.org/jira/browse/PROTON-1684) - Change build for updated minimum tool versions
 - [PROTON-1687](https://issues.apache.org/jira/browse/PROTON-1687) - Improve efficiency of the transport output buffer
 - [PROTON-1693](https://issues.apache.org/jira/browse/PROTON-1693) - [ruby] Replace C-reactor based code with new Container
 - [PROTON-1707](https://issues.apache.org/jira/browse/PROTON-1707) - Remove extraneous directories in C++ binding source
 - [PROTON-1713](https://issues.apache.org/jira/browse/PROTON-1713) - Various doc fixes

## Bugs fixed

 - [PROTON-1079](https://issues.apache.org/jira/browse/PROTON-1079) - Ruby Reactor interface fails with SSL.new ArgumentError
 - [PROTON-1081](https://issues.apache.org/jira/browse/PROTON-1081) - Incorrect error message formatting in message.c
 - [PROTON-1238](https://issues.apache.org/jira/browse/PROTON-1238) - Add fallback operator&lt;&lt; for wrapped proton-c objects
 - [PROTON-1517](https://issues.apache.org/jira/browse/PROTON-1517) - SyncRequestResponse(BlockingConnection).call() fails with timeout
 - [PROTON-1522](https://issues.apache.org/jira/browse/PROTON-1522) - Password is logged on connecting with Python client
 - [PROTON-1531](https://issues.apache.org/jira/browse/PROTON-1531) - C epoll proactor listener cleanup race
 - [PROTON-1537](https://issues.apache.org/jira/browse/PROTON-1537) - ruby: update API in line with new C++ API changes
 - [PROTON-1556](https://issues.apache.org/jira/browse/PROTON-1556) - [proton-cpp] ssl_client_options is not self-assignable
 - [PROTON-1636](https://issues.apache.org/jira/browse/PROTON-1636) - Fairly Consistent (but intermittent) hangs in ruby-example-test/ruby-test-container using Travis CI
 - [PROTON-1641](https://issues.apache.org/jira/browse/PROTON-1641) - Windows proactor hang on incoming connections
 - [PROTON-1677](https://issues.apache.org/jira/browse/PROTON-1677) - Travis CI builds failing due to glibc bug
 - [PROTON-1685](https://issues.apache.org/jira/browse/PROTON-1685) - [go] support for marshalling/unmarshaling AMQP arrays
 - [PROTON-1686](https://issues.apache.org/jira/browse/PROTON-1686) - [go] unmarshal maps with illegal key types
 - [PROTON-1689](https://issues.apache.org/jira/browse/PROTON-1689) - [cpp] exception thrown in handler can result in garbage exception from run()
 - [PROTON-1694](https://issues.apache.org/jira/browse/PROTON-1694) - Some mutexes in the libuv proactor implementation are not properly initialised and destroyed
 - [PROTON-1697](https://issues.apache.org/jira/browse/PROTON-1697) - Tests of Ruby and Go bindings don't correctly use the path for saslpasswd2 discovered by cmake
 - [PROTON-1700](https://issues.apache.org/jira/browse/PROTON-1700) - [cpp] Reconnecting container does not respond to stop
 - [PROTON-1704](https://issues.apache.org/jira/browse/PROTON-1704) - [c proactor] test_ipv4_ipv6 intermittent failure on FreeBSD
 - [PROTON-1710](https://issues.apache.org/jira/browse/PROTON-1710) - Proton C++ will crash if told to run 0 threads
 - [PROTON-1711](https://issues.apache.org/jira/browse/PROTON-1711) - SSL_IMPL none SASL_IMPL none build attempts to build c-ssl-tests and fails
 - [PROTON-1717](https://issues.apache.org/jira/browse/PROTON-1717) - [C proactor] Allow initialization of transport and connection before binding
 - [PROTON-1720](https://issues.apache.org/jira/browse/PROTON-1720) - [ruby] support for SSL configuration via connection options
