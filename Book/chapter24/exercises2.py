# ======================================================================
# 🔊 TEXT-TO-SPEECH AND SPEECH RECOGNITION EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: pyttsx3, openai-whisper, yt-dlp installed
# ======================================================================

# pip install pyttsx3 openai-whisper yt-dlp


# import whisper  # Uncomment when needed (large download on first use)

# =====================================================================
#                    SECTION 1: PYTTSX3 BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: INSTALL AND IMPORT PYTTSX3
#
# Learn: Installing pyttsx3, basic imports
#
# Tasks:
# 1. Install pyttsx3: pip install pyttsx3
# 2. Import pyttsx3
# 3. On Linux, you may need: sudo apt install espeak
# 4. Verify import works without errors
# 5. Understand: pyttsx3 uses your OS's built-in speech engine
# ----------------------------------------------------------------------

import pyttsx3

# ----------------------------------------------------------------------
# 🟢 2: INITIALIZE THE SPEECH ENGINE
#
# Learn: pyttsx3.init()
#
# Tasks:
# 1. Create engine: engine = pyttsx3.init()
# 2. The engine object controls all speech functions
# 3. You only need to initialize once per program
# 4. Store the engine in a variable for later use
# 5. Verify no errors occur during initialization
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 3: MAKE THE COMPUTER SPEAK
#
# Learn: engine.say(), engine.runAndWait()
#
# Tasks:
# 1. Initialize the engine
# 2. Queue speech: engine.say('Hello, world!')
# 3. Execute speech: engine.runAndWait()
# 4. Note: say() queues text, runAndWait() plays it
# 5. Make sure your speakers aren't muted!
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 4: SPEAK MULTIPLE SENTENCES
#
# Learn: Queuing multiple say() calls
#
# Tasks:
# 1. Initialize the engine
# 2. Call say() multiple times with different text
# 3. Call runAndWait() once at the end
# 4. All queued text plays in order
# 5. Try: say('First.'); say('Second.'); say('Third.'); runAndWait()
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 5: GET CURRENT ENGINE PROPERTIES
#
# Learn: engine.getProperty()
#
# Tasks:
# 1. Get volume: engine.getProperty('volume')  # Returns 0.0-1.0
# 2. Get rate: engine.getProperty('rate')  # Words per minute
# 3. Get voices: engine.getProperty('voices')  # List of Voice objects
# 4. Print each property value
# 5. Note: Default volume is 1.0 (100%), default rate is ~200 WPM
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 6: LIST AVAILABLE VOICES
#
# Learn: Voice objects and their attributes
#
# Tasks:
# 1. Get voices: voices = engine.getProperty('voices')
# 2. Loop through each voice
# 3. Print: voice.id, voice.name, voice.gender, voice.languages
# 4. Note which voices are available on your system
# 5. Different OS have different voices available
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 2: CUSTOMIZING SPEECH
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 7: CHANGE SPEAKING RATE
#
# Learn: engine.setProperty('rate', value)
#
# Tasks:
# 1. Get current rate: engine.getProperty('rate')
# 2. Set slower rate: engine.setProperty('rate', 100)
# 3. Speak something and observe the slower speed
# 4. Set faster rate: engine.setProperty('rate', 300)
# 5. Experiment to find a comfortable rate
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 8: CHANGE VOLUME
#
# Learn: engine.setProperty('volume', value)
#
# Tasks:
# 1. Get current volume: engine.getProperty('volume')
# 2. Set to 50%: engine.setProperty('volume', 0.5)
# 3. Speak something at lower volume
# 4. Set back to 100%: engine.setProperty('volume', 1.0)
# 5. Note: Value must be between 0.0 and 1.0
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 9: CHANGE VOICE
#
# Learn: engine.setProperty('voice', voice_id)
#
# Tasks:
# 1. Get list of voices: voices = engine.getProperty('voices')
# 2. Set to second voice: engine.setProperty('voice', voices[1].id)
# 3. Speak something with the new voice
# 4. Try each available voice
# 5. Note: Use voice.id, not the voice object itself
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 10: CREATE A CONFIGURABLE SPEAKER
#
# Learn: Combining property settings
#
# Tasks:
# 1. Create a function: configure_engine(rate, volume, voice_index)
# 2. Set all three properties based on parameters
# 3. Return the configured engine
# 4. Test with different configurations
# 5. Add default parameter values for convenience
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 3: SAVING AUDIO FILES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 11: SAVE SPEECH TO WAV FILE
#
# Learn: engine.save_to_file()
#
# Tasks:
# 1. Initialize the engine
# 2. Call: engine.save_to_file('Hello world', 'output.wav')
# 3. Must call: engine.runAndWait()  # Creates the file
# 4. Verify the .wav file was created
# 5. Play the file to verify it sounds correct
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 12: SAVE LONG TEXT TO AUDIO
#
# Learn: Converting text files to audio
#
# Tasks:
# 1. Read text from a file (or use a long string)
# 2. Pass the entire text to save_to_file()
# 3. Call runAndWait() to create the audio
# 4. Note: pyttsx3 can only save .wav files, not .mp3
# 5. Measure how long it takes for different text lengths
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 13: CREATE AUDIO WITH CUSTOM VOICE
#
# Learn: Combining settings with file saving
#
# Tasks:
# 1. Configure the engine with desired rate, volume, voice
# 2. Save text to a .wav file
# 3. Call runAndWait()
# 4. Verify the saved audio has the custom settings
# 5. Create audio files with different voices
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 14: BATCH CONVERT TEXT FILES TO AUDIO
#
# Learn: Processing multiple files
#
# Tasks:
# 1. Get a list of .txt files in a folder
# 2. For each text file, read its contents
# 3. Save as a .wav file with the same base name
# 4. Use a single engine for all conversions
# 5. Report progress as files are converted
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 4: WHISPER BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 15: INSTALL AND IMPORT WHISPER
#
# Learn: Installing openai-whisper
#
# Tasks:
# 1. Install: pip install openai-whisper
# 2. Note: This is a large download
# 3. Import: import whisper
# 4. First model load will download additional files
# 5. Verify import works without errors
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 16: LOAD A WHISPER MODEL
#
# Learn: whisper.load_model()
#
# Tasks:
# 1. Load base model: model = whisper.load_model('base')
# 2. Available models: 'tiny', 'base', 'small', 'medium', 'large-v3'
# 3. First load downloads the model (needs internet)
# 4. Smaller models = faster but less accurate
# 5. 'base' is good for most purposes
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 17: TRANSCRIBE AN AUDIO FILE
#
# Learn: model.transcribe()
#
# Tasks:
# 1. Load a model
# 2. Create or obtain an audio file (.wav, .mp3, etc.)
# 3. Transcribe: result = model.transcribe('audio.wav')
# 4. Get text: result['text']
# 5. Print the transcribed text
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 18: TRANSCRIBE WITH LANGUAGE SPECIFIED
#
# Learn: language parameter
#
# Tasks:
# 1. Load a model
# 2. Specify language: result = model.transcribe('audio.wav', language='English')
# 3. Whisper auto-detects language, but specifying can help
# 4. Run: whisper --help in terminal to see supported languages
# 5. Compare results with and without language specified
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 19: COMPARE MODEL ACCURACY AND SPEED
#
# Learn: Different Whisper models
#
# Tasks:
# 1. Create a test audio file with known content
# 2. Transcribe with 'tiny' model, time it
# 3. Transcribe with 'base' model, time it
# 4. Transcribe with 'small' model, time it
# 5. Compare accuracy and time for each
# 6. Note the tradeoff between speed and accuracy
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: EXAMINE TRANSCRIPTION RESULTS
#
# Learn: Result dictionary structure
#
# Tasks:
# 1. Transcribe an audio file
# 2. Print result.keys() to see available data
# 3. Access result['text'] for full transcription
# 4. Access result['segments'] for timing info
# 5. Each segment has 'start', 'end', 'text' keys
# 6. Explore other available keys
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: SUBTITLE FILES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 21: CREATE SRT SUBTITLE FILE
#
# Learn: whisper.utils.get_writer()
#
# Tasks:
# 1. Transcribe an audio file
# 2. Get writer: write_func = whisper.utils.get_writer('srt', '.')
# 3. Write file: write_func(result, 'output_name')
# 4. Check for output_name.srt in current directory
# 5. Open the file to see the SRT format
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 22: CREATE VTT SUBTITLE FILE
#
# Learn: VTT format for web videos
#
# Tasks:
# 1. Transcribe an audio file
# 2. Get writer: write_func = whisper.utils.get_writer('vtt', '.')
# 3. Write file: write_func(result, 'output_name')
# 4. Check for output_name.vtt
# 5. Compare VTT format to SRT format
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 23: CREATE TSV AND JSON OUTPUT
#
# Learn: Other output formats
#
# Tasks:
# 1. Transcribe an audio file
# 2. Create TSV output using get_writer('tsv', '.')
# 3. Create JSON output using get_writer('json', '.')
# 4. Examine each output format
# 5. TSV is useful for spreadsheets, JSON for programs
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 24: CREATE ALL SUBTITLE FORMATS
#
# Learn: Batch subtitle generation
#
# Tasks:
# 1. Transcribe an audio file once
# 2. Loop through formats: ['srt', 'vtt', 'tsv', 'json', 'txt']
# 3. Create each format using get_writer()
# 4. All files share the same base name
# 5. Verify all files were created
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: YT-DLP VIDEO DOWNLOADING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 25: INSTALL AND IMPORT YT-DLP
#
# Learn: Installing yt-dlp
#
# Tasks:
# 1. Install: pip install yt-dlp
# 2. Import: import yt_dlp
# 3. Note: yt-dlp works with YouTube and many other sites
# 4. Update regularly: pip install -U yt-dlp
# 5. Verify import works without errors
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 26: DOWNLOAD A VIDEO
#
# Learn: Basic video download
#
# Tasks:
# 1. Import yt_dlp
# 2. Set video_url to a YouTube video URL
# 3. Use: with yt_dlp.YoutubeDL() as ydl:
# 4. Call: ydl.download([video_url])  # Note: list of URLs
# 5. Check current directory for downloaded video
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 27: DOWNLOAD WITH OPTIONS
#
# Learn: YoutubeDL options dictionary
#
# Tasks:
# 1. Create options dict with 'quiet': True, 'no_warnings': True
# 2. Pass to YoutubeDL: yt_dlp.YoutubeDL(options)
# 3. This suppresses verbose output
# 4. Add 'outtmpl': 'my_video.%(ext)s' to set filename
# 5. Download and verify the filename
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 28: EXTRACT AUDIO ONLY
#
# Learn: Audio extraction options
#
# Tasks:
# 1. Create options dict with audio extraction settings
# 2. Set 'format': 'm4a/bestaudio/best'
# 3. Add postprocessor for FFmpegExtractAudio
# 4. Set output template to control filename
# 5. Download and verify only audio was saved
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 29: GET VIDEO METADATA
#
# Learn: extract_info() and sanitize_info()
#
# Tasks:
# 1. Create options with 'skip_download': True
# 2. Use: info = ydl.extract_info(video_url)
# 3. Sanitize: json_info = ydl.sanitize_info(info)
# 4. Access: json_info['title'], json_info['duration'], etc.
# 5. Print available keys: json_info.keys()
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 30: SAVE METADATA TO JSON
#
# Learn: Exporting video information
#
# Tasks:
# 1. Get video metadata (don't download video)
# 2. Sanitize the info dictionary
# 3. Import json module
# 4. Write to file: json.dumps(json_info)
# 5. Open the JSON file to examine the data
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: PRACTICAL COMBINATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 31: TEXT FILE TO SPEECH
#
# Learn: Reading and speaking text files
#
# Tasks:
# 1. Open and read a text file
# 2. Initialize pyttsx3 engine
# 3. Speak the file contents
# 4. Optionally save to .wav file
# 5. Handle long files by splitting into chunks
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 32: TRANSCRIBE AND SAVE TEXT
#
# Learn: Audio to text file
#
# Tasks:
# 1. Transcribe an audio file with Whisper
# 2. Get the text from result['text']
# 3. Write to a .txt file
# 4. Include any cleanup (remove extra whitespace, etc.)
# 5. Verify the text file contents
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 33: ROUND-TRIP: TEXT -> AUDIO -> TEXT
#
# Learn: Testing TTS and STT together
#
# Tasks:
# 1. Start with a text string
# 2. Use pyttsx3 to save as .wav file
# 3. Use Whisper to transcribe the .wav file
# 4. Compare original text with transcribed text
# 5. Note any differences (punctuation, capitalization, etc.)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 34: DOWNLOAD AND TRANSCRIBE VIDEO
#
# Learn: Full video-to-text pipeline
#
# Tasks:
# 1. Download a video using yt-dlp (or just audio)
# 2. Load Whisper model
# 3. Transcribe the downloaded file
# 4. Save transcription to text file
# 5. Optionally create subtitle files
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 35: AUDIOBOOK CREATOR
#
# Scenario: Convert text files to audiobook chapters
#
# Tasks:
# 1. Read a text file (book chapter)
# 2. Split into reasonable chunks if very long
# 3. Configure voice for pleasant listening (slower rate)
# 4. Save each chunk to numbered .wav files
# 5. Report total duration and progress
# 6. Handle special characters and formatting
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 36: PODCAST TRANSCRIBER
#
# Scenario: Create text transcripts from podcasts
#
# Tasks:
# 1. Accept audio file path as input
# 2. Let user choose Whisper model (speed vs accuracy)
# 3. Transcribe with progress indication
# 4. Clean up transcription (paragraphs, punctuation)
# 5. Save as .txt and create .srt subtitles
# 6. Report word count and duration
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 37: NEWS READER
#
# Scenario: Scrape news and read aloud
#
# Tasks:
# 1. Get news text from a website or RSS feed
# 2. Clean HTML tags and formatting
# 3. Use pyttsx3 to read headlines and summaries
# 4. Allow user to hear full article or skip
# 5. Optionally save audio for later listening
# 6. Use confirm dialogs between articles
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 38: YOUTUBE SUBTITLE GENERATOR
#
# Scenario: Create better subtitles than auto-generated
#
# Tasks:
# 1. Accept YouTube URL from user
# 2. Download audio only with yt-dlp
# 3. Get video metadata for filename
# 4. Transcribe with Whisper 'base' or 'medium' model
# 5. Generate SRT and VTT subtitle files
# 6. Clean up temporary audio file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 39: VOICE MEMO ORGANIZER
#
# Scenario: Transcribe and organize voice recordings
#
# Tasks:
# 1. Find all audio files in a folder
# 2. Transcribe each file
# 3. Extract first few words as summary
# 4. Create an index file with filename, date, summary
# 5. Save full transcriptions to text files
# 6. Optionally move processed files to subfolder
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 40: INTERACTIVE VOICE ASSISTANT
#
# Scenario: Basic speak-and-respond system
#
# Tasks:
# 1. Use pyttsx3 to ask a question
# 2. Record user's audio response (use another library or file)
# 3. Transcribe the response with Whisper
# 4. Process the text response
# 5. Speak an appropriate reply
# 6. Loop for conversation
# 7. Note: Full implementation needs audio recording capability
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 41: MEETING NOTES GENERATOR
#
# Scenario: Create notes from recorded meetings
#
# Tasks:
# 1. Transcribe meeting audio with Whisper
# 2. Add timestamps at regular intervals
# 3. Try to identify speaker changes (challenging!)
# 4. Summarize key points (basic version: extract sentences)
# 5. Create formatted meeting notes document
# 6. Include action items if keywords detected
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 42: LANGUAGE LEARNING TOOL
#
# Scenario: Practice pronunciation with feedback
#
# Tasks:
# 1. Display text in target language
# 2. Speak the text with pyttsx3 (if language supported)
# 3. User records themselves saying it
# 4. Transcribe with Whisper
# 5. Compare transcription to original text
# 6. Highlight differences for correction
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 43: BATCH VIDEO PROCESSOR
#
# Scenario: Download and transcribe multiple videos
#
# Tasks:
# 1. Accept a list of video URLs (from file or input)
# 2. Download audio from each video
# 3. Transcribe each audio file
# 4. Create subtitle files for each
# 5. Generate summary report
# 6. Handle errors gracefully (skip failed downloads)
# 7. Clean up intermediate files
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: ACCESSIBLE DOCUMENT READER
#
# Scenario: Read documents aloud for accessibility
#
# Tasks:
# 1. Open various document formats (txt, pdf, docx)
# 2. Extract text from each format
# 3. Configure voice for clarity (slower, clear voice)
# 4. Read document with pauses between sections
# 5. Allow user to pause/resume with keyboard
# 6. Save audio version of document
# ----------------------------------------------------------------------


