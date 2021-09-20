# svglob :scissors:

Combine all of the segments of an SVG file into one path.

## Why?

The software for some cutting machines (_cough Cricut_) is picky about lines
being defined as a single shape. If they are separate paths the software
will try to rearrange them when plotting.

Also, the Shaper Utilities add-in for Fusion 360 injects a bunch of metadata
into the SVG file that this tool removes. This also resets the line thickness
which Shaper makes so thick that the Cricut preview is unreadable.

## Problems?

Create an issue and we can fix it together.

## Development?

Fork this project to implement features (or get someone else that isn't me
to do it). If you think other people would use your fork, push it to your
repository, publish them as a PyPI package named `svglob-<your_username>`,
and I will promote it in this readme. If I find anything useful I will consider
pulling it into `svglob`. I would encourage you to do the same if you want
a feature from one of the forks.

# Community Forks :sparkles:

_none_
