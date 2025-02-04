from collections.abc import Mapping
from dataclasses import dataclass

from checkov.common.checks.base_check_registry import BaseCheckRegistry


@dataclass
class EntityDetails:
    provider_type: str
    data: Mapping


class ServerlessRegistry(BaseCheckRegistry):

    def extract_entity_details(self, entity: EntityDetails):
        return f"serverless_{entity.provider_type}", entity.data

    def scan(self, scanned_file, entity, skipped_checks, runner_filter):
        entity_type, entity_configuration = self.extract_entity_details(entity)
        results = {}
        checks = self.get_checks(entity_type)
        for check in checks:
            skip_info = {}
            if skipped_checks:
                if check.id in [x['id'] for x in skipped_checks]:
                    skip_info = [x for x in skipped_checks if x['id'] == check.id][0]

            if runner_filter.should_run_check(check):
                self.logger.debug("Running check: {} on file {}".format(check.name, scanned_file))
                result = check.run(scanned_file=scanned_file, entity_configuration=entity_configuration,
                                   entity_name=entity_type, entity_type=entity_type, skip_info=skip_info)
                results[check] = result
        return results