# ======================================================================
# 🔊 QUICK REFERENCE - pyttsx3 Text-to-Speech
# ======================================================================
#
# Initialize:
#   import pyttsx3
#   engine = pyttsx3.init()
#
# Speak:
#   engine.say('Hello, world!')      # Queue text
#   engine.runAndWait()              # Execute (blocks until done)
#
# Get properties:
#   engine.getProperty('rate')       # Words per minute (default ~200)
#   engine.getProperty('volume')     # 0.0 to 1.0 (default 1.0)
#   engine.getProperty('voices')     # List of Voice objects
#
# Set properties:
#   engine.setProperty('rate', 150)          # Slower
#   engine.setProperty('rate', 250)          # Faster
#   engine.setProperty('volume', 0.5)        # 50% volume
#   voices = engine.getProperty('voices')
#   engine.setProperty('voice', voices[1].id)  # Change voice
#
# Voice attributes:
#   voice.id         # Unique identifier (use this to set voice)
#   voice.name       # Human-readable name
#   voice.gender     # May be None
#   voice.languages  # List of supported languages
#
# Save to file:
#   engine.save_to_file('Text to save', 'output.wav')
#   engine.runAndWait()  # Must call this to create the file!
#
# Note: pyttsx3 only saves .wav files, not .mp3
#
# ======================================================================


