from checkov.bitbucket.dal import Bitbucket
from checkov.json_doc.runner import Runner as JsonRunner
from checkov.runner_filter import RunnerFilter


class Runner(JsonRunner):
    check_type = "bitbucket_configuration"

    def __init__(self):
        self.bitbucket = Bitbucket()
        super().__init__()

    def run(self, root_folder=None, external_checks_dir=None, files=None,
            runner_filter=RunnerFilter(), collect_skip_comments=True):
        self.prepare_data()

        report = super().run(root_folder=self.bitbucket.bitbucket_conf_dir_path, external_checks_dir=external_checks_dir,
                             files=files,
                             runner_filter=runner_filter, collect_skip_comments=collect_skip_comments)
        # JsonRunner._change_files_path_to_relative(report)

        return report

    def prepare_data(self):
        self.bitbucket.persist_all_confs()

    def require_external_checks(self):
        # default json runner require only external checks. Bitbucket runner brings build in checks
        return False

    def import_registry(self):
        from checkov.bitbucket.registry import registry
        return registry
