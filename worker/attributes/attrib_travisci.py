import os

ATTRIBUTE_SLUG = 'has_travisci'
WEIGHT = 5


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
        if f.lower().startswith('.travis.yml'):
            found = True
            break

    return {'name': ATTRIBUTE_SLUG, 'value': found}


def score(project):
    """Score the attribute for project"""
    svalue = 0
    for attribute in project:
        rvalue = attribute['value']
        if attribute.get('name', False) == ATTRIBUTE_SLUG:
            if bool(rvalue):
                svalue = WEIGHT
                break
    return (ATTRIBUTE_SLUG, svalue,
            attribute.get('project_score_attribute_id'), rvalue)
