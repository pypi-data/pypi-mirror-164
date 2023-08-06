
class SparkFeatureMetricProfile:

    def __init__(self, validators=[], **kwargs):        
        if not isinstance(validators, list):
            raise ValueError("The validators must be a list.") 
        elif len(validators) < 1:
            raise ValueError("At least one validator must be informed in validators list.") 
        self.profile_validators = []
        for validator in validators:
            self.profile_validators.append(validator(**kwargs))

    def get_flatten_metrics(self):
        return self.df_flat_metrics

    def get_profiles(self):
        return self.profile_validators

    def flat_metrics(self):
        self.df_flat_metrics = self.profile_validators[0].get_metric()
        for i in range(1, len(self.profile_validators)):
            self.df_flat_metrics = self.df_flat_metrics.unionByName(self.profile_validators[i].get_metric(), allowMissingColumns=True)
        return self.df_flat_metrics

    def fit(self, **kwargs):
        for profile_validator in self.profile_validators:
            profile_validator.fit(**kwargs)


