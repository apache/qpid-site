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

# Qpid WCF

A [Windows Communication
Foundation](http://msdn.microsoft.com/en-us/library/ms731082.aspx)
channel implementation that speaks AMQP.

  - *Languages* - .NET
  - *Platforms* - Windows
  - *AMQP versions* - 0-10
  - *Downloads* - [qpid-wcf-0.28.zip](http://archive.apache.org/dist/qpid/0.28/qpid-wcf-0.28.zip) \[[ASC](http://archive.apache.org/dist/qpid/0.28/qpid-wcf-0.28.zip.asc), [SHA1](http://archive.apache.org/dist/qpid/0.28/SHA1SUM)]
  - *Source location* -  <http://svn.apache.org/repos/asf/qpid/trunk/qpid/wcf/>

## Features

<div class="two-column" markdown="1">

 - WCF service model programming using one-way contracts
 - WCF channel model programming using `IInputChannel`- and `IOutputChannel`-based factories
 - WCF-to-WCF applications using SOAP message encoders
 - WCF-to-non-WCF applications using raw content encoders
 - [Secure connection via SSL]({{site_url}}/releases/qpid-0.28/programming/book/ch04s04.html)
 - [Full distributed transactions]({{site_url}}/releases/qpid-0.28/programming/book/ch04s05.html)
 - Programmatic access to AMQP message properties on WCF messages

</div>

## Documentation

This is the documentation for the last released version, 0.28.  You can
find previous versions with our
[past releases]({{site_url}}/releases/index.html#past-releases).

<div class="two-column" markdown="1">

 - [README](http://svn.apache.org/repos/asf/qpid/tags/0.28/qpid/wcf/ReadMe.txt)
 - [Using the Qpid WCF client]({{site_url}}/releases/qpid-0.28/programming/book/QpidWCF.html)
 - [API reference](http://msdn.microsoft.com/en-us/library/vstudio/ms735119\(v=vs.90\).aspx)
 - [Examples](http://svn.apache.org/repos/asf/qpid/tags/0.28/qpid/wcf/samples)

</div>

## Issues

For more information about finding and reporting bugs, see
[Qpid issues]({{site_url}}/issues.html).

<div class="indent">
  <form id="jira-search-form">
    <input type="hidden" name="jql" value="project = QPID and component = 'WCF/C++ Client' and text ~ '{}' order by updatedDate desc"/>
    <input type="text" name="text"/>
    <button type="submit">Search</button>
  </form>
</div>

<div class="two-column" markdown="1">

 - [Open bugs](http://issues.apache.org/jira/issues/?jql=resolution+%3D+EMPTY+and+issuetype+%3D+%22Bug%22+and+component+%3D+%22WCF%2FC%2B%2B+Client%22+and+project+%3D+%22QPID%22)
 - [Fixed bugs](http://issues.apache.org/jira/issues/?jql=resolution+%3D+%22Fixed%22+and+issuetype+%3D+%22Bug%22+and+component+%3D+%22WCF%2FC%2B%2B+Client%22+and+project+%3D+%22QPID%22)
 - [Requested enhancements](http://issues.apache.org/jira/issues/?jql=resolution+%3D+EMPTY+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+component+%3D+%22WCF%2FC%2B%2B+Client%22+and+project+%3D+%22QPID%22)
 - [Completed enhancements](http://issues.apache.org/jira/issues/?jql=resolution+%3D+%22Fixed%22+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+component+%3D+%22WCF%2FC%2B%2B+Client%22+and+project+%3D+%22QPID%22)
 - [Report a bug](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&priority=3&summary=[Enter%20a%20brief%20description]&components=12313020)
 - [Request an enhancement](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&priority=3&summary=[Enter%20a%20brief%20description]&components=12313020)
 - [Jira summary page](http://issues.apache.org/jira/browse/QPID/component/12313020)

</div>
