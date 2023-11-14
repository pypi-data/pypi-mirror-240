from datetime import datetime


class ExpertMetricsEstimator:
    def __init__(self, project_data):
        self.project = project_data

    def _get_all_descendant_acts(self, index=1):
        return [
            desc[index]
            for act in self.project["activities"]
            for desc in act["descendant_activities"]
        ]

    def _calculate_percentage(self, condition, index=1):
        all_descendant_acts = self._get_all_descendant_acts(index)
        matching_count = sum(1 for desc in all_descendant_acts if condition(desc))
        return matching_count / len(all_descendant_acts) if all_descendant_acts else 0

    def follower_preds(self):
        descendant_percentage = self._calculate_percentage(
            lambda x: x not in self._get_all_descendant_acts(0), 0
        )
        return "Да" if descendant_percentage <= 0.05 else "Нет"

    def outrun(self):
        fss_percentage = self._calculate_percentage(lambda x: x == "FFS")
        return "Да" if fss_percentage <= 0.05 else "Нет"

    def finish_start(self):
        fs_ffs_percentage = self._calculate_percentage(lambda x: x in ["FS", "FFS"])
        return "Да" if fs_ffs_percentage >= 0.85 else "Нет"

    def others(self):
        other_percentage = self._calculate_percentage(lambda x: x not in ["FS", "FFS"])
        return "Да" if other_percentage <= 0.15 else "Нет"

    def crit_index(self):
        if "plan_deadline" not in self.project:
            return None

        acts_start_date = datetime.strptime(
            self.project["activities"][0]["start_date"].split()[0], "%Y-%m-%d"
        )
        acts_deadline_date = datetime.strptime(
            self.project["plan_deadline"].split()[0], "%Y-%m-%d"
        )
        acts_end_date = datetime.strptime(
            self.project["activities"][-1]["start_date"].split()[0], "%Y-%m-%d"
        )
        ldeadline = (acts_deadline_date - acts_start_date).days
        lcp = (acts_end_date - acts_start_date).days
        index = ldeadline / lcp
        return "Да" if index >= 1 else "Нет"

    def calculate_metrics(self):
        return {
            "follower_preds": self.follower_preds(),
            "outrun": self.outrun(),
            "finish_start": self.finish_start(),
            "others": self.others(),
            "crit_index": self.crit_index(),
        }

    def calculate_formal_metrics(self):
        # Check if all activities have non-empty 'labor_resources' and 'volume' fields
        all_have_labor_resources = "Да" if all(
            'labor_resources' in act and act['labor_resources'] for act in self.project['activities']) else "Нет"
        all_have_volume = "Да" if all(
            'volume' in act and act['volume'] for act in self.project['activities']) else "Нет"

        # Check if at least one activity has a non-empty 'descendant_activities' field
        at_least_one_has_descendants = "Да" if any(
            'descendant_activities' in act and act['descendant_activities'] for act in
            self.project['activities']) else "Нет"

        return {
            "all_have_labor_resources": all_have_labor_resources,
            "at_least_one_has_descendants": at_least_one_has_descendants,
            "all_have_volume": all_have_volume
        }
