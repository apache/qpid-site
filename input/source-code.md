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

# Source Code

Qpid employs
[revision control](http://en.wikipedia.org/wiki/Revision_control) to
track and manage changes to its source code.


## Browse the code

The [Dashboard]({{site_url}}/dashboard.html) page provides links to the
repository for each individual component. The repositories are all directly
viewable, and GitHub mirrors are additionally provided for each.

## Check out the code

To access code from one of the Git repositories, use the `git clone` command
with its URL, e.g for Qpid JMS:

    Qpid JMS
    % git clone https://git-wip-us.apache.org/repos/asf/qpid-jms.git qpid-jms

Alternatively, you can use the mirror repositories available on GitHub to
create your own fork.

To access code from a Subversion repository, use the `svn checkout` command
with its URL, .e.g for Qpid for Java:

    Qpid for Java
    % svn checkout http://svn.apache.org/repos/asf/qpid/java/trunk qpid-java

## Install the code

Consult the install documentation below, or see the respective component
documentation for more details.

 - [How to build Qpid for Java](https://cwiki.apache.org/confluence/display/qpid/qpid+java+build+how+to)
 - [Installing Qpid C++](https://git-wip-us.apache.org/repos/asf?p=qpid-cpp.git;a=blob_plain;f=INSTALL.txt)
 - [Installing Qpid Python](https://git-wip-us.apache.org/repos/asf?p=qpid-python.git;a=blob_plain;f=README.md)

## Notifications

The traffic on these lists is automatically generated.  Please do not
post any messages to them.

To subscribe, send an email with subject "subscribe" to the subscribe
address.  To unsubscribe, send "unsubscribe" to the unsubscribe
address.

### Commits list

Alerts for changes committed to the Qpid source.  

 - Send "subscribe" to <commits-subscribe@qpid.apache.org>
 - Send "unsubscribe" to <commits-unsubscribe@qpid.apache.org>
 - [List information](http://mail-archives.apache.org/mod_mbox/qpid-commits/)
 - [Archive](http://qpid.2158936.n2.nabble.com/Apache-Qpid-commits-f7106555.html)
 - [News feed](http://mail-archives.apache.org/mod_mbox/qpid-commits/?format=atom)

### Notifications list

Alerts for build and test failures from our continuous integration
servers.

 - Send "subscribe" to <notifications-subscribe@qpid.apache.org>
 - Send "unsubscribe" to <notifications-unsubscribe@qpid.apache.org>
 - [List information](http://mail-archives.apache.org/mod_mbox/qpid-notifications/)
 - [News feed](http://mail-archives.apache.org/mod_mbox/qpid-notifications/?format=atom)

## More information

 - [Subversion project](http://subversion.apache.org/)
 - [Subversion manual](http://svnbook.red-bean.com/)
 - [Subversion at Apache](http://www.apache.org/dev/version-control.html)
 - [Git project](http://git-scm.com)
 - [Git documentation](http://git-scm.com/documentation)
 - [Git at Apache](http://www.apache.org/dev/git.html)
 - [Jenkins project](http://jenkins-ci.org/)
 - [Jenkins documentation](https://wiki.jenkins-ci.org/display/JENKINS/Meet+Jenkins)
 - [Continuous integration at Apache](http://ci.apache.org/)
