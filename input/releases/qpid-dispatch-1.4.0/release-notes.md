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

# Qpid Dispatch 1.4.0 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-1082](https://issues.apache.org/jira/browse/DISPATCH-1082) - Log messages can not be correlated to a specific connection
 - [DISPATCH-1099](https://issues.apache.org/jira/browse/DISPATCH-1099) - Add a timer facility for the core thread
 - [DISPATCH-1103](https://issues.apache.org/jira/browse/DISPATCH-1103) - auto-links should retry after detach
 - [DISPATCH-1105](https://issues.apache.org/jira/browse/DISPATCH-1105) - Remove untested and presumed unused iovec facility
 - [DISPATCH-1107](https://issues.apache.org/jira/browse/DISPATCH-1107) - Need info for logs to help disambiguate router connections
 - [DISPATCH-1108](https://issues.apache.org/jira/browse/DISPATCH-1108) - Tests failing in travis due to import errors
 - [DISPATCH-1109](https://issues.apache.org/jira/browse/DISPATCH-1109) - use serving host and port as defaults for connect screen in console served by router
 - [DISPATCH-1123](https://issues.apache.org/jira/browse/DISPATCH-1123) - Add a link-endpoint API for in-core modules that need to terminate links
 - [DISPATCH-1128](https://issues.apache.org/jira/browse/DISPATCH-1128) - Add delivery rate to connection mouseover on topology page
 - [DISPATCH-1129](https://issues.apache.org/jira/browse/DISPATCH-1129) - Receiver crash due to data corruption on multicast streamed messages
 - [DISPATCH-1130](https://issues.apache.org/jira/browse/DISPATCH-1130) - Expose which message priority is being handled by an inter-router link
 - [DISPATCH-1132](https://issues.apache.org/jira/browse/DISPATCH-1132) - Cleanup and memory reduction in the message module
 - [DISPATCH-1133](https://issues.apache.org/jira/browse/DISPATCH-1133) - Router core modules for Core extensions

## Bugs fixed

 - [DISPATCH-1010](https://issues.apache.org/jira/browse/DISPATCH-1010) - Intermittent test failure with system_tests_disallow_link_resumable_link_route
 - [DISPATCH-1081](https://issues.apache.org/jira/browse/DISPATCH-1081) - Messages to multicast addresses are being released when no receivers attached
 - [DISPATCH-1086](https://issues.apache.org/jira/browse/DISPATCH-1086) - Dispatch Router sporadically goes into a state where TLS connections to the auth service fail
 - [DISPATCH-1090](https://issues.apache.org/jira/browse/DISPATCH-1090) - Transfer/Disposition(state=release) loop forms when application disconnects abruptly from brokered queue until link credit is exhausted.
 - [DISPATCH-1098](https://issues.apache.org/jira/browse/DISPATCH-1098) - Fedora 28 python3-only test issues
 - [DISPATCH-1101](https://issues.apache.org/jira/browse/DISPATCH-1101) - system_tests_link_routes_add_external_prefix failure on python3
 - [DISPATCH-1102](https://issues.apache.org/jira/browse/DISPATCH-1102) - Add/Delete link route prefix memory leak
 - [DISPATCH-1104](https://issues.apache.org/jira/browse/DISPATCH-1104) - qdstat --log log levels are wrong
 - [DISPATCH-1106](https://issues.apache.org/jira/browse/DISPATCH-1106) - Interrouter link name collisions when routers started in same second
 - [DISPATCH-1110](https://issues.apache.org/jira/browse/DISPATCH-1110) - Intermittent router hang while running QIT's AMQP large content test
 - [DISPATCH-1111](https://issues.apache.org/jira/browse/DISPATCH-1111) - auth delegation plugin: authenticated identity should be taken from nested map
 - [DISPATCH-1112](https://issues.apache.org/jira/browse/DISPATCH-1112) - Interconnect not sending the detach response under load
 - [DISPATCH-1113](https://issues.apache.org/jira/browse/DISPATCH-1113) - Can't update log/AUTHSERVICE
 - [DISPATCH-1116](https://issues.apache.org/jira/browse/DISPATCH-1116) - qdmanage lets the module of log instance be changed
 - [DISPATCH-1117](https://issues.apache.org/jira/browse/DISPATCH-1117) - doc on update logging with qdmanage is inaccurate
 - [DISPATCH-1118](https://issues.apache.org/jira/browse/DISPATCH-1118) - Fix Valgrind errors in the tests
 - [DISPATCH-1119](https://issues.apache.org/jira/browse/DISPATCH-1119) - Assert in qdr_del_link_ref in self test system_tests_multi_tenancy
 - [DISPATCH-1121](https://issues.apache.org/jira/browse/DISPATCH-1121) - qd_parse_as_(u)int() fails to detect over/underflow of 32bit integers
 - [DISPATCH-1126](https://issues.apache.org/jira/browse/DISPATCH-1126) - ERROR Attempt to attach too many inter-router links for priority sheaf.
 - [DISPATCH-1131](https://issues.apache.org/jira/browse/DISPATCH-1131) - validate link route prefix field
 - [DISPATCH-1134](https://issues.apache.org/jira/browse/DISPATCH-1134) - Console test should be skipped if it was manually executed but console was not built
 - [DISPATCH-1137](https://issues.apache.org/jira/browse/DISPATCH-1137) - Connection info contains stale pointer to container id