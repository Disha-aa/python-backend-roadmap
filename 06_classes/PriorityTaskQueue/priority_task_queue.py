import json
import time
from pathlib import Path


class Task:
    def __init__(self, task_id: int, name: str, priority: int, payload: dict):
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.payload = payload


class PriorityTaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task: Task):
        self.queue.append(task)

    def get_next_task(self) -> Task:
        if not self.queue:
            return None

        self.queue.sort(key=lambda t: t.priority, reverse=True)
        return self.queue.pop()


def main():
    CURRENT_DIR = Path(__file__).resolve().parent
    CURRENT_TASK_PATH = CURRENT_DIR / "current_task.json"
    PRIORITY_TASK_PATH = CURRENT_DIR / "tasks_for_priority_task.json"

    while True:
        queue = PriorityTaskQueue()

        if CURRENT_TASK_PATH.exists() and CURRENT_TASK_PATH.stat().st_size > 0:
            with open(CURRENT_TASK_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    parts = line.split(" | ")
                    name = parts[1]
                    print(f"[FINISHED] Task '{name}' was finished")
                    time.sleep(1)
            CURRENT_TASK_PATH.unlink()

        with open(PRIORITY_TASK_PATH, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f, start=1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split(" | ")
                priority = int(parts[0])
                name = parts[1]
                payload = json.loads(parts[2])

                task = Task(task_id=idx, name=name, priority=priority, payload=payload)
                queue.add_task(task)

        next_task = queue.get_next_task()

        if next_task:
            print(
                f"[START] We're taking on a new task: '{next_task.name}' (Priority: {next_task.priority})"
            )
            with open(CURRENT_TASK_PATH, "w", encoding="utf-8") as f:
                payload_str = json.dumps(next_task.payload, ensure_ascii=False)
                f.write(f"{next_task.priority} | {next_task.name} | {payload_str}\n")

        else:
            print("Queue is empty")

        with open(PRIORITY_TASK_PATH, "w", encoding="utf-8") as f:
            for task in queue.queue:

                payload_str = json.dumps(task.payload, ensure_ascii=False)
                f.write(f"{task.priority} | {task.name} | {payload_str}\n")


if __name__ == "__main__":
    main()
