# Description: Template script for making new metric classes
# Author: Anton D. Lautrup
# Date: 18-08-2023

from pandas import DataFrame
from abc import ABC, abstractmethod

from ...utils.variable_detection import get_cat_variables
from ...utils.preprocessing import consistent_label_encoding

class MetricClass(ABC):
    """
    The Metric Class defines an abstract method that contains a skeleton of
    some evaluation metric algorithm
    """ 

    def __init__(
            self,
            real_data: DataFrame,
            synt_data: DataFrame,
            hout_data: DataFrame = None,
            cat_cols: list = None,
            num_cols: list = None,
            nn_dist: str = None,
            analysis_target : str = None,
            do_preprocessing: bool = True,
            verbose: bool = True
    ) -> None:
        
        if do_preprocessing:
            if cat_cols is None:
                cat_cols = get_cat_variables(real_data, threshold=10)
                num_cols = [column for column in real_data.columns if column not in cat_cols]
                print('SynthEval: inferred categorical columns...')
                
            CLE = consistent_label_encoding(real_data, synt_data, cat_cols, hout_data)
            real_data = CLE.encode(real_data)
            synt_data = CLE.encode(synt_data)
            if hout_data is not None: hout_data = CLE.encode(hout_data)

        self.real_data = real_data
        self.synt_data = synt_data
        self.hout_data = hout_data
        self.cat_cols = cat_cols
        self.num_cols = num_cols

        self.nn_dist = nn_dist
        self.analysis_target = analysis_target

        self.results = {}

        self.verbose = verbose

        pass

    @staticmethod
    @abstractmethod
    def name() -> str:
        """name/keyword to reference the metric"""
        pass

    @staticmethod
    @abstractmethod
    def type() -> str:
        """privacy or utility"""
        pass

    @abstractmethod
    def evaluate(self) -> float | dict:
        """ Function for evaluating the metric"""
        pass

    @abstractmethod
    def format_output(self) -> str:
        """ Return string for formatting the output, when the
        metric is part of SynthEval. 
|                                          :                    |       
        """
        pass

    @abstractmethod
    def normalize_output(self) -> dict:
        """ To add this metric to utility or privacy scores map the main 
        result(s) to the zero one interval where zero is worst performance 
        and one is best.
        
        pass or return None if the metric should not be used in such scores.

        Return dictionary of lists 'val' and 'err'
        """
        pass
    
    ### Hooks
    def privacy_loss(self) -> tuple:
        """ Extra function for handling privacy loss. I.e. the difference in
        metric from training data to synthetic data compared to test data.
        This measure is only relevant for a select few metrics.
        
        Privacy loss is always treated as a privacy metric.
        
        Returns normalised output and formatted string.
        """
        pass