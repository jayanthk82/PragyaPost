from transformers import AutoTokenizer,EncoderDecoderModel
def slm(post):
    model = EncoderDecoderModel.from_pretrained("/home/jayanth/Documents/SMART-RETRIVEVAL /env/LINKEDIN/model /bert2bert")
    tokenizer = AutoTokenizer.from_pretrained("/home/jayanth/Documents/SMART-RETRIVEVAL /env/LINKEDIN/model /tokenizer-b2b")
    inputs = tokenizer(post, return_tensors="pt").to(model.device)
    summary_ids = model.generate(**inputs, max_length=200, num_beams=3)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
