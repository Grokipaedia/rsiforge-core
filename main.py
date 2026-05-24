# main.py

from core.adaptive_runtime_loop import AdaptiveRuntimeLoop


def print_banner():
    print("\n==============================")
    print("       RSIForge Core")
    print(" Minimal Self-Improving Loop ")
    print("==============================\n")


def main():

    runtime = AdaptiveRuntimeLoop()

    print_banner()

    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("INPUT > ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nShutting down RSIForge Core.\n")
            break

        result = runtime.run_cycle(user_input)

        print("\n--- Runtime Result ---")
        print(f"Iteration : {result['iteration']}")
        print(f"Input     : {result['input']}")
        print(f"Output    : {result['output']}")
        print(f"Score     : {result['score']:.4f}")
        print(f"Strategy  : {result['strategy']}")
        print(f"Proposal  : {result['proposal']}")
        print(f"Mutation  : {result['mutation_result']}")
        print("-----------------------\n")


if __name__ == "__main__":
    main()
