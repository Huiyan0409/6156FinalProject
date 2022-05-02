# 6156FinalProject： Multi-task method generation

## prerequests
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