# ======================================================================
# 🔊 QUICK REFERENCE - Whisper Speech Recognition
# ======================================================================
#
# Install:
#   pip install openai-whisper
#
# Import and load model:
#   import whisper
#   model = whisper.load_model('base')
#
# Available models (speed vs accuracy tradeoff):
#   'tiny'     - Fastest, least accurate (74MB)
#   'base'     - Good balance (142MB) - RECOMMENDED
#   'small'    - Better accuracy (472MB)
#   'medium'   - High accuracy (1.5GB)
#   'large-v3' - Best accuracy (3GB)
#
# Transcribe:
#   result = model.transcribe('audio.wav')
#   result = model.transcribe('audio.mp3', language='English')
#
# Get transcription text:
#   text = result['text']
#
# Get segments with timing:
#   for segment in result['segments']:
#       print(segment['start'], segment['end'], segment['text'])
#
# Create subtitle files:
#   writer = whisper.utils.get_writer('srt', '.')  # Format, output dir
#   writer(result, 'output_name')  # Creates output_name.srt
#
# Subtitle formats:
#   'srt'  - SubRip (most common)
#   'vtt'  - WebVTT (web videos)
#   'tsv'  - Tab-separated values
#   'json' - JSON format
#   'txt'  - Plain text
#
# GPU acceleration (if available):
#   model = whisper.load_model('base', device='cuda')
#
# ======================================================================


