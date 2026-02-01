import sys
try:
    print("Attempting to import torch...")
    import torch
    print(f"Torch imported successfully. Version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
except ImportError as e:
    print(f"Failed to import torch: {e}")
except OSError as e:
    print(f"OSError (DLL failed): {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
