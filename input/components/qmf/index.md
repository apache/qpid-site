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

# QMF

The Qpid Management Framework is a general-purpose management bus
built on Qpid messaging. It takes advantage of the scalability,
security, and rich capabilities of Qpid to provide flexible and
easy-to-use manageability to a large set of applications.

  - *Languages* - C++, Python
  - *Platforms* - Linux
  - *AMQP versions* - 0-10
  - *Downloads* - [qpid-cpp-{{current_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/{{current_release}}/qpid-cpp-{{current_release}}.tar.gz) \[[ASC](http://www.apache.org/dist/qpid/{{current_release}}/qpid-cpp-{{current_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/{{current_release}}/qpid-cpp-{{current_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/{{current_release}}/qpid-cpp-{{current_release}}.tar.gz.sha1)], [qpid-qmf-{{current_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/{{current_release}}/qpid-qmf-{{current_release}}.tar.gz) \[[ASC](http://www.apache.org/dist/qpid/{{current_release}}/qpid-qmf-{{current_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/{{current_release}}/qpid-qmf-{{current_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/{{current_release}}/qpid-qmf-{{current_release}}.tar.gz.sha1)]
  - *Source location* -  <http://svn.apache.org/repos/asf/qpid/trunk/qpid/cpp/>,<br/> <http://svn.apache.org/repos/asf/qpid/trunk/qpid/extras/qmf/>

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases]({{site_url}}/releases/index.html#past-releases).

<div class="two-column" markdown="1">

 - [Introduction]({{current_release_url}}/cpp-broker/book/ch02s02.html)
 - [C++ API reference]({{current_release_url}}/qmf/cpp/api/index.html)
 - [C++ examples]({{current_release_url}}/qmf/cpp/examples/index.html)
 - [Python examples]({{current_release_url}}/qmf/python/examples/index.html)
 - [Ruby examples]({{current_release_url}}/qmf/ruby/examples/index.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/{{current_release}}/qpid/cpp/INSTALL)
 - [Map message protocol](https://cwiki.apache.org/confluence/display/qpid/qmf+map+message+protocol)

</div>

## Issues

For more information about finding and reporting bugs, see
[Qpid issues]({{site_url}}/issues.html).

<form id="jira-search-form">
  <input type="hidden" name="jql" value="project = QPID and component = 'Qpid Managment Framework' and text ~ '{}' order by updatedDate desc"/>
  <input type="text" name="text"/>
  <button type="submit">Search</button>
</form>

<div class="two-column" markdown="1">

 - [Open bugs](http://issues.apache.org/jira/issues/?jql=resolution+%3D+EMPTY+and+issuetype+%3D+%22Bug%22+and+component+%3D+%22Qpid+Managment+Framework%22+and+project+%3D+%22QPID%22)
 - [Fixed bugs](http://issues.apache.org/jira/issues/?jql=resolution+%3D+%22Fixed%22+and+issuetype+%3D+%22Bug%22+and+component+%3D+%22Qpid+Managment+Framework%22+and+project+%3D+%22QPID%22)
 - [Requested enhancements](http://issues.apache.org/jira/issues/?jql=resolution+%3D+EMPTY+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+component+%3D+%22Qpid+Managment+Framework%22+and+project+%3D+%22QPID%22)
 - [Completed enhancements](http://issues.apache.org/jira/issues/?jql=resolution+%3D+%22Fixed%22+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+component+%3D+%22Qpid+Managment+Framework%22+and+project+%3D+%22QPID%22)
 - [Report a bug](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&priority=3&summary=[Enter%20a%20brief%20description]&components=12312536)
 - [Request an enhancement](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&priority=3&summary=[Enter%20a%20brief%20description]&components=12312536)
 - [Jira summary page](http://issues.apache.org/jira/browse/QPID/component/12312536)

</div>
