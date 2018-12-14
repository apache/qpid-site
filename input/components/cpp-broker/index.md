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

# Qpid C++ Broker

<div class="feature" markdown="1">

A [message-oriented middleware][mom] message broker written in C++
that stores, routes, and forwards messages using AMQP.

[mom]:http://en.wikipedia.org/wiki/Message-oriented_middleware

</div>

## Features

<div class="two-column" markdown="1">

 - Speaks AMQP 1.0 and 0-10
 - Runs on Linux and Windows
 - Access control lists
 - Flexible logging
 - Header-based routing
 - Heartbeats
 - [High availability]({{current_cpp_release_url}}/cpp-broker/book/chapter-ha.html)
 - [Message groups]({{current_cpp_release_url}}/cpp-broker/book/Using-message-groups.html)
 - Message TTLs and arrival timestamps
 - Pluggable persistence
 - [Pluggable authentication via SASL]({{current_cpp_release_url}}/cpp-broker/book/chap-Messaging_User_Guide-Security.html)
 - [Producer flow control]({{current_cpp_release_url}}/cpp-broker/book/producer-flow-control.html)
 - [Queue replication]({{current_cpp_release_url}}/cpp-broker/book/ha-queue-replication.html)
 - Resource limits
 - Secure connection via SSL
 - [Server-side selectors](https://issues.apache.org/jira/browse/QPID-4558?focusedCommentId=13592659&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-13592659)
 - Specialized queueing with [last value queue]({{current_cpp_release_url}}/cpp-broker/book/ch01s06.html), priority queue, and ring queue
 - [Threshold alerts](https://issues.apache.org/jira/browse/QPID-3002)
 - Transactions
 - Undeliverable message handling

</div>

## Documentation

<div class="two-column" markdown="1">

 - [C++ broker book]({{current_cpp_release_url}}/cpp-broker/book/index.html)
 - [Managing the C++ broker]({{current_cpp_release_url}}/cpp-broker/book/chapter-Managing-CPP-Broker.html#section-Managing-CPP-Broker)
 - [Installing Qpid C++](https://raw.githubusercontent.com/apache/qpid-cpp/master/INSTALL.txt)
 - [Qpid extensions to AMQP](https://cwiki.apache.org/confluence/display/qpid/qpid+extensions+to+amqp)

</div>
</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - {{current_cpp_release_link}}
 - [Past releases]({{site_url}}/releases/index.html#past-releases)

## Issues

 - [Report a bug](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12310520&issuetype=1&priority=3)
 - [Request an improvement](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12310520&issuetype=4&priority=3)
 - <form id="-jira-goto-form">Go to issue <input name="jira" value="QPID-"/></form>
 - [JIRA project page](https://issues.apache.org/jira/browse/QPID)

## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-cpp)
 - [Git clone URL](https://gitbox.apache.org/repos/asf/qpid-cpp.git)

## Resources

 - [Security](security.html)
 - [Qpid extensions to AMQP](https://cwiki.apache.org/confluence/display/qpid/qpid+extensions+to+amqp)

</div>
