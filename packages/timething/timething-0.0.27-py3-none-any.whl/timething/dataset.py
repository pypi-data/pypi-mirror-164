import base64
import typing
from dataclasses import dataclass
from pathlib import Path

import pandas as pd  # type: ignore
import torch
import torch.nn.utils.rnn as rnn
import torchaudio  # type: ignore
from torch.utils.data import Dataset

from timething import align, utils


@dataclass
class CSVRecord:
    "A line in the dataset metadata csv"

    # id in the dataset
    id: str

    # path a sigle chapter audio file
    file: Path

    # corresponding transcript
    transcript: str


@dataclass
class Base64Record:
    "Recording and transcript in raw b64 input form. Used for inference"

    # the transcription
    transcript: str

    # base64 encoded audio bytes. Not decoded
    recording: str

    @property
    def audio(self):
        return base64.b64decode(self.recording)


@dataclass
class Recording:
    """
    A single example recording
    """

    # id in the dataset
    id: str

    # audio data
    audio: torch.Tensor

    # corresponding transcript
    transcript: str

    # transcript before cleaning
    original_transcript: str

    # the alignment for this recording, if present on disk
    alignment: typing.Optional[align.Alignment]

    # recording sample rate
    sample_rate: int

    @property
    def duration_seconds(self):
        return self.audio.shape[-1] / self.sample_rate


class SpeechDataset(Dataset):
    """
    Process a folder of audio files and transcriptions
    """

    def __init__(
        self,
        metadata: Path,
        resample_to: typing.Optional[int] = None,
        alignments_path: typing.Optional[Path] = None,
        clean_text_fn=None,
    ):
        self.resample_to = resample_to
        self.clean_text_fn = clean_text_fn
        self.records = csv(metadata)
        self.alignments_path = alignments_path

    def __getitem__(self, idx):
        "Return a single (audio, transcript) example from the dataset"

        assert idx >= 0
        assert idx <= len(self)
        record = self.records[idx]

        # read in audio
        audio, sample_rate = torchaudio.load(record.file)

        # resample, if needed
        if self.resample(sample_rate):
            tf = torchaudio.transforms.Resample(sample_rate, self.resample_to)
            audio = tf(audio)

        # squash to or retain mono
        audio = torch.mean(audio, 0, keepdim=True)

        # read and process transcription
        transcript = record.transcript
        if self.clean_text_fn:
            transcript = self.clean_text_fn(transcript)

        # read in aligments if they exist on disk
        alignment = None
        if self.alignments_path:
            path = utils.alignment_filename(self.alignments_path, record.id)
            if path.exists():
                alignment = utils.read_alignment(
                    self.alignments_path, alignment_id=record.id
                )

        return Recording(
            record.id,
            audio,
            transcript,
            record.transcript,
            alignment,
            sample_rate,
        )

    def __len__(self):
        "number of examples in this dataset"
        return len(self.records)

    def resample(self, sample_rate) -> bool:
        "should examples be resampled or not"
        return self.resample_to is not None and sample_rate != self.resample_to


class InferenceDataset(Dataset):
    "A single batch of records to perform alignment on."

    def __init__(
        self,
        records: typing.List[Base64Record],
        format: str,
        sample_rate=44100,
        clean_text_fn=None,
    ):
        self.records = records
        self.format = format
        self.sample_rate = sample_rate
        self.clean_text_fn = clean_text_fn

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        assert idx >= 0
        assert idx <= len(self)
        record = self.records[idx]

        # audio
        audio, sample_rate = utils.load_audio(record.audio, self.format)

        # resample, if needed
        if self.sample_rate != sample_rate:
            tf = torchaudio.transforms.Resample(sample_rate, self.sample_rate)
            audio = tf(audio)

        # mono
        audio = torch.mean(audio, 0, keepdim=True)

        # transcript
        cleaned_transcript = record.transcript
        if self.clean_text_fn:
            cleaned_transcript = self.clean_text_fn(record.transcript)

        return Recording(
            str(idx),
            audio,
            cleaned_transcript,
            record.transcript,
            None,
            sample_rate,
        )


def csv(metadata: Path) -> typing.List[CSVRecord]:
    "read in the dataset csv"
    records = []
    for (_, row) in read_meta(metadata).iterrows():
        file_path = metadata.parent / row.id
        records.append(CSVRecord(row.id, file_path, row.transcript))

    return records


def read_meta(metadata: Path):
    "read in metadata csv"
    return pd.read_csv(metadata, delimiter="|", names=("id", "transcript"))


def collate_fn(recordings: typing.List[Recording]):
    "Collate invididual examples into a single batch"
    ids = [r.id for r in recordings]
    xs = [r.audio for r in recordings]
    ys = [r.transcript for r in recordings]
    ys_original = [r.original_transcript for r in recordings]

    xs = [el.permute(1, 0) for el in xs]
    xs = rnn.pad_sequence(xs, batch_first=True)  # type: ignore
    xs = xs.permute(0, 2, 1)  # type: ignore

    return xs, ys, ys_original, ids
