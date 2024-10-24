import sys
from parsing import parse_input
# from inference_engine_back import InferenceEngine


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    print(input_file)
    rules, facts, queries = parse_input(input_file)

    # engine = InferenceEngine(rules, facts)

    # for query in queries:
    #     result = engine.evaluate(query)
    #     print(f"Query: {query} -> {result}")


if __name__ == "__main__":
    main()
