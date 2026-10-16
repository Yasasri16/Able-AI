import librosa
import numpy as np

def load_audio(file_path, sr=16000):
    """
    Load an audio file and return the waveform and sample rate.
    """
    audio, sr = librosa.load(file_path, sr=sr)
    return audio, sr

def extract_mfcc(audio, sr, n_mfcc=13):
    """
    Extract MFCC features from the audio.
    """
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    return mfccs.T  # Transpose to have time steps as rows

def normalize_audio(audio):
    """
    Normalize audio to range [-1, 1]
    """
    return audio / np.max(np.abs(audio))

if __name__ == "__main__":
    # Quick test
    audio, sr = load_audio("../sample.wav")
    print("Audio loaded with shape:", audio.shape)
    audio = normalize_audio(audio)
    mfccs = extract_mfcc(audio, sr)
    print("MFCCs shape:", mfccs.shape)