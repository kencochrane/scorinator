import os

ATTRIBUTE_SLUG = 'has_readme'
WEIGHT = 10


def run(project):
    """ Look to see if a project has a readme file """
    proj_dir = project.get('project_directory', None)
    if not proj_dir:
        return None

    try:
        files = os.listdir(proj_dir)
    except OSError:
        return None
    found = False

    for f in files:
        if f.lower().startswith('readme'):
            found = True
            break

    return {
            'name': ATTRIBUTE_SLUG, 'value_b': found
            }


def score(project):
    """Score the attribute for project"""
    for attribute in project:
        if attribute.get('name', False) == ATTRIBUTE_SLUG:
            if bool(attribute['value_b']):
                return WEIGHT
    return 0
