# debugulator

## Add (&amp; remove) multiple targeted print/logging lines to Python logic


### Motivation

<a href="http://www.youtube.com/watch?feature=player_embedded&v=OPuE-FYM3YA#t=2m23s" target="_blank"><img src="http://img.youtube.com/vi/OPuE-FYM3YA/0.jpg" /></a>

Every Python developer encounters bugs or unexpected behaviour at some point.

There are numerous debugging modules available, but often crucial insight
comes from the straightforward tried-and-tested "old-school" method of adding
in pragmatically-placed calls to the built-in ``print()`` (in Python 3) or
logging facility functions, to trace the flow through the code logic and
observe the states of objects at set points.

However, adding calls to print or logging functions, &amp; removing them when
they aren't pinpointing anything useful &amp; in fact clogging up the tracing
output, is time-consuming and tedious.

Thanks to Professor Frunk\*, you can automate much of this mundane manual task
with his simple tool, ``debugulator``.

\*No relation to J. I. Q. N. Frink Jr., copyright The Simpsons, as depicted here in [Season 8 Episode 1: Treehouse of Horror, VII](https://en.wikipedia.org/wiki/Treehouse_of_Horror_VII)


### About: Ultimate Vision

[Note: this is the project vision, which will be implemented incrementally.]

The ``debugulator`` API provides a set of methods to add in single or multiple
custom printing or logging calls, with user-defined messages including
reference to the ``str()`` or ``repr()`` of key objects, via targeting
syntactical and semantical elements of the code, including across chains
of dependent modules.

It also provides methods to remove these (or manually-added equivalents).

``debugulator`` can be used on Python 2 or 3 scripts (though Python 2 is
becoming deprecated, only simple changes are required to adapt the API from 2
to 3, so it may as well be supported).


### About: Current Project State

**Progress**:

- 04/05/19: Repository created, ``README.md`` file written to outline vision.
