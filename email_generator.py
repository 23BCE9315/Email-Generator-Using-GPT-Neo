def generate_text(model, tokenizer, recipient_name, event_name, special_instructions, end_note, max_length=900):
    prompt = (
        f"Subject: {event_name}\n\n"
        f"Dear {recipient_name},\n\n"
        f"{special_instructions}\n\n"
    )

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=2,
        early_stopping=True
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated_text = generated_text.split("-----Original Message-----")[0].strip()

    email_body = (
        f"{generated_text}\n\n"
        f"{end_note}\n\n"
        f"Shaily Vyas\n"
        f"sav@gmail.com\n"
        f"90205-50403"
    )

    return email_body
