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

# Proton-J/Proton-C

If you're new to proton development, you might be wondering why there
are two apparently independent projects (proton-c and proton-j) that
share the same git repo and release cycle.

These projects aren't actually quite as independent as they look.
There is a common test suite that runs against both implementations to
help keep them in sync with each other. This is the python test suite
that lives underneath the top level [tests/python](https://git-wip-us.apache.org/repos/asf?p=qpid-proton.git;a=tree;f=tests/python)
directory. These tests have been integrated into the maven build via
jython so that the whole java build looks like a normal maven build
and java developers don't need to deal with cmake or getting jython
themselves or anything that's outside of the normal java experience.

Likewise, the cmake build will detect if java is unavailable and opt
out of building the java code, so it's easy for C developers to
pretend that Java doesn't exist. It also does this for all the
different bindings, e.g. if perl or ruby isn't installed it will not
attempt to build them.

As a core proton developer, it's a good idea to make a point of having
all the optional stuff enabled. This will ensure that you are testing
any of your changes against the widest range of code possible.

It's also good to be aware of exactly how the common test suite
integrates with both proton-c and proton-j. The python binding
actually consists of a hand written wrapper layer that encapsulates
the raw swig generated API. The raw swig API is actually much lower
level and is available in the 'cproton' module. When you run the
python test suite in jython, the swig generated cproton doesn't
actually exist since it is a C module. Instead, you get the cproton.py
that resides in the java source tree underneath
[proton-j/src/main/resources](https://git-wip-us.apache.org/repos/asf?p=qpid-proton.git;a=tree;f=proton-j/src/main/resources).
This cproton.py and its dependent files serve as a shim that adapts
between the Java API and the C API. These files can actually be quite
handy as a reference for how to translate a given idiom from proton-j
into proton-c or vice versa.

You might notice some parts of the shim are stubbed out, e.g. like
this:


    def pn_flowcontroller(window):
        raise Skipped()

Throwing a Skipped exception will signal to the test runner that
whatever code is being called is not available, and the test will be
reported as "skipped" rather than flagged as an error.
