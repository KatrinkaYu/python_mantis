
import random

def test_delete_project(app):

    if len(app.project.get_project_list())==0:
        app.project.add("proj_for_delete")
    old_projects = app.project.get_project_list()
    proj = random.choice(old_projects)
    app.project.delete_by_name(proj)
    new_projects = app.project.get_project_list()
    old_projects.remove(proj)
    assert sorted(old_projects) == sorted(new_projects)