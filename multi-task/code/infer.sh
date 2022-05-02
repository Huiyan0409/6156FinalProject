batch_size=16
data_dir=../dataset
output_dir=model/test
# dev_file=$data_dir/dev_1.jsonl
test_file=$data_dir/demo_1.jsonl
test_model=$output_dir/checkpoint-best-bleu/pytorch_model.bin #checkpoint for test
source_length=256
target_length=128
beam_size=10

python run.py --do_test --model_type roberta --model_name_or_path microsoft/codebert-base --load_model_path $test_model --test_filename $test_file --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --eval_batch_size $batch_size