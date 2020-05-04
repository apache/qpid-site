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

# Qpid Dispatch 1.1.0 Release Notes

Dispatch is a lightweight AMQP 1.0 message router. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**NOTE**: In previous releases, inter-router and route container links were each created in their own sessions. This restricted the total number of links that can be established between routers or between routers and brokers,
since the maximum number of sessions between two containers is limited to 32,768. To avoid this limitation, DISPATCH-952 changed to use a single session for all links. In concert with this change, DISPATCH-981 ensures that links initiated by the router have their name prefixed with the originating container_id, to prevent name collisions occurring during link routing. As a result of these changes, if you upgrade to Dispatch Router 1.1.0 from a prior release, any durable subscription links being routed through a router to a broker will see their subscription name change from the brokers perspective to incorporate the container_id prefix.	


## New features and improvements

 - [DISPATCH-89](https://issues.apache.org/jira/browse/DISPATCH-89) - Model the legacy topic exchange behavior of qpidd
 - [DISPATCH-834](https://issues.apache.org/jira/browse/DISPATCH-834) - Create config tool to create/read/update/delete router config files
 - [DISPATCH-856](https://issues.apache.org/jira/browse/DISPATCH-856) - Return router's hostname as a read-only attribute on the router entity
 - [DISPATCH-859](https://issues.apache.org/jira/browse/DISPATCH-859) - Introduce SYSTEMD and SYSVINIT cmake switches to install files accordingly
 - [DISPATCH-861](https://issues.apache.org/jira/browse/DISPATCH-861) - Update to recent rhea.js
 - [DISPATCH-864](https://issues.apache.org/jira/browse/DISPATCH-864) - Remove the SYSTEMD and SYSVINIT flags introduced by DISPATCH-859
 - [DISPATCH-872](https://issues.apache.org/jira/browse/DISPATCH-872) - Add a counter for dropped-presettleds on links
 - [DISPATCH-878](https://issues.apache.org/jira/browse/DISPATCH-878) - qdrouterd should log real port if port 0 was specified for the listener port property in qdrouterd.conf
 - [DISPATCH-884](https://issues.apache.org/jira/browse/DISPATCH-884) - Add schema property to allow configurable TLS protocol versions
 - [DISPATCH-885](https://issues.apache.org/jira/browse/DISPATCH-885) - Modify qd_compose_insert_[string,symbol,binary] to add zero-length [string, symbol, binary] for null input
 - [DISPATCH-888](https://issues.apache.org/jira/browse/DISPATCH-888) - Balanced distribution algorithm visits each link to determine the best_eligible_link
 - [DISPATCH-892](https://issues.apache.org/jira/browse/DISPATCH-892) - Support code coverage testing
 - [DISPATCH-901](https://issues.apache.org/jira/browse/DISPATCH-901) - add authz support to auth service plugin
 - [DISPATCH-911](https://issues.apache.org/jira/browse/DISPATCH-911) - Add link and address level counters at the global router level
 - [DISPATCH-918](https://issues.apache.org/jira/browse/DISPATCH-918) - Improve router config consistency and metadata
 - [DISPATCH-921](https://issues.apache.org/jira/browse/DISPATCH-921) - Install console dependencies with npm during make install
 - [DISPATCH-925](https://issues.apache.org/jira/browse/DISPATCH-925) - Doc: Update anchor name format
 - [DISPATCH-932](https://issues.apache.org/jira/browse/DISPATCH-932) - Provide per-ingress router counts for deliveries on egress links
 - [DISPATCH-938](https://issues.apache.org/jira/browse/DISPATCH-938) - Doc: Remove the "Configuration Reference"
 - [DISPATCH-942](https://issues.apache.org/jira/browse/DISPATCH-942) - allow resumable link routes to be refused
 - [DISPATCH-946](https://issues.apache.org/jira/browse/DISPATCH-946) - Detect if npm install needs to be executed and display a message
 - [DISPATCH-951](https://issues.apache.org/jira/browse/DISPATCH-951) - log details for the proton found during build
 - [DISPATCH-963](https://issues.apache.org/jira/browse/DISPATCH-963) - Router crash during shutdown in system_tests_distribution
 - [DISPATCH-971](https://issues.apache.org/jira/browse/DISPATCH-971) - Revert DISPATCH-744 - Don't reject unsettled multicasts
 - [DISPATCH-972](https://issues.apache.org/jira/browse/DISPATCH-972) - Dispatch Router doc should be consistent with "sudo" usage
 - [DISPATCH-1012](https://issues.apache.org/jira/browse/DISPATCH-1012) - Release undeliverable deliveries, don't hold them

## Bugs fixed

 - [DISPATCH-580](https://issues.apache.org/jira/browse/DISPATCH-580) - Log stats should be graphable
 - [DISPATCH-590](https://issues.apache.org/jira/browse/DISPATCH-590) - List of log modules on the overview page is occationally doubled
 - [DISPATCH-801](https://issues.apache.org/jira/browse/DISPATCH-801) - Stand-alone version of the console does not open at all when running offline
 - [DISPATCH-831](https://issues.apache.org/jira/browse/DISPATCH-831) - Change conntector.cost default value to 1 instead of '1'
 - [DISPATCH-869](https://issues.apache.org/jira/browse/DISPATCH-869) - Multiple brokers in a topology are displayed as a single broker
 - [DISPATCH-875](https://issues.apache.org/jira/browse/DISPATCH-875) - Document address and link route wildcards
 - [DISPATCH-876](https://issues.apache.org/jira/browse/DISPATCH-876) - config file linkRoute should use connection instead of connector 
 - [DISPATCH-877](https://issues.apache.org/jira/browse/DISPATCH-877) - Document how to configure TLS ciphers
 - [DISPATCH-879](https://issues.apache.org/jira/browse/DISPATCH-879) - Document how Dispatch Router uses alternate failover URLs
 - [DISPATCH-880](https://issues.apache.org/jira/browse/DISPATCH-880) - Document how Dispatch Router disconnects connections
 - [DISPATCH-886](https://issues.apache.org/jira/browse/DISPATCH-886) - Console does not properly escape HTML in entity names
 - [DISPATCH-891](https://issues.apache.org/jira/browse/DISPATCH-891) - Router incref assert in system_tests_delivery_abort
 - [DISPATCH-893](https://issues.apache.org/jira/browse/DISPATCH-893) - Compile fails using libwebsockets 7
 - [DISPATCH-894](https://issues.apache.org/jira/browse/DISPATCH-894) - Unable to run system tests on CentOS 6 (Python 2.6)
 - [DISPATCH-902](https://issues.apache.org/jira/browse/DISPATCH-902) - Intermittent crash with link to broker when broker closed
 - [DISPATCH-905](https://issues.apache.org/jira/browse/DISPATCH-905) - Dispatch Router not failing over to slave broker when master broker goes away
 - [DISPATCH-907](https://issues.apache.org/jira/browse/DISPATCH-907) - cannot set address phase via qdmanage tool
 - [DISPATCH-910](https://issues.apache.org/jira/browse/DISPATCH-910) - Inter-router connections with dir 'in' have no host name
 - [DISPATCH-912](https://issues.apache.org/jira/browse/DISPATCH-912) - system_tests_user_id_proxy and system_tests_policy failing
 - [DISPATCH-916](https://issues.apache.org/jira/browse/DISPATCH-916) - qdmanage get-attributes and get-operations not taking into account passed in type
 - [DISPATCH-919](https://issues.apache.org/jira/browse/DISPATCH-919) - Display a warning when running Dispatch tests if python-unittest2 is not installed
 - [DISPATCH-922](https://issues.apache.org/jira/browse/DISPATCH-922) - Subsecond timestamps improperly formatted
 - [DISPATCH-927](https://issues.apache.org/jira/browse/DISPATCH-927) - detach not echoed back on multi-hop link route
 - [DISPATCH-928](https://issues.apache.org/jira/browse/DISPATCH-928) - calling map_destination for 'undefined' address causes segfault
 - [DISPATCH-931](https://issues.apache.org/jira/browse/DISPATCH-931) - Syntax error and missing dependencies in docker files
 - [DISPATCH-940](https://issues.apache.org/jira/browse/DISPATCH-940) - When running qdrouterd with -c and -d combined, configuration file is reporting as not found
 - [DISPATCH-941](https://issues.apache.org/jira/browse/DISPATCH-941) - Router is returning incorrect files from http get requests.
 - [DISPATCH-943](https://issues.apache.org/jira/browse/DISPATCH-943) - segfault in remote_sasl
 - [DISPATCH-944](https://issues.apache.org/jira/browse/DISPATCH-944) - remote_sasl plugin leaving connections open
 - [DISPATCH-945](https://issues.apache.org/jira/browse/DISPATCH-945) - Crash on shutdown when a http+websocket connection is open
 - [DISPATCH-947](https://issues.apache.org/jira/browse/DISPATCH-947) - system tests on master branch failing when run against latest master proton
 - [DISPATCH-948](https://issues.apache.org/jira/browse/DISPATCH-948) - Move rhea npm dependency from dispatch-management to stand-alone 
 - [DISPATCH-952](https://issues.apache.org/jira/browse/DISPATCH-952) - qdrouterd seg fault after reporting "too many sessions"
 - [DISPATCH-953](https://issues.apache.org/jira/browse/DISPATCH-953) - Relative path name self test fails unless dispatch is installed
 - [DISPATCH-954](https://issues.apache.org/jira/browse/DISPATCH-954) - Fix Coverity issue on master branch
 - [DISPATCH-962](https://issues.apache.org/jira/browse/DISPATCH-962) - links established to 'unavailable' addresses are not refused correctly
 - [DISPATCH-964](https://issues.apache.org/jira/browse/DISPATCH-964) - Auto-links are closed with an incorrect error indication
 - [DISPATCH-966](https://issues.apache.org/jira/browse/DISPATCH-966) - Qpid dispatch unstable inter-router connections
 - [DISPATCH-967](https://issues.apache.org/jira/browse/DISPATCH-967) - Policy management interface does not forward log warning messages
 - [DISPATCH-981](https://issues.apache.org/jira/browse/DISPATCH-981) - link routing results in name collisions now that single session is used
 - [DISPATCH-983](https://issues.apache.org/jira/browse/DISPATCH-983) - link routed receiver link did not issue flow
 - [DISPATCH-986](https://issues.apache.org/jira/browse/DISPATCH-986) - Coverity issues on master
 - [DISPATCH-991](https://issues.apache.org/jira/browse/DISPATCH-991) - Master qdstat throws keyError when running against 1.0.1 router
 - [DISPATCH-992](https://issues.apache.org/jira/browse/DISPATCH-992) - System test is failing in some scenarios - system_tests_delivery_abort.py
 - [DISPATCH-994](https://issues.apache.org/jira/browse/DISPATCH-994) - segfault in qdr_link_second_attach
 - [DISPATCH-1021](https://issues.apache.org/jira/browse/DISPATCH-1021) - Router core dumps when 3 senders and 3 receivers are sending/receiving very large presettled messages to a multicast address 
 - [DISPATCH-1022](https://issues.apache.org/jira/browse/DISPATCH-1022) - Router crashes when a client sends an end immediately following a detach in a link routed case
 - [DISPATCH-1023](https://issues.apache.org/jira/browse/DISPATCH-1023) - qdr_deliovery_t objects leak in two router presettled case

## Tasks

 - [DISPATCH-833](https://issues.apache.org/jira/browse/DISPATCH-833) - Remove 'Add mode' from hawtio and stand-alone consoles
 - [DISPATCH-862](https://issues.apache.org/jira/browse/DISPATCH-862) - have the CI build log detal which commit is being used from the Proton repo
 - [DISPATCH-955](https://issues.apache.org/jira/browse/DISPATCH-955) - Assure console works with updated schema attribute names 
 - [DISPATCH-978](https://issues.apache.org/jira/browse/DISPATCH-978) - Audit memory allocations to remove cases of uninitialized data
 - [DISPATCH-989](https://issues.apache.org/jira/browse/DISPATCH-989) - remove defunct/broken test tool for console