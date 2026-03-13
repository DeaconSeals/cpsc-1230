# Hands-On: Development Environment

To complete the work in this course you will need a **development
environment** -- a collection of tools with which you build software.
Development environments range from the small and simple to the large and
complex, but at the core of each is the
[compiler](https://en.wikipedia.org/wiki/Compiler) and 
[runtime system](https://en.wikipedia.org/wiki/Runtime_system) of the programming
language being used. At a minimum, a development environment must provide the
tools necessary for you to write a program as a 
[text file](https://en.wikipedia.org/wiki/Text_file), translate the program into an
executable form, and then run/execute the program on a computer. For the
purposes of this course it will be important to choose a development that is a
["Goldilocks fit"](https://en.wikipedia.org/wiki/Goldilocks_principle) for you
-- not too little, not too much, but just right.

There is quite of bit of material here, so you can jump to a particular section through the following list.

- [Python](#python)
- [Integrated Development Environment](#integrated-development-environment-ide)
	- [jGRASP](#jgrasp)
  - [Visual Studio Code](#visual-studio-code)
	- [Online IDE](#online-ide-provided-by-vocareum)
- [Editor + Command Line](#editor--command-line)
	- [Text Editors](#text-editors)
	- [Command Line](#command-line)
	- [Running Python](#running-python)
- [unittest](#testing-framework---unittest)
- [Checkstyle](#style-auditor---checkstyle)
- [Git](#source-control---git)


## Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is an
interpreted programming language that will be the focus of this course. Unlike
compiled programming languages, Python code is executed by an interpreter, and
this allows for highly dynamic programming. The default Python interpreter (
[CPython](https://en.wikipedia.org/wiki/CPython)) is written in C and Python.
Because Python code is so dynamic, it tends to be less strict than other
programming languages and is a popular language for beginners. However, the
inherent flexibility of Python also allows developers to adopt bad practices
that wouldn't be allowed in more strict programming languages (e.g., strict
languages would generate errors or warnings). Python is also a language with a
high level of abstraction, meaning there are often a lot of things
happening "under the hood" that the developer may not be aware of. This high
level of abstraction means that Python requires less code than low-level
languages, but this comes at the cost of control and awareness of underlying
mechanisms that informed developers should be aware of.

As a high-level language, Python comes "with batteries" and includes built-in
utilities for [debugging](https://docs.python.org/3/library/pdb.html),[testing]
(https://docs.python.org/3/library/unittest.html), and [provides informative
error messages](https://docs.python.org/3/tutorial/errors.html) by default. You
may manually install Python to your own computer ([you can find instructions
here](https://www.python.org/about/gettingstarted/)), though many development
environments may come bundled with Python.

## Integrated Development Environment (IDE)

An integrated development environment
([IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)) is a
software application that provides access within a single interface to a
variety of tools such as an editor, compiler, debugger, runtime environment,
and so on.

While there are many IDEs available for Python, here are some that I can recommend.

### jGRASP

[jGRASP](https://jgrasp.org/) is a lightweight IDE developed at Auburn and used
in hundreds of schools across the world. It is designed with education in mind,
and strives to be simple but complete. [Object
viewers](https://jgrasp.org/viewers.html) are unique to jGRASP and offer dynamic
visualization of program execution during debug mode. jGRASP is freely available
from [https://jgrasp.org/](https://jgrasp.org/). Support for Python was recently
added to jGRASP and can be found in the beta version.

### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is an open-source source
code editor from Microsoft that has become one of the most popular IDEs in
recent years. VS Code is highly capable and full-featured while retaining a
small, easily-used feel. A jGRASP plugin for VS Code is planned for development,
so all the benefits of jGRASP's object viewers should be available within VS
Code soon.

### Online IDE provided by Vocareum

[Vocareum](https://www.vocareum.com/), the cloud-based auto-grading tool that we
will use in this course, provides a simple IDE. You will be required to use this
IDE for the lab tests, and you can use this IDE for the programming assignments
if you like. More details and instructions regarding Vocareum will be provided
in a separate activity.


## Editor + Command Line

While IDEs can provide convenience and power, there are reasons that you might
want to use a small set of separate tools rather than an integrated
environment.

- Using an IDE can obscure what lower-level tools are being used when a program
  is compiled, executed, tested, and debugged.
- Using an IDE can confuse the separation between a program, the IDE, the
  language, and the different tools being used.
- Being able to work at the command line with fundamental programming tools is
  important.

The minimum tools necessary to work in this mode are an editor, a Python
installation (often included by default), and a terminal/shell/command-line
window.

### Text Editors

A good text editor can be used for far more than programming, and this is
another advantage of going this route. Once you get comfortable with a
powerful text editor, you'll want to use it for most everything.

#### Sublime, Zed, NotePad++

Sublime Text is a well-known example of a set of modern, powerful text editors.
I've included two other examples (Zed and NotePad++), but there are many
offerings in this category and most are supported by extensive package managers
that allow features to added and removed. Certain collections of these features
can offer a level of tool integration that can feel like a simple IDE.

[Sublime](https://www.sublimetext.com/) is implemented in C++ and Python and 
offers significant speed even under heavy workloads. Sublime is a
closed-source project developed by a small private company (Sublime HQ) in
Australia. A limited version of Sublime is available for free, but the full
version - with all the nice features you really want - must be purchased.

[Zed](https://zed.dev/) is an impressive successor to
[Atom](https://github.blog/2022-06-08-sunsetting-atom/) but it is still in the
development stage. You can sign up to use a pre-release version if interested
and is (currently) completely free.

[NotePad++](https://notepad-plus-plus.org/) is a popular editor for Windows
users. Most of the features are similar to what you would find in Sublime and VS
Code.

#### Emacs and vi
 
Emacs and vi are the old guard of text editors, each with its own legion of
devoted followers who keep the [editor
war](https://en.wikipedia.org/wiki/Editor_war) coals smoldering to this day.
This is Marvel-D.C., Hamilton-Burr, Coke-Pepsi.  This is Auburn-Alabama,
Michigan-Ohio State, Army-Navy. If vi had oak trees, Emacs would have [poisoned
them](https://en.wikipedia.org/wiki/Toomer%27s_Corner). Think I'm kidding or
exaggerating?  [I'm not.](https://www.emacswiki.org/emacs/ChurchOfEmacs)

Hyperbole and drama aside, both [Emacs](https://www.gnu.org/software/emacs/) and
vi (now [Vim](https://www.vim.org/)) are extremely powerful, extremely stable,
and simply excellent text editors. Anyone who considers themselves a programmer
or who wants to be one should give both a try, and be able to at least write a
[Hello World](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) in
one of them.


### Command Line

The [command line](https://en.wikipedia.org/wiki/Command-line_interface) is a
text-based interface to your computer's operating system. Terms such as *command
prompt*,
*[terminal](https://askubuntu.com/questions/506510/what-is-the-difference-between-terminal-console-shell-and-command-line/506628#506628)*,
*[shell](https://en.wikipedia.org/wiki/Shell_%28computing%29#Text_.28CLI.29_shells)*,
*shell prompt*, and others are often used interchangeably, but for our purposes
I'll just use **command line**.

Both [macOS](https://www.apple.com/macos/) and 
[Linux](https://www.linuxfoundation.org/projects/linux/) 
distributions provide a command line interface through built-in terminal applications: 
[macOS Terminal](https://support.apple.com/guide/terminal/welcome/mac), 
[Ubuntu terminal](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview). 
Terminal applications can be added to 
Microsoft [Windows](https://www.microsoft.com/en-us/windows), 
including the 
[Ubuntu terminal](https://ubuntu.com/tutorials/tutorial-ubuntu-on-windows#1-overview)
for Windows 10 
through [Ubuntu on Windows](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab).

Here are a few good resources for learning to work with the command line.

- [https://programminghistorian.org/en/lessons/intro-to-bash](https://programminghistorian.org/en/lessons/intro-to-bash)
- [https://ubuntu.com/tutorials/command-line-for-beginners#1-overview](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
- [https://linuxcommand.org/tlcl.php](https://linuxcommand.org/tlcl.php)
- [https://fabiensanglard.net/bash/](https://fabiensanglard.net/bash/)
- [https://www.youtube.com/playlist?list=PLzV58Zm8FuBKtREubmlbKHnPI-_LZlkzH](https://www.youtube.com/playlist?list=PLzV58Zm8FuBKtREubmlbKHnPI-_LZlkzH)


### Running Python

Many commend-line environments come with Python pre-installed, though there may
be minor discrepancies to how to invoke a Python program, depending on how the
language is installed in your environment. Typically, you'd invoke Python with
either the `python` or `python3` command. If we wanted to run a Python program
written in the file `WarEagle.py`, we may use one of the commands as follows.
(The `$` character represents the command-line prompt.)

```bash
$ python WarEagle.py
```
OR
```bash
$ python3 WarEagle.py
```

## Testing Framework - unittest

[unittest](https://docs.python.org/3/library/unittest.html) is a module for
[unit testing](https://en.wikipedia.org/wiki/Unit_testing) software written in
Python that comes built-in to the language. Writing good test cases is an
important skill to develop, and you are strongly encouraged to write test cases
for all your assignments.

## Source Control - Git

If you want to get a head start on using a professional tool for backup,
synchronization, and more, then you could explore the use of
[git](https://git-scm.com/). This carries a steep learning curve and isn't
necessary for this course so ... *caveat discipulus*.

If you use git you may also want to use a web-based code hosting service like
[GitHub](https://github.com/). I support the use of hosting services, but all
assignment-related code must be kept strictly in private repositories during the
semester. Services such as GitHub, [BitBucket](https://bitbucket.org/product),
and [GitLab](https://about.gitlab.com/) all offer free private repos for
educational use.

