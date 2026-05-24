class Solution:
    def _parse_log(self, log: str) -> Tuple[int, str, int]:
        function_id, log_type, timestamp = log.split(":")
        return int(function_id), log_type, int(timestamp)


    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        call_stack = []
        prev = 0 # to store start time of recent function
        for log in logs:
            function_id, log_type, timestamp = self._parse_log(log)
            if log_type == "start":
                if call_stack:
                    top = call_stack[-1]
                    times[top] += timestamp - prev
                call_stack.append(function_id)
                prev = timestamp
            else:
                top = call_stack.pop()
                times[top] += timestamp - prev + 1
                prev = timestamp + 1
        return times
        