import { RealtimeSession } from 'speechmatics';
async function fetchJWTAndStartSession() {
    console.log("entered JWT")
    try {
        const response = await fetch('/get-jwt');
        console.log(" before response ok")
        if (response.ok) {
            const data = await response.json();
            console.log(`JWT Token: ${data.key_value}`)  

            // console.log("JWT Token:", data.token); // Use this token for Speechmatics authentication

            // Initialize Speechmatics session with the JWT
            session = new RealtimeSession(data.key_value);

            // Add listeners for various Speechmatics events
            session.addListener('RecognitionStarted', () => console.log('RecognitionStarted'));
            session.addListener('Error', (error) => console.log('Session error:', error));
            session.addListener('AddTranscript', (message) => console.log('AddTranscript:', message));
            session.addListener('AddPartialTranscript', (message) => console.log('AddPartialTranscript:', message));
            session.addListener('EndOfTranscript', () => console.log('EndOfTranscript'));

            // Start the session and set up the media recorder for audio streaming
            await session.start();
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            console.log("we are listening!  ")
            mediaRecorder = new MediaRecorder(stream, {
                mimeType: 'audio/webm;codecs=opus',
                audioBitsPerSecond: 16000
            });

            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    session.sendAudio(event.data);
                }
            };
            mediaRecorder.start(1000); // Start recording and sending audio data every 1000ms
        } else {
            console.error("Failed to fetch JWT");
        }
    } catch (error) {
        console.error("Error fetching JWT:", error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetchJWTAndStartSession();
    document.getElementById('submitTranscriptBtn').addEventListener('click', submitTranscript);
    document.getElementById('start').addEventListener('click', startRecording);
    document.getElementById('stop').addEventListener('click', stopRecording);
    // Enable the start button only after DOM is fully loaded and scripts are ready
    document.getElementById('start').disabled = false;
});