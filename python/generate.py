#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import re
import urllib
import yaml

from pprint import pformat
from pygments import highlight as pygments_highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from xml.sax.saxutils import escape as escape_html

from plano import *
## General ##

def setup_release_script():
    if len(ARGS) not in (5, 6):
        exit("Usage: script RELEASE ISSUES_RELEASE SOURCE_RELEASE RELEASE-DIR [CHECKOUT-DIR]")

    notice("Setting up script '{}'", ARGS[0])

    release = ARGS[1]
    issues_release = ARGS[2]
    source_release = ARGS[3]
    release_dir = ARGS[4]

    try:
        checkout_dir = ARGS[5]
    except IndexError:
        checkout_dir = None

    assert release != ""
    assert issues_release != ""
    assert source_release != ""
    assert release_dir != ""
    assert checkout_dir is None or checkout_dir != ""

    call_and_print_on_error("asciidoc --version")
    call_and_print_on_error("asciidoctor --version")
    call_and_print_on_error("cmake --version")
    call_and_print_on_error("dot -V")
    call_and_print_on_error("doxygen --version")
    #call_and_print_on_error("epydoc --version")
    #call_and_print_on_error("fop -version")
    call_and_print_on_error("gcc --version")
    call_and_print_on_error("make --version")
    call_and_print_on_error("rdoc --version")
    call_and_print_on_error("which sphinx-build")
    call_and_print_on_error("svn --version")
    call_and_print_on_error("which javadoc")
    call_and_print_on_error("xsltproc --version")

    notice("Release script inputs:")
    notice("  release:         {}", pformat(release))
    notice("  issues_release:  {}", pformat(issues_release))
    notice("  source_release:  {}", pformat(source_release))
    notice("  release_dir:     {}", pformat(release_dir))
    notice("  checkout_dir:    {}", pformat(checkout_dir))

    make_dir(release_dir)

    return (release, issues_release, source_release, release_dir, checkout_dir)

def get_svn_release_url(module, release):
    project_url = "http://svn.apache.org/repos/asf/qpid"

    release_path_prefix = "tags/"
    if release.startswith("branches/"):
      release_path_prefix = ""

    if module == "main":
        path = "{}{}/qpid".format(release_path_prefix, release)

        if release == "trunk":
            path = "trunk/qpid"

        return "{}/{}".format(project_url, path)
    elif module == "cpp":
        path = "{}qpid-cpp-{}-rc/qpid".format(release_path_prefix, release)

        if release == "trunk":
            path = "trunk/qpid"

        return "{}/{}".format(project_url, path)

    path = "{}/{}{}".format(module, release_path_prefix, release)

    if release == "trunk":
        path = "{}/trunk".format(module, release)

    return "{}/{}".format(project_url, path)

def get_git_release_branch_url(module, release, path=""):
    """
    Get a URL to file path in GitHub

    If called without PATH it returns a URL that you can append paths
    to.
    """

    modules = {
        "cpp": "https://github.com/apache/qpid-cpp/tree",
        "proton": "https://github.com/apache/qpid-proton/tree",
    }

    if release == "trunk":
        release = "main"
    elif release == "master":
        release = "main"

    return "{}/{}/{}".format(modules[module], release, path.lstrip("/"))

def fetch_source(module, release):
    work_dir = make_temp_dir()
    user_temp_dir = make_user_temp_dir()
    dir_name = "qpid-{}-{}".format(module, release)
    source_dir = join(user_temp_dir, "transom", dir_name)
    url = "http://gitbox.apache.org/repos/asf/qpid-{}.git".format(module)

    if is_dir(source_dir):
        debug("Source already exists")
        return source_dir

    make_dir(source_dir)

    with working_dir(work_dir):
        call("git clone --bare --depth 20 --branch '{}' '{}' .", release, url)
        call("git archive '{}' | tar -xf - -C '{}'", release, source_dir, shell=True)

    return source_dir

## API reference ##

_doxygen_conf_template = u"""
DISABLE_INDEX = yes
EXTRACT_ALL = no
EXAMPLE_PATH = {example_paths}
GENERATE_HTML = yes
GENERATE_LATEX = no
GENERATE_TREEVIEW = yes
HAVE_DOT = no
PROJECT_NUMBER = {release}
QUIET = yes
RECURSIVE = yes
INPUT = {input_paths}
PROJECT_NAME = "{title}"
STRIP_FROM_PATH = {strip_paths}
HTML_OUTPUT = {output_dir}
"""

