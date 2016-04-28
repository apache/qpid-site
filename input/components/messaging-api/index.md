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

# Qpid Messaging API

A connection-oriented messaging API that supports many languages and
platforms.

  - *Languages* - C++, Perl, Python, Ruby, .NET
  - *Platforms* - Linux, Windows
  - *AMQP versions* - 1.0, 0-10
  - *Downloads* - C++, bindings: [qpid-cpp-{{current_cpp_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz) \[[ASC](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/cpp/{{current_cpp_release}}/qpid-cpp-{{current_cpp_release}}.tar.gz.sha1)],<br/>Python: [qpid-python-{{current_release}}.tar.gz](http://www.apache.org/dyn/closer.lua/qpid/{{current_release}}/qpid-python-{{current_release}}.tar.gz) \[[ASC](http://www.apache.org/dist/qpid/{{current_release}}/qpid-python-{{current_release}}.tar.gz.asc), [MD5](http://www.apache.org/dist/qpid/{{current_release}}/qpid-python-{{current_release}}.tar.gz.md5), [SHA1](http://www.apache.org/dist/qpid/{{current_release}}/qpid-python-{{current_release}}.tar.gz.sha1)]
  - *Source location* -  <http://svn.apache.org/repos/asf/qpid/trunk/qpid/cpp/>,<br/> <http://svn.apache.org/repos/asf/qpid/trunk/qpid/python/>

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases]({{site_url}}/releases/index.html#past-releases).

<div class="two-column" markdown="1">

 - [Using the Qpid Messaging API]({{current_release_url}}/programming/book/ch02.html)
 - [C++ API reference]({{current_release_url}}/messaging-api/cpp/api/index.html)
 - [C++ examples]({{current_release_url}}/messaging-api/cpp/examples/index.html)
 - [Perl examples]({{current_release_url}}/messaging-api/perl/examples/index.html)
 - [Python API reference]({{current_release_url}}/messaging-api/python/api/index.html)
 - [Python examples]({{current_release_url}}/messaging-api/python/examples/index.html)
 - [Ruby API reference]({{current_release_url}}/messaging-api/ruby/api/index.html)
 - [Ruby examples]({{current_release_url}}/messaging-api/ruby/examples/index.html)
 - [The .NET Binding for the C++ Messaging Client]({{current_release_url}}/programming/book/ch05.html)
 - [.NET API reference]({{current_release_url}}/messaging-api/dotnet/api/index.html)
 - [.NET examples]({{current_release_url}}/messaging-api/dotnet/examples/index.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/{{current_release}}/qpid/cpp/INSTALL)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/tags/{{current_release}}/qpid/python/README.txt)
 - [Installing the Ruby Messaging API](http://svn.apache.org/repos/asf/qpid/tags/{{current_release}}/qpid/cpp/bindings/qpid/ruby/README.rdoc)
 - [Installing the .NET Messaging API](http://svn.apache.org/repos/asf/qpid/tags/{{current_release}}/qpid/cpp/bindings/qpid/dotnet/ReadMe.txt)

</div>

### Examples

  | Language | Hello World | Client | Server | Spout | Drain |
  | - | - | - | - | - | - |
  | *C++* | [hello_world.cpp]({{current_release_url}}/messaging-api/cpp/examples/hello_world.cpp.html) | [client.cpp]({{current_release_url}}/messaging-api/cpp/examples/client.cpp.html) | [server.cpp]({{current_release_url}}/messaging-api/cpp/examples/server.cpp.html) | [spout.cpp]({{current_release_url}}/messaging-api/cpp/examples/spout.cpp.html) | [drain.cpp]({{current_release_url}}/messaging-api/cpp/examples/drain.cpp.html) |
  | *Perl* | [hello_world.pl]({{current_release_url}}/messaging-api/perl/examples/hello_world.pl.html) | [client.pl]({{current_release_url}}/messaging-api/perl/examples/client.pl.html) | [server.pl]({{current_release_url}}/messaging-api/perl/examples/server.pl.html) | [spout.pl]({{current_release_url}}/messaging-api/perl/examples/spout.pl.html) | [drain.pl]({{current_release_url}}/messaging-api/perl/examples/drain.pl.html) |
  | *Python* | [hello]({{current_release_url}}/messaging-api/python/examples/hello.html) |  | [server]({{current_release_url}}/messaging-api/python/examples/server.html) | [spout]({{current_release_url}}/messaging-api/python/examples/spout.html) | [drain]({{current_release_url}}/messaging-api/python/examples/drain.html) |
  | *Ruby* | [hello_world.rb]({{current_release_url}}/messaging-api/ruby/examples/hello_world.rb.html) | [client.rb]({{current_release_url}}/messaging-api/ruby/examples/client.rb.html) | [server.rb]({{current_release_url}}/messaging-api/ruby/examples/server.rb.html) | [spout.rb]({{current_release_url}}/messaging-api/ruby/examples/spout.rb.html) | [drain.rb]({{current_release_url}}/messaging-api/ruby/examples/drain.rb.html) |
  | *.NET* | [helloworld.cs]({{current_release_url}}/messaging-api/dotnet/examples/csharp.example.helloworld.cs.html) | [client.cs]({{current_release_url}}/messaging-api/dotnet/examples/csharp.example.client.cs.html) | [server.cs]({{current_release_url}}/messaging-api/dotnet/examples/csharp.example.server.cs.html) | [spout.cs]({{current_release_url}}/messaging-api/dotnet/examples/csharp.example.spout.cs.html) | [drain.cs]({{current_release_url}}/messaging-api/dotnet/examples/csharp.example.drain.cs.html) |

## Issues

For more information about finding and reporting bugs, see
[Qpid issues]({{site_url}}/issues.html).

<form id="jira-search-form">
  <input type="hidden" name="jql" value="project = QPID and component in ('C++ Client', 'Dot Net Client', 'Perl Client', 'Python Client', 'Ruby Client') and text ~ '{}' order by updatedDate desc"/>
  <input type="text" name="text"/>
  <button type="submit">Search</button>
</form>

<div class="two-column" markdown="1">

 - [Open bugs](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20EMPTY%20and%20issuetype%20%3D%20%22Bug%22%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Fixed bugs](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20Fixed%20and%20issuetype%20%3D%20%22Bug%22%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Requested enhancements](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20EMPTY%20and%20issuetype%20in%20\(%22New%20Feature%22%2C%20%22Improvement%22\)%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Completed enhancements](https://issues.apache.org/jira/issues/?jql=resolution%20%3D%20Fixed%20and%20issuetype%20in%20\(%22New%20Feature%22%2C%20%22Improvement%22\)%20and%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20and%20project%20%3D%20%22QPID%22)
 - [Report a bug](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=1&priority=3&summary=[Enter%20a%20brief%20description]&components=12311396)
 - [Request an enhancement](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310520&issuetype=4&priority=3&summary=[Enter%20a%20brief%20description]&components=12311396)
 - [Jira summary page](http://issues.apache.org/jira/browse/QPID/component/12311396)

</div>
