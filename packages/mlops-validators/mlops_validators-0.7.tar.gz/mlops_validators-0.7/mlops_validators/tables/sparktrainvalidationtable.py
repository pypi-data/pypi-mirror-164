from mlops_validators.tables import SparkValidationTable

class SparkTrainValidationTable(SparkValidationTable):
                     
    def __init__(self, **kwargs):  
        df_train = kwargs.get("df_train", None)
        df_validation = kwargs.get("df_validation", None)
        feature = kwargs.get("feature", None)
        target = kwargs.get("target", None)
        train_frequency_label = kwargs.get("train_frequency_label", "train_")
        validation_frequency_label = kwargs.get("validation_frequency_label", "validation_")
        train_totals_label = kwargs.get("train_totals_label", "train_total")
        validation_totals_label = kwargs.get("validation_totals_label", "validation_total")
        train_label_buckets_min = kwargs.get("train_label_buckets_min", "_train_min")
        train_label_buckets_max = kwargs.get("train_label_buckets_max", "_train_max")                
        validation_label_buckets_min = kwargs.get("validation_label_buckets_min", "_validation_min")
        validation_label_buckets_max = kwargs.get("validation_label_buckets_max", "_validation_max")
        if train_frequency_label == validation_frequency_label:
            raise ValueError("The train_frequency_label can not be equal to validation_frequency_label.")
        if train_totals_label == validation_totals_label:
            raise ValueError("The train_totals_label can not be equal to validation_totals_label.")
        if not (feature in df_train.columns and feature in df_validation.columns):
            raise ValueError("The feature must be in df_train and df_validation DataFrames.")
        if isinstance(target, str):
            if not (target in df_train.columns and feature in df_validation.columns):
                raise ValueError("The target must be in df_train and df_validation DataFrames.")
        super().__init__(df=df_train, feature_A=feature, feature_B=target, 
                         frequency_label=train_frequency_label, 
                         frequency_totals_label=train_totals_label, 
                         buckets_min_label=train_label_buckets_min,
                         buckets_max_label=train_label_buckets_max,
                         **kwargs)        
        self.validation_table = SparkValidationTable(df=df_validation, 
                                                     feature_A=feature, feature_B=target, 
                                                     frequency_label=validation_frequency_label,
                                                     frequency_totals_label=validation_totals_label,
                                                     buckets_min_label=validation_label_buckets_min,
                                                     buckets_max_label=validation_label_buckets_max,
                                                     **kwargs)        
        self.train_frequency_label = train_frequency_label
        self.validation_frequency_label = validation_frequency_label
        self.train_totals_label = train_totals_label
        self.validation_totals_label = validation_totals_label
        self.validation_frequency_table = None         
        self.train_validation_table = None  

    def __merge_maps(self, map_one, map_two):
        keys = map_one.keys() | map_two.keys()
        merged_maps = {key: [map_one.get(key,"")] + [map_two.get(key,"")] for key in keys}
        return merged_maps

    def get_frequency_table(self):
        return self.train_validation_table
    
    def get_map_frequency_columns(self):
        return self.__merge_maps(self.map_frequency_columns, self.validation_table.map_frequency_columns)

    def get_values_frequency_columns(self):
        return super().get_values_frequency_columns() + self.validation_table.get_values_frequency_columns()

    def get_map_proportion_columns(self):
        return self.__merge_maps(self.map_proportion_columns, self.validation_table.map_proportion_columns)

    def get_values_proportion_columns(self):
        labels = super().get_values_proportion_columns() + self.validation_table.get_values_proportion_columns()
        return labels

    def get_map_percentage_columns(self):
        return self.__merge_maps(self.map_percentage_columns, self.validation_table.map_percentage_columns)

    def get_values_percentage_columns(self):
        labels = super().get_values_percentage_columns() + self.validation_table.get_values_percentage_columns()
        return labels
    
    def fit(self, **kwargs):
        super().fit(**kwargs)                           
        self.validation_frequency_table = self.validation_table.fit(**kwargs).get_frequency_table()               
        select_train_columns = [self.frequency_table[col] for col in self.frequency_table.columns]
        select_valid_columns = [self.validation_frequency_table[col] for col in self.validation_frequency_table.columns if col != self.buckets_label]
        select_columns = select_train_columns + select_valid_columns                
        key = self.frequency_table[self.buckets_label] == self.validation_frequency_table[self.buckets_label]            
        self.train_validation_table = self.frequency_table.join(self.validation_frequency_table, key, how="fullouter").select(select_columns)        
        self.train_validation_table = self.train_validation_table.sort(self.buckets_label) 
        return self