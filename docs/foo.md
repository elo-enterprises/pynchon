<div class="container-fluid">

<div class="navbar-header">

<div class="navlinks">

<span class="navbar-brand"> pynchon [API Documentation](index.html)
</span> [Modules](moduleIndex.html) [Classes](classIndex.html)
[Names](nameIndex.html)

<div id="search-box-container">

<div class="input-group">

<span class="input-group-btn">
<span id="search-clear-button" class="btn btn-default">![Clear](fonts/x-circle.svg)</span>
<span id="search-help-button" class="btn btn-default">![Help](fonts/info.svg)</span>
</span>

</div>

</div>

</div>

<div id="search-results-container" style="display: none;">

<div id="search-buttons">

<span id="search-docstrings-button" class="label label-default"> search
in docstrings </span>

</div>

# Cannot search: JavaScript is not supported/enabled in your browser.

<div id="search-help-box" class="hint">

Search bar offers the following options:

  - **Term presence.** The below example searches for documents that
    must contain “foo”, might contain “bar” and must not contain “baz”:
    `+foo bar -baz`

  - **Wildcards.** The below example searches for documents with words
    beginning with “foo”: `foo*`

  - **Search in specific fields.** The following search matches all
    objects in "twisted.mail" that matches “search”:
    `+qname:twisted.mail.* +search`
    
    Possible fields: 'name', 'qname' (fully qualified name),
    'docstring', and 'kind'. Last two fields are only applicable if
    "search in docstrings" is enabled.

  - **Fuzzy matches.** The following search matches all documents that
    have a word within 1 edit distance of “foo”: `foo~1`

</div>

<div id="search-status">

</div>

<div id="search-warn-box" class="warning" style="display: none;">

<span id="search-warn"></span>

</div>

<div style="margin-top: 8px;">

Results provided by [Lunr.js](https://lunrjs.com)

</div>

</div>

</div>

</div>

<div class="container-fluid">

<div class="sidebarcontainer" style="display: none;">

<div class="sidebar">

<div>

<div class="thingTitle">

<span>Package</span> `os`

</div>

<div>

<div class="childrenKindTitle">

Modules

</div>

  - 
    
    <div class="itemName">
    
    `models`
    
    </div>

  - 
    
    <div class="itemName">
    
    `pidfile`
    
    </div>

<div class="childrenKindTitle">

Functions

</div>

  - 
    
    <div class="itemName">
    
    `filter_pids`
    
    </div>

  - 
    
    <div class="itemName">
    
    `invoke`
    
    </div>

</div>

</div>

<div>

<div class="thingTitle">

<span>Package</span> `util`

</div>

<div>

<div class="childrenKindTitle">

Modules

</div>

  - 
    
    <div class="itemName">
    
    `console`
    
    </div>

  - 
    
    <div class="itemName">
    
    `files`
    
    </div>

  - 
    
    <div class="itemName">
    
    `os`
    
    </div>

  - 
    
    <div class="itemName">
    
    `shfmt`
    
    </div>

  - 
    
    <div class="itemName">
    
    `text`
    
    </div>

  - 
    
    <div class="itemName">
    
    `click`
    
    </div>

  - 
    
    <div class="itemName">
    
    `complexity`
    
    </div>

  - 
    
    <div class="itemName">
    
    `config`
    
    </div>

  - 
    
    <div class="itemName">
    
    `events`
    
    </div>

  - 
    
    <div class="itemName">
    
    `grip`
    
    </div>

  - 
    
    <div class="itemName">
    
    `lme`
    
    </div>

  - 
    
    <div class="itemName">
    
    `oop`
    
    </div>

  - 
    
    <div class="itemName">
    
    `python`
    
    </div>

  - 
    
    <div class="itemName">
    
    `tagging`
    
    </div>

  - 
    
    <div class="itemName">
    
    `testing`
    
    </div>

  - 
    
    <div class="itemName">
    
    `typing`
    
    </div>

<div class="childrenKindTitle">

Functions

</div>

  - 
    
    <div class="itemName">
    
    `click_recursive_help`
    
    </div>

  - 
    
    <div class="itemName">
    
    `find_src_root`
    
    </div>

  - 
    
    <div class="itemName">
    
    `get_root`
    
    </div>

  - 
    
    <div class="itemName">
    
    `is_python_project`
    
    </div>

<div class="childrenKindTitle">

Variables

</div>

  - 
    
    <div class="itemName">
    
    `LOGGER`
    
    </div>

</div>

</div>

</div>

<div id="collapseSideBar">

<span class="btn btn-link"></span>

</div>

</div>

<div id="main">

<div class="page-header">

# `pynchon`.`util`.`os`

<div id="showPrivate">

Toggle Private API

</div>

</div>

<div class="categoryHeader">

package documentation

</div>

<div class="extrasDocstring">

</div>

<div class="moduleDocstring">

<div>

pynchon.util.os

</div>

</div>

<div id="splitTables">

|        |           |                         |
| ------ | --------- | ----------------------- |
| Module | `models`  | pynchon.util.os.models  |
| Module | `pidfile` | pynchon.util.os.pidfile |

From `__init__.py`:

|          |               |                                                                                                                  |
| -------- | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| Function | `filter_pids` | :param \*\*kwargs:                                                                                               |
| Function | `invoke`      | dependency-free replacement for the \`invoke\` module, which fixes problems with subprocess.POpen and os.system. |

</div>

<div id="childList">

<div class="basefunction">

<span id="pynchon.util.os.filter_pids"></span>
<span id="filter_pids"></span>

<div class="functionHeader">

<span class="py-keyword">def</span>
<span class="py-defname">filter\_pids</span><span class="function-signature">(\*\*kwargs)</span>:
[¶](#filter_pids "pynchon.util.os.filter_pids")

</div>

<div class="docstring functionBody">

<div>

:param \*\*kwargs:

</div>

</div>

</div>

<div class="basefunction">

<span id="pynchon.util.os.invoke"></span> <span id="invoke"></span>

<div class="functionHeader">

<span class="py-keyword">def</span>
<span class="py-defname">invoke</span><span class="function-signature">(cmd:
`str`, \*\*kwargs)</span>: [¶](#invoke "pynchon.util.os.invoke")

</div>

<div class="docstring functionBody">

<div>

dependency-free replacement for the \`invoke\` module, which fixes
problems with subprocess.POpen and os.system.

:param cmd: str: :param cmd: str: :param \*\*kwargs:

</div>

</div>

</div>

</div>

</div>

</div>

<div class="container">

[API Documentation](index.html) for pynchon, generated by
[pydoctor](https://github.com/twisted/pydoctor/) 23.4.0 at 2023-05-12
02:29:48.

</div>
