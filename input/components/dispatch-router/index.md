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

# Dispatch Router

<div class="feature" markdown="1">

A high-performance, lightweight AMQP 1.0 message router, written in C
and built on [Qpid Proton]({{site_url}}/proton/index.html). It provides
flexible and scalable interconnect between any AMQP endpoints, whether
they be clients, brokers or other AMQP-enabled services.  More about
[Dispatch Router](overview.html).

</div>

## Features

 - Arbitrary topology - redundancy without restrictions
 - Automatic re-routing when topology changes
 - Configurable addressing semantics
 - Run-time configuration and query via management tools
 - Full support for the draft AMQP management specification

## Documentation

<div class="two-column" markdown="1">
<div class="column" markdown="1">

 - [Dispatch router book]({{current_dispatch_release_url}}/book/book.html)
 - [Installing Qpid Dispatch](https://git-wip-us.apache.org/repos/asf?p=qpid-dispatch.git;a=blob_plain;f=README;hb={{current_dispatch_release}})

</div>
<div class="column" markdown="1">

 - [qdrouterd]({{current_dispatch_release_url}}/man/qdrouterd.html) - Router daemon
 - [qdrouterd.conf]({{current_dispatch_release_url}}/man/qdrouterd.conf.html) - Daemon configuration
 - [qdstat]({{current_dispatch_release_url}}/man/qdstat.html) - Get router statistics
 - [qdmanage]({{current_dispatch_release_url}}/man/qdmanage.html) - Manage the router

</div>
</div>
</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - {{current_dispatch_release_link}}
 - [Past releases]({{site_url}}/releases/index.html#past-releases)
 - [Work in progress]({{site_url}}/releases/qpid-dispatch-master/index.html)

## Issues

 - [Report a bug](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12315321&issuetype=1&priority=3)
 - [Request an improvement](https://issues.apache.org/jira/secure/CreateIssue.jspa?pid=12315321&issuetype=4&priority=3)
 - <form id="-jira-goto-form">Go to issue <input name="jira" value="DISPATCH-"/></form>
 - [JIRA project page](http://issues.apache.org/jira/browse/DISPATCH)

## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-dispatch)
 - [Git clone URL](https://git-wip-us.apache.org/repos/asf/qpid-dispatch.git)

</div>
