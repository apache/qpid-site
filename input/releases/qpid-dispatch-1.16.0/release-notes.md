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

# Qpid Dispatch 1.16.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1800](https://issues.apache.org/jira/browse/DISPATCH-1800) - [dev-adaptors] message_body_data objects never freed
 - [DISPATCH-1922](https://issues.apache.org/jira/browse/DISPATCH-1922) - Remove support for Python 2.6
 - [DISPATCH-1923](https://issues.apache.org/jira/browse/DISPATCH-1923) - Remove support for Python 3.5
 - [DISPATCH-1933](https://issues.apache.org/jira/browse/DISPATCH-1933) - Tests should produce JUnit-compatible XML report about individual tests (not aggregated CTest test targets)
 - [DISPATCH-1955](https://issues.apache.org/jira/browse/DISPATCH-1955) - TCP adaptor logs could show total bytes and other statistics
 - [DISPATCH-1961](https://issues.apache.org/jira/browse/DISPATCH-1961) - Add Q2 flow control support to HTTP/1.x adaptor
 - [DISPATCH-2011](https://issues.apache.org/jira/browse/DISPATCH-2011) - Support hwasan variant of address sanitizer on Aarch64 in CMake
 - [DISPATCH-2073](https://issues.apache.org/jira/browse/DISPATCH-2073) - [tcp] Support end-to-end flow control

## Bugs fixed

 - [DISPATCH-1660](https://issues.apache.org/jira/browse/DISPATCH-1660) - Intermittent failure in system_tests_policy_oversize_basic
 - [DISPATCH-1679](https://issues.apache.org/jira/browse/DISPATCH-1679) - leak: qd_connector_t and qd_timer_t
 - [DISPATCH-1697](https://issues.apache.org/jira/browse/DISPATCH-1697) - Leak: qd_conn_identifier
 - [DISPATCH-1698](https://issues.apache.org/jira/browse/DISPATCH-1698) - leak: qdr_connection_ref_t
 - [DISPATCH-1723](https://issues.apache.org/jira/browse/DISPATCH-1723) - alloc.c: Items of type 'qdr_error_t' remain allocated at shutdown: 1
 - [DISPATCH-1740](https://issues.apache.org/jira/browse/DISPATCH-1740) - system_tests_policy_oversize_compound fails due to an unsuppressed leak
 - [DISPATCH-1756](https://issues.apache.org/jira/browse/DISPATCH-1756) - [macOS] failure in system_tests_http
 - [DISPATCH-1835](https://issues.apache.org/jira/browse/DISPATCH-1835) - double free detected with tcp adapter
 - [DISPATCH-1857](https://issues.apache.org/jira/browse/DISPATCH-1857) - concurrent tcp connection attempts can result in hangs
 - [DISPATCH-1878](https://issues.apache.org/jira/browse/DISPATCH-1878) - Client app not getting a response through tcpListener
 - [DISPATCH-1917](https://issues.apache.org/jira/browse/DISPATCH-1917) - Thread race accessing connector-&gt;conn_msg buffer (TSAN)
 - [DISPATCH-1918](https://issues.apache.org/jira/browse/DISPATCH-1918) - Thread race between I/O and Core over link-&gt;undelivered and unsettled lists
 - [DISPATCH-1921](https://issues.apache.org/jira/browse/DISPATCH-1921) - Skupper 0.4: malloc corrupted handling back-to-back TCP connections
 - [DISPATCH-1925](https://issues.apache.org/jira/browse/DISPATCH-1925) - Thread race in qd_message_extend vs qd_message_stream_data_buffers
 - [DISPATCH-1941](https://issues.apache.org/jira/browse/DISPATCH-1941) - Crash in HTTP1 adaptor: member access within null pointer of type 'const struct qd_buffer_t'
 - [DISPATCH-1947](https://issues.apache.org/jira/browse/DISPATCH-1947) - TCP adaptor has no receive flow control
 - [DISPATCH-1948](https://issues.apache.org/jira/browse/DISPATCH-1948) - ASAN flags alignment errors in alloc_poolc
 - [DISPATCH-1949](https://issues.apache.org/jira/browse/DISPATCH-1949) - ASAN flags shift errors on signed conversion
 - [DISPATCH-1959](https://issues.apache.org/jira/browse/DISPATCH-1959) - Update PatternFly packages for the 1.16.0 release
 - [DISPATCH-1964](https://issues.apache.org/jira/browse/DISPATCH-1964) - TCP adaptor connection object should be a pooled type
 - [DISPATCH-1965](https://issues.apache.org/jira/browse/DISPATCH-1965) - Dispatch does not compile with gcc 10 when -Og is used
 - [DISPATCH-1968](https://issues.apache.org/jira/browse/DISPATCH-1968) - Crash after running series of 1Mb iperf3 against TCP adaptor
 - [DISPATCH-1973](https://issues.apache.org/jira/browse/DISPATCH-1973) - ASan failure in system_tests_http2 in _update_qdr_http_request_info
 - [DISPATCH-1981](https://issues.apache.org/jira/browse/DISPATCH-1981) - TCP adaptor Q2 test does not always trigger q2 holdoff
 - [DISPATCH-1984](https://issues.apache.org/jira/browse/DISPATCH-1984) - [http1] compilation issue on s390
 - [DISPATCH-1985](https://issues.apache.org/jira/browse/DISPATCH-1985) - system_test Logger class optionally also writes logs to a file
 - [DISPATCH-1988](https://issues.apache.org/jira/browse/DISPATCH-1988) - Router crash when sending an empty transfer frame followed by an abort
 - [DISPATCH-1997](https://issues.apache.org/jira/browse/DISPATCH-1997) - Cannot build on fedora rawhide
 - [DISPATCH-2001](https://issues.apache.org/jira/browse/DISPATCH-2001) - streaming messages incorrectly use priority 0 inter-router links
 - [DISPATCH-2003](https://issues.apache.org/jira/browse/DISPATCH-2003) - Qdstat memory usage truncated to uint32_t value
 - [DISPATCH-2009](https://issues.apache.org/jira/browse/DISPATCH-2009) - Cannot build on fedora F34
 - [DISPATCH-2012](https://issues.apache.org/jira/browse/DISPATCH-2012) - [tsan] data race warning in qdr_link_process_initial_delivery_CT
 - [DISPATCH-2015](https://issues.apache.org/jira/browse/DISPATCH-2015) - [http1] ThreadSanitizer: data race in system_tests_http1_adaptor
 - [DISPATCH-2016](https://issues.apache.org/jira/browse/DISPATCH-2016) - [test] system_test Tester.get_port() returns ports that fail with 'Address already in use' error
 - [DISPATCH-2030](https://issues.apache.org/jira/browse/DISPATCH-2030) - core_link_endpoint.c: runtime error: store to misaligned address
 - [DISPATCH-2038](https://issues.apache.org/jira/browse/DISPATCH-2038) - [test] AsyncTestReceiver has mutable default argument value
 - [DISPATCH-2040](https://issues.apache.org/jira/browse/DISPATCH-2040) - Some details missing on dispositions forwarded by router on transacted sessions
 - [DISPATCH-2043](https://issues.apache.org/jira/browse/DISPATCH-2043) - TCP adaptor log messages need attention
 - [DISPATCH-2045](https://issues.apache.org/jira/browse/DISPATCH-2045) - qd_hash_internal_remove_item writes to freed (pooled) memory on router shutdown
 - [DISPATCH-2046](https://issues.apache.org/jira/browse/DISPATCH-2046) - Panic in handle due to deleted connector.
 - [DISPATCH-2050](https://issues.apache.org/jira/browse/DISPATCH-2050) - fields for received delivery state are not relayed 
 - [DISPATCH-2056](https://issues.apache.org/jira/browse/DISPATCH-2056) - AddressSanitizer: use-after-poison in qdr_connection_set_context during system_tests_tcp_adaptor, system_tests_http2
 - [DISPATCH-2074](https://issues.apache.org/jira/browse/DISPATCH-2074) - Unused function in tcp_adaptor.c
 - [DISPATCH-2075](https://issues.apache.org/jira/browse/DISPATCH-2075) - TCP adaptor requires 0.34 proton
 - [DISPATCH-2088](https://issues.apache.org/jira/browse/DISPATCH-2088) - SEGV in qd_buffer_dec_fanout
 - [DISPATCH-2089](https://issues.apache.org/jira/browse/DISPATCH-2089) - [tools] Scraper not html-escaping user transfer data properly
 - [DISPATCH-2090](https://issues.apache.org/jira/browse/DISPATCH-2090) - [tools] Scraper mishandling non-terminal dispositions
 - [DISPATCH-2091](https://issues.apache.org/jira/browse/DISPATCH-2091) - TCP adaptor does not close listener connection when RX window is full
 - [DISPATCH-2098](https://issues.apache.org/jira/browse/DISPATCH-2098) - Crash when ctrl-c on router that has a libwebsockets listener connected to a console (2)
 - [DISPATCH-2099](https://issues.apache.org/jira/browse/DISPATCH-2099) - [TCP] crash in qd_message_stream_data_release() on connection close
 - [DISPATCH-2104](https://issues.apache.org/jira/browse/DISPATCH-2104) - qdstat --autolinks showing int32(0) in output

## Tasks

 - [DISPATCH-1814](https://issues.apache.org/jira/browse/DISPATCH-1814) - Apply autofixes to resolve some flake8 code formatting issues
 - [DISPATCH-1960](https://issues.apache.org/jira/browse/DISPATCH-1960) - Re-factor Q2 flow logic to allow adaptors to support Q2