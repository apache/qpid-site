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

# Qpid Dispatch 1.12.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-975](https://issues.apache.org/jira/browse/DISPATCH-975) - Policy has no provision for limiting user message size
 - [DISPATCH-1479](https://issues.apache.org/jira/browse/DISPATCH-1479) - multicast/routing behaviour doc improvements
 - [DISPATCH-1608](https://issues.apache.org/jira/browse/DISPATCH-1608) - Display workerThreads in the output of qdstat -g and qdmanage query --type=router
 - [DISPATCH-1611](https://issues.apache.org/jira/browse/DISPATCH-1611) - In debug mode, provide time and backtrace of leaked pool allocations
 - [DISPATCH-1615](https://issues.apache.org/jira/browse/DISPATCH-1615) - Backtrace of leaked allocations does not show object address
 - [DISPATCH-1616](https://issues.apache.org/jira/browse/DISPATCH-1616) - Scraper could export facts for creating sequence diagrams
 - [DISPATCH-1617](https://issues.apache.org/jira/browse/DISPATCH-1617) - Prevent router startup if edge or standalone routers have 'edge' role listeners

## Bugs fixed

 - [DISPATCH-1581](https://issues.apache.org/jira/browse/DISPATCH-1581) - Policy counters are int and should be uint64
 - [DISPATCH-1593](https://issues.apache.org/jira/browse/DISPATCH-1593) - Fix legend in console's topology view
 - [DISPATCH-1606](https://issues.apache.org/jira/browse/DISPATCH-1606) - Qpid dispatch console keeps trying to open connections when using empty username and password against a listener configured with SASL plain
 - [DISPATCH-1607](https://issues.apache.org/jira/browse/DISPATCH-1607) - [test] one_router test_48_connection_uptime_last_dlv ConnectionUptimeLastDlvTest intermittent fail
 - [DISPATCH-1609](https://issues.apache.org/jira/browse/DISPATCH-1609) - Policy denial logs omit the 'C' in the connection ID
 - [DISPATCH-1610](https://issues.apache.org/jira/browse/DISPATCH-1610) - qd_pn_free_link_session_t objects leaking when connections are socket closed
 - [DISPATCH-1612](https://issues.apache.org/jira/browse/DISPATCH-1612) - Automatically fill in the address and port that was used to serve the console into the console's connect form
 - [DISPATCH-1613](https://issues.apache.org/jira/browse/DISPATCH-1613) - Remove error log that is issued when &gt; QDR_N_PRIORITY router links attach
 - [DISPATCH-1614](https://issues.apache.org/jira/browse/DISPATCH-1614) - Edge router crash when interior closes edge uplink connection
 - [DISPATCH-1618](https://issues.apache.org/jira/browse/DISPATCH-1618) - Server shutdown leaks policy setting objects
 - [DISPATCH-1622](https://issues.apache.org/jira/browse/DISPATCH-1622) - Router crash when trying to create connector via qdmanage
 - [DISPATCH-1626](https://issues.apache.org/jira/browse/DISPATCH-1626) - On released callback invoked twice for same delivery tag
 - [DISPATCH-1627](https://issues.apache.org/jira/browse/DISPATCH-1627) - Occasional leak of qd_iterator_buffer during system_tests_link_route_credit test
 - [DISPATCH-1628](https://issues.apache.org/jira/browse/DISPATCH-1628) - Crash after enforcing oversize message connection close
 - [DISPATCH-1630](https://issues.apache.org/jira/browse/DISPATCH-1630) - Coverity issues on master branch