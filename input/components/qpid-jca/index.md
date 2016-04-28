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

# Qpid JCA

A
[Java EE Connector Architecture](http://en.wikipedia.org/wiki/Java_EE_Connector_Architecture)
1.5 compliant resource adapter that allows for JEE integration between
EE applications and AMQP 0-10 message brokers.

  - *Languages* - Java
  - *Platforms* - JVM
  - *AMQP versions* - 0-10
  - *Download* - [qpid-java-{{current_java_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz) \[[ASC](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/java/{{current_java_release}}/qpid-java-{{current_java_release}}.tar.gz.sha1)]
  - *Source location* -  <http://svn.apache.org/repos/asf/qpid/java/trunk/jca/>

## Features

<div class="two-column" markdown="1">

 - [JCA 1.5](http://jcp.org/en/jsr/detail?id=112) compliant
 - Outbound and inbound connectivity
 - Connects to [JBoss EAP](http://www.redhat.com/products/jbossenterprisemiddleware/application-platform/), [Geronimo](http://geronimo.apache.org/), and [Glassfish](https://glassfish.java.net/)
 - Supports binding to Swing and other non-managed clients

</div>

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases]({{site_url}}/releases/index.html#past-releases).

<div class="two-column" markdown="1">

 - [README](http://svn.apache.org/repos/asf/qpid/java/tags/{{current_java_release}}/jca/README.txt)
 - [Connect with JBoss EAP 5](http://svn.apache.org/repos/asf/qpid/java/tags/{{current_java_release}}/jca/README-JBOSS.txt)
 - [Connect with JBoss EAP 6](http://svn.apache.org/repos/asf/qpid/java/tags/{{current_java_release}}/jca/README-JBOSS-EAP6.txt)
 - [Connect with Geronimo](http://svn.apache.org/repos/asf/qpid/java/tags/{{current_java_release}}/jca/README-GERONIMO.txt)
 - [Connect with Glassfish](http://svn.apache.org/repos/asf/qpid/tags/{{current_java_release}}/qpid/java/jca/example/README-GLASSFISH.txt)
 - [Examples](http://svn.apache.org/repos/asf/qpid/java/tags/{{current_java_release}}/jca/example/)

</div>

## Issues

For more information about finding and reporting bugs, see
[Qpid issues]({{site_url}}/issues.html).

<div class="indent">
  <form id="jira-search-form">
    <input type="hidden" name="jql" value="project = QPID and component = JCA and text ~ '{}' order by updatedDate desc"/>
    <input type="text" name="text"/>
    <button type="submit">Search</button>
  </form>
</div>

<div class="two-column" markdown="1">

 - [Open bugs](http://issues.apache.org/jira/issues/?jql=resolution+%3D+EMPTY+and+component+%3D+%22JCA%22+and+project+%3D+%22QPID%22)
 - [Fixed bugs](http://issues.apache.org/jira/issues/?jql=resolution+%3D+%22Fixed%22+and+issuetype+%3D+%22Bug%22+and+component+%3D+%22JCA%22+and+project+%3D+%22QPID%22)
 - [Requested enhancements](http://issues.apache.org/jira/issues/?jql=resolution+%3D+EMPTY+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+component+%3D+%22JCA%22+and+project+%3D+%22QPID%22)
 - [Completed enhancements](http://issues.apache.org/jira/issues/?jql=resolution+%3D+%22Fixed%22+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+component+%3D+%22JCA%22+and+project+%3D+%22QPID%22)
 - [Report a bug](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&priority=3&summary=[Enter%20a%20brief%20description]&components=12317036)
 - [Request an enhancement](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&priority=3&summary=[Enter%20a%20brief%20description]&components=12317036)
 - [Jira summary page](http://issues.apache.org/jira/browse/QPID/component/12317036)

</div>