# ======================================================================
# 🔊 QUICK REFERENCE - yt-dlp Video Downloading
# ======================================================================
#
# Install:
#   pip install yt-dlp
#
# Basic download:
#   import yt_dlp
#   with yt_dlp.YoutubeDL() as ydl:
#       ydl.download(['https://youtube.com/watch?v=VIDEO_ID'])
#
# Download with options:
#   options = {
#       'quiet': True,               # Suppress output
#       'no_warnings': True,         # Suppress warnings
#       'outtmpl': 'video.%(ext)s',  # Output filename template
#   }
#   with yt_dlp.YoutubeDL(options) as ydl:
#       ydl.download([url])
#
# Download audio only:
#   options = {
#       'quiet': True,
#       'outtmpl': 'audio.%(ext)s',
#       'format': 'm4a/bestaudio/best',
#       'postprocessors': [{
#           'key': 'FFmpegExtractAudio',
#           'preferredcodec': 'm4a',
#       }]
#   }
#
# Get metadata only (no download):
#   options = {'skip_download': True, 'quiet': True}
#   with yt_dlp.YoutubeDL(options) as ydl:
#       info = ydl.extract_info(url)
#       json_info = ydl.sanitize_info(info)
#       print(json_info['title'])
#       print(json_info['duration'])  # In seconds
#
# Common metadata keys:
#   'title', 'description', 'duration', 'view_count',
#   'channel', 'upload_date', 'thumbnail', 'formats'
#
# ======================================================================


