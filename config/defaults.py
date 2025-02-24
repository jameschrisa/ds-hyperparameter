"""Default configuration values for Deepseek R1"""

DEFAULT_CONFIG = {
    "model": {
        "batch_size": 32,
        "learning_rate": 1e-4,
        "warmup_steps": 1000,
        "weight_decay": 0.01,
        "gradient_accumulation_steps": 1,
        "max_grad_norm": 1.0,
        "num_epochs": 3
    },
    "training": {
        "fp16": True,
        "distributed": False,
        "seed": 42,
        "logging_steps": 100,
        "save_steps": 1000,
        "eval_steps": 500
    },
    "data": {
        "max_seq_length": 512,
        "train_file": "train.json",
        "validation_file": "validation.json",
        "preprocessing_num_workers": 4
    }
}
