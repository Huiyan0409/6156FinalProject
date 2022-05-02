# 6156FinalProject： Multi-task method generation

## prerequests
pytorch == 1.11

transformers==4.17.0

Need at least one GPU

## How to train
1. `cd multi-task/code`
2. open train.sh, it should have something like these:
`
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
# model_path=$output_dir/checkpoint-last/pytorch_model.bin --load_model_path $model_path
fn_weights=0.5

python run.py --do_train --do_eval  --model_type roberta --model_name_or_path $pretrained_model    --train_filename $train_file --dev_filename $dev_file --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --train_batch_size $batch_size --eval_batch_size $batch_size --learning_rate $lr --num_train_epochs $epochs --fn_weights $fn_weights
`
