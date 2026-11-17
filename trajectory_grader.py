import json

def grade_trajectory(steps_taken: list, expected_tools: list) -> dict:
    matched = [tool for tool in expected_tools if tool in steps_taken]
    accuracy = len(matched) / len(expected_tools) if expected_tools else 1.0
    return {
        "trajectory_valid": accuracy == 1.0,
        "tool_accuracy": round(accuracy, 2),
        "missing_tools": list(set(expected_tools) - set(steps_taken))
    }

if __name__ == "__main__":
    print(json.dumps(grade_trajectory(["search", "parse", "summarize"], ["search", "parse"]), indent=2))
