# 6156FinalProject： Multi-task method generation

## Team Members
Changshu Liu (cl4062), Zhangyi Pan (zp2223), Huiyan Zhang (hz2757)

## Project Overview
Given a description of a method in words which is called docstring, and a signature that contains the function name and the input name, researchers believe that there are models which can predict the code of the entire method successfully. To better finish this task, we proposed a new multi-task learning framework, containing a common encoder and two different decoders. The first decoder was used to generate the summarization of the docstring and the second decoder could come up with the code of the method body. In this repo, you can find code and dataset to train and test our newly proposed model. 

## Repository Structure
/dataset: contains the dataset we derived from the orginal CodeXGLUE study and used in this project

/help-functions: contains several functions we used to derive the dataset

/multi-task: the main part of our project, contains the code, the used dataset and the evaluator

/paper-work: contains the project proposal, project progress report, project final report and the demo slides

## Prerequests
pytorch == 1.11

transformers==4.17.0

Need at least one GPU

## How to train
1. `cd multi-task/code`
2. open train.sh, it should have something like these:  
```
lr=5e-5  
batch_size=12  
beam_size=10  
source_length=256  
target_length=128  
data_dir=../dataset  
output_dir=model/test_scratch_0.5  
train_file=$data_dir/train_mini.jsonl  
dev_file=$data_dir/dev_1.jsonl  
epochs=30  
pretrained_model=microsoft/codebert-base #Roberta: roberta-base  
model_path=$output_dir/checkpoint-last/pytorch_model.bin #--load_model_path $model_path  
fn_weights=0.5  

python run.py --do_train --do_eval  --model_type roberta --model_name_or_path $pretrained_model    --train_filename $train_file --dev_filename $dev_file --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --train_batch_size $batch_size --eval_batch_size $batch_size --learning_rate $lr --num_train_epochs $epochs --fn_weights $fn_weights
```


Remeber to specify the correct path to `data_dir`. If need  load a checkpoint, specify the path to `model_path` and add a new arg `--load_model_path` to `python run.py`

3. `sh run.sh`

## How to test
1. `cd multi-task/code`
2. open infer.sh and you can find something as follows:
```
batch_size=16  
data_dir=../dataset  
output_dir=model/test  
#dev_file=$data_dir/dev_1.jsonl  
test_file=$data_dir/demo_1.jsonl  
test_model=$output_dir/checkpoint-best-bleu/pytorch_model.bin #checkpoint for test  
source_length=256  
target_length=128  
beam_size=10  

python run.py --do_test --model_type roberta --model_name_or_path microsoft/codebert-base --load_model_path $test_model --test_filename $test_file --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --eval_batch_size $batch_size
```
Use `test_file` to specify the test data and use `test_model` to load a check_point.  
Some checkpoints can be found in this link https://drive.google.com/drive/folders/1w9C-Hc5XNbWQXIZko0JTIEDzOOsEsWc6?usp=sharing
(test_0.2 means when \alpha is set to 0.2)   
3. `sh infer.sh`
Aftrer running this script, under `output_dir` you can find some .output files where you find the outputs of the model.

## How to evaluate
1. `cd multi-task/code`
2. open evaluate.sh, specify the path to .gold file and the path to .output file. They can be found under `output_dir`
3. `sh evaluate.sh`  
After running this script, you may have the following output:
```
Total: 500
21.301916237468262
```

## CodeGPT
Go to this link: https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Method-Generation
