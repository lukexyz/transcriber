import transcriber

model = transcriber.load_model("tiny")
result = model.transcribe("audio/recordings/Recording (3).m4a")
print(result["text"])
