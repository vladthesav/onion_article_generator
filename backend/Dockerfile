from huggingface/transformers-pytorch-cpu

COPY . .
#COPY models/model.pt .

RUN pip3 install -r requirements.txt

#run models.py just to dopwnload weights 
EXPOSE 3500

#ENTRYPOINT [ "python3" ]

CMD ["python3","api.py"]