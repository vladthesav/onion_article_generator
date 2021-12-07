import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, GPT2Config
import numpy as np

import os

import warnings
warnings.filterwarnings('ignore')


device = torch.device("cpu")
print("Device = {}".format(device))

print("loading model..")
tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
model = GPT2LMHeadModel.from_pretrained('model')
#model = torch.load("model.pt")
#model.module.load_state_dict(torch.load("model.pt"))
model.eval()

def choose_from_top(probs, n=5):
    ind = np.argpartition(probs, -n)[-n:]
    top_prob = probs[ind]
    top_prob = top_prob / np.sum(top_prob) # Normalize
    choice = np.random.choice(n, 1, p = top_prob)
    token_id = ind[choice][0]
    return int(token_id)


def predict(input_sequence, moddel=model, len_sequence = 20):
    with torch.no_grad(): 
        cur_ids = torch.tensor(tokenizer.encode(input_sequence)).unsqueeze(0).to(device)
        outputs = model(cur_ids, labels=cur_ids)
        #cur_ids = torch.tensor(tokenizer.encode(input_sentence.strip() + " : ")).unsqueeze(0)

        for i in range(len_sequence):
            outputs = model(cur_ids, labels=cur_ids)
            loss, logits = outputs[:2]
            softmax_logits = torch.softmax(logits[0,-1], dim=0) #Take the first(from only one in this case) batch and the last predicted embedding
            if i < 3:
                n = 20
            else:
                n = 3
        
            next_token_id = choose_from_top(softmax_logits.to('cpu').numpy(), n=n) #Randomly(from the topN probability distribution) select the next word
            cur_ids = torch.cat([cur_ids, torch.ones((1,1)).long().to(device) * next_token_id], dim = 1) # Add the last word to the running sequence

            if next_token_id in tokenizer.encode('<|endoftext|>'): break
                
                
    output_list = list(cur_ids.squeeze().numpy())
    output_text = tokenizer.decode(output_list)

    output_text_str = output_text.encode('utf-8')
    #return output_text.decode('utf-8')
    return output_text_str


#print("testing model: ",predict("Donald Trump"))