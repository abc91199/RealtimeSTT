from RealtimeSTT import AudioToTextRecorder
import logging

def on_realtime_update(text):
    print(f"Realtime: {text}")

def on_realtime_stable(text):
    print(f"Stabilized: {text}")

if __name__ == '__main__':
    # Set up logging to debug level
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # )

    recorder = AudioToTextRecorder(
        # Use the large-v3 model
        model="mlx-community/whisper-large-v3-turbo-q4",
        # model="large-v3-turbo",
        
        # Use MPS device for Apple Silicon
        device="cpu",
        
        # Optimization settings
        # compute_type="int8",
        # transcription_backend="faster_whisper"
        transcription_backend="mlx",
        
        # Set logging level to debug
        # level=logging.DEBUG
        min_gap_between_recordings=0.1
    )

    print("Starting recording... Speak into your microphone")
    try:
        while True:
            text = recorder.text()
            print(f"Final transcription: {text}")
    except KeyboardInterrupt:
        print("\nStopping recording...")
        recorder.shutdown() 