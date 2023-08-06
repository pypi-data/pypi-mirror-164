import shutil
import pickle
import logging
from pathlib import Path
from turtle import down

from torch.utils.data import DataLoader

logger = logging.getLogger(__name__)


class ASR:
    @classmethod
    def run(
        cls,
        target_dir: str,
        cache_dir: str,
        remove_all_cache: bool = False,
        start: int = 0,
        stop: int = 3,
        num_workers: int = 6,
        prepare_asr_data: dict = {},
        prepare_tokenizer_data: dict = {},
        build_tokenizer: dict = {},
        build_asr_dataset: dict = {},
        build_asr_batch_sampler: dict = {},
        build_asr_upstream: dict = {},
        build_asr_downstream: dict = {},
    ):
        def stage_check(stage_id: int, successful: bool):
            assert (
                successful
            ), f"Stage {stage_id} is not done before or is corrupted. Please re-run this stage."
            if stage_id == stop:
                exit(0)

        target_dir = Path(target_dir)
        target_dir.mkdir(exist_ok=True, parents=True)

        cache_dir = Path(cache_dir)
        cache_dir.mkdir(exist_ok=True, parents=True)
        if remove_all_cache:
            shutil.rmtree(cache_dir)

        STAGE_ID = 0
        if start <= STAGE_ID:
            logger.info(f"Stage {STAGE_ID}: prepare ASR data")
            train_csv, valid_csv, test_csvs = cls.prepare_asr_data(
                target_dir, cache_dir, _get_path_only=False, **prepare_asr_data
            )

        train_csv, valid_csv, test_csvs = cls.prepare_asr_data(
            target_dir, cache_dir, _get_path_only=True, **prepare_asr_data
        )

        all_csv_exist = train_csv.is_file() and valid_csv.is_file()
        for test_csv in test_csvs:
            all_csv_exist = all_csv_exist and test_csv.is_file()
        stage_check(STAGE_ID, all_csv_exist)

        STAGE_ID = 1
        if start <= STAGE_ID:
            logger.info(f"Stage {STAGE_ID}: prepare tokenizer data")
            tokenizer_data_path = cls.prepare_tokenizer_data(
                target_dir,
                cache_dir,
                train_csv,
                _get_path_only=False,
                **prepare_tokenizer_data,
            )

        tokenizer_data_path = cls.prepare_tokenizer_data(
            target_dir,
            cache_dir,
            train_csv,
            _get_path_only=True,
            **prepare_tokenizer_data,
        )
        stage_check(STAGE_ID, tokenizer_data_path.is_file())

        STAGE_ID = 2
        if start <= STAGE_ID:
            logger.info(f"Stage {STAGE_ID}: build tokenizer")
            tokenizer_path = cls.build_tokenizer(
                target_dir,
                cache_dir,
                tokenizer_data_path,
                _get_path_only=False,
                **build_tokenizer,
            )

        tokenizer_path = cls.build_tokenizer(
            target_dir,
            cache_dir,
            tokenizer_data_path,
            _get_path_only=True,
            **build_tokenizer,
        )
        stage_check(STAGE_ID, tokenizer_path.is_file())

        STAGE_ID = 3
        if start <= STAGE_ID:
            logger.info(f"Stage {STAGE_ID}: Train ASR")
            train_dataloader = cls.build_dataloader(
                target_dir,
                cache_dir,
                "train",
                train_csv,
                tokenizer_path,
                build_asr_dataset,
                build_asr_batch_sampler,
                num_workers,
            )
            valid_dataloader = cls._build_dataloader(
                target_dir,
                cache_dir,
                "valid",
                valid_csv,
                tokenizer_path,
                build_asr_dataset,
                build_asr_batch_sampler,
                num_workers,
            )
            with Path(tokenizer_path).open("rb") as f:
                tokenizer = pickle.load(f)
            model = cls.build_asr_model(
                len(tokenizer), build_asr_upstream, build_asr_downstream
            )
            from ipdb import set_trace
            set_trace()

    @classmethod
    def build_dataloader(
        cls,
        _target_dir: str,
        _cache_dir: str,
        _mode: str,
        _data_csv: str,
        _tokenizer_path: str,
        build_asr_dataset: dict,
        build_asr_batch_sampler: dict,
        num_workers: int,
    ):
        dataset = cls.build_asr_dataset(
            _target_dir,
            _cache_dir,
            _mode,
            _data_csv,
            _tokenizer_path,
            **build_asr_dataset,
        )
        batch_sampler = cls.build_asr_batch_sampler(
            _target_dir,
            _cache_dir,
            _mode,
            _data_csv,
            dataset,
            **build_asr_batch_sampler,
        )
        dataloader = DataLoader(
            dataset,
            batch_sampler=batch_sampler,
            num_workers=num_workers,
            collate_fn=cls.build_asr_collate_fn(_mode),
        )
        return dataloader

    @classmethod
    def build_asr_model(
        cls,
        _model_output_size: str,
        _build_asr_upstream: dict,
        _build_asr_downstream: dict,
    ):
        from s3prl.nn.upstream import UpstreamDownstreamModel

        upstream = cls.build_asr_upstream(**_build_asr_upstream)
        assert isinstance(upstream.output_size, int)

        downstream = cls.build_asr_downstream(
            upstream.output_size, _model_output_size, **_build_asr_downstream
        )
        assert downstream.input_size == upstream.output_size
        assert downstream.output_size == _model_output_size

        model = UpstreamDownstreamModel(upstream, downstream)
        return model
