import time


class QueryLogger:
    def __init__(self, is_print: bool = False):
        self.queries = []
        self.sql_list = []
        # 바로 표시할지 여부 확인
        self.is_print = is_print

    def __call__(self, execute, sql, params, many, context):
        current_query = {"sql": sql, "params": params, "many": many}

        start = time.monotonic()
        try:
            result = execute(sql, params, many, context)
        except Exception as e:
            current_query["status"] = "error"
            current_query["exception"] = e
            raise
        else:
            current_query["status"] = "ok"
            return result
        finally:
            # 수행 시간
            duration = time.monotonic() - start

            current_query["duration"] = duration

            self.sql_list.append(current_query["sql"])
            current_query["sql_count"] = len(self.sql_list)
            from collections import Counter

            result = Counter(self.sql_list)
            for key, value in result.items():
                if value >= 2:
                    current_query["duplicate_query"] = value

            if self.is_print:
                # 바로 표시
                print(current_query)
            else:
                # 배열에 저장
                self.queries.append(current_query)
