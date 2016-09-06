# Dashboard

<div id="-dashboard-forms" class="feature">
  <form id="-jira-goto-form">
    Go to <span class="accesskey">i</span>ssue <input name="jira" accesskey="i" autofocus="autofocus" tabindex="1"/>
  </form>

  <form id="-viewvc-goto-form" action="http://svn.apache.org/viewvc" method="get">
    <input type="hidden" name="view" value="revision"/>
    Go to <span class="accesskey">r</span>evision <input type="text" name="revision" accesskey="r" tabindex="2"/>
  </form>

  <form id="-jira-search-form">
    <span class="accesskey">S</span>earch issues <input name="text" type="text" accesskey="s" tabindex="3"/>
  </form>
</div>

### Source modules

<div id="-source-modules" class="scroll" markdown="1">

| Module | Issues | Test builds | Source code |
| ------ | ------ | ----------- | ----------- |
| [C++]({{site_url}}/components/cpp-broker/index.html) | [Open issues](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPID%20AND%20resolution%20%3D%20Unresolved%20AND%20component%20in%20\(%22C%2B%2B%20Broker%22%2C%20%22C%2B%2B%20Client%22%2C%20%22C%2B%2B%20Clustering%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Tools%22%2C%20%22Qpid%20Managment%20Framework%22%2C%20%22Ruby%20Client%22\)%20ORDER%20BY%20priority%20DESC) &#x2014; [New bug](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&components=12311395&components=12311396&summary=[Enter%20a%20brief%20description]&priority=3) &#x2014; [New improvement](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&components=12311395&components=12311396&summary=[Enter%20a%20brief%20description]&priority=3) | [Linux](https://builds.apache.org/view/M-R/view/Qpid/job/Qpid-cpp-trunk-test/) | [Git](https://git-wip-us.apache.org/repos/asf/qpid-cpp.git), [GitHub mirror](https://github.com/apache/qpid-cpp) |
| [Java]({{site_url}}/components/java-broker/index.html) | [Open issues](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPID%20AND%20resolution%20%3D%20Unresolved%20AND%20component%20in%20\(%22Java%20Broker%22%2C%20%22Java%20Client%22%2C%20%22Java%20Common%22%2C%20%22Java%20Management%20%3A%20JMX%20Console%22%2C%20%22Java%20Performance%20Tests%22%2C%20%22Java%20Tests%22%2C%20%22Java%20Tools%22%2C%20JCA\)%20ORDER%20BY%20priority%20DESC) &#x2014; [New bug](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&components=12311388&components=12311389&summary=[Enter%20a%20brief%20description]&priority=3) &#x2014; [New improvement](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&components=12311388&components=12311389&summary=[Enter%20a%20brief%20description]&priority=3) | [Java 7](https://builds.apache.org/view/M-R/view/Qpid/job/Qpid-Java-Java-Test-IBMJDK1.7/), [Java 8](https://builds.apache.org/view/M-R/view/Qpid/job/Qpid-Java-Java-Test-JDK1.8/) | [Subversion](https://svn.apache.org/repos/asf/qpid/java/trunk), [GitHub mirror](https://github.com/apache/qpid-java) |
| [Python]({{site_url}}/components/messaging-api/index.html) | [Open issues](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPID%20AND%20resolution%20%3D%20Unresolved%20AND%20component%20in%20\(%22Python%20Client%22%2C%20%22Python%20Test%20Suite%22\)%20ORDER%20BY%20priority%20DESC) &#x2014; [New bug](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&components=12311544&summary=[Enter%20a%20brief%20description]&priority=3) &#x2014; [New improvement](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&components=12311544&summary=[Enter%20a%20brief%20description]&priority=3) | - | [Git](https://git-wip-us.apache.org/repos/asf/qpid-python.git), [GitHub mirror](https://github.com/apache/qpid-python) |
| [Dispatch]({{site_url}}/components/dispatch-router/index.html) | [Open issues](https://issues.apache.org/jira/issues/?jql=project%20%3D%20DISPATCH%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC) &#x2014; [New bug](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12315321&issuetype=1&summary=[Enter%20a%20brief%20description]&priority=3) &#x2014; [New improvement](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12315321&issuetype=4&summary=[Enter%20a%20brief%20description]&priority=3) | - | [Git](https://git-wip-us.apache.org/repos/asf/qpid-dispatch.git), [GitHub mirror](https://github.com/apache/qpid-dispatch) |
| [JMS]({{site_url}}/components/jms/index.html) | [Open issues](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPIDJMS%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC) &#x2014; [New bug](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12314524&issuetype=1&summary=[Enter%20a%20brief%20description]&priority=3) &#x2014; [New improvement](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12314524&issuetype=4&summary=[Enter%20a%20brief%20description]&priority=3) | [Java 7](https://builds.apache.org/view/M-R/view/Qpid/job/Qpid-JMS-Test-JDK7/), [Java 8](https://builds.apache.org/view/M-R/view/Qpid/job/Qpid-JMS-Test-JDK8/) | [Git](https://git-wip-us.apache.org/repos/asf/qpid-jms.git), [GitHub mirror](https://github.com/apache/qpid-jms) |
| [Proton]({{site_url}}/proton/index.html) | [Open issues](https://issues.apache.org/jira/issues/?jql=project%20%3D%20PROTON%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC) &#x2014; [New bug](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12313720&issuetype=1&summary=[Enter%20a%20brief%20description]&priority=3) &#x2014; [New improvement](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12313720&issuetype=4&summary=[Enter%20a%20brief%20description]&priority=3) | [C](https://builds.apache.org/view/M-R/view/Qpid/job/Qpid-proton-c/), [Java](https://builds.apache.org/view/M-R/view/Qpid/job/Qpid-proton-j/) | [Git](https://git-wip-us.apache.org/repos/asf/qpid-proton.git), [GitHub mirror](https://github.com/apache/qpid-proton) |
| [Website](https://git-wip-us.apache.org/repos/asf?p=qpid-site.git;a=blob_plain;f=README.md;hb=HEAD) | [Open issues](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPID%20AND%20resolution%20%3D%20Unresolved%20AND%20component%20%3D%20Website%20ORDER%20BY%20priority%20DESC) &#x2014; [New bug](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&components=12312307&summary=[Enter%20a%20brief%20description]&priority=3) &#x2014; [New improvement](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&components=12312307&summary=[Enter%20a%20brief%20description]&priority=3) | - | [Git](https://git-wip-us.apache.org/repos/asf/qpid-site.git) |

</div>

---

<section id="-dashboard-links" class="flex" markdown="1">
<section markdown="1">

### Issues

 - [Your assigned issues](https://issues.apache.org/jira/issues/?filter=-1)
 - [Your reported issues](https://issues.apache.org/jira/issues/?filter=-2)
 - [Your recent issues](https://issues.apache.org/jira/issues/?filter=-3)

</section>
<section markdown="1">

### List archives

 - [Users](http://qpid.2158936.n2.nabble.com/Apache-Qpid-users-f2158936.html)
 - [Developers](http://qpid.2158936.n2.nabble.com/Apache-Qpid-developers-f7254403.html)
 - [Commits](http://qpid.2158936.n2.nabble.com/Apache-Qpid-commits-f7106555.html)
 - [Notifications](http://mail-archives.apache.org/mod_mbox/qpid-notifications/)

</section>
<section markdown="1">

### Apache services

 - [Qpid at Jenkins](https://builds.apache.org/view/M-R/view/Qpid/)
 - [Qpid at Review Board](https://reviews.apache.org/groups/qpid/)
 - [URI shortener](http://s.apache.org/)
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
 - [Devel snapshots]({{site_url}}/releases/index.html#development-snapshots)

</section>
</section>
