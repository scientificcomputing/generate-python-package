def test_bake_project(cookies):
    result = cookies.bake(extra_context={"repository_name": "my_project"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "my_project"
    assert result.project_path.is_dir()

    assert result.project.basename == "my_project"
    assert result.project.isdir()
