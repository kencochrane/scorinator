import os

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
        if f.lower().startswith('license'):
            found = True
            break

    return {
            'name': 'has_license', 'value_b': found
            }