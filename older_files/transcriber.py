import speechmatics
from httpx import HTTPStatusError

# API_KEY = "Bearer G72VFVaQL0LN9norx6eJqCQcolesaTpK"
API_KEY = "G72VFVaQL0LN9norx6eJqCQcolesaTpK"
PATH_TO_FILE = "Avenida Central 2.m4a"
LANGUAGE = "en"
CONNECTION_URL = f"wss://eu2.rt.speechmatics.com/v2"

# Create a transcription client
ws = speechmatics.client.WebsocketClient(
    speechmatics.models.ConnectionSettings(
        url=CONNECTION_URL,
        auth_token=API_KEY,
    )
)


# Define an event handler to print the partial transcript
def print_partial_transcript(msg):
    print(f"[partial] {msg['metadata']['transcript']}")


# Define an event handler to print the full transcript
def print_transcript(msg):
    print(f"[   FULL] {msg['metadata']['transcript']}")


# Register the event handler for partial transcript
ws.add_event_handler(
    event_name=speechmatics.models.ServerMessageType.AddPartialTranscript,
    event_handler=print_partial_transcript,
)

# Register the event handler for full transcript
ws.add_event_handler(
    event_name=speechmatics.models.ServerMessageType.AddTranscript,
    event_handler=print_transcript,
)

settings = speechmatics.models.AudioSettings()

# Define transcription parameters
# Full list of parameters described here: https://speechmatics.github.io/speechmatics-python/models
conf = speechmatics.models.TranscriptionConfig(
    language=LANGUAGE,
    enable_partials=True,
    max_delay=5,
)

print("Starting transcription (type Ctrl-C to stop):")
with open(PATH_TO_FILE, "rb") as fd:
    try:
        ws.run_synchronously(fd, conf, settings)
    except KeyboardInterrupt:
        print("\nTranscription stopped.")
    except HTTPStatusError as e:
        if e.response.status_code == 401:
            print("Invalid API key - Check your API_KEY at the top of the code!")
        else:
            raise e
