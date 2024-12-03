import os
import logging
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_mel_spectrogram(file_path, n_mels=128, fixed_length=128):
    """Extract mel spectrogram from audio file."""
    try:
        audio, sr = librosa.load(file_path, sr=None)
        mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mels)
        log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

        if log_mel_spectrogram.size == 0:
            raise ValueError(f"Empty feature array extracted from file: {file_path}")

        if log_mel_spectrogram.shape[1] < fixed_length:
            pad_width = fixed_length - log_mel_spectrogram.shape[1]
            log_mel_spectrogram = np.pad(log_mel_spectrogram, ((0, 0), (0, pad_width)), mode='constant')
        else:
            log_mel_spectrogram = log_mel_spectrogram[:, :fixed_length]

        return log_mel_spectrogram

    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
        return None

def load_data(audio_directory):
    """Load audio data and extract features."""
    X, y = [], []
    for genre in os.listdir(audio_directory):
        genre_path = os.path.join(audio_directory, genre)
        if os.path.isdir(genre_path):
            for file in os.listdir(genre_path):
                if file.endswith('.wav'):
                    file_path = os.path.join(genre_path, file)
                    features = extract_mel_spectrogram(file_path)
                    if features is not None:
                        X.append(features.flatten())
                        y.append(genre)

    if not X or not y:
        raise ValueError("No data found. Please check the audio directory.")

    return np.array(X), np.array(y)

def prepare_data(X, y):
    """Prepare data for training."""
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
    X_validation, X_test, y_validation, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    label_encoder = LabelEncoder()
    y_train = label_encoder.fit_transform(y_train)
    y_validation = label_encoder.transform(y_validation)
    y_test = label_encoder.transform(y_test)

    num_classes = len(label_encoder.classes_)
    y_train = to_categorical(y_train, num_classes)
    y_validation = to_categorical(y_validation, num_classes)
    y_test = to_categorical(y_test, num_classes)

    return (X_train.reshape((X_train.shape[0], 128, 128, 1)),
            X_validation.reshape((X_validation.shape[0], 128, 128, 1)),
            X_test.reshape((X_test.shape[0], 128, 128, 1)),
            y_train, y_validation, y_test, num_classes)

def build_model(input_shape, num_classes):
    """Build and compile the CNN model."""
    model = Sequential()
    model.add(Input(shape=input_shape))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def main(audio_directory):
    """Main function to execute the workflow."""
    logging.info("Loading data...")
    X, y = load_data(audio_directory)

    logging.info("Preparing data...")
    X_train, X_validation, X_test, y_train, y_validation, y_test, num_classes = prepare_data(X, y)

    logging.info("Building model...")
    model = build_model((128, 128, 1), num_classes)

    logging.info("Training model...")
    history = model.fit(X_train, y_train, validation_data=(X_validation, y_validation), epochs=50, batch_size=32)

    logging.info("Evaluating model...")
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    logging.info(f"Test Accuracy: {test_accuracy:.2f}")

if __name__ == "__main__":
    AUDIO_DIRECTORY = '/content/drive/MyDrive/classically_punk_music_genres/genres'
    main(AUDIO_DIRECTORY)