

def test_add_project(app):
    proj = "new_test_project"
    old_projects = app.project.get_project_list()
    inlist = True
    while inlist:
        if proj in old_projects:
            proj = proj + '1'
            inlist = True
        else:
            inlist = False
    app.project.add(proj)
    new_projects = app.project.get_project_list()
    old_projects.append(proj)
    assert sorted(old_projects) == sorted(new_projects)