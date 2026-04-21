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

<div class="retired-component" markdown="1">
**WARNING**: Qpid C++ has been retired and is no longer maintained. This page is for historic
reference and may be stale. No new features, bug fixes, or security updates will be provided.
</div>

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
 - [High availability]({{final_cpp_release_url}}/cpp-broker/book/chapter-ha.html)
 - [Message groups]({{final_cpp_release_url}}/cpp-broker/book/Using-message-groups.html)
 - Message TTLs and arrival timestamps
 - Pluggable persistence
 - [Pluggable authentication via SASL]({{final_cpp_release_url}}/cpp-broker/book/chap-Messaging_User_Guide-Security.html)
 - [Producer flow control]({{final_cpp_release_url}}/cpp-broker/book/producer-flow-control.html)
 - [Queue replication]({{final_cpp_release_url}}/cpp-broker/book/ha-queue-replication.html)
 - Resource limits
 - Secure connection via SSL
 - [Server-side selectors](https://issues.apache.org/jira/browse/QPID-4558?focusedCommentId=13592659&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-13592659)
 - Specialized queueing with [last value queue]({{final_cpp_release_url}}/cpp-broker/book/ch01s06.html), priority queue, and ring queue
 - [Threshold alerts](https://issues.apache.org/jira/browse/QPID-3002)
 - Transactions
 - Undeliverable message handling

</div>

## Documentation

This is the documentation for the final released version.

<div class="two-column" markdown="1">

 - [C++ broker book]({{final_cpp_release_url}}/cpp-broker/book/index.html)
 - [Managing the C++ broker]({{final_cpp_release_url}}/cpp-broker/book/chapter-Managing-CPP-Broker.html#section-Managing-CPP-Broker)
 - [Installing Qpid C++](https://raw.githubusercontent.com/apache/qpid-cpp/{{final_cpp_release}}/INSTALL.txt)

</div>
</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - [Archive](https://archive.apache.org/dist/qpid/cpp/)

## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-cpp)

## Resources

 - [Security](security.html)
 - [Qpid extensions to AMQP](https://cwiki.apache.org/confluence/display/qpid/qpid+extensions+to+amqp)

</div>
