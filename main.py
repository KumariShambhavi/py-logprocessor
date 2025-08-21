from logprocessor.processor import LogProcessor

def main() -> None:
    processor = LogProcessor()
    processor.process_logs()

if __name__ == "__main__":
    main()
