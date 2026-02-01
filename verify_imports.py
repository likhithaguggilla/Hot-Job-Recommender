import sys
import os

# Add the project root to the python path
project_root = r"c:\Users\likki\OneDrive\Desktop\7_Likhitha\Courses & Competitions\hot-job-recommender"
sys.path.append(project_root)

print(f"Testing imports from {project_root}")

try:
    print("Attempting to import src.utils.loggers...")
    from src.utils import loggers
    print("  - Success")

    print("Attempting to import src.engine.vector_db...")
    from src.engine import vector_db
    print("  - Success")

    print("Attempting to import src.utils.validator...")
    from src.utils import validator
    print("  - Success")

    print("\nAll critical imports succeeded!")

except ImportError as e:
    print(f"\nCRITICAL IMPORT ERROR: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\nUNKNOWN ERROR: {e}")
    sys.exit(1)
