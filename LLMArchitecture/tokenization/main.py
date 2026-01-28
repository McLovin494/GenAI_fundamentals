import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there my name is Arion Dutta"
tokens = enc.encode(text)
decoded = enc.decode([25216, 1354, 922, 1308, 382, 1754, 294, 415, 29215])
print(f"Tokens = {tokens}")
print(f"Decoded tokens {decoded}")