def gen_doxygen(release, title, input_paths, strip_paths, output_dir,
                example_paths=[], config_file=None):
    input_paths = " ".join(input_paths)
    strip_paths = " ".join(strip_paths)
    example_paths = " ".join(example_paths)

    make_dir(output_dir)

    source_conf = ""
    local_conf = _doxygen_conf_template.format(**locals())

    if config_file is not None:
        source_conf = read(config_file)

    path = make_temp_file()

    write(path, source_conf)
    append(path, local_conf)

    call("doxygen {}", path)

    touch(join(output_dir, "_transom_ignore_pages"))

def gen_epydoc(release, title, input_paths, input_namespaces, output_dir):
    input_paths = ":".join(input_paths)
    input_namespaces = " ".join(input_namespaces)

    make_dir(output_dir)

    options = list()
    options.append("--graph all")
    options.append("--html")
    options.append("--name \"{}\"".format(title))
    options.append("--no-private")
    options.append("--output {}".format(output_dir))
    options.append("--quiet")
    options.append("--url \"http://qpid.apache.org/index.html\"")
    options = " ".join(options)

    env = ENV
    env["PYTHONPATH"] = input_paths

    call("epydoc {} {}", options, input_namespaces, env=env)

    touch(join(output_dir, "_transom_ignore_pages"))

def gen_javadoc(release, title, input_paths, input_namespaces, output_dir):
    input_paths = ":".join(input_paths)
    input_namespaces = ":".join(input_namespaces)

    make_dir(output_dir)

    options = list()
    options.append("-windowtitle \"{}\"".format(title))
    options.append("-doctitle \"{}\"".format(title))
    options.append("-sourcepath {}".format(input_paths))
    options.append("-subpackages {}".format(input_namespaces))
    options.append("-d {}".format(output_dir))
    options.append("-notimestamp")
    options = " ".join(options)

    call("javadoc {}", options)

    touch(join(output_dir, "_transom_ignore_pages"))

def gen_rdoc(release, title, base_input_path, input_paths, output_dir):
    output_dir = absolute_path(output_dir)

    # rdoc really wants to make the last dir
    make_dir(parent_dir(output_dir))

    options = list()
    options.append("--fmt html")
    options.append("--op {}".format(output_dir))
    options.append("--quiet")
    options.append("--title \"{}\"".format(title))
    options = " ".join(options)

    input_paths = " ".join(input_paths)

    with working_dir(base_input_path):
        call("rdoc {} {}", options, input_paths)

    touch(join(output_dir, "_transom_ignore_pages"))

def gen_yard(release, title, input_dir, input_namespaces, output_dir):
    output_dir = absolute_path(output_dir)

    options = list()
    options.append("--quiet")
    options.append("--no-progress")
    options.append("--title \"{}\"".format(title))
    options.append("--output-dir {}".format(output_dir))

    for namespace in input_namespaces:
        options.append("--api {}".format(namespace))

    options = " ".join(options)

    with working_dir(input_dir): 
        call("yard {}", options)

    # Workaround an annoying yard behavior - https://github.com/lsegal/yard/issues/837
    #move(join(output_dir, "_index.html"), join(output_dir, "index.html"))

    touch(join(output_dir, "_transom_ignore_pages"))

## Examples ##

def gen_examples(release, title, lang, input_dir, input_names, output_dir,
                 readme_url=None, source_url=None):
    remove(output_dir)

    notice("Generating {}", title)

    for name in input_names:
        gen_example_page(release=release,
                         input_dir=input_dir,
                         input_name=name,
                         output_dir=output_dir,
                         lang=lang)

    gen_examples_index(release=release,
                       input_names=input_names,
                       output_dir=output_dir,
                       title=title,
                       readme_url=readme_url,
                       source_url=source_url)

_example_page_template = u"""
<h1>{title}</h1>
{content}
<p><a href="{input_name}">Download this file</a></p>
"""

def gen_example_page(release, input_dir, input_name, output_dir, lang):
    input_path = join(input_dir, input_name)
    output_path = join(output_dir, input_name)
    html_output_path = join(output_dir, "{}.html.in".format(input_name))

    content = read(input_path)
    content = strip_license_header(content, lang)
    content = content.strip()
    content = highlight(content, lang)

    title = input_name
    html = _example_page_template.format(**locals())

    copy(input_path, output_path)
    write(html_output_path, html)