# ======================================================================
# 🔊 QUICK REFERENCE - Common Patterns
# ======================================================================
#
# Pattern 1: Text file to speech
# -----------------------------
#   engine = pyttsx3.init()
#   with open('document.txt') as f:
#       text = f.read()
#   engine.say(text)
#   engine.runAndWait()
#
# Pattern 2: Audio file to text
# -----------------------------
#   model = whisper.load_model('base')
#   result = model.transcribe('audio.wav')
#   with open('transcript.txt', 'w') as f:
#       f.write(result['text'])
#
# Pattern 3: YouTube to transcript
# --------------------------------
#   # Download audio
#   options = {'format': 'm4a/bestaudio/best', ...}
#   with yt_dlp.YoutubeDL(options) as ydl:
#       ydl.download([url])
#   # Transcribe
#   model = whisper.load_model('base')
#   result = model.transcribe('audio.m4a')
#   # Save subtitles
#   writer = whisper.utils.get_writer('srt', '.')
#   writer(result, 'video')
#
# Pattern 4: Speak and save
# -------------------------
#   engine = pyttsx3.init()
#   engine.setProperty('rate', 150)  # Slower for clarity
#   engine.say('Playing now...')
#   engine.runAndWait()
#   engine.save_to_file('Same text for file', 'output.wav')
#   engine.runAndWait()
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# 1. Install packages:
#    pip install pyttsx3 openai-whisper yt-dlp
#
# 2. Linux additional setup:
#    sudo apt install espeak ffmpeg
#
# 3. macOS additional setup:
#    brew install ffmpeg
#
# 4. Windows:
#    - Usually works out of the box
#    - May need ffmpeg for yt-dlp: download from ffmpeg.org
#
# 5. First Whisper use:
#    - Will download model files (may take several minutes)
#    - Needs internet connection for first download
#    - Models are cached for future use
#
# 6. GPU acceleration (optional):
#    - See Appendix A for NVIDIA CUDA setup
#    - Use: whisper.load_model('base', device='cuda')
#
# 7. Test installation:
#    >>> import pyttsx3
#    >>> engine = pyttsx3.init()
#    >>> engine.say('Hello')
#    >>> engine.runAndWait()
#
#    >>> import whisper
#    >>> model = whisper.load_model('tiny')  # Small for testing
#
# ======================================================================
