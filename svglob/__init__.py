from svgpathtools import svg2paths, wsvg, Path


def glob(file, suffix):
    '''Combine SVG paths into one compound path.'''
    paths, _, svg_attributes = svg2paths(file, return_svg_attributes=True)
    compound = Path(*[segment for path in paths for segment in path])
    new_file = file[:-4] + suffix + file[-4:]
    wsvg(compound, svg_attributes=svg_attributes, filename=new_file)
    return new_file
