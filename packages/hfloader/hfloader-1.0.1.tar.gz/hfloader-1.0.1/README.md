# HFLoader - Hugging Face Model Loader

### This package provides the user with one method that returns both a `tokenizer` and a `model` when loading `HuggingFace Models`, without the need for knowing which `AutoModel` to use.

This package utilizes the `transformers` library to load a tokenizer and model, without having to know the [AutoModel](https://huggingface.co/docs/transformers/model_doc/auto#auto-classes). This means that with one command, you can easily load the tokenizer and model of a given model on [HuggingFace Model Hub](https://huggingface.co/models). This can then be easily fed into the `pipeline` function of `transformers`.

# Installation
The package can be installed with the following command:

    

    pip install hfloader

# How to Use
Here is a bit of code you can reference to see how to use the package.

    import hfloader as hfl
    
    huggingface_model = "cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer, model = hfl.load_model(huggingface_model)
    
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, torch_dtype=torch.bfloat16, device_map="auto")

The return of the command `load_model()` is going to be a tokenizer and a model, which can then be used in the pipeline method provided by transformers. It does so without the need to know which AutoModel to use, which can prove to be a hassle when trying out different models.

## Requirements
> pip install transformers
## Notes
I don't have plans to upkeep this project unless it necessitates it. I was able to achieve the goal I had set out when developing the package.