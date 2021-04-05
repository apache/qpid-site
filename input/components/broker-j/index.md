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

<div id="-left-column" markdown="1">

# Broker-J

<div class="feature" markdown="1">

A [message-oriented middleware][mom] message broker written in Java
that stores, routes, and forwards messages using AMQP.

[mom]:http://en.wikipedia.org/wiki/Message-oriented_middleware

</div>

## Features

<div class="two-column" markdown="1">

 - Speaks and translates among all versions of AMQP
 - AMQP over WebSockets
 - Management via REST, AMQP Management, and web console
 - [Access control lists]({{current_broker_j_release_url}}/book/Java-Broker-Security-AccessControlProviders.html)
 - Flexible logging
 - Flow to disk
 - Header-based routing
 - Heartbeats
 - [High availability]({{current_broker_j_release_url}}/book/Java-Broker-High-Availability.html)
 - Message groups
 - Pluggable persistence supporting Derby, SQL, and BDB stores
 - [Pluggable authentication]({{current_broker_j_release_url}}/book/Java-Broker-Security.html#Java-Broker-Security-Authentication-Providers) supporting LDAP, Kerberos, OAUTH2 and SSL client certificates
 - [Producer flow control]({{current_broker_j_release_url}}/book/Java-Broker-Runtime-Disk-Space-Management.html#Qpid-Producer-Flow-Control)
 - Secure connection via SSL
 - Server-side selectors
 - Specialized queuing with last value queue, priority queue, and sorted queue
 - Threshold alerts
 - Transactions
 - [Undeliverable message handling]({{current_broker_j_release_url}}/book/Java-Broker-Runtime-Handling-Undeliverable-Messages.html)
 - Virtual hosts
 - Support for message compression

</div>

## Documentation

 - [Broker book]({{current_broker_j_release_url}}/book/index.html)
 - [How to build Apache Qpid Broker-J](https://github.com/apache/qpid-broker-j/blob/main/README.md)

</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - {{current_broker_j_release_link}}
 - [Past releases]({{site_url}}/releases/index.html#past-releases)

## Issues

 - [Report a bug](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12310520&issuetype=1&priority=3)
 - [Request an improvement](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12310520&issuetype=4&priority=3)
 - <form id="-jira-goto-form">Go to issue <input name="jira" value="QPID-"/></form>
 - [JIRA project page](https://issues.apache.org/jira/browse/QPID)

## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-broker-j)
 - [Git clone URL](https://gitbox.apache.org/repos/asf/qpid-broker-j.git)

## Resources

 - [Security](security.html)
 - [FAQ](https://cwiki.apache.org/confluence/display/qpid/qpid+java+faq)
 - [Design documents](https://cwiki.apache.org/confluence/display/qpid/java+broker+design)
 - [Qpid extensions to AMQP](https://cwiki.apache.org/confluence/display/qpid/qpid+extensions+to+amqp)
 - [More on the wiki](https://cwiki.apache.org/confluence/display/qpid/qpid+java+documentation)

</div>