_formatter = HtmlFormatter(linenos=False)

def highlight(string, lang):
    lexer = get_lexer_by_name(lang)
    return pygments_highlight(string, lexer, _formatter)

_license_header_regexes = {
    "c": re.compile(r"/\*.*?\*/", re.DOTALL),
    "cpp": re.compile(r"/\*.*?\*/", re.DOTALL),
    "csharp": re.compile(r"/\*.*?\*/", re.DOTALL),
    "java": re.compile(r"/\*.*?\*/", re.DOTALL),
    "php": re.compile(r"/\*.*?\*/", re.DOTALL),
}

def strip_license_header(string, lang):
    if lang in _license_header_regexes:
        regex = _license_header_regexes[lang]
        return re.sub(regex, "", string)
    elif lang in ("perl", "python", "ruby", "ini"):
        input_lines = string.split(LINE_SEP)
        output_lines = list()

        for i, line in enumerate(input_lines):
            if not line.startswith("#") and line != "":
                output_lines.extend(input_lines[i:])
                break

        return LINE_SEP.join(output_lines)
    else:
        return string

_examples_index_template = """
# {title}

## Example files

{example_links}

## More information

{info_links}
"""

def gen_examples_index(release, input_names, output_dir, title,
                       readme_url=None, source_url=None):
    output_path = join(output_dir, "index.md")
    example_links = list()
    info_links = list()

    for name in input_names:
        example_links.append(" - [{}]({}.html)".format(name, name))

    if readme_url:
        info_links.append(" - [README]({})".format(readme_url))

    if source_url:
        info_links.append(" - [Source location]({})".format(source_url))

    example_links = LINE_SEP.join(example_links)
    info_links = LINE_SEP.join(info_links)

    index = _examples_index_template.format(**locals())

    write(output_path, index)

## Release notes ##

def render_release_notes(project, release):
    issues = _fetch_issues(project, release)
    lines = list()

    improvements = _render_issues(issues, "New Feature", "Improvement")
    bugs = _render_issues(issues, "Bug")
    tasks = _render_issues(issues, "Task")

    if improvements is not None:
        lines.append("\n## New features and improvements\n")
        lines.append(improvements)

    if bugs is not None:
        lines.append("\n## Bugs fixed\n")
        lines.append(bugs)

    if tasks is not None:
        lines.append("\n## Tasks\n")
        lines.append(tasks)

    return "\n".join(lines)

def _fetch_issues(project, release):
    query = list()

    fix_version = release

    if project in ("qpid-cpp", "qpid-python"):
        fix_version = "{}-{}".format(project, release)

    if project in ("qpid-cpp", "qpid-java", "qpid-python", "broker-j"):
        project = "qpid"

    if project == "qpid-interop-test":
        project = "qpidit"

    if project == "proton":
        fix_version = "proton-c-{}".format(release)

    if project == "proton-j":
        project = "proton"
        fix_version = "proton-j-{}".format(release)

    if project == "protonj2":
        project = "proton"
        fix_version = "protonj2-{}".format(release)

    if project == "proton-dotnet":
        project = "proton"
        fix_version = "proton-dotnet-{}".format(release)

    query.append("project = '{}'".format(project))
    query.append("fixVersion = '{}'".format(fix_version))
    query.append("resolution = 'fixed'")

    query = " and ".join(query)
    query = "{} order by key asc".format(query)

    page_size = 100

    params = {
        "jql": query,
        "fields": "summary,issuetype",
        "maxResults": page_size,
        }

    issues = list()

    for i in range(100):
        params["startAt"] = i * page_size
        
        url = "https://issues.apache.org/jira/rest/api/2/search?{}".format(urllib.parse.urlencode(params))
        filename, headers = urllib.request.urlretrieve(url)

        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.Loader)

        issues.extend(data["issues"])

        if len(issues) >= int(data["total"]):
            break

    return issues

def _render_issues(issues, *types):
    filtered_issues = [x for x in issues
                       if x["fields"]["issuetype"]["name"] in types]

    if not filtered_issues:
        return None

    lines = list()

    for issue in filtered_issues:
        key = escape_html(issue["key"])
        url = "https://issues.apache.org/jira/browse/{}".format(key)
        summary = escape_html(issue["fields"]["summary"])

        lines.append(" - [{}]({}) - {}".format(key, url, summary))

    return "\n".join(lines)
