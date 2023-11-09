import subprocess

from planned import Planned


def test_monitoring_external_process(tmp_path):
    test_script_path = tmp_path / "test_process.py"
    # 'test_process.py' の中身を書き込む
    test_script_path.write_text("import time\n" "time.sleep(2)\n")
    process = subprocess.Popen(["python", str(test_script_path)])
    action_executed = False

    def my_custom_action():
        nonlocal action_executed
        action_executed = True

    planned_instance = Planned(
        ["pgrep", "-f", str(test_script_path)], my_custom_action  # noqa: E501
    )
    planned_instance.run_monitoring()
    assert action_executed, "The custom action was not executed as expected."

    # プロセスが終了したことを確認
    process.poll()
    assert (
        process.returncode is not None
    ), "The test process did not finish as expected."
