# Deepseek R1 Hyperparameter Tuner 🎛️

An intuitive, modular CLI tool for tuning Deepseek R1 hyperparameters. Think of it as your friendly control panel for fine-tuning your model - no more wrestling with complex command-line arguments!

## ✨ Features

- 🎨 Beautiful, colored interface with interactive menus
- ✅ Real-time parameter validation
- 💾 Automatic configuration saving and loading
- 📊 Visual parameter organization
- 🔄 Smart defaults for quick starts
- 📝 Comprehensive logging system
- 🔧 Easy reset to default settings
- 📦 Modular, maintainable codebase

## 🏗️ Project Structure

```
deepseek_tuner/
├── __init__.py
├── main.py              # Application entry point
├── config/             # Configuration management
│   ├── __init__.py
│   ├── manager.py      # Handles loading/saving configs
│   └── defaults.py     # Default parameter values
├── ui/                 # User interface components
│   ├── __init__.py
│   ├── menu.py        # Interactive menu system
│   ├── display.py     # Output formatting
│   └── validators.py  # Input validation
├── utils/             # Utility functions
│   ├── __init__.py
│   └── logger.py      # Logging system
└── data/              # Data storage
    ├── logs/          # Log files
    └── backups/       # Configuration backups
```

## 🚀 Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/deepseek-tuner
   cd deepseek-tuner
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the tuner:
   ```bash
   python -m deepseek_tuner.main
   ```

## 🎮 Usage Guide

The tuner organizes parameters into three main categories:

### Model Parameters
- `batch_size`: Number of samples processed in one forward/backward pass
- `learning_rate`: Step size for gradient descent optimization
- `warmup_steps`: Number of steps for learning rate warmup
- `weight_decay`: L2 regularization factor
- `gradient_accumulation_steps`: Number of steps to accumulate gradients
- `max_grad_norm`: Maximum gradient norm for gradient clipping
- `num_epochs`: Number of training epochs

### Training Parameters
- `fp16`: Enable mixed precision training
- `distributed`: Enable distributed training
- `seed`: Random seed for reproducibility
- `logging_steps`: Frequency of logging
- `save_steps`: Frequency of model checkpointing
- `eval_steps`: Frequency of evaluation

### Data Parameters
- `max_seq_length`: Maximum sequence length for input text
- `train_file`: Path to training data file
- `validation_file`: Path to validation data file
- `preprocessing_num_workers`: Number of workers for data preprocessing

## 🔧 Configuration Management

The tool provides several ways to manage your configurations:

### Saving Configurations
- Configurations are automatically saved to `data/config.yaml`
- Backups are created automatically before major changes
- Manual saves available through the menu

### Resetting to Defaults
- Reset to default values at any time through the menu
- Automatic backup creation before reset
- Confirmation required to prevent accidents

### Logging System
- Daily log files in `data/logs/`
- Tracks all parameter changes and actions
- View recent logs through the menu
- Helps diagnose any issues

## 🏃‍♂️ Development Guide

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Write clear, documented code
4. Add tests if necessary
5. Submit a pull request

### Testing
Run tests with:
```bash
python -m pytest tests/
```

### Code Style
We follow PEP 8 guidelines. Format your code with:
```bash
black .
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the logs in `data/logs/`
2. Check existing issues on GitHub
3. Create a new issue if needed
4. Join our community discussions