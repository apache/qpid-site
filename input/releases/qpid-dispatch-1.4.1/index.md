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

# Qpid Dispatch 1.4.1

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

## Downloads

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of
the files you download.

| Content | Download | Verify |
|---------|----------|--------|
| Dispatch router | [qpid-dispatch-1.4.1.tar.gz](http://archive.apache.org/dist/qpid/dispatch/1.4.1/qpid-dispatch-1.4.1.tar.gz) | [ASC](https://archive.apache.org/dist/qpid/dispatch/1.4.1/qpid-dispatch-1.4.1.tar.gz.asc), [SHA512](https://archive.apache.org/dist/qpid/dispatch/1.4.1/qpid-dispatch-1.4.1.tar.gz.sha512) |

## Documentation


<div class="two-column" markdown="1">

 - [Using Qpid Dispatch](user-guide/index.html)
 - [Installing Qpid Dispatch from
   source](https://gitbox.apache.org/repos/asf?p=qpid-dispatch.git;a=blob_plain;f=README;hb=1.4.1)
 - [qdrouterd](man/qdrouterd.html) - Router daemon
 - [qdrouterd.conf](man/qdrouterd.conf.html) - Daemon configuration
 - [qdstat](man/qdstat.html) - Get router statistics
 - [qdmanage](man/qdmanage.html) - Manage the router

</div>


## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/dispatch/1.4.1)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+DISPATCH+AND+fixVersion+%3D+%271.4.1%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](https://gitbox.apache.org/repos/asf/qpid-dispatch.git/tree/refs/tags/1.4.1)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("1.4.1" === "{{current_dispatch_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>