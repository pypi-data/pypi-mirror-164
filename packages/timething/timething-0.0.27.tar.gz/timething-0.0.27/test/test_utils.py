import helper
import torchaudio

from timething import align, utils  # type: ignore


def test_load_config():
    cfg = utils.load_config("german")
    assert cfg.language == "de"
    assert cfg.local_files_only is False


def test_read_write_alignment_roundtrip():
    with helper.tempdir() as tmp:
        alignment = helper.alignment(
            n_model_frames=30,
            words_cleaned=[
                align.Segment("hello", 2, 8, 1.0),
                align.Segment("world", 11, 20, 1.0),
            ],
        )

        alignment_id = "a01"
        utils.write_alignment(tmp, alignment_id, alignment)

        # read it back in
        got = utils.read_alignment(tmp, alignment_id)
        want = helper.alignment(
            words_cleaned=alignment.words_cleaned,
            n_model_frames=alignment.n_model_frames,
            n_audio_samples=alignment.n_audio_samples,
            sampling_rate=alignment.sampling_rate,
        )

        assert got.chars_cleaned == want.chars_cleaned
        assert got.words_cleaned == want.words_cleaned
        assert got.n_model_frames == want.n_model_frames
        assert got.n_audio_samples == want.n_audio_samples
        assert got.sampling_rate == want.sampling_rate


def test_load_audio():
    one_path = helper.fixtures / "audio" / "one.mp3"
    with one_path.open("rb") as f:
        loaded_audio, _ = utils.load_audio(f.read(), format="mp3")
    audio, _ = torchaudio.load(one_path)
    assert loaded_audio.equal(audio)
