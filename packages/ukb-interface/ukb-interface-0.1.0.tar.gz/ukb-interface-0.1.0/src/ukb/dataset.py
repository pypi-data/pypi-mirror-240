from __future__ import annotations

import os 
import logging
import numpy as np 
import pandas as pd 
import scipy.io as sio

from tqdm import tqdm

from category import Category

from typing import Any, Optional 
from typing import TYPE_CHECKING
from numpy.typing import ArrayLike

if TYPE_CHECKING:
    from collections.abc import Sequence


class Dataset:

    def __init__(
        self,
        subset: Sequence[str]
    ):

        if all(isinstance(e, str) for e in subset):
            self.str_criterions = '_'.join(subset)
        else:
            raise('Fatal Error: subset parameter is not a list full of string')
    
    def get_str_criterions(
        self,
    ):
        return self.str_criterions



class UKB_MORPHOLOGY(Dataset):

    def __init__(
        self,
        root: str,
        subset: str | Sequence[str],
        normalize: bool = True,
        z_threshold: Optional[float] = None,
        category_dir: Optional[str] = None,
        collection_dir: Optional[str] = None
    ):
        
        """
        UK Biobank Dataset interface based on BUPT dataset structure

        Parameters
        ----------
        root: string, required
            directory where ukb dataset is placed. all csv data
            should be placed in `dataset_splits` subdirectory.
        subset: string, or sequence of string, required
            string representation of criterion categories to load in,
            it can be one ukb.Category instance, string value of one category, or
            a sequence or list of ukb.Category instances, or string sequence of these categories.
        normalize: bool, optional
            normalize each feature of the dataset. Default: True
        z_threshold: float, optional
            remove data points that have one or more features that
            has z-value larger than given threshold. If None or a negative value
            is given, then no thresholding will be applied.
            Default = None.
        category_dir: string, optional
            category directory if a new category of features is placed in
            custom path (csv file normally) where all features will
            be loaded, but not from default directory.
            pre-defined files
            Default: None
        collection_dir: string, optional
            directory where collection of subset data are placed.
            Default: $(root)/collections/
        """

        # record basic parameters of dataset
        self.d              = os.path.join(root, 'data') # where all dataset splits are placed
        self.sbst           = subset if isinstance(subset, list) else [subset]
        self.normalize      = normalize
        self.z              = z_threshold
        
        self.eid            = pd.DataFrame(
                                pd.read_table(os.path.join(self.d, 'id'))
                              ).rename({'f.eid': 'eid'}, axis=1)
        self.N              = self.eid.size

        # get string representation of dataset
        subset_is_string = self.__check_input__()
        self.sbst_in_str    = self.__tostring__(self.sbst, subset_is_string)

        super().__init__(self.sbst_in_str)

        # claim 4 important subdirectory under root directory of dataset
        self.collection_dir = os.path.join(root, 'collections') if collection_dir is None\
                                else collection_dir
        self.reference_dir  = os.path.join(root, 'dicts') if category_dir is None\
                                else category_dir
        self.mask_dir       = os.path.join(self.collection_dir, 'masks')

        self.log_dir        = os.path.join(self.collection_dir, 'logs')

        # setup dataset directory
        assert(os.path.exists(self.reference_dir))
        self.__setup_dataset_structure__()

        # setup logger
        self.log_fn         = os.path.join(self.log_dir, '{}.txt'.format(self.str_criterions))
        self.logger         = self.__setup_logger__('dataset', log_file=self.log_fn)
        self.logger.info(self.eid)

        # two import file under this dataset structure
        # 1. data collection file (csv file)
        # 2. valid mask of this collection from whole UK Biobank

        self.collection_fn  = os.path.join(self.collection_dir, '{}.csv'.format(self.str_criterions))
        self.mask_fn        = os.path.join(self.mask_dir, '{}.npy'.format(self.str_criterions))

        self.references     = self.__get_reference__()

        # make dataset if not exist or load it out if existed
        self.__dataset__    = self.__fetch_data__()
        self.__data__       = self.__normalize__(self.__dataset__.to_numpy()[: , 1:  ])
        self.eids           = self.__dataset__.to_numpy()[: , 0: 1]
        self.features       = self.__dataset__.columns[1: ]
        self.mask           = np.load(self.mask_fn)

    def __check_input__(
        self, 
    ):         
        """ 
        check validity of input
        """

        # check if input directory exists
        assert(os.path.exists(self.d))

        # check if subset is valid
        subset_is_string    = isinstance(self.sbst, str) or all(isinstance(e, str) for e in self.sbst)
        subset_is_category  = isinstance(self.sbst, Category) or all(isinstance(e, Category) for e in self.sbst)
        
        assert(
            (not subset_is_string and subset_is_category) 
            or 
            (not subset_is_category and subset_is_string)
        )
        
        # check given normalize flag is a boolean value
        assert(isinstance(self.normalize, bool))

        return subset_is_string
    
    def __setup_dataset_structure__(
        self
    ):
        os.makedirs(self.collection_dir, exist_ok=True)
        os.makedirs(self.mask_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)
    
    def __setup_logger__(
        self, 
        name, 
        log_file, 
        level=logging.INFO
    ):
        """To setup as many loggers as you want"""

        logger_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        handler = logging.FileHandler(log_file)        
        handler.setFormatter(logger_formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

    def __tostring__(
        self,
        subset_list,
        is_string,
    ):

        if is_string:
            return self.sbst 
        else:
            return [e.val for e in self.sbst]


    def __get_reference__(
        self,
    ):
        d = self.reference_dir
        return dict([
            (
                categ, # key is the category string
                pd.DataFrame(
                    pd.read_csv(
                        os.path.join(
                            d, 
                            '{}_dict.csv'.format(categ)
                        )
                    )
                ) # value is the corresponding .csv category file
            ) for categ in self.sbst
        ])


    def __fetch_data__(
        self,
    ):

        if not os.path.exists(self.collection_fn) or not os.path.exists(self.mask_fn):
            self.__make_dataset__()
        
        return self.__load_dataset__()

    def __get_field_id_list__(
        self,
        df_ref
    ):
        return df_ref['Field ID'].to_numpy()
    
    def __get_desc_list__(
        self,
        df_ref
    ):
        return df_ref['Description'].to_numpy()
    
    def __make_dataset__(
        self,
    ):

        print('>>> Make Dataset >>>')
        print('Categories: {}'.format(self.sbst))

        # traverse each row of reference dictionary to get stats of each criterion on the population
        all_field_id = np.concatenate([self.__get_field_id_list__(self.references[categ])
                                       for categ in self.sbst_in_str])

        all_desc     = np.concatenate([self.__get_desc_list__(self.references[categ])
                                       for categ in self.sbst_in_str])

        # set first column of data as subject id list
        data_df = self.eid.copy()
        
        total_file = 0
        # concatenate each criterion column to form an all-in-one dataframe
        for field_id, desc in tqdm(zip(all_field_id, all_desc), desc='making dataset'):
            data, file_cnt = self.__get_field_data__(field_id=field_id)

            nonan_data = data[~np.isnan(data)]
            
            # filtering out all outliner
            need_thresholding = self.z is not None and self.z > 0
            if need_thresholding:
                invalid_filt = np.abs(data - nonan_data.mean()) > 3 * nonan_data.std()
                data[invalid_filt] = np.nan


            data_df = pd.concat([data_df, pd.DataFrame(data, columns=[desc])], axis=1)

            self.logger.info('Category Field ID:{}, desc: {}, {} File Added'.format(field_id, desc, file_cnt))

            total_file += file_cnt

        # save valid mask
        mask_valid = np.all(~(data_df.isna().to_numpy()), axis=1)
        np.save(self.mask_fn, mask_valid)

        self.logger.info('Dataset Head: ', data_df.head())

        # save data file
        data_df.to_csv(self.collection_fn, index=False)

        print('<<< Dataset Made <<<')
    

    def __get_field_data__(
        self,
        field_id='0',
        dtype=np.float32
    ):
        """ 
        Get data column with given field ID across all subjects (subjects with NaN value data are excluded).
        (only cross-section imaging data, that is, instance 2 data are included, 
        f.{field_id}.3.x.csv are excluded as it is a repeat imaging instance)

        Parameters
        ----------
        field_id: field id of UK Biobank dataset to access specific data
        dtype: return data type, default is np.float32

        return:
        field_data: data column pointed by input field id with NaN value included
        cnt: number of files read to fetch complete field data (a logging parameter)
        """
        
        # initialize field data with a full nan array benefitting
        # data array update steps
        field_data = np.full((self.N, ), fill_value=np.nan)

        cnt = 0
        for file in os.listdir(os.path.join(self.d)):
            
            # skip data with wrong file name
            if not file.startswith('f.{}'.format(field_id)) or\
                file.startswith('f.{}.3'.format(field_id)):
                continue 
            
            # substitue UKB data .csv NA to np.nan (may not be the case if the download of UKB data using
            # different pipeline other than R .tab file)
            df_col = pd.DataFrame(pd.read_csv(os.path.join(self.d, file))).replace({'NA': np.nan})
            assert ( self.N == df_col.size )

            # alter data to given type format
            col_data = df_col[df_col.columns[0]].to_numpy().astype(dtype)

            # update valid mask for update 
            # entries with existed value will be ignored in this update manner
            # to avoid data overwrite
            update_mask = np.logical_and(~np.isnan(col_data), np.isnan(field_data))
            field_data[update_mask] = col_data[update_mask]

            cnt += 1

        return field_data, cnt


    def __load_dataset__(
        self
    ):
        print('>>> Load Datasets, Categories: {} >>>'.format(self.sbst))
        data = pd.DataFrame(pd.read_csv(self.collection_fn))
        print('<<< Dataset Loaded, Categories: {} <<<'.format(self.sbst))

        self.logger.info('head of dataset loaded: {}'.format(data.head()))

        return data

    def __normalize__(
        self,
        dat
    ):

        epsilon = 1e-8

        if self.normalize:
            return (dat - dat.mean()) / (dat.std() + epsilon)
        else:
            return dat

    def __getitem__(
        self,
        idx 
    ):
        return self.data[idx]
    
    def n_features(
        self
    ):
        """ 
        Number of valid features (columns) in this subset.
        """

        return len(self.features)
    
    def n_subjects(
        self,
    ):
        """ 
        Number of subjects in this subset.
        (Rows without nan value are considered as a subject)
        """

        return self.mask.sum()
    
    def to_numpy(
        self,
        only_valid: bool = False
    ):
        """
        Transfer dataset data into numpy array for
        further analysis. If different subsets of datset
        are to be compared, a full rows of data is more 
        efficient as the shape of arrays are equal.
        
        Parameters
        ----------
        only_valid: boolean, optional
            drop all rows that have nan value if set to True. 
            Return all rows if set to False. Default: False.
        """

        return self.__data__ if not only_valid \
                else self.__dataset__.dropna().to_numpy()[:, 1: ]
    
    def to_csv(
        self,
        d: str,
        **kwargs
    ):

        """ 
        Save dataset as csv file. It is necessary
        if users ask for data export to other coding
        environment such as R to use a csv file. 
        (Aligned with pandas.DataFrame.to_csv())

        Parameters
        ----------
        d: string, required
            output csv file path.
        """

        self.dataset.to_csv(d, **kwargs)
        return True

    def head(
        self,
        n: int = 5
    ):
        """ 
        Get first n rows of dataset. 
        (Aligned with pandas.DataFrame.head())

        Parameters
        ----------
        n: int, optional
            number of rows to return. Default: 5
        """
        return self.__dataset__.head(n)


if __name__ == '__main__':

    dataset = UKB_MORPHOLOGY(
        root='/data/share/UKB/',
        subset=['gmv', 'scv']
    )

    print(dataset.n_subjects())
    print(dataset.n_features())
    print(dataset.N)
    print(dataset.head(10))
    print(dataset.to_numpy(only_valid=True))
