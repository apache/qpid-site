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

<div id="-dashboard-forms">
  <form id="-jira-goto-form">
    Go to <span class="accesskey">i</span>ssue <input name="jira" accesskey="i" autofocus="autofocus" tabindex="1"/>
  </form>

  <form id="-jira-search-form">
    <span class="accesskey">S</span>earch issues <input name="text" type="text" accesskey="s" tabindex="3"/>
  </form>
</div>

# Dashboard

<div id="-source-modules" class="scroll" markdown="1">

| Module | Release | Issues | Tests | Source code |
| ------ | ------- | ------ | ----- | ----------- |
| [Qpid Broker-J]({{site_url}}/components/broker-j/index.html)               | {{broker_j_release.brief_link}} | {{dashboard_asf_jira_links("QPID", 12310520, ["Broker-J", "Java Build", "Java Documentation", "Java Performance Tests", "Java Tests", "Java Tools"])}} | {{travis_ci_badge("apache", "qpid-broker-j")}}  | {{dashboard_asf_git_links("qpid-broker-j")}} |
| [Qpid C++](https://github.com/apache/qpid-cpp/blob/main/README.md)       | {{cpp_release.brief_link}} | {{dashboard_asf_jira_links("QPID", 12310520, ["C++ Broker", "C++ Build", "C++ Client", "C++ Clustering", "C++ Documentation", "C++ Tests", "C++ Tools", ".NET Client", "Perl Client", "Python Client (Wrapped)", "QMF", "Ruby Client"])}} | {{asf_jenkins_badge("Qpid-CPP-Test")}} {{appveyor_ci_badge("ApacheSoftwareFoundation", "qpid-cpp", "wma611lkq1fcyo18")}} | {{dashboard_asf_git_links("qpid-cpp")}} |
| [Qpid Dispatch]({{site_url}}/components/dispatch-router/index.html)        | {{dispatch_release.brief_link}} | {{dashboard_asf_jira_links("DISPATCH", 12315321)}} | {{travis_ci_badge("apache", "qpid-dispatch")}} | {{dashboard_asf_git_links("qpid-dispatch")}} |
| [Qpid Interop Test]({{site_url}}/components/interop-test/index.html)       | {{interop_test_release.brief_link}} | {{dashboard_asf_jira_links("QPIDIT", 12318621)}} | - | {{dashboard_asf_git_links("qpid-interop-test")}} |
| [Qpid JMS]({{site_url}}/components/jms/index.html)                         | {{jms_release.brief_link}} | {{dashboard_asf_jira_links("QPIDJMS", 12314524)}} | {{asf_jenkins_badge("Qpid-JMS-Test-JDK11")}} {{travis_ci_badge("apache", "qpid-jms")}} {{asf_jenkins_badge("Qpid-JMS-Test-JDK11-Windows")}} | {{dashboard_asf_git_links("qpid-jms")}} |
| [Qpid JMS AMQP 0-x]({{site_url}}/components/jms/amqp-0-x.html)             | {{jms_amqp_0_x_release.brief_link}} | {{dashboard_asf_jira_links("QPID", 12310520, ["JMS AMQP 0-x"])}} | <a href="https://builds.apache.org/job/Qpid/job/Qpid-JMS-AMQP-0-x-Broker-J-TestMatrix"><img src="https://builds.apache.org/buildStatus/icon?job=Qpid/Qpid-JMS-AMQP-0-x-Broker-J-TestMatrix" height="20"/></a> | {{dashboard_asf_git_links("qpid-jms-amqp-0-x")}} |
| [Qpid Proton-J]({{site_url}}/proton/index.html)                            | {{proton_j_release.brief_link}} | {{dashboard_asf_jira_links("PROTON", 12313720, ["proton-j"])}} | {{asf_jenkins_badge("Qpid-Proton-J-JDK8")}} {{travis_ci_badge("apache", "qpid-proton-j")}} | {{dashboard_asf_git_links("qpid-proton-j")}} |
| [Qpid Proton]({{site_url}}/proton/index.html)                              | {{proton_release.brief_link}} | {{dashboard_asf_jira_links("PROTON", 12313720)}} | {{asf_jenkins_badge("Qpid-Proton-C")}} {{travis_ci_badge("apache", "qpid-proton")}} | {{dashboard_asf_git_links("qpid-proton")}} |
| [Qpid Python](https://github.com/apache/qpid-python/blob/main/README.md) | {{python_release.brief_link}} | {{dashboard_asf_jira_links("QPID", 12310520, ["Python Client", "Python Examples", "Python Test Suite"])}} | - | {{dashboard_asf_git_links("qpid-python")}} |
| [Qpid Site](https://github.com/apache/qpid-site/blob/asf-site/README.md)   | - | {{dashboard_asf_jira_links("QPID", 12310520, ["Website"])}} | {{travis_ci_badge("apache", "qpid-site", "asf-site")}} | {{dashboard_asf_git_links("qpid-site")}} |

</div>

---

<section id="-dashboard-links" class="flex" markdown="1">
<section markdown="1">

### Issues

 - [Your assigned issues](https://issues.apache.org/jira/issues/?filter=-1)
 - [Your reported issues](https://issues.apache.org/jira/issues/?filter=-2)
 - [Your recent issues](https://issues.apache.org/jira/issues/?filter=-3)
 - [All Qpid issues](https://issues.apache.org/jira/issues/?jql=project%20in%20\(QPID%2C%20QPIDIT%2C%20QPIDJMS%2C%20PROTON%2C%20DISPATCH\))

</section>
<section markdown="1">

### List archives

 - [Users](https://lists.apache.org/list.html?users@qpid.apache.org)
 - [Developers](https://lists.apache.org/list.html?dev@qpid.apache.org)
 - [Commits](https://lists.apache.org/list.html?commits@qpid.apache.org)
 - [Notifications](https://lists.apache.org/list.html?notifications@qpid.apache.org)

</section>
<section markdown="1">

### Apache services

 - [Qpid at Jenkins](https://builds.apache.org/view/M-R/view/Qpid/)
 - [Qpid at Review Board](https://reviews.apache.org/groups/qpid/)
 - [URL shortener](http://s.apache.org/)
 - [Pastebin](https://paste.apache.org/)

</section>
<section markdown="1">

### Wiki

 - [Index](https://cwiki.apache.org/confluence/display/qpid/Index)
 - [Developer pages](https://cwiki.apache.org/confluence/display/qpid/developer+pages)
 - [Documentation](https://cwiki.apache.org/confluence/display/qpid/documentation)
 - [Releases](https://cwiki.apache.org/confluence/display/qpid/Releases)

</section>
<section markdown="1">

### More

 - [Components]({{site_url}}/components/index.html)
 - [Releases]({{site_url}}/releases/index.html)

</section>
</section>
