import argparse
from .resolve_mod import ResolveMod

def main():
    parser = argparse.ArgumentParser(description="DaVinci Resolve Studio Mod Suite")
    parser.add_argument("--unlock", action="store_true", help="Unlock Studio features")
    args = parser.parse_args()

    mod = ResolveMod()
    if args.unlock:
        success = mod.unlock_studio()
        print("Success!" if success else "Failed to unlock Studio.")

if __name__ == "__main__":
    main()