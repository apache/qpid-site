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

# Qpid Dispatch 1.3.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

NOTE: Dispatch 1.3.0 builds against Proton 0.25.0, but a number of tests will
fail due to import errors. A patch can be found on
[DISPATCH-1108](https://issues.apache.org/jira/browse/DISPATCH-1108)
to resolve these test failures until a newer release of Dispatch is available.

## New features and improvements

 - [DISPATCH-977](https://issues.apache.org/jira/browse/DISPATCH-977) - Document transaction support
 - [DISPATCH-1054](https://issues.apache.org/jira/browse/DISPATCH-1054) - Add console test to make test
 - [DISPATCH-1059](https://issues.apache.org/jira/browse/DISPATCH-1059) - Force Overview and Entities tree to be full page height 
 - [DISPATCH-1064](https://issues.apache.org/jira/browse/DISPATCH-1064) - Doc link route reconnect behavior
 - [DISPATCH-1065](https://issues.apache.org/jira/browse/DISPATCH-1065) - Doc new router statistics
 - [DISPATCH-1066](https://issues.apache.org/jira/browse/DISPATCH-1066) - Document capability to restrict TLS and SSL protocol versions used in connections
 - [DISPATCH-1067](https://issues.apache.org/jira/browse/DISPATCH-1067) - Doc improvements for router policies
 - [DISPATCH-1070](https://issues.apache.org/jira/browse/DISPATCH-1070) - Use patternfly cards on overview page
 - [DISPATCH-1075](https://issues.apache.org/jira/browse/DISPATCH-1075) - Dropdown list of routers on the console's Entities page should be sorted
 - [DISPATCH-1076](https://issues.apache.org/jira/browse/DISPATCH-1076) - Don't concat console's source files into a single file

## Bugs fixed

 - [DISPATCH-322](https://issues.apache.org/jira/browse/DISPATCH-322) - Graph icon is missing when browser window is narrow
 - [DISPATCH-993](https://issues.apache.org/jira/browse/DISPATCH-993) - Test system_tests_topology_disposition fails intermittently
 - [DISPATCH-1008](https://issues.apache.org/jira/browse/DISPATCH-1008) - Router should preserve original connection information when attempting to make failover connections
 - [DISPATCH-1061](https://issues.apache.org/jira/browse/DISPATCH-1061) - Clear popups on console's topology page 
 - [DISPATCH-1062](https://issues.apache.org/jira/browse/DISPATCH-1062) - Link address can be reported incorrectly as mobile+phase-0
 - [DISPATCH-1063](https://issues.apache.org/jira/browse/DISPATCH-1063) - Receiver unable to receive messages on waypoint address with external-address in two router case
 - [DISPATCH-1069](https://issues.apache.org/jira/browse/DISPATCH-1069) - memory grows on a long-lived connection when links are opened and closed
 - [DISPATCH-1071](https://issues.apache.org/jira/browse/DISPATCH-1071) - Switching between traffic visualizations sometimes shows both 
 - [DISPATCH-1072](https://issues.apache.org/jira/browse/DISPATCH-1072) - Number of clients doesn't always update on topology page
 - [DISPATCH-1074](https://issues.apache.org/jira/browse/DISPATCH-1074) - Fix mouseover on an address on console's Chord page 
 - [DISPATCH-1077](https://issues.apache.org/jira/browse/DISPATCH-1077) - Reported rate of message traffic is incorrect on console's 'message traffic' page
 - [DISPATCH-1078](https://issues.apache.org/jira/browse/DISPATCH-1078) - Tab bar icon changes for topology page
 - [DISPATCH-1080](https://issues.apache.org/jira/browse/DISPATCH-1080) - system_tests_ssl failing consistently on Travis
 - [DISPATCH-1083](https://issues.apache.org/jira/browse/DISPATCH-1083) - File console/stand-alone/package-lock.json constantly regenerated
 - [DISPATCH-1084](https://issues.apache.org/jira/browse/DISPATCH-1084) - The color for new addresses on topology visualizations is incorrect
 - [DISPATCH-1085](https://issues.apache.org/jira/browse/DISPATCH-1085) - When sender closes connection after sending a large streaming message, receiver gets aborted message
 - [DISPATCH-1087](https://issues.apache.org/jira/browse/DISPATCH-1087) - qdstat and qdmanage dont run on environments that have only python3
 - [DISPATCH-1089](https://issues.apache.org/jira/browse/DISPATCH-1089) - Dispatch creates sender autolinks with null source terminus and receiver autolinks with null target terminus
 - [DISPATCH-1091](https://issues.apache.org/jira/browse/DISPATCH-1091) - name collision with 'builtins' library in python2
 - [DISPATCH-1092](https://issues.apache.org/jira/browse/DISPATCH-1092) - in some cases qdrouterd crashes due to stale pn_session_t
 - [DISPATCH-1093](https://issues.apache.org/jira/browse/DISPATCH-1093) - adding connectors dynamically causes extra connections for existing connectors
 - [DISPATCH-1094](https://issues.apache.org/jira/browse/DISPATCH-1094) - Log file messages out of order according to time stamps
 - [DISPATCH-1095](https://issues.apache.org/jira/browse/DISPATCH-1095) - Skipped system tests are marked as failed on rhel6 
 - [DISPATCH-1097](https://issues.apache.org/jira/browse/DISPATCH-1097) - Fix Coverity issue on main branch
