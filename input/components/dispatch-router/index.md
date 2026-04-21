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
**WARNING**: Qpid Dispatch has been retired and is no longer maintained. This page is for historic
reference and may be stale. No new features, bug fixes, or security updates will be provided.
</div>

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

 - [Dispatch router book]({{final_dispatch_release_url}}/user-guide/index.html)
 - [Installing Qpid Dispatch](https://gitbox.apache.org/repos/asf?p=qpid-dispatch.git;a=blob_plain;f=README.adoc;hb={{final_dispatch_release}})

</div>
<div class="column" markdown="1">

 - [qdrouterd]({{final_dispatch_release_url}}/man/qdrouterd.html) - Router daemon
 - [qdrouterd.conf]({{final_dispatch_release_url}}/man/qdrouterd.conf.html) - Daemon configuration
 - [qdstat]({{final_dispatch_release_url}}/man/qdstat.html) - Get router statistics
 - [qdmanage]({{final_dispatch_release_url}}/man/qdmanage.html) - Manage the router

</div>
</div>
</div>

<div id="-right-column" class="right-column-adjusted" markdown="1">

## Releases

 - [Archive](https://archive.apache.org/dist/qpid/dispatch/)

## Issues

 - [JIRA project page](http://issues.apache.org/jira/browse/DISPATCH)

## Source code

 - [Browse via GitHub](https://github.com/apache/qpid-dispatch)

## Resources

 - [Security](security.html)

</div>
